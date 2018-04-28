import requests # required when connecting to a url
from bs4 import BeautifulSoup # scrape, pick certain pieces of a webpage (ignore rest)
import operator # allows you to work with built-in data types

# Create a list of every word
def start(url):
	word_list = []
	source_code = requests.get(url).text   # get source code as plain text
	soup = BeautifulSoup(source_code, "lxml")  # need to work with soup object #option:lxml
	# by inspecting link elements on page, can see properties that are unique to these elements
	for post_text in soup.findAll('a', {'class': 'title text-semibold'}):
		content = post_text.string  # only get the text (removes html crap)
		words = content.lower().split()  # lowercase everything, split into words
		for each_word in words:
			#print(each_word)
			word_list.append(each_word)
		clean_up_list(word_list)

# Remove symbols from words
def clean_up_list(word_list):
	clean_word_list = []
	for word in word_list:
		symbols = "!@#$%^&*()_+-=<>?:~{|}`[],./\"" # escaped " last
		for i in range(0, len(symbols)):
			word = word.replace(symbols[i], "")
		if len(word) > 0:
			#print(word)
			clean_word_list.append(word)
	create_dictionary(clean_word_list)	
	
# Dictionary for word counts
def create_dictionary(clean_word_list):
	word_count = {}  # blank dictionary
	for word in clean_word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	for key, value in sorted(word_count.items(), key=operator.itemgetter(1)): # 0:key, 1:val
		print(key, value)
	
	
# Run the program			
start('https://thenewboston.com/forum/')
