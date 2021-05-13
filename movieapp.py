import json

def load_movies():
    with open('moviedatabase.json') as database:
        movies = json.load(database)
    return movies

def load_users():
    with open('appusers.json') as users:
        users = json.load(users)
    return users

def save_to_file(users):
    jsonfile = open("appusers.json","w")
    jsonfile.write(json.dumps(users,indent = 2))
    jsonfile.close()

def user_registration():
    user = {
	    "username": "",
            "age": 0,
            "gender": "",
            "fav_director": [],
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
 
    user["username"] = input("Please insert a username ")
   
    age = input("What is your age? ")
    while(True):
        if(age.isnumeric()):
            user["age"] = int(age)
            break
        else:
            age = input("Please input a valid number for your age: ")
    
    gender = input("What is your gender \n F/m: ")
    while(True):
        if((gender != "M") and (gender != "F")):
            print("Invalid input. Please insert 'F' or 'M': ")
        else:
            user["gender"] = gender
            break

    print("Please rate the following genres on a scale of 0 to 10.")
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
 

def main():
    movies = []
    movies = load_movies()
    users = []
    users = load_users()
    print("Welcome to the Movie Recommendation App! \n")
    user_status = input("Do you wish to \n A. Log in \n B. Sign up? \n A/B: ")
    while (True):
        if(user_status=="A"):
            username(input("Please insert your username: "))
            check_username(username)
            break 
        elif(user_status=="B"):
            user = user_registration()
            users.append(user)
            save_to_file(users)
            break
        else:
            user_status = input("Your input could not be read. Please answer with 'A' for log in or 'B' for sign up: \n A/B: ")



main()

