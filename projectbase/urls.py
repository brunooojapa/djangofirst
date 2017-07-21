from django.conf.urls import include, url
from django.contrib import admin
from news import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', views.NewViewSet)
router.register(r'categories', views.CategoryNewsViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
