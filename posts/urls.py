from django.urls import path, include
from django.views.decorators.cache import cache_page 
from .views import *


app_name = 'posts'
urlpatterns = [
    # path('', cache_page(60)(MusHome.as_view()), name='home'),
    path('', MusHome.as_view(), name='home'),
    path('about/',  about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MusCategory.as_view(), name='category'),
    path('api/v1/musician/', MusicianViewList.as_view()),
    path('api/v1/musician/<int:pk>/', MusicianDetail.as_view()),
    
]
