import concurrent.futures
import requests

def check_website(url):
  response = requests.get(url)
  if response.status_code == 200:
    with open('successful_urls.txt', 'a') as f:
      f.write(url + '\n')
      print(url)
# Website List
with open('website_list.txt', 'r', encoding="utf-8") as f:
  websites = f.readlines()
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
  futures = [executor.submit(check_website, website) for website in websites]
  concurrent.futures.wait(futures)
