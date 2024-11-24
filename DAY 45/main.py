from bs4 import BeautifulSoup
import requests

# with open(file="website.html", mode="r", encoding="utf8") as html_file:
#     contents = html_file.read()
    
# print(contents)

response = requests.get("https://news.ycombinator.com/")

title_lines = BeautifulSoup(response.text, "html.parser").select(selector=".titleline > a")
score_lines = BeautifulSoup(response.text, "html.parser").select(selector=".score")

final_list = []

for i in range(0, len(title_lines)):
    final_list.append([title_lines[i].getText(), 
                       title_lines[i].get('href'), 
                       int(score_lines[i].getText().split(' ')[0])])
    
    
def list_sort(item):
    return item[2]

final_list.sort(reverse = True, key = list_sort)
print(final_list)