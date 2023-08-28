from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateBusiness.as_view(), name='get_post_business'),
    path('<int:pk>/', views.UpdateBusiness.as_view(), name='get_delete_update_business'),
]