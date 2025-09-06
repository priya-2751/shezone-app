from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shezone-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Store connected children
connected_children = {}

@app.route('/')
def index():
    return render_template('dashboard.html')  # parent dashboard

# Child sends location
@socketio.on('send_location')
def handle_send_location(data):
    child_id = data.get('child_id')
    lat = data.get('lat')
    lng = data.get('lng')
    # Save latest location
    connected_children[child_id] = {'lat': lat, 'lng': lng}
    # Emit to parent in real-time
    emit('receive_location', {'child_id': child_id, 'lat': lat, 'lng': lng}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
