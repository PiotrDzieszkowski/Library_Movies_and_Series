from secrets import choice
from string import capwords
from faker import Faker
import random
from datetime import date
today = date.today()
fake = Faker()

type = ["science fiction", "fantasy", "drama", "romance", "comedy", "zombie", "action", "historical", "horror", "war"]
choice = random.choice(type)

movies_and_series = []

class Movie:
    def __init__(self, title, year, type, watched):
        self.title = title
        self.year = year
        self.type = type
        self.watched = watched
    def __str__(self):
        return f'Film: "{self.title} {self.year} {self.type} {self.watched}"'
    def __repr__(self):
        return f"{self.title} {self.year} {self.type} {self.watched}"
    def play(self, watched=1):
        self.watched += watched

class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.episode = episode
        self.season = season
    def __str__(self):
        return f'Serial: "{self.title} {self.year} {self.type} S{self.season:02d} E{self.episode:02d} {self.watched}"'
    def __repr__(self):
        return f"{self.title} {self.year} {self.type} S{self.season:02d} E{self.episode:02d} {self.watched}"

def create_library(number_of):
    
    movies_and_series = []
    for n in range(number_of):
        #zapomniałem jak z listy wybrać dowolne słowo
        movie = Movie(title=fake.word().title(), year=fake.year(), type=random.choice(type), watched=fake.random_int(0,20))
        movies_and_series.append(movie)   
    for n in range(number_of):
        series = Series(title=fake.word().title(), year=fake.year(), type=fake.word(), watched=fake.random_int(0,20), episode=fake.random_int(1,20), season=fake.random_digit_not_null())
        movies_and_series.append(series)
    return movies_and_series  

def get_movies(mylist):
    sorted_movies = []
    
    for n in mylist:
        if isinstance(n, Movie) and not isinstance(n, Series):
            sorted_movies.append(n)
    sorted_movies = sorted(sorted_movies, key=lambda movie:movie.title)
    return sorted_movies

def get_series(mylist):
    sorted_movies = []
    
    for n in mylist:
        if isinstance(n, Series):
            sorted_movies.append(n)
    sorted_movies = sorted(sorted_movies, key=lambda series:series.title)
    return sorted_movies

def decorator(func):
    def wrapper(mylist):
        for _ in range(10):
            func(mylist)
    return wrapper
@decorator
def generate_views(mylist):
    n = len(mylist)-1
    random_number = fake.random_int(0, n, 1)
    mylist[random_number].watched = fake.random_int(0, 100, 1)
    print(mylist[random_number])
    
def top_titles(mylist,number):

    by_titles = sorted(mylist, key=lambda movie: movie.watched, reverse=True)
    result = []
    for i in range(number):
        result.append(by_titles[i])
    
    return result
while True:
    Top_5 = create_library(5)
    print("\n")
    print("Library of Movies and Series")
    print('Today Date: {}\n'.format(today.strftime("%d/%m/%Y")))
    print("Top 5:")
    for i in range(len(Top_5)):
        print(Top_5[i])
    print("\n")


    only_movies = get_movies(Top_5)
    print("Movies:")
    for i in range(len(only_movies)):
        print(only_movies[i])

    print("\n")

    only_series = get_series(Top_5)
    print("Series:")
    for i in range(len(only_series)):
        print(only_series[i])

    print("\n")


    print("The most frequently viewing titles: ")
    generate_views(Top_5)

    print("\n")

    print("\n")


    print("The most popular titles:")
    display = 6
    for i in range(display):
        print(top_titles(Top_5, display)[i])

    print("\n")

    def content_type(genre_type, quantity):

        quantity = int(quantity)
    
        contacts =[]
        print('Today Date: {}\n'.format(today.strftime("%d/%m/%Y")))
        if genre_type == "M":
            for n in range(quantity):
                fake = Faker()
                contact = Movie(title=fake.word().title(), year=fake.year(), type=random.choice(type), watched=fake.random_int(0,20))
                contacts.append(contact)
        if genre_type == "S":
            for n in range(quantity):
                fake = Faker()
                contact = Series(title=fake.word().title(), year=fake.year(), type=fake.word(), watched=fake.random_int(0,20), episode=fake.random_int(1,20), season=fake.random_digit_not_null())
                contacts.append(contact)
        for n in contacts:
            print(n)

    
   
    while True:
        genre_type = input("Want to see the most popular: Movies [M] or Series [S]? ")    
        quantity = input("How many views you want to see. Give me a number? " )
        content_type(genre_type, quantity)