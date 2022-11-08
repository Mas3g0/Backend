from . import views
from django.urls import path

# create a name space
app_name = 'account'


urlpatterns = [
    path("account/signup",views.resgisterView,name='signup'),
    path("<pk>/update",views.UserEditView.as_view(),name='edit_profile'),
]