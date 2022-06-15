from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.signup, name='sign-up'),
    path('sign-in/', views.signin, name='sign-in'),
    path('sign-out/', views.signout, name='sign-out'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.newsDetail, name='news-detail'),
    path('projects/continuing/', views.projects, name='continuing-projects'),
    path('projects/finished/', views.projects, name='finished-projects'),
    path('project/<int:id>/', views.projectDetail, name='project-detail'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)