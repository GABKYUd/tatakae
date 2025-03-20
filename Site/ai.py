from flask import Flask, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__)

def compare_answers(user_answer, correct_answer):
    similarity = SequenceMatcher(None, user_answer, correct_answer).ratio()
    return similarity

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    user_answer = data['userAnswer']
    correct_answer = data['correctAnswer']
    similarity = compare_answers(user_answer, correct_answer)
    return jsonify({'similarity': similarity})

if __name__ == '__main__':
    app.run(debug=True)