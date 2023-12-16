from filmsai_rest import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('films', views.FilmsViewSet, basename='films')
router.register('comments', views.CommentsViewSet, basename='comments')

urlpatterns = router.urls