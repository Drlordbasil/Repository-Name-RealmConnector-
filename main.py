Here are the code optimizations for the Python script:

1. Add type annotations to improve code readability and catch potential type errors:
```python


class WebContentRecommendationSystem:
    def search_web_content(self) -> str:
        ...

    def extract_content_information(self, html_content: str) -> List[Dict[str, str]]:
        ...

    def process_text_data(self, text_data: str) -> str:
        ...

    def classify_content(self, content: str) -> str:
        ...

    def recommend_content(self) -> None:
        ...


```

2. Use list comprehension instead of a for loop to extract content information:
```python


def extract_content_information(self, html_content: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html_content, "html.parser")
    articles = soup.find_all("article")
    return [{"title": article.find("h2").text.strip(),
             "summary": article.find("p").text.strip()} for article in articles]


```

3. Group related user interaction methods together:
```python


class WebContentRecommendationSystem:
    def get_user_preferences(self) -> None:
        ...

    def update_user_preferences(self) -> None:
        ...


```

4. Use f-strings for string formatting:
```python
print(f"Error occurred while searching web content: {e}")
```

5. Use a generator expression and join method instead of manually iterating over recommendations:
```python


def display_recommendations(self) -> None:
    recommendations = "\n".join(
        [f"Title: {recommendation['title']}\nSummary: {recommendation['summary']}\n--------------------------"
         for recommendation in self.recommendations])
    print(recommendations)


```

6. Implement main() to encapsulate the example usage code:
```python


def main() -> None:
    recommendation_system = WebContentRecommendationSystem("user123")
    recommendation_system.run()


if __name__ == "__main__":
    main()
```

These optimizations should improve the performance, readability, and maintainability of the script.
