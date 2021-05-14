****Movie Recommending App using python and json
__Team: Maria Apitonian, Suren Chilingaryan
__Course: ENGS110A Introduction to Programming
__Instructor: Satenik Mnatsakanyan

Description: This app recommends movies to users based on implicit and explicit genre preferences. The app asks users to register and 
explicitly report their genre preferences, rating 7 genres on a scale of 1 to 10. Then, the user begins to watch and rate recommended movies.
The rating of each movie is ascribed to the rating of the genre it belongs to.

Method: As mentioned, the app makes movie recommendations in two ways. The user either explicitly selects a genre and is recommended 3 random movies
from that genre, or chooses to trust the app to make smart recommendations based on their watch history. In the second case, the app accesses
the average rating of each genre and picks a movie from each of the user's top genres. The user is once again given a choice between 3 movies of
different genres.
