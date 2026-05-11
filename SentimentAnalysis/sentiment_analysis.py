# sentiment_analysis.py

import requests
import json


def sentiment_analyzer(text_to_analyse):
    """
    Analyze the sentiment of the given text using the Watson NLP API.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict: A dictionary containing the sentiment label and score.
    """

    # URL of the sentiment analysis service
    url = (
        "https://sn-watson-sentiment-bert.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    # Construct the request payload
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Custom header specifying the model ID
    headers = {
        "grpc-metadata-mm-model-id":
        "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # Send POST request to the API
    response = requests.post(url, json=payload, headers=headers)

    # Parse JSON response
    formatted_response = json.loads(response.text)

    # Extract sentiment label and score
    label = formatted_response["documentSentiment"]["label"]
    score = formatted_response["documentSentiment"]["score"]

    # Return sentiment analysis result
    return {
        "label": label,
        "score": score
    }