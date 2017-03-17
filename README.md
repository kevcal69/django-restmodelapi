# Django Model Rest API

This is a Django Model Rest API resolver. It simplifies request in for models.

  - All GET Request
  - Handles foreignkey
  - Easy to use

### How to use: step 1 python
```sh
from contrib.restmodels import Resource, ResourceForeignKey, ResourceAPI

class SampleModelAPI(Resource):
    fields = [
        'field1',
        'field2'
    ]

#: Working with foreignkeys
class SampleModeAPIWithForeignkey(Resource):
    fields = [
        'field1',
        'field2',
        ('field3', ResourceForeignKey('app', 'anothersample', AnotherSampleAPI))
    ]


ResourceAPI.register('app', 'sample', SampleModelAPI)
ResourceAPI.register('app', 'samplewithforeginkey', SampleModeAPIWithForeignkey)
```

The ResourceAPI acts as services that handles the model seemlessly.

### How to use : step 2 javascript (optional)
```sh
#: Require the restmodel.js
#: Either
#:      source it: <script src="path_to/restmodel.js">
#:      some sort of amd require: require('restmodel')
#: in your javascript

#: new RestModel('appname', 'namespace')
var Sample = new RestModel('app', 'sample');

Sample.objects.filter({
    field: field_value,
    field1: field_value2
}).then(function(response_data) {
    #: do your stuff
    #: response_data == JSON
    console.log(response_data);
});

```
Will soon add rest capabilities... :) stay tune
