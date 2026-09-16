from dataclasses import dataclass
import csv

@dataclass
class Record:
    id: str
    name: str
    age: str
    city: str
    score: str

    def is_valid(self):
        if self.id.strip()!="" and self.name.strip()!="" and self.age.strip()!="" and self.city.strip()!="" and self.score.strip()!="":
            return True
        else:
            return False

    def get_errors(self):
        errors= []

        if self.id.strip()=="":
            errors.append("id is empty")
        if self.name.strip()=="":
            errors.append("name is empty")

        if self.age.strip()=="":
            errors.append("age is empty")
        else:
            try:
                int(self.age)
            except ValueError:
                errors.append("age is not a number")

        if self.city.strip()=="":
            errors.append("city is empty")
        if self.score.strip()=="":
            errors.append("score is empty")
        return errors
        
with open('messy_people.csv','r') as file:
    read_FILE= csv.DictReader(file)
    data= list(read_FILE)

valid_records= []
invalid_records= []

for i in data:
    obj= Record(i["id"], i["name"], i["age"], i["city"], i["score"])
    if obj.is_valid():
        valid_records.append(obj)
    else:
        invalid_records.append(obj)
        

print("Valid Records=",len(valid_records))
print("Invalid Records=",len(invalid_records))

print("\nValid records are:")
for record in valid_records:
    print(record)

print("\nInvalid records are:")
for record in invalid_records:
    print(record)
    print(record.get_errors())