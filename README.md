# 📚 Google Books AI Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Cohere](https://img.shields.io/badge/Cohere-Command-purple)
![License](https://img.shields.io/badge/license-MIT-green)

A powerful Python library that combines the Google Books API with Cohere's LLM capabilities to create an intelligent book discovery and analysis system. This tool enables sophisticated book searches, AI-powered analysis, and smart recommendations.

## 🌟 Features

### Smart Search & Analysis
- **Intelligent Book Discovery**: Advanced search capabilities using the Google Books API
- **AI-Powered Analysis**: Deep insights into themes, writing styles, and connections between books
- **Content Analysis**: Generate comprehensive analysis of book themes, patterns, and relationships
- **Book Comparisons**: Understanding how different books relate to each other

### Recommendation Engine
- **Smart Book Matching**: Find similar books based on themes and writing style
- **Category-Based Discovery**: Explore books within and across related categories
- **Contextual Recommendations**: Get suggestions based on book content and metadata

## 🛠️ Technical Stack

- **Language**: Python 3.8+
- **AI Model**: Cohere Command
- **Book Data**: Google Books API
- **Required Libraries**: cohere, requests

## 📋 Prerequisites

- Python 3.8 or higher
- Cohere API key
- Google Books API key

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/google-books-ai-assistant.git
cd google-books-ai-assistant
```

2. Install required packages:
```bash
pip install cohere requests
```

3. Set up environment variables:
```bash
export COHERE_API_KEY="your-cohere-api-key"
export GOOGLE_BOOKS_API_KEY="your-google-books-api-key"
```

## 🚀 Quick Start

```python
from google_books_assistant import GoogleBooksAssistant

# Initialize the assistant
assistant = GoogleBooksAssistant(
    cohere_api_key="your-cohere-api-key",
    google_books_api_key="your-google-books-api-key"
)

# Search for books
books = assistant.search_books("artificial intelligence ethics", max_results=5)

# Analyze books
analysis = assistant.analyze_books(
    books,
    "What are the main ethical concerns discussed in these books?"
)

# Get recommendations
recommendations = assistant.recommend_similar_books("Superintelligence by Nick Bostrom", max_recommendations=3)
```

## 📖 Detailed Usage Examples

### Book Search and Analysis
```python
# Search for specific books
books = assistant.search_books(
    query="machine learning introduction",
    max_results=5
)

# Print book details
for book in books:
    print(f"Title: {book['title']}")
    print(f"Authors: {', '.join(book['authors'])}")
    print(f"Description: {book['description'][:200]}...")
    print("---")

# Analyze specific aspects of the books
analysis = assistant.analyze_books(
    books,
    "How do these books approach teaching machine learning concepts?"
)
print(analysis)
```

### Getting Book Recommendations
```python
# Get recommendations based on a book
recommendations = assistant.recommend_similar_books(
    book_title="Deep Learning by Ian Goodfellow",
    max_recommendations=3
)

# Print recommendations
for book in recommendations:
    print(f"Recommended: {book['title']}")
    print(f"By: {', '.join(book['authors'])}")
    print("---")
```

## 📁 Project Structure

```
google-books-ai-assistant/
├── google_books_assistant.py   # Main assistant class implementation
├── requirements.txt           # Project dependencies
├── README.md                 # Project documentation
└── examples/                 # Usage examples
    ├── search_example.py
    ├── analysis_example.py
    └── recommendations_example.py
```

## 🔧 API Reference

### GoogleBooksAssistant

#### `__init__(cohere_api_key: str, google_books_api_key: str)`
Initializes the assistant with required API keys.

#### `search_books(query: str, max_results: int = 5) -> List[Dict]`
Searches for books using the Google Books API.
- `query`: Search terms
- `max_results`: Maximum number of books to return
- Returns: List of book dictionaries containing title, authors, description, etc.

#### `analyze_books(books: List[Dict], question: str) -> str`
Analyzes books using Cohere's LLM.
- `books`: List of book dictionaries from search_books()
- `question`: Analysis question or prompt
- Returns: AI-generated analysis text

#### `recommend_similar_books(book_title: str, max_recommendations: int = 3) -> List[Dict]`
Finds similar books based on a reference book.
- `book_title`: Title of the reference book
- `max_recommendations`: Maximum number of recommendations to return
- Returns: List of recommended book dictionaries

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Books API for comprehensive book data access
- Cohere for their powerful LLM capabilities

## 📧 Contact

Eddie Otudor - [Eddie Otudor](mailto:edbeeotudor@gmail.com)

Project Link: [https://github.com/beloveddie/google_books_ai_assistant](https://github.com/beloveddie/google_books_ai_assistant)

---

⭐️ If you find this project useful, please consider giving it a star!
