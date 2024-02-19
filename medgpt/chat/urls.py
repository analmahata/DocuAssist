from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
                  path('', views.chat_page, name='chat_page'),
                  # Add more URL patterns for other chat-related views as needed
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
