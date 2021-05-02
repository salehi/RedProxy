import requests
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from proxy.tasks import save_to_db


async def index(request: WSGIRequest):
    method = request.method
    scheme = 'https'
    host = request.META['API_HOST']
    path = request.path
    query_string = request.META['QUERY_STRING']
    body = request.body
    data = body.decode("utf-8")
    user_agent = request.META['HTTP_USER_AGENT']
    authorization = request.META.get('HTTP_AUTHORIZATION', None)
    accept = request.META.get('HTTP_ACCEPT', 'application/json, text/plain, */*')
    content_type = request.META.get('HTTP_CONTENT_TYPE', 'application/json;charset=utf-8')
    referer = request.META.get('HTTP_REFERER', 'https://backoffice.timcheh.com/')
    origin = request.META.get('HTTP_ORIGIN', 'https://backoffice.timcheh.com')
    headers = {
        'user-agent': user_agent,
        'origin': origin,
        'referer': referer,
        'accept': accept,
        'content-type': content_type,
    }
    if authorization:
        headers.update({'authorization': authorization})
    url = f'{scheme}://{host}{path}'
    req = requests.request(
        method,
        url,
        params=query_string,
        data=data,
        headers=headers
    )
    save_to_db.delay(method, url, query_string, data, headers, req.status_code, req.text)
    return HttpResponse(req.content, status=req.status_code)
