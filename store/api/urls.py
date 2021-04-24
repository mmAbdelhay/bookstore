from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index),
    path('create', views.create),
    path("login", obtain_auth_token),
    path("signup", views.api_signup),
    path('store', views.CreateBook.as_view()),
    path('list', views.ListBook.as_view()),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('<int:pk>', views.CrudBook.as_view()),
]
