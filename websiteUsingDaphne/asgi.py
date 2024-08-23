"""
ASGI config for websiteUsingDaphne project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing  # Replace with your app's routing module


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websiteUsingDaphne.settings')

application = ProtocolTypeRouter({
    # Just HTTP for now. (We can add other protocols later.)    
    'http':get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

