from django.urls import path, re_path
from .views import *
from . import views
from .Password import *
from .forms import UserPasswordResetForm, UserPasswordConfirmForm
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'check_session', check_session, name='check_session'),
    re_path(r'auth',UserModelAPI.as_view()),
    re_path(r'auth/<int:id>',UserModelAPI_ID.as_view()),
    re_path(r'',views.indexPage,name='index'),
    re_path(r'verify/',views.verifyPage,name='verify'),
    re_path(r'register/', views.registerPage, name='register'),
    re_path(r'activate/<uidb64>/<token>', views.activate, name='activate'),
    re_path(r'login/',views.loginPage,name='login'),
    re_path(r'base/',views.basePage,name='base'),
    re_path(r'submit/', views.submit_form, name='submit_form'),
    re_path(r'logout/', views.logout_view, name='logout'),
   
    # path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', views.profilePage, name='profile'),
    path('edit_profile/', views.edit_profilePage, name='edit_profile'),
    path('change/', views.change_passwordPage, name='change_password_page'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
    template_name='Login/password_reset_form.html',
    email_template_name = 'Login/password_reset_email.html',
    subject_template_name = 'Login/password_reset_subject.txt',
    success_url = '/password_reset_done/',
    form_class=UserPasswordResetForm),name='password_reset'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='Login/password_reset_confirm.html',
        form_class = UserPasswordConfirmForm), name='password_reset_confirm'
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)