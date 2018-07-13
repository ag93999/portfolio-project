from django.urls import path
from . import views


urlpatterns = [
    # ex: blog/
    path('', views.allblog, name='allblog'),
    # ex: blog/id/
    path('<int:blog_id>/', views.detail, name='detail')
]
