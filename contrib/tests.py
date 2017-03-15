from django.test import TestCase
from .models import SampleModel, SampleModel2
from contrib.restmodels import Resource, ResourceForeignKey, RESTAPI


class SampleModelAPI(Resource):
    query_set = SampleModel.objects.all()
    fields = ['title']


class SampleModelAPI2(Resource):
    query_set = SampleModel2.objects.all()
    fields = ['titles',
              ('sample', ResourceForeignKey('sample', 'sample1'))]


RESTAPI.register('sample', 'sample1', SampleModelAPI)
RESTAPI.register('sample', 'sample2', SampleModelAPI2)


class RestmodelTestCase(TestCase):
    def setUp(self):
        self.data = SampleModel.objects.create(title='Sample')

    def test_resolve_method(self):
        mySample = SampleModelAPI()
        results = mySample.resolve_fields()
        for result in results:
            self.assertEqual(result['title'], self.data.title)

    def test_resolve_method_with_error_fields(self):
        mySample = SampleModelAPI2()
        with self.assertRaises(AttributeError):
            mySample.resolve_fields()
