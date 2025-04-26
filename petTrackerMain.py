from pymongo import MongoClient
from bson import ObjectId

# Connection to Client 
client = MongoClient('mongodb://localhost:27017/')


#Connection to  Database set 
db = client['PetTracker']

#connection to specific collection sets 
ownerUserColletion = db['Owner/User']

petColletion = db['Pets']

ActivitesColletion = db['Activities']

print("Connection to database")


def add_Owner(firstName, lastName, email, phoneNumber, dob, street, city, state, zipCode):
    #creating the state of first name connecting the variable to a string
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


# add_Owner(
#     'Justis', 'Guin', 'justis.guin@email.com', '123-234-2345',
#     '2004-07-05', '424 N Martin St', 'Muncie', 'Indiana', '47725'
# )

1   

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

# registerNewPet(
#         ownerId=ObjectId('680d39fde335150715c48224'), 
#         PetName='Indy', 
#         typeOfPet='Dog',
#         breed='Pitbull',
#         age= 2,
#         weight= 27.2,
#         vaccinateStatus= True,
#         microchipped= True,
#         adoptionDate='2023-01-10', 
#         favoriteFood=['Ice','Bananas']
# )

#Crud section 
# def updatePetInto():


