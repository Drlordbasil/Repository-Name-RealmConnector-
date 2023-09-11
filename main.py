Certainly! Here's a refactored version of your script that incorporates the suggested improvements:

```python
from typing import List, Dict
from bs4 import BeautifulSoup


class WebContentRecommendationSystem:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id

    def search_web_content(self) -> str:
        ...

    def extract_content_information(self, html_content: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html_content, "html.parser")
        articles = soup.find_all("article")
        return [
            {"title": article.find("h2").text.strip(), "summary": article.find("p").text.strip()}
            for article in articles
        ]

    def process_text_data(self, text_data: str) -> str:
        ...

    def classify_content(self, content: str) -> str:
        ...

    def recommend_content(self) -> None:
        ...

    def get_user_preferences(self) -> None:
        ...

    def update_user_preferences(self) -> None:
        ...

    def display_recommendations(self) -> None:
        recommendations = "\n".join(
            f"Title: {recommendation['title']}\nSummary: {recommendation['summary']}\n--------------------------"
            for recommendation in self.recommendations
        )
        print(recommendations)

    def run(self) -> None:
        self.get_user_preferences()
        self.search_web_content()
        self.recommend_content()
        self.display_recommendations()


def main() -> None:
    recommendation_system = WebContentRecommendationSystem("user123")
    recommendation_system.run()


if __name__ == "__main__":
    main()
```

The refactored version incorporates the following improvements:

1. Type annotations have been added to improve code readability and catch potential type errors.
2. List comprehension is used instead of a for loop in the `extract_content_information` method for more concise and efficient code.
3. Related user interaction methods (`get_user_preferences` and `update_user_preferences`) have been grouped together within the class.
4. f-strings are used for string formatting, making the code more concise and readable.
5. Generator expression and the `join` method are utilized in the `display_recommendations` method instead of manually iterating over recommendations.
6. A `run` method is introduced within the class to encapsulate the example usage code.
7. The `__init__` method has been added to initialize the `user_id` attribute.

These optimizations and best practices should improve both the performance and readability of your code.