Movie Recommending App using Python and JSON

Team: Maria Apitonian, Suren Chilingaryan

Course: ENGS110A Introduction to Programming

Instructor: Satenik Mnatsakanyan

Description: This app recommends movies to users based on implicit and explicit genre preferences. The app asks users to register and 
explicitly report their genre preferences, rating available genres on a scale of 1 to 10. Then, the user begins to watch and rate recommended movies.
The rating of each movie is ascribed to the rating of the genre it belongs to.

Recommendation methods: As mentioned, the app makes movie recommendations in two ways. The user either explicitly selects a genre and is recommended 3 random 
movies from that genre, or chooses to trust the app to make smart recommendations based on their watch history. In the second case, the app accesses
the average rating of each genre and picks a movie from each of the user's top 3 most highly-rated genres. The user is once again given a 
choice between these 3 movies. The app also provides additional information about the movies (director,leading actors, date and place of release) 
to help the user decide which to choose. The more movies the user watches, the more accurate the automatic recommendation method becomes!
