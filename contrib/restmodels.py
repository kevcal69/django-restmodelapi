from __future__ import unicode_literals


class RESTAPI(object):
    registered_api = []

    def register(self, app, namespace, instance):
        self.registered_api.append(
            (app, namespace, instance())
        )

    def __getapi__(self, app, namespace):
        return next((k for i, v, k in self.registered_api
                     if i == app and v == namespace), None)


class Resource(object):
    query_set = None
    fields = []
    exclude = []
    filters = {}

    def resolve_fields(self):
        results = []

        for item in self.query_set:
            result = {}
            for field in self.fields:
                try:
                    if type(field) == tuple:
                        query_set = getattr(item, field[0], None)
                        result[field[0]] = field[1].resolve(query_set)
                    else:
                        result[field] = getattr(item, field, None)
                except Exception:
                    print 'No %s attribute found. Check your fields'
                    raise

                # [result.update({field: item.__getattribute__(field)})
                #     for field in self.fields]

            results.append(result)
        return results


class ResourceForeignKey(object):

    def __init__(self, app, namespace):
        self.app = app
        self.namespace = namespace
        self.query_set = None

    def resolve(self, query_set):
        api_resolver = ResourceAPI.__getapi__(self.app, self.namespace)
        if api_resolver is None:
            raise Exception('Error')
        api_resolver.query_set = query_set.__class__.objects.all()
        return api_resolver.resolve_fields()

ResourceAPI = RESTAPI()
