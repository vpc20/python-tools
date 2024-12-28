# you can use this in jupyter notebook
import urllib.request

from IPython.display import HTML

urllib.request.urlretrieve("https://adventofcode.com/2024/day/21", "temp.html")
HTML(filename="temp.html")
