from flask import Flask, request, jsonify
from flask_cors import CORS
from TFIDF_Weighted import get_recommendations  # Import your recommendation logic

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Title parameter is required"}), 400
    try:
        recommendations = get_recommendations(title)
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)