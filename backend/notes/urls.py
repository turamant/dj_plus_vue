
from rest_framework import routers

from .views import NoteViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register('notes', NoteViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls