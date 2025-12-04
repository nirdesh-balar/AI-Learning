import json

def load_data(filename):
    with open(filename,"r") as f:
        data = json.load(f)

    return data

data = load_data("data.json")
#print(data)

# cleaning and structuring data

def clean_data(data):
    text_to_num = {"one":1,"two":2,"three":3,"four":4}
    cleaned_data = []
    unique_data = set()
    for user in data:
        # Clean rating
        raw_rating = str(user["rating"]).strip().lower()
        if(raw_rating in text_to_num):
            raw_rating = text_to_num[raw_rating]

        user["rating"] = raw_rating

        # Handle missing vlaue
        raw_age = user.get("age")
        if(raw_age == None):
            user["age"] = None

        #deduplaction 
        
        if(user["name"].strip() in unique_data):
            continue
        unique_data.add(user["name"])
        cleaned_data.append(user)

    return cleaned_data
data_f = clean_data(data)

# avg of rating and % of poor rating 
def avg_rating(data):
    sum = 0
    for i in data:
        sum = sum + float(i["rating"])
    avg = sum / len(data)
    print(avg)
    poor_rating=0
    for i in data:
        if (float(i["rating"])<3):
            poor_rating +=1
    presentage_poor_rating = poor_rating*100/len(data)
    print(presentage_poor_rating)


#print(avg_rating(data_f))

# Recommendation 

def recommendation(data):
    recomm = []

    for user in data :
        current_recomm = {}
        current_recomm["name"] = user["name"]

        if(float(user["rating"])>=4):
            current_recomm["brand"]="Apple"
        else:
            current_recomm["brand"]="Samsung"
        
        recomm.append(current_recomm)
    
    return recomm

print(recommendation(data_f))
