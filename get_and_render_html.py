import requests
from render_html import render_in_browser

# Making a request with the requests library
response = requests.get('https://example.com')

# Rendering the HTML response in the default browser
html_content = response.text
render_in_browser(html_content)
