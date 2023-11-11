# ghibli-studio

#### Create an endpoint to get movie data from ghibli API.

`ghibli api docs`: https://ghibli.rest/docs/


#### how to use the api

`
movie_id=d6bd6efc-37b2-4c40-b092-367cea8c88fe
endpoint: http://127.0.0.1:8000/api/v1/movies/fetch/?id=movie_id`

output for aboev query
```
[
    {
        "id": "d6bd6efc-37b2-4c40-b092-367cea8c88fe",
        "title": "The Boy and the Heron",
        "original_title": "君たちはどう生きるか",
        "original_title_romanised": "Kimitachi wa Dō Ikiru ka",
        "image": "https://static.wikia.nocookie.net/studio-ghibli/images/d/d2/How_Do_You_Live_Poster_2.jpg",
        "movie_banner": "https://static.wikia.nocookie.net/studio-ghibli/images/5/53/The_Boy_and_the_Heron_04.jpg/revision/latest/scale-to-width-down/1000?cb=20230821211402",
        "description": "The psychological growth of a teenage boy through interactions with his friends and uncle.",
        "director": "Hayao Miyazaki",
        "producer": "Toshio Suzuki",
        "release_date": "2023",
        "running_time": "124",
        "rt_score": "TBA",
        "people": [],
        "species": [
            "https://ghibli.rest/species?id=af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
        ],
        "locations": [
            "https://ghibli.rest/locations?id="
        ],
        "vehicles": [
            ""
        ],
        "url": "https://ghibli.rest/films?id=d6bd6efc-37b2-4c40-b092-367cea8c88fe"
    }
]
```


This end point will return all the movies if no query params provided. that is if `movie_id` is empty string then all movies data will be returned.

#### Process people data

For each request get the movie people. People api returns the people data with keys like: id, name, url, age. I have taken 
`"id", "name", "species", "url"` for our usecase. So in the end the end-point will return the people data in above form for all the people of a movie.

#### Authentication
I have added additional permission to check the genuine user.

`{"Authorization": ghiblikey}`


#### Exception handling and Logs
At each level I have tried to handle the possible exceptions being thrown. If something breaks at `ghibli` end that will be easily found through the error message. 
Debugging will become much easier with all the exceptions and log statement added at each points.

#### config ini
Keep all the secret information in this file like `auth key`, `password` etc.
And add it into .gitignore file to avoid commit. (I have commited this file too just to make the project runnable end to end)

#### Caching of api request

New movies are frequently asked, so there will be a lot of query and a lot of api hit. So to avoid that I have added a caching layer.
`@method_decorator(cache_page(60))`
This will keep the data of `60 seconds` in cache and delete after that.

#### Test Case
Testcase is very important part of software development. I have added tests for few files incluing the end-point by creating a fake request.






