import requests
from bs4 import BeautifulSoup

def search_recipes(ingredients, urls):
    for url in urls:
        base_url = url
    # base_url = 'https://www.allrecipes.com/search?q='


    # Join the ingredients to form the search query:
    query = '+'.join(ingredients)
    search_url = base_url + query

    # send a GET request to the search URL
    response = requests.get(search_url)

    #Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find elements containing recipe information- change based on website structure
    recipe_titles = soup.find_all('span', class_='card__title-text')

    # Extract and print the titles of the recipes
    if recipe_titles:
        print(f"Recipes Found on {url}:")
        for title in recipe_titles:
            print(title.text.strip())

    else:
        print(f"No recipes found for these ingredients on {url}.")

# Example of using the function

user_input = input("enter three ingredients separated by commas:")
ingredients = user_input.split(',')

urls = [
    'https://www.allrecipes.com/search?q='
]

search_recipes(ingredients, urls)