from django.urls import re_path
from . import views

urlpatterns = [
    re_path('api/$',views.Student_data.as_view()),
    re_path('api2/$',views.Backlogs_data.as_view()),
    re_path('at_least/$',views.atleast_one_record)
]
