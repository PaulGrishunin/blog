from Project import settings
from . import views
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.register, name='registration'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('tags/', views.tags_list, name='tag_list_url'),
    path('tag/<str:slug>', views.tag_detail, name='tag_detail_url'),
    path('post/<int:slug>/comment/', views.add_comment_to_post, name='add_comment_to_post')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
