from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog_main import views as main_views
from blogs import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', main_views.home, name='home'),

    # Blog
    path('category/<int:category_id>/', blog_views.posts_by_category, name='posts_by_category'),
    path('search/', blog_views.search, name='search'),
    path('categories/', blog_views.categories_list, name='categories_list'),

    # Auth
    path('register/', main_views.register, name='register'),
    path('login/', main_views.user_login, name='login'),
    path('logout/', main_views.user_logout, name='logout'),

    # Dashboard
    path('dashboard/', include('dashboards.urls')),

    # Comments
    path('delete-comment/<int:comment_id>/', blog_views.delete_comment, name='delete_comment'),

    # Slug MUST be last
    path('<slug:slug>/', blog_views.blogs, name='blogs'),
]

# Serve media & static in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
