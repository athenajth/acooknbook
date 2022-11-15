import pandas as pd
#from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import csv
import argparse


#don't need to use after inital txt doc created
def find_recipe_urls(): 
	myurls = ["https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/2", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/3", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/4", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/5", 
			"https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook/6"]

	with open("recipeurls.txt", 'w') as f:
		for myurl in myurls: 
			print(myurl)
			page_html = requests.get(myurl).text 
			page_soup = soup(page_html, "html.parser")

			base_url = "https://www.eatyourbooks.com"
			for ahref in page_soup.find_all('a', href=True, class_="RecipeTitleExp"): 
				url_str = base_url+ahref['href']
				print ('\t'+url_str)
				f.write(url_str+'\n')


#don't need to use after inital db.csv created
def create_new_ingredientsdbcsv(url_txt): 
	#myurl = 'https://www.eatyourbooks.com/library/recipes/2023109/harissa-and-manchego-omelettes'

	# create csv file of all products
	with open("dbingredients.csv", 'w') as c:
		# create the csv writer
		writer = csv.writer(c)

		c.write("Recipe, Ingredients\n")

		#read from file of urls
		with open(url_txt, 'r') as t:
			for line in t.readlines(): 
				myurl = line.strip()
				print(myurl)
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
		ingred = i.get_text().strip()
		print('\t'+ingred)
		recipe_ingredients.append(ingred)

	# write a row to the csv file
	csvwriter.writerow([recipe_name,recipe_ingredients])

def read_ingredients_db(): 
	df = pd.read_csv("ingredientsdb.csv")
	print(df['ingredients'].str.contains('basil'))

def parse_cmdline(): 
    parser = argparse.ArgumentParser(description='des')
    parser.add_argument('-u', '--url_txt', help='path to txt file with the urls of recipes')
    parser.add_argument('-d', '--db_csv', help='path to csv file with the ingredients db')

    args = parser.parse_args()

    return [args.url_txt, args.db_csv]

def main():
	[url_txt, db_csv] = parse_cmdline()
	if url_txt == None: 
		print("Scraping the following pages for recipe urls: ")
		find_recipe_urls()
		url_txt = "recipeurls.txt"

	if db_csv == None: 
		print("Creating new ingredients database from urls in "+ url_txt +": ")
		create_new_ingredientsdbcsv(url_txt)
		db_csv = "dbingredients.csv"


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