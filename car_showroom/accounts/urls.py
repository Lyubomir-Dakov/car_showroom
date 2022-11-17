from django.urls import path, include

from car_showroom.accounts.views import index, SignUpView, SignInView, SignOutView, UserDetailView, UserEditView, \
    UserDeleteView

urlpatterns = (
    path('', index, name='index'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('details/<int:pk>', include([
        path('', UserDetailView),
        path('logout/', SignOutView.as_view(), name='logout'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ]))
)
