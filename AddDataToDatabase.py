import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendancerealtime-432c3-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "19565":
        {
            "name":"Elon Musk",
            "major":"Robotics",
            "starting_year" : 2018,
            "total_attendance":6,
            "standing":"B",
            "year":4,
            "Last_attendance_time":"2023-05-21 00:54:34"
        },
    "32166":
        {
            "name": "Akash",
            "major": "AI/ML",
            "starting_year": 2023,
            "total_attendance": 10,
            "standing": "G",
            "year": 2,
            "Last_attendance_time": "2023-05-22 00:54:34"
        }


}
for key,value in data.items():
    ref.child(key).set(value)