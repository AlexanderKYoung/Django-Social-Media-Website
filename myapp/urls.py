  
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ActivityCreateView, ActivityDetailView, ActivityListView, ActivityReplyCreateView, CalendarView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ReplyCreateView, PostNotification, DeleteNotification
from . import views
urlpatterns = [
    path('home/', PostListView.as_view(), name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('upload/', views.showfile, name='upload'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    #path('reply/<int:pk>/', ReplyDetailView.as_view(), name="reply-detail"),
    path('post/<int:pk>/reply/', ReplyCreateView.as_view(), name="reply-create"),
    path('notification/delete/<int:notification_pk>', DeleteNotification.as_view(), name="notification-delete"),
    path('notification/<int:notification_pk>/post/<int:post_pk>', PostNotification.as_view(), name="post-notification"),
    path('activity/', ActivityListView.as_view(), name="activity"),
    path('health/', views.health, name="health"),
    path('shopping/', views.shopping, name="shopping"),
    path('shopping-detail', views.shoppingDetail, name="shopping-detail"),
    path('meeting/', views.meeting, name="meeting"),
    path(r'^calendar/$', views.CalendarView.as_view(), name="calendar"),
    path('activity/new/', ActivityCreateView.as_view(), name="make-activity"),
    path('meeting/new/', views.makeMeeting, name="make-meeting"),
    path('activity/<int:pk>/', ActivityDetailView.as_view(), name="activity-detail"),
    path('activity/<int:pk>/reply/', ActivityReplyCreateView.as_view(), name="reply-create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)