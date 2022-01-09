from django.urls import include, path

from authenticate.controllers.login import Login

loginCls = Login()
urlpatterns = [
    path('login/', loginCls.login),
    path('me/', loginCls.me)
]