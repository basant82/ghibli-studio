from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from ghibli_project.api.ghibli.service import GhibliStudioService
from .permissions.custom_permissions import GhibliApiPermissions
import logging
from movie.exceptions import GhibliMovieException
import traceback

logger = logging.getLogger(__name__)


class MovieViewset(viewsets.ViewSet):
    """
    Movie View set to get the movie details
    decorator will keep the data of 1 min in cache to avoid hitting api for frequently asked movie
    permission will check the auth key to validate the genuine user
    """

    @method_decorator(cache_page(60))
    @action(
        detail=False,
        methods=["get"],
        url_path="fetch",
        permission_classes=[GhibliApiPermissions],
    )
    def get_movies_details(self, request) -> Response:
        """
        get movie details
        if no movie_id is being passed then whole movie data will be returned
        """
        try:
            logger.info(f"fetch movie data")
            movie_id = request.GET.get("id", "")
            movie_data = GhibliStudioService(movie_id=movie_id).get_movie_details()
            return Response(movie_data)
        except Exception as ex:
            logger.info(f"error in getting movie details. ex - {traceback.format_exc}")
            raise GhibliMovieException
