import pandas as pd
#from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import csv

#don't need to use after inital txt doc created
def find_recipe_urls(): 
	myurls = ["https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/2", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/3", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/4", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/5", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/6"]

	for myurl in myurls: 
		page_html = requests.get(myurl).text 
		page_soup = soup(page_html, "html.parser")

		base_url = "https://www.eatyourbooks.com"
		for ahref in page_soup.find_all('a', href=True, class_="RecipeTitleExp"): 
			print (base_url+ahref['href'])


#don't need to use after inital db.csv created
def create_new_ingredientsdbcsv(): 
	#later read from file of urls
	myurl = 'https://www.eatyourbooks.com/library/recipes/2023109/harissa-and-manchego-omelettes'


	# create csv file of all products
	with open("created_ingreds.csv", 'w') as f:
		# create the csv writer
		writer = csv.writer(f)

		f.write("Recipe, Ingredients\n")

		# write a row to the csv file
		webpage_ingredients_to_row(writer, myurl)

def webpage_ingredients_to_row(csvwriter, myurl): 
	#https://www.geeksforgeeks.org/scrap-books-using-beautifulsoup-from-books-toscrape-in-python/
	# variable to store website link as string
	#myurl = 'https://www.eatyourbooks.com/library/recipes/2023109/harissa-and-manchego-omelettes'
	# grab website and store in variable uclient
	#uClient = uReq(myurl)
	 
	# read and close HTML
	#page_html = uClient.read()
	#uClient.close()
	page_html = requests.get(myurl).text #https://stackoverflow.com/questions/36709165/typeerror-object-of-type-response-has-no-len
	#print(page_html)
	 
	# call BeautifulSoup for parsing
	page_soup = soup(page_html, "html.parser")

	#recipe_name = page_soup.find("h1").getText()
	#https://stackoverflow.com/questions/36651256/beautifulsoup-get-h2-text-without-class
	h1_txt = page_soup.find("h1")
	h1_txt_h2 = h1_txt.find(class_="h2")
	recipe_name = h1_txt_h2.previous_sibling.strip()
	print(recipe_name)

	

	#print(recipe_name)

	#recipe_ingredients = [x.get_text().strip() for x in page_soup.findAll("li", {"class": ['first ingredient', 'ingredient']})]
	html_ingre = page_soup.findAll("li", {"class": ['first ingredient', 'ingredient']})

	recipe_ingredients = []
	for i in html_ingre:
		#print(i.get_text().strip())
		recipe_ingredients.append(i.get_text().encode('utf-8').strip())
	print(recipe_ingredients)

	for i in recipe_ingredients: 
		print(i)



	# write a row to the csv file
	csvwriter.writerow([recipe_name,recipe_ingredients])





def read_ingredients_db(): 
	df = pd.read_csv("ingredientsdb.csv")
	print(df['ingredients'].str.contains('basil'))

def main():
	find_recipe_urls()
	#create_new_ingredientsdbcsv()

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