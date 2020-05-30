from django.urls import path
from myapp import views


#TEMPLATE TAGGING
app_name= 'myapp'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/',views.user_login, name="user_login"),
    path('additem/',views.addItem, name="addItem"),
    path('int:itemid>/',views.itemView,name="itemdet"),
    path('users/<int:userid>/', views.userView, name="userdet"),
    path('<int:itemid>/a/a',views.itemDel, name = "comDel"),
]
