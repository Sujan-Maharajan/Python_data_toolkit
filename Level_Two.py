from dataclasses import dataclass
import csv

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
        
with open('messy_people.csv','r') as file:
    read_FILE= csv.DictReader(file)
    data= list(read_FILE)

valid_records= []
invalid_records= []
duplicate_count= 0
seen_ids= set()

for i in data:
    obj= Record(i["id"], i["name"], i["age"], i["city"], i["score"])

    if obj.id.strip()!="":

        if obj.id in seen_ids:
            duplicate_id= True
            duplicate_count+= 1
        else:
            duplicate_id= False
            seen_ids.add(obj.id)

    else:
        duplicate_id= False

    if obj.is_valid(duplicate_id):
        valid_records.append(obj)
    else:
        invalid_records.append((obj,duplicate_id))
        

print("Valid Records=",len(valid_records))
print("Invalid Records=",len(invalid_records))
print("Duplicate Ids=",duplicate_count)

print("\nValid records are:")
for record in valid_records:
    print(record)

print("\nInvalid records are:")
for record, duplicate_id in invalid_records:
    print(record)
    print(record.get_errors(duplicate_id))