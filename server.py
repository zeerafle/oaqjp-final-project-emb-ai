"""Main entry of the Flask app for Emotion Detection"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_api():
    """Function for emotionDetector route"""
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result['dominant_emotion']:
        return f"For the given statement, the system response is 'anger': {result['anger']}, \
                 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} \
                 and 'sadness': {result['sadness']}. \
                 The dominant emotion is {result['dominant_emotion']}", 200

    return 'Invalid text! Please try again!', 200

if __name__ == "__main__":
    app.run(debug=True)
