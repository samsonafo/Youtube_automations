import requests

def get_book_recommendations(query, max_results=5):
    """
    Fetches book recommendations based on a search query from Google Books API.
    
    Args:
    query (str): The genre, author, or keyword to search for.
    max_results (int): The maximum number of book recommendations to return.
    
    Returns:
    list of dict: A list of book recommendations, each represented as a dictionary.
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(url)
    books = response.json().get('items', [])
    
    recommendations = []
    for book in books:
        volume_info = book.get('volumeInfo', {})
        title = volume_info.get('title')
        authors = volume_info.get('authors', [])
        description = volume_info.get('description', 'No description available')
        link = volume_info.get('infoLink')
        
        recommendations.append({
            'title': title,
            'authors': authors,
            'description': description,
            'link': link
        })
    
    return recommendations

def display_recommendations(recommendations):
    """
    Displays the book recommendations in a readable format.
    
    Args:
    recommendations (list of dict): A list of book recommendations to display.
    """
    if not recommendations:
        print("No recommendations found.")
        return
    
    print(f"\nTop {len(recommendations)} Book Recommendations:\n")
    for i, book in enumerate(recommendations, 1):
        print(f"{i}. {book['title']} by {', '.join(book['authors'])}")
        print(f"   Description: {book['description'][:200]}...")  # Displaying first 200 characters of the description
        print(f"   More info: {book['link']}\n")

if __name__ == "__main__":
    user_input = input("Enter your favorite genre, author, or keyword: ").strip()
    recommendations = get_book_recommendations(user_input)
    display_recommendations(recommendations)