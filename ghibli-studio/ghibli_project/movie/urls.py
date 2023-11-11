from rest_framework import routers
from .views import MovieViewset

__author__ = "root"

urlpatterns = []

router = routers.SimpleRouter()


router.register("api/v1/movies", MovieViewset, basename="MovieViewset")

urlpatterns += router.urls
