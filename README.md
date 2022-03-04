# VatsimTraffic

A simple web scraper that checks the number of pilots connected to the VATSIM Network and logs the result in a CSV file along with the current timestamp. Developed to analyse
server popularity at various times and days of the week.

## Usage:

- Create a python virtual environment and install the dependencies from requirements.txt. 
- Each time traffic.py is run, it will update the CSV file.
- If you would like to automate the process on Linux, edit the run.sh file to point to your virtual environment and then use crontabs or a similar daemon to run this script at set intervals.
