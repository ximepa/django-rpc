from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from example.rpc import router as rpc_router


urlpatterns = patterns(
    '',
    url(r'^', include('example.main.urls', 'main')),
    url(r'^tricks/', include('example.tricks.urls', 'tricks')),
    url(r'^game/', include('example.game.urls', 'game')),
    url(r'^baserpc/', include(rpc_router.urls))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
