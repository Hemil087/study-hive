from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('upload/', views.upload_resource, name='upload_resource'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='user_profile'),
    path('resource/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('resource/<int:resource_id>/bookmark/', views.add_bookmark, name='add_bookmark'),
    path('resource/<int:resource_id>/unbookmark/', views.remove_bookmark, name='remove_bookmark'),
    path('bookmarks/', views.bookmarks_list, name='bookmarks_list'),
]