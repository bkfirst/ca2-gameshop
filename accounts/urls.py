from django.urls import path
from shop import views 
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    #change password
    path('change-password/', auth_views.PasswordChangeView.as_view(
            template_name='registration/password-change-form.html',
            success_url = '/accounts/login/'
        ),
        name='change_password',
        
    ),

    #password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html',
        ),
        name='password_reset_page'
    ),   

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password-reset-done.html',
        ),
        name='password_reset_done'
    ),  

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password-reset-confirm.html',
        ),
        name='password_reset_confirm'
    ),  

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password-reset-complete.html',
        ),
        name='password_reset_complete'
    ),  
]
