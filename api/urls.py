from django.urls import path,include
from .views import  projects

urlpatterns = [
    path('project/', projects),

    path('auth/', include('dj_rest_auth.urls'))
]