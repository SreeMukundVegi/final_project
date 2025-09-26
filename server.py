"""
server.py

Flask web server for the Emotion Detection application.
Provides routes for the main page and emotion analysis of text input.
"""

from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the main index page of the Emotion Detection web application.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Detect the emotion of a given text.

    Gets the 'textToAnalyze' query parameter from the GET request,
    calls the emotion_detector function, and returns a formatted
    response. If the text is empty or invalid, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


# Run the Flask web server on localhost:5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
