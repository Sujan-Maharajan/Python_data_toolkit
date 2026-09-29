from Level_One import Record
from Level_Three import Dataset
import time

dataset= Dataset()
dataset.load("messy_people.csv")
dataset.clean()

def log_time(func):
    def wrapper(*args,**kwargs):
        start_time= time.time()

        result= func(*args,**kwargs)

        end_time= time.time()

        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")

        return result

    return wrapper

@log_time
def average_score(dataset: Dataset) -> float:
    total_score= 0

    for record in dataset.records:
        total_score+= record.score
    average= total_score/ len(dataset.records)

    return average
print("Average Score:",average_score(dataset))

def people_per_city(dataset: Dataset) -> dict:
    city_count= {}

    for record in dataset.records:
        city= record.city

        if city not in city_count:
            city_count[city]= 1
        else:
            city_count[city]+=1
    return city_count
print("People per city:", people_per_city(dataset))

def highest_age(dataset: Dataset) -> Record:
    highest_age= dataset.records[0]

    for record in dataset.records:
        if record.age > highest_age.age:
            highest_age= record

    return highest_age
print("Highest age:",highest_age(dataset))

def lowest_age(dataset: Dataset) -> Record:
    lowest_age= dataset.records[0]

    for record in dataset.records:
        if record.age < lowest_age.age:
            lowest_age= record

    return lowest_age
print("Lowest age:",lowest_age(dataset))