# firebase_config.py
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Use your downloaded Firebase service account JSON
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
