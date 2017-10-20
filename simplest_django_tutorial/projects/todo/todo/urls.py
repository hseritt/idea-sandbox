from django.conf.urls import url
from django.contrib import admin
from tasks.views import index, delete


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
      regex=r'^$',
      view=index,
      name='tasks_index',
    ),
    url(
      regex=r'^task/(?P<task_id>\d+)/$',
      view=delete,
      name='tasks_delete',
    )
]