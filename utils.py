from transformers import pipeline 
#Load sentiment analysis model from Hugging Face 
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_text(text):
    # Step 1: Sentiment analysis
    sentiment_result = sentiment_analyzer(text)[0]
    sentiment = sentiment_result["label"]
    confidence = round(sentiment_result["score"], 2)

    # Step 2:Simple ethics risk logic (keyword based)
    risk_keywords =["kill", "hate", "voilence", "racist ","abuse"]
    ethics = "High Risk" if any (word
                 in text.lower() for word in risk_keywords) else "Low Risk"
    
    # Step 3: Generates explanation 
    explanation = ( f"The text expresses a **{sentiment}** sentiment with confidence{confidence}. "
        f"Ethical resk is assesed as **{ethics}** based on keyword scanning"
    )

    return {
        "sentiment": sentiment,
        "ethics"   : ethics,
        "explanation": explanation
    }