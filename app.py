
from flask import Flask, render_template, request
import pandas as pd
import folium
import openrouteservice
from geopy.geocoders import Nominatim
import threading
import webbrowser

app = Flask(__name__)

# ORS API key (replace with your own)
ORS_API_KEY ="eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjU4Mzk4ODY3YWNlOTdmNWRjNmQwZWZiOTY1MmVjYjg4MGI1MWJjMDM5YjVkZTBkZWQ5MTdjNzRjIiwiaCI6Im11cm11cjY0In0="
client = openrouteservice.Client(key=ORS_API_KEY)

# Load crime data
df = pd.read_csv("triplicane_crime_geocoded.csv")

# Geocoder
geolocator = Nominatim(user_agent="shezone_app", timeout=10)

def geocode_place(place_name):
    try:
        location = geolocator.geocode(place_name)
        if location:
            return (location.latitude, location.longitude)
    except Exception as e:
        print("Geocoding error:", e)
    return None

# ---------- ROUTES ----------

# LOGIN PAGE
@app.route("/login")
def login():
    return render_template("login.html")

# SIGNUP PAGE
@app.route("/signup")
def signup():
    return render_template("signup.html")

# ROLE SELECTION
@app.route("/role")
def role():
    return render_template("role.html")

# CHILD DASHBOARD
@app.route("/child-dashboard")
def child_dashboard():
    return render_template("child-dashboard.html")

# PARENT DASHBOARD
@app.route("/pdashboard")
def parent_dashboard():
    return render_template("pdashboard.html")

# SOS PAGE
@app.route("/sos")
def sos():
    return render_template("sos.html")

# CONNECT CHILD
@app.route("/connect-child")
def connect_child():
    return render_template("connect-child.html")

# ALERTS
@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

@app.route("/parent")
def parent():
    return render_template("parent.html")

@app.route("/parents")
def parents():
    return render_template("parents.html")

@app.route("/trackchild")
def track_child():
    return render_template("trackchild.html")

# SETTINGS
@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/setting")
def setting():
    return render_template("setting.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/findroute")
def findroute():
    return render_template("findroute.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")


# SAFE ROUTE MAP
@app.route("/map", methods=["GET", "POST"])
def map_page():
    start_place = ""
    end_place = ""
    route_coords = []
    map_center = [13.0827, 80.2707]  # Default Chennai

    if request.method == "POST":
        start_place = request.form.get("start")
        end_place = request.form.get("end")

        start_coords = geocode_place(start_place)
        end_coords = geocode_place(end_place)

        if start_coords and end_coords:
            map_center = start_coords
            try:
                coords_list = [
                    [start_coords[1], start_coords[0]],
                    [end_coords[1], end_coords[0]]
                ]
                routes = client.directions(
                    coordinates=coords_list,
                    profile="foot-walking",
                    format="geojson"
                )
                if routes["features"]:
                    geometry = routes["features"][0]["geometry"]["coordinates"]
                    route_coords = [(lat, lon) for lon, lat in geometry]
            except Exception as e:
                print("Route error:", e)

    # Create map
    m = folium.Map(location=map_center, zoom_start=14)

    # Add unsafe zones
    for _, row in df.iterrows():
        try:
            lat, lon = row["latitude"], row["longitude"]
            if pd.notnull(lat) and pd.notnull(lon):
                folium.Marker(
                    location=[lat, lon],
                    popup="⚠ Unsafe Zone",
                    icon=folium.DivIcon(
                        html=f"""<div style="font-size:24px; color:red;">❌</div>"""
                    )
                ).add_to(m)
        except Exception as e:
            print("Marker error:", e)
            continue

    # Add route if available
    if route_coords:
        folium.PolyLine(
            route_coords, color="green", weight=6, opacity=0.8, tooltip="Route"
        ).add_to(m)
        folium.Marker(
            route_coords[0], popup="Start", icon=folium.Icon(color="green", icon="play")
        ).add_to(m)
        folium.Marker(
            route_coords[-1], popup="Destination", icon=folium.Icon(color="blue", icon="flag")
        ).add_to(m)

    return render_template("map.html", folium_map=m._repr_html_(),
                           start_place=start_place, end_place=end_place)


# Open browser automatically
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/login")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(host="0.0.0.0", port=5000, debug=True)
