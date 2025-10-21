from flask import Flask, render_template, jsonify, request
from language_utils import words_database
import language
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/api/get_data')
def get_data():
    nouns = words_database.get_nouns()
    verbs = words_database.get_verbs()
    adjectives = words_database.get_adjectives()
    return jsonify({
        'nouns': nouns,
        'verbs': verbs,
        'adjectives': adjectives,
    })


@app.post('/api/construct_sentence')
def construct_sentence():
    data = request.get_json()
    sentence = language.construct_sentence(data)
    return jsonify({"sentence": sentence})

if __name__ == '__main__':
    app.run()
