
Project: Pet Tracker Backend System
Using MongoDB and Python (PyMongo)

-------------------------------
1. Setting Up MongoDB
-------------------------------

- Option A: Local MongoDB (Recommended)
  1. Download and install MongoDB Community Server: https://www.mongodb.com/try/download/community
  2. Start the MongoDB server (mongod).
  3. Use MongoDB Compass to visually manage databases.


-------------------------------
2. Installing Necessary Python Packages
-------------------------------

Run the following commands:

    pip install pymongo
-------------------------------
3. Running the Script and Testing
-------------------------------

1. Open the Python script (e.g., pet_tracker.py) in an editor.
2. Start MongoDB server.
3. Run:

python pet_tracker.py

4. Use function calls:

- Add Owner:
  addOwner(firstname, lastname, email, phone, dob, street, city, state, zip)

- Register Pet:
  registerNewPet(owner_id, name, pet_type, breed, age, weight, vaccinated, adoption_date, favorite_foods)

- Update Pet Info:
  updatePetInto(pet_id, {"weight_kg": 20.5})

- Log New Pet Activity:
  logPetActivites(pet_id, activity_type, duration_minutes, date, location, notes)

- Retrieve Activities:
  getPetActivites(pet_id, activity_type=None)

- View Analytics:
  totalTimePerActivity(pet_id)
  mostFrequentActivity(pet_id)

5. View live data updates in MongoDB Compass.

-------------------------------
Additional Notes
-------------------------------

- Field names are case-sensitive.
- Dates should be string formatted 'YYYY-MM-DD'.
- Wrap IDs using ObjectId("your-id-here") when referencing documents.

