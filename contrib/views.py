import json
from django.views.generic import View
from django.http import HttpResponse

from contrib.restmodels import ResourceAPI


class ResourceGetAPI(View):
    def get(self, *args, **kwargs):
        app = self.request.GET.get('app', None)
        namespace = self.request.GET.get('namespace', None)
        if app is None or namespace is None:
            return HttpResponse({}, status=404)

        resource = ResourceAPI.__getapi__(app, namespace)
        if resource is None:
            return HttpResponse({}, status=403)

        context = resource.resolve_fields()

        return HttpResponse(json.dumps(context), status=403)
