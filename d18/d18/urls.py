
from django.contrib import admin
from django.urls import path, include
from products.views import *
from django.conf.urls.static import static
from  django.conf import settings
from django.contrib.auth import views as auth_views
#from store import settings - неверно,
#могут не подтянуться настройки и не будет поддерживаться аналогичный проект


urlpatterns = [
    path('', index, name = 'index'),
    path('products/', include('products.urls', namespace = 'products')),
    path('users/', include('users.urls', namespace = 'users')),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('admin/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('admin/', admin.site.urls),
]
#проверка того, что мы находим не на продакшене
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

