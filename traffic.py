
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import os

def findLength(data, start):
    length = 1
    index = start
    while data[index+1] != "<":
        length += 1
        index += 1 
    return length

def getPilots():
    url = 'https://stats.vatsim.net/who'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table_entries = str(soup.find_all(class_="table table-striped entry-content"))
    pilots_offset = 17
    pilots_index = table_entries.index("Pilots:")
    numLength = findLength(table_entries, pilots_index+17)
    pilots = int(table_entries[pilots_index+pilots_offset:pilots_index+pilots_offset+numLength])
    return pilots

def writeEntry(pilots):
    header = ['timestamp', 'pilots']
    original = []
    with open('data.csv', "r") as current:
        reader = csv.DictReader(current, delimiter=',')
        for row in reader:
            original.append(row)
    print(original)

    with open("temp.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        new = original
        new.append({
            'timestamp': str(datetime.now()),
            'pilots': pilots
        })
        print(new)
        for row in new:
            writer.writerow(row)
    
    try:
        os.remove("data.csv")
        os.rename("temp.csv", "data.csv")
    except FileNotFoundError as e:
        print(e)

def run():
    print("Scraping Vatsim stats...")
    pilots = getPilots()
    print("Pilots online:", pilots)
    writeEntry(pilots)
    print("CSV updated at", datetime.now())

if __name__ == "__main__":
    run()