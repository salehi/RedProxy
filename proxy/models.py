from django.db import models
from django.utils import timezone


class KeepIt(models.Model):
    class Meta:
        ordering = ['-created_at']

    method = models.TextField(null=True, db_index=True)
    url = models.TextField(null=True, db_index=True)
    query_string = models.TextField(null=True, db_index=True)
    headers = models.JSONField(null=True, db_index=True)
    data = models.JSONField(null=True, db_index=True)
    response = models.TextField(null=True, db_index=True)
    status_code = models.PositiveIntegerField(null=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
