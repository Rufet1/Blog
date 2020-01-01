from django.urls import path, re_path
from .views import * 
from django.conf.urls import url

app_name = "post"

urlpatterns = [
 path('index', post_index, name="index"),
 path('create', post_create, name="create"),
 path('categories/',category_list, name = 'categorylist'),
 path('category-create/',category_create, name = 'categorycreate'),
 url(r'^(?P<categoryid>[\w-]+)/category/$', category, name="category"),
 url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),
 url(r'^(?P<slug>[\w-]+)/update/$', post_update, name="update"),
 url(r'^(?P<slug>[\w-]+)/delete/$', post_delete , name="delete"),
 url(r'^(?P<commentid>[\w-]+)/commentdelete/$', comment_delete , name="commentdelete"),
 url(r'^(?P<categoryid>[\w-]+)/categorydelete/$', category_delete , name="categorydelete"),
#  url(r'^(?P<commentid>[\w-]+)/commentupdate/$', comment_update , name="commentupdate"),

]