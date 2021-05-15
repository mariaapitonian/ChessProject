import json
import random
import heapq

def load_movies():
    with open('moviedatabase.json') as database:
        movies = json.load(database)
    return movies

def load_users():
    with open('appusers.json') as users:
        users = json.load(users)
    return users





def test_new_user_username(users, username):
    for user in users:
        if(username==user["username"]):
            username = input("This username is taken. Please insert a different username")
    return username

def save_new_user(users):
    jsonfile = open("appusers.json", "w")
    jsonfile.write(json.dumps(users, indent = 2))
    jsonfile.close()

def load_old_user_info(username, users):
    while(True):
        for user in users:
            if(username==user["username"]):
                user_info = user
                return user_info
        username = input("Such a user does not exist. Please insert an existing username: ")





def user_registration(users, available_genres):
    user_info = {
	    "username": "",
            "age": 0,
            "gender": "",
	    "genre_history":[]
    }
   
    username = input("Please insert a username: ")
    user_info["username"] = test_new_user_username(users, username)
   
    age = input("What is your age? ")
    while(True):
        if(age.isnumeric()):
            user_info["age"] = int(age)
            break
        else:
            age = input("Please input a valid number for your age: ")
    
    gender = input("What is your gender? \n F/M: ")
    while(True):
        if((gender != "M") and (gender != "F")):
            print("Invalid input. Please insert 'F' or 'M': ")
        else:
            user_info["gender"] = gender
            break

    print("Please rate the following genres on a scale of 0 to 10. This will help us make better recommendations for you in the future:)")
    for genre in available_genres:
        user_genre = {
            "name":"",
            "movies":[],
            "average_rating":0
        }
        user_genre["name"] = genre
        print("\n", genre)
        rating = input("Rating: ")
        while(True):
            if((rating.isnumeric()) and (int(rating) <= 10) and (int(rating) >= 0)):
                user_genre["average_rating"] = int(rating)
                break
            else:
                rating = input("\n Please input a valid rating between 0 and 10: ")
        user_info["genre_history"].append(user_genre)
     
    return user_info
 




def random_recommendation(preferences, movies, available_genres):
    appropriate_movies = []
    random_values = []
    recommendations = []
            
    print("The available genres are: ")
    for genre in available_genres:
        print(genre, ", ")
    current_genre = input("\n Please type out the name of the genre you want to watch: ")

    #generating recommendations
    while(True):
        for movie in movies:
            if(current_genre==movie["Genre"]):
                appropriate_movies.append(movie)
        n = len(appropriate_movies)
        if(n==0):
            current_genre = input("We are sorry, we do not have movies of this genre. Please insert an appropriate genre name: ")
        else:
            break

    random_values = random.sample(range(0, n), 3)
    for value in random_values:
        recommendations.append(appropriate_movies[value])


    #checking which recommendation the user wants
    print("\n Based on your selected genre, we have generated three recommendations for you. Do you want to watch: \n")

    for i in range(0, 3):
        j=i+1
        print(j, ") ", recommendations[i]["Film Name"], "\n   Director: ", recommendations[i]["Director"], "\n   Leading actors: ", recommendations[i]["Leading actors"], "\n   Year of Release: ", recommendations[i]["Year of release"], "\n   Place of Release: ", recommendations[i]["Place of release"], "\n") 
    print("4 ) Thank you, none of the above \n")
    
    while(True):
        number = input("1/2/3/4: ")
        if((number.isnumeric()) and (int(number) <=3) and (int(number) >= 1)):
            selected_movie = recommendations[(int(number)-1)]
            return selected_movie
        elif((number.isnumeric()) and (int(number)==4)):
            return False
        else:
            number = input("Please insert a valid number between 1 and 4: ")


