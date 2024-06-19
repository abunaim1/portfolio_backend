from django.shortcuts import render
from .models import ContactModel
from .serializers import ContactSerializer
from rest_framework import viewsets
from django.conf import settings
from django.core.mail import send_mail


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        subject = contact.subject
        message = f'Message: {contact.message}'
        form_email = contact.email
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, form_email, recipient_list)
