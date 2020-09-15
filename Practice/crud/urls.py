from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/',views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout, name = 'logout'),
    path('create/',views.create, name = 'create'),
    path('create_article/', views.create_article, name = 'create_article'),
    path('delete_article/', views.delete_article, name = 'delete_article'),
    path('update/', views.update, name = 'update'),
    path('update_article/', views.update_article, name ='update_article'),
]
