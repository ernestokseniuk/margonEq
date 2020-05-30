from django.conf.urls import url
from myapp import views


#TEMPLATE TAGGING
app_name= 'myapp'
urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'user_login/$',views.user_login, name="user_login"),
    url(r'additem/$',views.addItem, name="addItem"),
    url(r'^(?P<itemid>[0-9]+)/$',views.itemView,name="itemdet"),
    url(r'users/(?P<userid>[0-9]+)/$', views.userView, name="userdet"),
    url(r'^(?P<itemid>[0-9]+)/a/a/a',views.itemDel, name = "comDel"),
]
