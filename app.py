from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route("/items", methods=["GET"])
def get_items():
    """
    Calls an external REST API and returns the JSON array to the client. The function demonstrates:
      • Making a GET request with `requests`.
      • Parsing JSON.
      • Basic error handling.
    """
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleVariableList?format=json"
    try:
        resp = requests.get(url, timeout=5)  # 5‑second timeout
        resp.raise_for_status()  # raise for HTTP errors
        data = resp.json()  # parse JSON into Python list/dict

        # Filter
        filtered = [
            item
            for item in data["Results"]
            if item["GroupName"] == "Active Safety System"
        ]

        return jsonify(filtered), 200  # Flask will set Content‑Type: application/json
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"HTTP error: {http_err}"}), resp.status_code
    except requests.exceptions.RequestException as err:
        return jsonify({"error": f"Network error: {err}"}), 503


# ------------------------------------------------------------------
if __name__ == "__main__":
    # Run the Flask development server on http://localhost:5000
    app.run(debug=True, port=5000)
