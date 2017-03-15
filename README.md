# Django Model Rest API

This is a Django Model Rest API resolver. It simplifies request in for models.

  - All GET Request
  - Handles foreignkey
  - Easy to use

### How to use
```sh
from contrib.restmodels import Resource, ResourceForeignKey, ResourceAPI

class SampleModelAPI(Resource):
    fields = [
        'field1',
        'field2',
        ('field3', ResourceForeignKey('app', 'anothersample', AnotherSampleAPI))
    ]

ResourceAPI.register('app', 'sample', SampleModelAPI)
```

### to be continued ....
