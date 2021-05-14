import json
import random


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
                preferences = user["genres"]
                return preferences
        username = input("Such a user does not exist. Please insert an existing username: ")



def user_registration(users):
    user = {
	    "username": "",
            "age": 0,
            "gender": "",
	    "fav_genre": [],
            "genres":[
            {   "name":"Romance",
                "movies":[],
                "movie_number":1,
                "average_rating":0
            },
            {   "name":"Crime",
                "movies":[],
                "movie_number":1,
                "average_rating":0
            },
            {   "name":"Action",
                "movies":[],
                "movie_number":1,
                "average_rating":0
            },
            {   "name":"Drama",
                "movies":[],
                "movie_number":1,
                "average_rating":0
            },
            {   "name":"Sci-Fi and Fantasy",
                "movies":[],
                "movie_number":1,
                "average_rating":0
            },
            {   "name":"Horror",
                "movies":[],
                "movie_number":1,
                "average_rating":0
            },
            {   "name":"Comedy",
                "movies":[],
                "movie_number":1,
                "average_rating":0
            }
        ]       

    }
 
    username = input("Please insert a username: ")
    test_new_user_username(users, username)
   
    age = input("What is your age? ")
    while(True):
        if(age.isnumeric()):
            user["age"] = int(age)
            break
        else:
            age = input("Please input a valid number for your age: ")
    
    gender = input("What is your gender? \n F/M: ")
    while(True):
        if((gender != "M") and (gender != "F")):
            print("Invalid input. Please insert 'F' or 'M': ")
        else:
            user["gender"] = gender
            break

    print("Please rate the following genres on a scale of 0 to 10. This will help us make better recommendations for you in the future:)")
    for genre in user["genres"]:
        print("\n", genre["name"])
        rating = input("Rating: ")
        while(True):
            if((rating.isnumeric()) and (int(rating) <= 10) and (int(rating) >= 0)):
                genre["average_rating"] = int(rating)
                break
            else:
                rating = input("\n Please input a valid rating between 0 and 10: ")
    
    return user
 

def random_recommendation(preferences, movies):
    appropriate_movies = []
    random_values = []
    recommendations = []
            
    
    current_genre = input("The available genres are Crime, Comedy, Sci-Fi and Fantasy, Romance, Horror, Action, Drama. Please type out the name of the genre you want to watch:")

        #generating recommendations
    for movie in movies:
        if(current_genre==movie["Genre"]):
            appropriate_movies.append(movie)
    n = len(appropriate_movies)

    random_values = random.sample(range(0, n), 3)

    print(random_values)
    for value in random_values:
        recommendations.append(appropriate_movies[value])


        #checking which recommendation the user wants
    print("\n Based on your selected genre, we have generated three recommendations for you. Do you want to watch: \n")

    for i in range(0, 3):
        print(i, ") Film Name: ", recommendations[i]["Film Name"], "\n")
        #print(i, ") Film Name: ", recommendations[i]["Film Name"], "\n   Director: " recommendations[i]["Director"], "\n   Leading actors: ", recommendations[i]["Leading actors"], "\n   Year of Release: ", recommendations[i]["Year of release"], "\n   Place of Release: ", recommendations[i]["Place of release"], "\n") 
    print("4) Thank you, none of the above \n")
    

    while(True):
        number = input("1/2/3/4: ")
        if((number.isnumeric()) and (int(number) <=3) and (int(number) >= 1)):
            selected_movie = recommendations[(int(number)-1)]
            return selected_movie
        elif((number.isnumeric()) and (int(number)==4)):
            return False
        else:
            number = input("Please insert a valid number between 1 and 4")

#def smart_recommendation(preferences, movies):
    

def main():
    movies = []
    movies = load_movies()
    users = []
    users = load_users()

    print("Welcome to the Movie Recommendation App! \n")

    user_status = input("Do you wish to \n A. Log in \n B. Sign up? \n A/B: ")
    while (True):
        if(user_status=="A"):
            username = (input("Please insert your username: "))
            preferences = load_old_user_info(username, users)
            break 
        elif(user_status=="B"):
            user = user_registration(users)
            users.append(user)
            save_new_user(users)
            preferences = user["genres"]
            break
        else:
            user_status = input("Your input could not be read. Please answer with 'A' for log in or 'B' for sign up: \n A/B: ")

    print("You are now logged in!")



    current_preference = input("Is there a particular genre of movie you would like to watch right now? If not, we will give you recommendations based on your user history and account information! \nY/N: ")
    

    while(True):
        #if(current_preference=="N"):
            #selected_movie = smart_recommendation(preferences, movies)
            #break
        if(current_preference=="Y"):
            selected_movie = random_recommendation(preferences, movies)
            if(selected_movie):
                print("You have selected ", selected_movie["Film Name"], ". Good choice!")
                #rating = rate_movie()
                break
            else:
                print("Okay! Hope we can give you better recommendations next time")
                break
        else:
            current_preference = input("Please answer with 'Y' or 'N'")








main()

