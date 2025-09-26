from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector  # Import your package
app = Flask(__name__)
# Home route → loads index.html
@app.route('/')
def index():
    return render_template('index.html')
# Emotion detection API route
@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)
    # If dominant_emotion is None, show error message
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 200
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

# Run app
if __name__ == "__main__":
    app.run(host="localhost", port=5000)
