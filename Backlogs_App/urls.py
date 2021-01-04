from django.urls import re_path
from . import views

urlpatterns = [
    re_path('api/$',views.Student_data.as_view()),
]
