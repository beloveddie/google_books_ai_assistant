import os
import requests
import cohere
from typing import List, Dict, Optional
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GoogleBooksAssistant:
    def __init__(self, cohere_api_key: str, google_books_api_key: str):
        """
        Initialize the Google Books AI Assistant.
        
        Args:
            cohere_api_key (str): Your Cohere API key
            google_books_api_key (str): Your Google Books API key
        """
        self.cohere_client = cohere.Client(cohere_api_key)
        self.google_books_api_key = google_books_api_key
        self.google_books_base_url = "https://www.googleapis.com/books/v1/volumes"
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def search_books(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Search for books using the Google Books API.
        
        Args:
            query (str): Search query
            max_results (int): Maximum number of results to return
            
        Returns:
            List[Dict]: List of book information dictionaries
        """
        try:
            params = {
                'q': query,
                'key': self.google_books_api_key,
                'maxResults': max_results
            }
            
            response = requests.get(self.google_books_base_url, params=params)
            response.raise_for_status()
            
            results = response.json()
            books = []
            
            for item in results.get('items', []):
                volume_info = item.get('volumeInfo', {})
                books.append({
                    'title': volume_info.get('title'),
                    'authors': volume_info.get('authors', []),
                    'description': volume_info.get('description', ''),
                    'categories': volume_info.get('categories', []),
                    'preview_link': volume_info.get('previewLink'),
                    'page_count': volume_info.get('pageCount')
                })
                
            return books
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error searching Google Books API: {str(e)}")
            return []

    def analyze_books(self, books: List[Dict], question: str) -> str:
        """
        Analyze books using Cohere's LLM to answer questions about them.
        
        Args:
            books (List[Dict]): List of book information
            question (str): User's question about the books
            
        Returns:
            str: AI-generated response analyzing the books
        """
        try:
            # Create a context from the books data
            context = "\n".join([
                f"Book: {book['title']}\n"
                f"Authors: {', '.join(book['authors'])}\n"
                f"Description: {book['description']}\n"
                f"Categories: {', '.join(book['categories'])}\n"
                for book in books
            ])

            # Create prompt for the LLM
            prompt = f"""Based on the following books information:

{context}

Question: {question}

Please provide a detailed analysis of these books in relation to the question. Include relevant comparisons, themes, and insights."""

            # Generate response using Cohere
            response = self.cohere_client.generate(
                model='command',
                prompt=prompt,
                max_tokens=500,
                temperature=0.7,
                k=0,
                stop_sequences=[],
                return_likelihoods='NONE'
            )

            return response.generations[0].text.strip()

        except Exception as e:
            self.logger.error(f"Error analyzing books with Cohere: {str(e)}")
            return "I apologize, but I encountered an error while analyzing the books."

    def recommend_similar_books(self, book_title: str, max_recommendations: int = 3) -> List[Dict]:
        """
        Recommend similar books based on a given book title.
        
        Args:
            book_title (str): Title of the reference book
            max_recommendations (int): Maximum number of recommendations
            
        Returns:
            List[Dict]: List of recommended book information
        """
        try:
            # First, search for the reference book
            reference_book = self.search_books(book_title, max_results=1)
            
            if not reference_book:
                return []
                
            # Extract categories and relevant terms from the reference book
            categories = reference_book[0].get('categories', [])
            
            # Search for books in similar categories
            similar_books = []
            for category in categories:
                query = f"subject:{category}"
                books = self.search_books(query, max_results=max_recommendations)
                
                # Filter out the reference book and duplicates
                books = [book for book in books if book['title'] != book_title]
                similar_books.extend(books)
            
            # Limit to max_recommendations
            return similar_books[:max_recommendations]
            
        except Exception as e:
            self.logger.error(f"Error recommending similar books: {str(e)}")
            return []

def main():
    """
    Example usage of the GoogleBooksAssistant
    """
    # Initialize the assistant with API keys
    assistant = GoogleBooksAssistant(
        cohere_api_key=os.getenv("COHERE_API_KEY"),
        google_books_api_key=os.getenv("GOOGLE_BOOKS_API_KEY")
    )
    
    # Example: Search for books about artificial intelligence
    books = assistant.search_books("artificial intelligence ethics")
    
    # Example: Analyze the books
    analysis = assistant.analyze_books(
        books,
        "What are the main ethical concerns discussed in these books regarding AI?"
    )
    
    # Example: Get recommendations
    recommendations = assistant.recommend_similar_books("Superintelligence by Nick Bostrom")
    
    # Print results
    print("Analysis:", analysis)
    print("\nRecommended Books:")
    for book in recommendations:
        print(f"- {book['title']} by {', '.join(book['authors'])}")

if __name__ == "__main__":
    main()