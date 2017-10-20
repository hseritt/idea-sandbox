from django.conf.urls import url
from django.contrib import admin
from tasks.views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
      regex=r'^$',
      view=index,
      name='tasks_index',
    ),
]