from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from host import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),

    path("login/", views.common_login, name="login"),
    path("register/", views.register, name="register"),

    path("host/", include("host.urls")),
    path("teacher/", include("teacher.urls")),
    path("student/", include("student.urls")),
    path("usertable/", include("usertable.urls")),

    # Assignment URLs
    path("assignments/", include("assignments.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )