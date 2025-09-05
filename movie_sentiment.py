# sentiment_analyzer.py

# Rule-based lists of positive and negative words
positive_words = [
    "amazing", "outstanding", "excellent", "fantastic", "great", "awesome",
    "wonderful", "fun", "love", "best", "loved", "enjoyed"
]

negative_words = [
    "boring", "bad", "terrible", "awful", "poor", "worst", "dull",
    "disappointing", "hate", "long", "confusing", "slow"
]

def evaluate_review(review):
    review_lower = review.lower()
    pos_count = sum(word in review_lower for word in positive_words)
    neg_count = sum(word in review_lower for word in negative_words)

    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def analyze_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    sentiment = evaluate_review(line)
                    print(f"Review: {line}")
                    print(f"Sentiment: {sentiment}")
                    print("-" * 50)
    except FileNotFoundError:
        print(f"File {file} not found. Skipping file analysis.")

def interactive_mode():
    print("Interactive Movie Review Sentiment Analyzer")
    print("Type 'exit' to quit")
    while True:
        review = input("\nEnter a movie review: ")
        if review.lower() == "exit":
            break
        sentiment = evaluate_review(review)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    reviews_file = "reviews.txt"
    print("Analyzing reviews from file...\n")
    analyze_file(reviews_file)
    print("\nNow you can try interactive mode!")
    interactive_mode()