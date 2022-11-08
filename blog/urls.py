from django import views
from django.urls import path
from .views import contactView, displayTime, loginView, profileView, logoutView, aboutView
from ecommerce.views import Myviews
from blog.views import book_list, post_list, post_detail

#create a name space
app_name = 'blog'


urlpatterns = [
    path("books_list/",book_list),
    path("",post_list),
    path("contact/",contactView, name='contact'),
    path("about/",aboutView,name ='about'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path("login/",loginView,name='login'),
    path("profile/",profileView,name='profile'),
    path("logout/",logoutView,name='logout'),
    

]