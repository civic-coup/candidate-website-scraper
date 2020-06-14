import urllib
import requests
from bs4 import BeautifulSoup
import csv


# Google returns different results based on wether you use a desktop or mobile user agent
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

headers = {"user-agent" : USER_AGENT}

output_rows = []

with open('input.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(f'{row["candidate"]} running for {row["office"]}')
        
        query = row["candidate"] + ' ' + row["office"]
        query = query.replace(' ', '+')
        URL = f"https://google.com/search?q={query}"

        resp = requests.get(URL, headers=headers)
        
        # Parse successful responses
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            link = ""
            for g in soup.find_all('div', class_='r'):
                anchors = g.find_all('a')
                if anchors:
                    link = anchors[0]['href']
                    if "ballotpedia" not in link:
                        break
            print(f'\t SUCCESS: {link}')
        else:
            print(f'\t FAILURE: recieved status code: {resp.status_code}')
        
        output_rows.append([row["candidate"],row["district"],row["office"],link])
        line_count += 1
    print(f'Processed {line_count} lines.')



with open('output.csv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in output_rows:
        output_writer.writerow(row)
