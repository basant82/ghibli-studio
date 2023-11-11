# ghibli-studio

#### Create an endpoint to get movie data from ghibli API.

`ghibli api docs`: https://ghibli.rest/docs/


#### how to use the api

To run the server locally run this command `python manage.py runserver 8000`. 
A local server will start. 
There are few dependecies to install like `django, rest_framework, requests`


`
movie_id=d6bd6efc-37b2-4c40-b092-367cea8c88fe
endpoint: http://127.0.0.1:8000/api/v1/movies/fetch/?id=movie_id`

output for aboev query
```
[
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
            {
                "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
                "name": "Lusheeta Toel Ul Laputa",
                "species": "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
                "url": "https://ghibli.rest/people?id=598f7048-74ff-41e0-92ef-87dc1ad980a9"
            },
            {
                "id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
                "name": "Pazu",
                "species": "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
                "url": "https://ghibli.rest/people?id=fe93adf2-2f3a-4ec4-9f68-5422f1b87c01"
            },
            {
                "id": "3bc0b41e-3569-4d20-ae73-2da329bf0786",
                "name": "Captain Dola",
                "species": "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
                "url": "https://ghibli.rest/people?id=3bc0b41e-3569-4d20-ae73-2da329bf0786"
            },
            {
                "id": "40c005ce-3725-4f15-8409-3e1b1b14b583",
                "name": "Colonel Muska",
                "species": "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
                "url": "https://ghibli.rest/people?id=40c005ce-3725-4f15-8409-3e1b1b14b583"
            },
            {
                "id": "5c83c12a-62d5-4e92-8672-33ac76ae1fa0",
                "name": "General Mouro",
                "species": "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
                "url": "https://ghibli.rest/people?id=5c83c12a-62d5-4e92-8672-33ac76ae1fa0"
            },
            {
                "id": "e08880d0-6938-44f3-b179-81947e7873fc",
                "name": "Uncle Pom",
                "species": "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
                "url": "https://ghibli.rest/people?id=e08880d0-6938-44f3-b179-81947e7873fc"
            },
            {
                "id": "2a1dad70-802a-459d-8cc2-4ebd8821248b",
                "name": "Laputian Robot",
                "species": "https://ghibli.rest/species?id=",
                "url": "https://ghibli.rest/people?id=2a1dad70-802a-459d-8cc2-4ebd8821248b"
            }
        ],
        "species": [
            "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
        ],
        "locations": [
            "https://ghibli.rest/locations?id="
        ],
        "vehicles": [
            "https://ghibli.rest/vehicles?id=4e09b023-f650-4747-9ab9-eacf14540cfb"
        ],
        "url": "https://ghibli.rest/films?id=2baf70d1-42bb-4437-b551-e5fed5a87abe"
    }
]
```


This end point will return all the movies if no query params provided. that is if `movie_id` is empty string then all movies data will be returned.

#### Process people data

For each request get the movie people. People api returns the people data with keys like: id, name, url, age. I have taken 
`"id", "name", "species", "url"` for our usecase. So in the end the end-point will return the people data in above form for all the people of a movie.

#### Authentication
I have added additional permission to check the genuine user. Header of the request must have `Authorization`

`{"Authorization": ghiblikey}`


#### Exception handling and Logs
At each level I have tried to handle the possible exceptions being thrown. If something breaks at `ghibli` end that will be easily found through the error message. 
Debugging will become much easier with all the exceptions and log statement added at each points.

#### config ini
Keep all the secret information in this file like `auth key`, `password`, `base_url` etc.
And add it into .gitignore file to avoid commit. (I have commited this file too just to make the project runnable end to end)

#### Caching of api request

New movies are frequently asked, so there will be a lot of query and a lot of api hit. So to avoid that I have added a caching layer.
`@method_decorator(cache_page(60))`
This will keep the data of `60 seconds` in cache and delete after that.

#### Test Case
Testcase is very important part of software development. I have added tests for few files incluing the end-point by creating a fake request.






