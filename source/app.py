from flask import Flask, render_template, jsonify, request, session
import language
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/api/set_subject')
def set_subject():
    """
        If parameter subject == True we are dealing with personal pronoun,
         else we are dealing with noun (optionally with adjective)
    """
    data = request.get_json()
    subject = data.get('subject', True)
    session['subject_type'] = subject
    return jsonify({})



if __name__ == '__main__':
    app.run(debug=True)
