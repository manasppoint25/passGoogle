
from django.contrib import admin
from django.urls import path
from forgot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('forgot',views.forgot),
    path('confirm',views.confirm)
]
