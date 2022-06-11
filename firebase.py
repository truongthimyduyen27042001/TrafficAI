from time import sleep
import pyrebase
from datetime import datetime
config = {
    "apiKey": "AIzaSyDPmJ7q83NlOnZy-RQgx3rRLE64Q3I-S0g",
    "authDomain": "uploadcsv-c8bfd.firebaseapp.com",
    "databaseURL": "https://uploadcsv-c8bfd-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "uploadcsv-c8bfd",
    "storageBucket": "uploadcsv-c8bfd.appspot.com",
    "messagingSenderId": "939407755660",
    "appId": "1:939407755660:web:9014bdb0c480453032eea9",
    "measurementId": "G-C7WC170JGF"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
# db = firebase.database()
now = datetime.now()
# while (True):
#      if(datetime.now().hour == 15 and datetime.now().minute == 59 and datetime.now().second == 0):
#          storage.child("dataMovie.csv").put("dataMovie.csv")

#storage.child("mainFileVehicleID.csv").put("mainFileVehicleID.csv")
storage.child("mainFileVehicleID.csv").download('',"mainFileVehicleIDdownload.csv")
