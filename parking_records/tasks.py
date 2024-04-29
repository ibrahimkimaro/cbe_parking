# tasks.py
from django.utils import timezone
from .models import requstResponse

def soft_delete_request_response(record_id):
    try:
        record = requstResponse.objects.get(id=record_id)
        record.soft_delete()  # Soft delete the record
    except requstResponse.DoesNotExist:
        pass