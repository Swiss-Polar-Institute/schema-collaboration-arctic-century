from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('schema-collaboration/', include('core.urls')),
    path('schema-collaboration/management/', include('management.urls', namespace='management')),
    # path('comments/', include('comments.urls', namespace='comments')),
    path('schema-collaboration/admin/', admin.site.urls),
] + static('schema-collaboration/' + settings.STATIC_URL, document_root=settings.STATIC_ROOT)
