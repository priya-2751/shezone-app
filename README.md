# 🚺 SheZone: A Women safety app using ml 

SheZone is an innovative women’s safety and navigation platform designed to predict unsafe zones and provide safer travel routes. By integrating geospatial machine learning, crime data analysis, and interactive maps, SheZone empowers women with real-time safety insights and safe-route recommendations.


## Overview
SheZone leverages geospatial machine learning, crime data visualization, and route optimization to help women travel more safely.

## 🌟 Features
- 🔐 **Login & Role Selection** → User can log in as Parent or Child.  
- 🗺️ **Interactive Map** → Unsafe zones marked with ❌ using past crime dataset.  
- 📍 **Safe Route Suggestions** → Routes avoid unsafe areas and prioritize paths near police stations, shops, and crowded zones.  
- 🧠 **AI + ML Integration** → Uses clustering (DBSCAN, K-Means) and Random Forest for crime prediction.  
- 🚦 **Real-Time Maps** → Embedded using Folium, Flask, and OpenRouteService API.


## 🛠️ Tech Stack
- **Frontend**: HTML, CSS (pink theme 🎀), JavaScript  
- **Backend**: Python (Flask)  
- **ML Models**: Random Forest, DBSCAN, K-Means  
- **Maps**: Folium, OpenStreetMap, OpenRouteService API  
- **Dataset**: `triplicane_crime.csv` (NCRB + local crime reports)  

---

## 📂 Project Structure

SheZone/
├── README.md 
├── requirements.txt 
├── .env.example 
│ ├── login.html
│ ├── role_select.html 
│ ├── alerts.html
│ ├── child-dashboard.html
│ ├── child.html
│ ├── connect-child.html 
│ ├── role.html
│ ├── setting.html
│ ├── settings.html
│ ├── signup.html
│ ├── sos.html
│ ├── track-child.html
├── .gitattributes
├── Procfile
├── Procfile.txt
├── app.py
├── apps.py
├── firebase_config.py
├── triplicane_crime_geocoded.csv


## Security Features

-Unsafe Zone Marking – Highlights dangerous areas with ❌ based on crime data.
-Safe Routing System – Suggests alternative paths through safer locations.
-Real-Time Tracking – Location sharing between parent and child roles.
-Emergency SOS – Quick alert system (future feature).
-Data Privacy – Ensures sensitive data (like location) is not exposed publicly.

## License

This project is licensed under the MIT License.

  
