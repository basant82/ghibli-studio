import requests
from django.conf import settings
import logging
from movie.exceptions import (
    GhibliMovieApiException,
    GhibliPeopleApiException,
)
from typing import Dict, List
import traceback

logger = logging.getLogger(__name__)


class GhibliStudioService:
    def __init__(self, movie_id: str = "") -> None:
        """
        initialize GhibliStudioService

        :param movie_id: movie_id of the movie
        """
        self.movie_id = movie_id

    def get_movies_api_url(self) -> str:
        """
        return movie api url to hit for movie data
        """
        return f"{settings.GHIBLI_API_BASE_URL}/films?id={self.movie_id}"

    def get_movies_data(self):
        """
        get movie data from ghibli api and return
        """
        try:
            api_response = requests.get(url=self.get_movies_api_url())
            movie_data = api_response.json()
            return movie_data
        except Exception as ex:
            logger.info(f"error in fetching movie data. ex - {traceback.format_exc}")
            raise GhibliMovieApiException

    def get_people_data(self, people_url: str) -> Dict:
        """
        get people data by people url

        :param people_url: url end point for people data
        """
        try:
            api_response = requests.get(url=people_url)
            people_details = api_response.json()
            return people_details
        except Exception as ex:
            logger.info(f"error in fetching people data. ex - {traceback.format_exc}")
            raise GhibliPeopleApiException

    def get_movie_details(self) -> List[Dict]:
        """
        return all movie details and their people
        """
        logger.info(f"request came for movie data with movie id - {self.movie_id}")
        movie_data = self.get_movies_data()

        people_info_keys = ["id", "name", "species", "url"]
        for idx, movie in enumerate(movie_data):
            movie_people_data = []
            for people_url in movie.get("people", []):
                people_data = self.get_people_data(people_url)[0]
                people_data = {
                    key: people_data.get(key, "") for key in people_info_keys
                }
                movie_people_data.append(people_data)
            movie_data[idx]["people"] = movie_people_data

        return movie_data
