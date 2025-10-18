from flask import Flask, render_template, jsonify, request, session
import language
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/api/get_data')
def get_data():
    nouns = language.get_nouns()
    verbs = language.get_verbs()
    adjectives = language.get_adjectives()
    return jsonify({
        'nouns': nouns,
        'verbs': verbs,
        'adjectives': adjectives,
    })


if __name__ == '__main__':
    app.run(debug=True)
