from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('worker-panel/', views.worker_panel, name='worker_panel'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
]
