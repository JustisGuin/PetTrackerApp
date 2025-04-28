from pymongo import MongoClient
from bson import ObjectId

# Connection to Client 
client = MongoClient('mongodb://localhost:27017/')


#Connection to  Database set 
db = client['PetTracker']

#connection to specific collection sets 
ownerUserColletion = db['Owner/User']

petColletion = db['Pets']

activitesColletion = db['Activities']

print("Connection to database")


def add_Owner(firstName, lastName, email, phoneNumber, dob, street, city, state, zipCode):
    #Create an owner document (dictionary) using the provided input data
    ownerDocument = {
        'firstName': firstName,
        'lastname': lastName,
        'email': email,
        'phoneNumber': phoneNumber,
        'Dob': dob,
       'address': {
           'street': street,
           'city': city,
           'state': state, 
           'zipCode': zipCode
       }
    }
    #inserts results of owners into the ownersDocument
    results = ownerUserColletion.insert_one(ownerDocument)
    print(f'Owner added with id: {results.inserted_id}')


add_Owner(
     'Justis', 'Guin', 'justis.guin@email.com', '123-234-2345',
     '2004-07-05', '424 N Martin St', 'Muncie', 'Indiana', '47725'
 )

   

#Register New Pet 
def registerNewPet(ownerId, PetName, typeOfPet, breed, age, weight, vaccinateStatus, 
microchipped, adoptionDate, favoriteFood):
    newPet = {
        'Name': PetName,
        'Type': typeOfPet,
        'Breed': breed,
        'Age': age,
        'Weight': weight,
        'VaccinateStatus': vaccinateStatus,
        'Microchipped': microchipped,
        'owner_id': ownerId,
        'AdoptionDate': adoptionDate,
        'FavoriteFood': favoriteFood
    }

    registerPet = petColletion.insert_one(newPet)
    print(f'New Pet Registered with Id: {registerPet.inserted_id}')

registerNewPet(
         ownerId=ObjectId('680d39fde335150715c48224'), 
         PetName='Indy', 
         typeOfPet='Dog',
         breed='Pitbull',
         age= 2,
         Weight= 27.2,
         vaccinateStatus= True,
         microchipped= True,
         adoptionDate='2023-01-10', 
         favoriteFood=['Ice','Bananas']
 )
                 #objectID  #dictionary of updates 
def updatePetInto(petID,    updates):
    results = petColletion.update_one(
        {'_id': petID}, 
        #set operator to replace the value of a field with the specified value
        {'$set': updates} )
    
    if results.modified_count >0:
        print("Pets info has been updated")
    else:
        print("No changes have been made to Pets dataset")


#petInfo = print("Please enter pets _id correctly to update info")
updatePetInto(
     ObjectId('680d4ce2c86ff55aba42b7b6'),
     {'FavoriteFood': ['Treats','Chicken'], 'Weight': 29.2}  
)



def logPetActivites(petID, activityType, duration, date, location, notes):
    petActivites = {
        'pet_id': petID,
        'type': activityType,
        'duration_minutes': duration,
        'date': date,
        'location': location,
        'notes': notes
    }

    logPet = activitesColletion.insert_one(petActivites)
    print(f'New Pet Activity Logged: {logPet.inserted_id}')


logPetActivites(
    petID=ObjectId('680d4ce2c86ff55aba42b7b6'),
    activityType='walk',
    duration=30,
    date="2025-04-27",
    location="Muncie, IN",
    notes="Walked around the park nicely."
)



def getPetActivites(petID, activityType=None):
    query = {'pet_id:': petID}

    if activityType: 
        query['type'] = activityType
    
    activites = activitesColletion.find(query).sort('date', -1) 

    print(f"Activites for pet {petID}: ")
    for activity in activites:
         print(f"- {activity['date']} | {activity['type']} ({activity['duration_minutes']} minutes) at {activity['location']}")
         print(f"  notes: {activity['notes']}\n")



#getPetActivites(ObjectId('680d4ce2c86ff55aba42b7b6'))

getPetActivites(ObjectId("680d4ce2c86ff55aba42b7b6"), activityType='walk')  



def totalTimePerActivity(pet_id):
    pipeline = [
        {"$match": {"pet_id": pet_id}},
        {"$group": {
            "_id": "$type",
            "total_duration": {"$sum": "$duration_minutes"}
        }},
        {"$sort": {"total_duration": -1}}
    ]

    results = activitesColletion.aggregate(pipeline)

    print(f"Total time spent per activity for pet {pet_id}:")
    for activity in results:
        print(f"- {activity['_id']}: {activity['total_duration']} minutes")

totalTimePerActivity(ObjectId('680d4ce2c86ff55aba42b7b6'))



def mostFrequentActivity(pet_id):
    pipeline = [
        {"$match": {"pet_id": pet_id}},
        {"$group": {
            "_id": "$type",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 1}
    ]

    result = list(activitesColletion.aggregate(pipeline))

    if result:
        print(f"Most frequent activity for pet {pet_id}: {result[0]['_id']} ({result[0]['count']} times)")
    else:
        print(f"No activities found for pet {pet_id}.")


mostFrequentActivity(ObjectId("680d4ce2c86ff55aba42b7b6"))