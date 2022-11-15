import pandas as pd
#from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup

def get_page_ingredients(): 
	#https://www.geeksforgeeks.org/scrap-books-using-beautifulsoup-from-books-toscrape-in-python/
	# variable to store website link as string
	myurl = 'https://www.eatyourbooks.com/library/recipes/2023108/braised-eggs-with-leek-and'
	# grab website and store in variable uclient
	#uClient = uReq(myurl)
	 
	# read and close HTML
	#page_html = uClient.read()
	#uClient.close()
	page_html = requests.get(myurl).text #https://stackoverflow.com/questions/36709165/typeerror-object-of-type-response-has-no-len
	#print(page_html)
	 
	# call BeautifulSoup for parsing
	page_soup = soup(page_html, "html.parser")

	recipe_name = page_soup.find("h1").getText()
	#https://stackoverflow.com/questions/36651256/beautifulsoup-get-h2-text-without-class
	h1_txt = page_soup.find("h1")
	h1_txt_h2 = h1_txt.find(class_="h2")
	print(h1_txt_h2.previous_sibling.strip())

	

	#print(recipe_name)

	#recipe_ingredients = [x.get_text().strip() for x in page_soup.findAll("li", {"class": ['first ingredient', 'ingredient']})]
	html_ingre = page_soup.findAll("li", {"class": ['first ingredient', 'ingredient']})

	for i in html_ingre:
		print(i.get_text().strip())

	#print(recipe_ingredients)



def read_ingredients_db(): 
	df = pd.read_csv("ingredientsdb.csv")
	print(df['ingredients'].str.contains('basil'))

def main():
	get_page_ingredients()

	#read_ingredients_db()

if __name__ == "__main__":
	main()


#get data:
#use ocr to read screenshots to get ingredients with amounts
#or use eatyourbooks ingredients.
	#beautiful soup or some webscraper to get recipe: ingredients
		#find all recipe pages (maybe specify all 146 links? )

	#output to csv sheet

#choose recipe
	#see what ingredients needed
	#see what other recipes use x ingredients

#combine all ingredients in all chosen recipes into shopping list