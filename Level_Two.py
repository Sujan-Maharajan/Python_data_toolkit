from dataclasses import dataclass
import csv
from words_to_num import word_into_number

@dataclass
class Record:
    id: str
    name: str
    age: str
    city: str
    score: str

    def is_valid(self,duplicate_id=False):
        errors= self.get_errors(duplicate_id)

        if len(errors)==0:
            return True
        else:
            return False

    def get_errors(self,duplicate_id=False):
        errors= []

        if self.id.strip()=="":
            errors.append("id is empty")

        if duplicate_id:
            errors.append("id is duplicate")

        if self.name.strip()=="":
            errors.append("name is empty")

        if self.age.strip()=="":
            errors.append("age is empty")
        else:
            try:
                age= int(self.age)

                if age<0 or age>120:
                    errors.append("age is not in range")

            except ValueError:
                errors.append("age is not a number")

        if self.city.strip()=="":
            errors.append("city is empty")

        if self.score.strip()=="":
            errors.append("score is empty")
        else:
            try:
                score= float(self.score)

                if score<0 or score>100:
                    errors.append("score is not in range")

            except ValueError:
                errors.append("score is not a number")
        
        return errors

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
        
with open('messy_people.csv','r') as file:
    read_FILE= csv.DictReader(file)
    data= list(read_FILE)

cleaned_records= []
valid_ages= []
duplicate_count= 0
seen_ids= set()

#Collectting valid ages for mean

for i in data:
    age= clean_age(i["age"])

    if age is not None:
        valid_ages.append(age)

mean_age= sum(valid_ages)/len(valid_ages)
print("Mean Age=",mean_age)


for i in data:
    obj= Record(i["id"], i["name"], i["age"], i["city"], i["score"])

    age= clean_age(obj.age,mean_age)

    if age is None:
        continue

    obj.age= (age)

    if obj.id.strip()=="":
        continue

    if obj.id in seen_ids:
        duplicate_count+= 1
        continue

    seen_ids.add(obj.id)
    cleaned_records.append(obj)
        

print("Cleaned Records=",len(cleaned_records))
print("Duplicate Ids=",duplicate_count)

print("\nCleaned records are:")
for record in cleaned_records:
    print(record)