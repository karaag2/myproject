from django.urls import path
from .views import register_by_access_token,ManualTestView

urlpatterns = [
    path('test/', register_by_access_token, name='social-auth'),
    path('man/', ManualTestView.as_view(), name='manual-test')
]
