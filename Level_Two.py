from words_to_num import word_into_number
from dataclasses import dataclass
import csv

@dataclass
class Record:
    id: str
    name: str
    age: int
    city: str
    score: float

    # def is_valid(self,duplicate_id=False):
    #     errors= self.get_errors(duplicate_id)

    #     if len(errors)==0:
    #         return True
    #     else:
    #         return False

    # def get_errors(self,duplicate_id=False):
    #     errors= []

    #     if self.id.strip()=="":
    #         errors.append("id is empty")

    #     if duplicate_id:
    #         errors.append("id is duplicate")

    #     if self.name.strip()=="":
    #         errors.append("name is empty")

    #     if self.age.strip()=="":
    #         errors.append("age is empty")
    #     else:
    #         try:
    #             age= int(self.age)

    #             if age<0 or age>120:
    #                 errors.append("age is not in range")

    #         except ValueError:
    #             errors.append("age is not a number")

    #     if self.city.strip()=="":
    #         errors.append("city is empty")

    #     if self.score.strip()=="":
    #         errors.append("score is empty")
    #     else:
    #         try:
    #             score= float(self.score)

    #             if score<0 or score>100:
    #                 errors.append("score is not in range")

    #         except ValueError:
    #             errors.append("score is not a number")
        
    #     return errors

def clean_age(age,mean_age=None):
    age= age.strip()

    try:
        age= int(age)

    except ValueError:
        if age in word_into_number:
            age= word_into_number[age]
        else:
            return mean_age
        
    if age<0 or age>120:
        return None

    return age

def clean_name(name):
    name= name.strip()

    if name=="":
        return "Unknown name"

    return name

def clean_city(city):
    city= city.strip()

    if city=="":
        return "Unknown city"

    return city

def clean_score(score, mean_score=None):
    score= score.strip()

    try:
        score= float(score)

    except ValueError:
        return mean_score

    if score<0 or score>100:
        return None

    return score

if __name__== "__main__":
    
    with open('messy_people.csv','r') as file:
        read_FILE= csv.DictReader(file)
        data= list(read_FILE)

    cleaned_records= []
    valid_ages= []
    valid_scores= []
    duplicate_count= 0
    skipped_count= 0
    seen_ids= set()

    #Collectting valid ages and valid scores for mean

    for i in data:
        age= clean_age(i["age"])

        if age is not None:
            valid_ages.append(age)

        score= clean_score(i["score"])

        if score is not None:
            valid_scores.append(score)

    mean_age= sum(valid_ages)/len(valid_ages)
    mean_score= sum(valid_scores)/len(valid_scores)

    for i in data:
        obj= Record(i["id"], i["name"], i["age"], i["city"], i["score"])

        age= clean_age(obj.age,mean_age)

        if age is None:
            skipped_count+= 1
            continue

        obj.age= age
        obj.name= clean_name(obj.name)
        obj.city= clean_city(obj.city)

        score= clean_score(obj.score,mean_score)

        if score is None:
            skipped_count+= 1
            continue

        obj.score= score

        if obj.id.strip()=="":
            skipped_count+= 1
            continue

        if obj.id in seen_ids:
            duplicate_count+= 1
            continue

        seen_ids.add(obj.id)
        cleaned_records.append(obj)

    total_skipped= skipped_count + duplicate_count
            
    print("Total Records=",len(data))
    print("Mean Age=",mean_age)
    print("Mean Score=",mean_score)
    print("Cleaned Records=",len(cleaned_records))
    print("Duplicate Ids=",duplicate_count)
    print("Total Skipped Rows=",total_skipped)

    print("\nCleaned records are:")
    for record in cleaned_records:
        print(record)