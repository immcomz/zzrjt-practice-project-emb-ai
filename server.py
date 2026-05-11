''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template("index.html")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyze the sentiment of text passed through URL parameters.
    """

    # Retrieve text from request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Get sentiment analysis response
    response = sentiment_analyzer(text_to_analyze)

    # Extract label and score
    label = response["label"]
    score = response["score"]

    # Format and return the result
    return (
        "The given text has been identified as {} "
        "with a score of {}."
    ).format(label.split("_")[1], score)


if __name__ == "__main__":
    app.run(host="0.0.0.0")