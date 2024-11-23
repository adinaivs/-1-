from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import register, UserLoginView, UserLogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
]

# Обработка медиафайлов
if settings.DEBUG:  # Только в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
