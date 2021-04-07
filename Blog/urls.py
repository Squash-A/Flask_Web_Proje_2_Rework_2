
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = "index"),
    path('about/', views.about,name = "about"),
    path('detail/<int:id>', views.detail,name = "detail"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),
    path("info/",views.info,name = "info"),
    path("dashboard/",views.dashboard,name = "dashboard"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
