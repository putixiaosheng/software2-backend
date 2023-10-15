from django.urls import path
from user import views


urlpatterns = [
    path('first/',views.FirstView.as_view()),
    path('second/',views.SecondView.as_view()),
    path('three/',views.ThreeView.as_view())
]