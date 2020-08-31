# OutageDataCrawl
## Description 
OutageDataCrawl is Python + selenium based crawler which could help to crawl addresses on https://outagemap.coned.com/external/default.html 
the input is the url(fixed), output is a file which contains addresses grepped from the website，file name is: current date. csv, following the examples of the output:

* (base) YushuRao:OutageDataCrawl YushuRao$ cat Aug-25-2020.csv 
 *  9627 ATLANTIC AV###1598400447.1718469
 *  8682 15 AV###1598400462.453669
 *  3635 PAULDING AV###1598400477.3845341
 *  8682 15 AV###1598400492.281429
 *  3406 9 ST###1598401396.014292

the format is "address###timestamp" pattern, timestamp is the time point which we captured the address, so clients we would like to use this data can decide whether to remove the dup or not. 

file name is Aug-25-2020.csv, which is date.csv as demonstated as above. 

## Install Required dependency
### Python related
1. pip install selenium
you need to install pip first, take a look at here: https://pip.pypa.io/en/stable/installing/
### Selenium related
1. download firefox(chrome cannot work, the move action cannot work well on chrome), https://www.mozilla.org/en-US/exp/firefox/new/ 
2. download firefox driver,  https://github.com/mozilla/geckodriver/releases 
3. move firefox to your PATH, or  just "mv ./geckodriver /usr/local/bin"
4. python crawler.py
