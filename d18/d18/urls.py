
from django.contrib import admin
from django.urls import path, include
from products.views import *
from django.conf.urls.static import static
from  django.conf import settings

#from store import settings - неверно,
#могут не подтянуться настройки и не будет поддерживаться аналогичный проект


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('products/', include('products.urls', namespace = 'products')),
    path('users/', include('users.urls', namespace = 'users')),
]
#проверка того, что мы находим не на продакшене
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

