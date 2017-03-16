import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from contrib.restmodels import Resource, ResourceForeignKey, ResourceAPI

from contrib.models import SampleModel, SampleModel2


class SampleModelAPI(Resource):
    query_set = SampleModel.objects.all()
    fields = ['title']


class SampleModelAPI2(Resource):
    query_set = SampleModel2.objects.all()
    fields = ['title',
              ('sample', ResourceForeignKey('sample', 'sample1'))]


ResourceAPI.register('sample', 'sample1', SampleModelAPI)
ResourceAPI.register('sample', 'sample2', SampleModelAPI2)


class RestmodelTestCase(TestCase):
    def setUp(self):
        self.data = SampleModel.objects.create(title='Sample')
        self.data1 = SampleModel2.objects.create(title='ForeignKey',
                                                 sample=self.data)

    def test_resolve_method(self):
        mySample = SampleModelAPI()
        results = mySample.resolve_fields()
        for result in results:
            self.assertEqual(result['title'], self.data.title)

    def test_resolve_method_with_error_fields(self):
        mySample = SampleModelAPI2()
        result = mySample.resolve_fields()[0]
        self.assertEqual(result['title'], self.data1.title)
        self.assertEqual(result['sample'][0]['title'], self.data.title)


class RestGetAPIModelTestCase(TestCase):
    def setUp(self):
        self.data = SampleModel.objects.create(title='Sample')
        self.data1 = SampleModel2.objects.create(title='ForeignKey',
                                                 sample=self.data)
        self.base_url = reverse('resource-get-api')

    def test_get_data(self):
        response = self.client.get(
            self.base_url,
            {
                'app': 'sample',
                'namespace': 'sample2'
            })
        response = json.loads(response.content)[0]
        self.assertEqual(response['title'], self.data1.title)
        self.assertEqual(response['sample'][0]['title'], self.data.title)