def smart_recommendation(preferences, movies):
    recommendations = []
    #determining top 3 genres with highest cumulative average ratings
    genres = []
    average_ratings = []

    for genre in preferences:
        genres.append(genre["name"])
        average_ratings.append(int(genre["average_rating"]))
        
    zip_temp = zip(genres, average_ratings)
    zip_top = heapq.nlargest(3, zip_temp)
    top_genres, top_ratings = zip(*zip_top)
    
    #randomly selecting a movie from each top genre
    for genre in top_genres:
        appropriate_movies = []
        for movie in movies:
            if(genre==movie["Genre"]):
                appropriate_movies.append(movie)
        n = len(appropriate_movies)
        recommendations.append(appropriate_movies[random.randint(0, (n-1))])      
    
    #checking which recommendation the user wants
    print("\n Based on your rating history, we have generated three recommendations for you. Do you want to watch: \n")

    for i in range(0, 3):
        j=i+1
        print(j, ") ", recommendations[i]["Film Name"], "\n   Genre: ", recommendations[i]["Genre"], "\n   Director: ", recommendations[i]["Director"], "\n   Leading actors: ", recommendations[i]["Leading actors"], "\n   Year of Release: ", recommendations[i]["Year of release"], "\n   Place of Release: ", recommendations[i]["Place of release"], "\n") 
    print("4 ) Thank you, none of the above \n")
    
    while(True):
        number = input("1/2/3/4: ")
        if((number.isnumeric()) and (int(number) <=3) and (int(number) >= 1)):
            selected_movie = recommendations[(int(number)-1)]
            return selected_movie
        elif((number.isnumeric()) and (int(number)==4)):
            return False
        else:
            number = input("Please insert a valid number between 1 and 4: ")





def rate_movie():
    rating = input("We will wait for you to watch this movie. Once you have done so, please insert a rating from 0 to 10: ")
    while(True):
        if((rating.isnumeric()) and (int(rating)<=10) and (int(rating)>=0)):
            return rating
        else:
            rating = input("Please insert a valid number between 0 and 10: ")


def update_watch_history(rating, selected_movie, user_info):
    #for old genres
    for g in user_info["genre_history"]:
        if(g["name"]==selected_movie["Genre"]):
            g["average_rating"] = (int(g["average_rating"])*(len(g["movies"])+1)+(int(rating)))/(len(g["movies"])+2)
            (g["movies"]).append(selected_movie)
            return user_info
    
    #for new genres
    new_genre = {"name":"",
            "movies":[],
            "average_rating":0
    }
    new_genre["name"] = selected_movie["Genre"]
    new_genre["average_rating"] = int(rating)
    new_genre["movies"].append(selected_movie)
    user_info["genre_history"].append(new_genre)
    return user_info





def main():
    movies = []
    movies = load_movies()

    users = []
    users = load_users()

    available_genres = []
    for movie in movies:
        available_genres.append(movie["Genre"])
    available_genres = list(dict.fromkeys(available_genres))    
    
    print("Welcome to the Movie Recommendation App! \n")

    user_status = input("Do you wish to \n A. Log in \n B. Sign up? \n A/B: ")
    while (True):
        if(user_status=="A"):
            username = (input("Please insert your username: "))
            user_info = load_old_user_info(username, users)
            preferences = user_info["genre_history"]
            break 
        elif(user_status=="B"):
            user_info = user_registration(users, available_genres)
            users.append(user_info)
            save_new_user(users)
            preferences = user_info["genre_history"]
            break
        else:
            user_status = input("Your input could not be read. Please answer with 'A' for log in or 'B' for sign up: \n A/B: ")

    print("You are now logged in!")

    current_preference = input("Is there a particular genre of movie you would like to watch right now? If not, we will give you recommendations based on your user history and account information! \nY/N: ")
    
    while(True):
        if(current_preference=="N"):
            selected_movie = smart_recommendation(preferences, movies)
            break
        elif(current_preference=="Y"):
            selected_movie = random_recommendation(preferences, movies, available_genres)
            break
        else:
            current_preference = input("Please answer with 'Y' or 'N'")

    if(selected_movie):
        print("You have selected ", selected_movie["Film Name"], ". Good choice!")
        rating = rate_movie()
        print("You have rated ", selected_movie["Film Name"], rating, "out of 10. Thank you for your feedback :) Goodbye!")
                
        updated_user = update_watch_history(rating, selected_movie, user_info)
        users.remove(user_info)
        users.append(updated_user)
        save_new_user(users)
    else:
        print("Okay! Hope we can give you better recommendations next time. Goodbye!")







main()

