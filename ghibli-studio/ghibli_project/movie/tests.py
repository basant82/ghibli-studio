from unittest.mock import patch, Mock
from .views import MovieViewset
from ghibli_project.api.ghibli.service import GhibliStudioService
from django.conf import settings
from unittest import TestCase
from django.test import RequestFactory


class GhibliEndPointTestCase(TestCase):
    """
    Test ghibli api method
    """

    def __init__(self, methodName: str = ...) -> None:
        """
        initialize the testcase
        """
        super().__init__(methodName)
        self.movie_data = [
            {
                "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
                "title": "Castle in the Sky",
                "original_title": "天空の城ラピュタ",
                "original_title_romanised": "Tenkū no shiro Rapyuta",
                "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/npOnzAbLh6VOIu3naU5QaEcTepo.jpg",
                "movie_banner": "https://image.tmdb.org/t/p/w533_and_h300_bestv2/3cyjYtLWCBE1uvWINHFsFnE8LUK.jpg",
                "description": "The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
                "director": "Hayao Miyazaki",
                "producer": "Isao Takahata",
                "release_date": "1986",
                "running_time": "124",
                "rt_score": "95",
                "people": [
                    "https://ghibli.rest/people?id=598f7048-74ff-41e0-92ef-87dc1ad980a9",
                    "https://ghibli.rest/people?id=fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
                    "https://ghibli.rest/people?id=3bc0b41e-3569-4d20-ae73-2da329bf0786",
                    "https://ghibli.rest/people?id=40c005ce-3725-4f15-8409-3e1b1b14b583",
                    "https://ghibli.rest/people?id=5c83c12a-62d5-4e92-8672-33ac76ae1fa0",
                    "https://ghibli.rest/people?id=e08880d0-6938-44f3-b179-81947e7873fc",
                    "https://ghibli.rest/people?id=2a1dad70-802a-459d-8cc2-4ebd8821248b",
                ],
                "species": [
                    "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
                ],
                "locations": ["https://ghibli.rest/locations?id="],
                "vehicles": [
                    "https://ghibli.rest/vehicles?id=4e09b023-f650-4747-9ab9-eacf14540cfb"
                ],
                "url": "https://ghibli.rest/films?id=2baf70d1-42bb-4437-b551-e5fed5a87abe",
            }
        ]

    def setUp(self) -> None:
        """
        set up the testcase
        """
        super().setUp()

    @patch("ghibli_project.api.ghibli.service.GhibliStudioService.get_movie_details")
    def test_movie_api_endpoint_status_code(self, mock_movie_api):
        """
        test get_movies_details end point
        """

        request_obj = RequestFactory().get("/api/v1/movies/fetch/", {"id": ""})
        mock_movie_api.return_value = self.movie_data
        movie_api_data = MovieViewset().get_movies_details(request_obj)
        self.assertEqual(movie_api_data.status_code, 200)

    @patch("ghibli_project.api.ghibli.service.GhibliStudioService.get_movie_details")
    def test_movie_api_data(self, mock_movie_api):
        """
        test movie_api_data method
        """
        request_obj = RequestFactory()
        request_obj = request_obj.get("/movie/fetch/", {"id": ""})
        mock_movie_api.return_value = self.movie_data
        movie_api_data = MovieViewset().get_movies_details(request_obj)
        expected_people_data = self.movie_data[0]["people"]
        calculated_people_data = movie_api_data.data[0]["people"]
        self.assertListEqual(expected_people_data, calculated_people_data)


class GhibliStudioServiceTestCase(TestCase):
    """
    test ghibli studio service method
    """

    def setUp(self) -> None:
        """
        set up the test case
        """
        return super().setUp()

    def test_get_people_details(self):
        """
        test people details api data
        """
        ghibli_api_base_url = settings.GHIBLI_API_BASE_URL
        # empty people id should  return all people data
        people_id = ""
        people_url = f"{ghibli_api_base_url}/people?id={people_id}"
        people_api_data = GhibliStudioService().get_people_data(people_url=people_url)
        self.assertIsInstance(people_api_data, list)
