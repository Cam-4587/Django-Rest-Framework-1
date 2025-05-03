import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body # byte string ofJSON data
    print(request.GET)
    print(request.POST)
    data = {}
    try:
        data = json.loads(body) # string of JSON d ata -> Python Dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers # request.META ->
    data['params'] = dict(request.GET)
    data['headers'] = (dict(request.headers))
    data['content_type'] = request.content_type
    return JsonResponse(data)
