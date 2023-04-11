from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/", include("apps.users.urls")),
    path("admin/", admin.site.urls),
    path("session-task/", include("apps.session_task.urls")),
    path("", include("apps.contacts.urls")),
    path("", include("apps.users.urls_root")),
    path("logs/", include("apps.middleware_requests_logging.urls")),
]
#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
