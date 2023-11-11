from rest_framework import status


class GhibliMovieApiException(Exception):
    default_detail = "Exception in fetching Movie data."


class GhibliPeopleApiException(Exception):
    default_detail = "Exception in fetching People data."


class GhibliMovieException(Exception):
    default_detail = "Something wrong happend in getting movie data."
