# PyCharm: Settings -> Project Interpreter -> + -> Available Packages
import random # giving images random file names to prevent overlaps
import urllib.request # package to get data from websites

def download_web_image(url):
	name = random.randrange(1,1000)
	full_name = str(name) + ".jpeg"
	urllib.request.urlretrieve(url, full_name)
	
	
download_web_image("https://jpeg.org/images/jpeg-home.jpg")