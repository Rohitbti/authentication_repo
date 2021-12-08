from django.urls import path
from authentication import views
from django.conf.urls import url
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView, PasswordResetView


urlpatterns = [
    path('register/',views.register, name="register"),
    path("signup/",views.signup_view.as_view(), name="signup"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('home/',views.home, name="home"),
    path('change_password/',views.change_password_view, name="change_password"),
    url(r'^password_reset/$',views.reset_password_view, name='password_reset'),
    url(r'^password_reset/done/$',PasswordResetDoneView.as_view(template_name='reset_password_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="reset_password_confirm.html"), name="password_reset_confirm"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url(r'^reset/done/$',PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), 
    name='password_reset_complete'),
]