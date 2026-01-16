from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"},
]

# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.get("/")
def welcome():
    return jsonify({"message": "Welcome!"}), 200

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.get("/events")
def get_events():
    return jsonify(events), 200

# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201
@app.post("/events")
def create_event():
    data = request.get_json(silent=True) or {}

    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        # tests typically accept 400 or 422 for invalid input
        return jsonify({"error": "Missing required field: title"}), 400

    new_id = max((e["id"] for e in events), default=0) + 1
    new_event = {"id": new_id, "title": title.strip()}
    events.append(new_event)

    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)
