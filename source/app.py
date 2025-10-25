from flask import Flask, render_template, jsonify, request
from language_utils import words_database
import language
import os
import pickle
app = Flask(__name__)

def get_word_stats():
    with open('word_stats/adjectives.pkl', 'rb') as f:
        adjectives = pickle.load(f)
    with open('word_stats/verbs.pkl', 'rb') as f:
        verbs = pickle.load(f)
    return adjectives, verbs

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/api/get_data')
def get_data():
    nouns = words_database.get_nouns()
    verbs = words_database.get_verbs()
    adjectives = words_database.get_adjectives()
    adjectives_stats, verbs_stats = get_word_stats()
    return jsonify({
        'nouns': nouns,
        'verbs': verbs,
        'adjectives': adjectives,
        'adjectives_stats': adjectives_stats,
        'verbs_stats': verbs_stats
    })


@app.post('/api/construct_sentence')
def construct_sentence():
    data = request.get_json()
    sentence = language.construct_sentence(data)
    return jsonify({"sentence": sentence})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
