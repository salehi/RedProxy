from redproxy.celery import app
from .models import KeepIt


@app.task(name='keep_it', autoregister=True)
def save_to_db(method, url, query_string, data, headers, status_code, response):
    KeepIt.objects.create(
        method=method,
        url=url,
        query_string=query_string,
        headers=headers,
        data=data,
        status_code=status_code,
        response=response,
    )
