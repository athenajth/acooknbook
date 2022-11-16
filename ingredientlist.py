import pandas as pd
#from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup
import csv
import argparse


def get_eatyourbooks_pages(initial_url): 
	page_html = requests.get(initial_url).text 
	page_soup = soup(page_html, "html.parser")

	#get all links from pagination id, that doesn't have a class (don't want next-page)
	pages = page_soup.find('li', {"id":"pagination"}).find_all('a', attrs={'class': None})

	#include this inital url in eatyourbook pages
	pages_urls = [initial_url]
	for p in pages: 
		pages_urls.append(p['href'])
	return pages_urls


def recipe_and_ingredients_db_from_pages(): 
	#myurls = ["https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook"]
	myurls = get_eatyourbooks_pages("https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook")
	#print(myurls)

	with open("simpledb.csv", 'w') as c:
		csvwriter = csv.writer(c)

		c.write("Recipe,Page,Ingredients\n")


		for myurl in myurls: 
			print(myurl)
			page_html = requests.get(myurl).text 
			page_soup = soup(page_html, "html.parser")

			#get all blocks of book-data
			for b in page_soup.find_all('div', class_="book-data"): 

				#recipe title is the link text under class = "RecipeTitleExp"
				recipe_title = b.find('a', href=True, class_="RecipeTitleExp").get_text()
				print(recipe_title)

				#
				recipe_page_num = b.find('i', class_="PageNoExp").get_text().strip("(page ").strip(')')
				print(" Page",recipe_page_num)
				
				#ingredients is under an li, where <b>Ingredients</b>. But don't want that part to be part of the ingredients in csv
				lis = b.find_all('li')
				for l in lis: 
					lb = l.find('b')
					if lb:
						if 'Ingredients' in lb.get_text(): 
							recipe_ingredients = l.get_text().replace('Ingredients:','').strip()
							print('\t'+recipe_ingredients)
							break

				#write in csv
				csvwriter.writerow([recipe_title,recipe_page_num,recipe_ingredients])


def read_ingredients_db(dbcsv): 
	df = pd.read_csv(dbcsv)
	pd.set_option('display.max_colwidth', -1)


	print(df.head())

	print(df[df['Ingredients'].str.contains("basil")])


def get_ingredient_recipes(df, ingredient): 
	print(df[df['Ingredients'].str.contains(ingredient, case=False)])

def parse_cmdline(): 
    parser = argparse.ArgumentParser(description='des')
    #parser.add_argument('-u', '--url_txt', help='path to txt file with the urls of recipes')
    parser.add_argument('-d', '--db_csv', help='path to csv file with the ingredients db')
    parser.add_argument('-i', '--ingredient', help='ingredient to find in recipes', required='True')

    args = parser.parse_args()

    #return [args.db_csv, args.ingredient.upper()]
    return [args.db_csv, args.ingredient]


def main():
	[db_csv,ingredients] = parse_cmdline()

	# if url_txt == None: 
	# 	print("Scraping the following pages for recipe urls: ")
	# 	find_recipe_urls()
	# 	url_txt = "recipeurls.txt"

	# if db_csv == None: 
	# 	print("Creating new ingredients database from urls in "+ url_txt +": ")
	# 	create_new_ingredientsdbcsv(url_txt)
	# 	db_csv = "dbingredients.csv"

	#get_eatyourbooks_pages("https://www.eatyourbooks.com/library/186630/ottolenghi-simple-a-cookbook")

	if db_csv == None: 
		print("Creating new ingredients database: ")
		recipe_and_ingredients_db_from_pages()
		db_csv = "simpledb.csv"


	#read_ingredients_db("simpledb.csv")
	pd.set_option('display.max_colwidth', -1)

	df = pd.read_csv(db_csv)
	#df = df.applymap(lambda s: s.upper() if type(s) == str else s) #https://stackoverflow.com/questions/39512002/convert-whole-dataframe-from-lower-case-to-upper-case-with-pandas
	print(df.head())

	#get_ingredient_recipes(df, ingredients)

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
