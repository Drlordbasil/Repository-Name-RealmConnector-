import requests
from bs4 import BeautifulSoup
from transformers import pipeline


class WebContentRecommendationSystem:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = []
        self.recommendations = []
        self.nlp_summarization = pipeline("summarization")
        self.nlp_classification = pipeline("text-classification")

    def get_user_preferences(self):
        self.preferences = input(
            "Enter your preferences (topics, keywords, sources): ").split(", ")

    def update_user_preferences(self):
        self.preferences = input(
            "Update your preferences (topics, keywords, sources): ").split(", ")

    def search_web_content(self):
        search_query = " ".join(self.preferences)
        url = f"https://www.example.com/search?q={search_query}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
            return html_content
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while searching web content: {e}")
            return ""

    def extract_content_information(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        content_information = []
        articles = soup.find_all("article")
        for article in articles:
            title = article.find("h2").text.strip()
            summary = article.find("p").text.strip()
            content_information.append({"title": title, "summary": summary})
        return content_information

    def process_text_data(self, text_data):
        return self.nlp_summarization(text_data, max_length=100, min_length=10, do_sample=False)

    def classify_content(self, content):
        return self.nlp_classification(content)[0]["label"]

    def recommend_content(self):
        html_content = self.search_web_content()
        content_information = self.extract_content_information(html_content)
        for content_info in content_information:
            title = content_info["title"]
            summary = content_info["summary"]
            processed_summary = self.process_text_data(summary)
            classification = self.classify_content(processed_summary)
            if classification in self.preferences:
                self.recommendations.append(
                    {"title": title, "summary": processed_summary})

    def update_recommendations(self):
        self.recommendations = []

    def display_recommendations(self):
        for recommendation in self.recommendations:
            print(f"Title: {recommendation['title']}")
            print(f"Summary: {recommendation['summary']}")
            print("--------------------------")

    def run(self):
        self.get_user_preferences()
        self.recommend_content()
        self.display_recommendations()


# Example Usage
recommendation_system = WebContentRecommendationSystem("user123")
recommendation_system.run()
