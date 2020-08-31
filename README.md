# OutageDataCrawl
## Description 
OutageDataCrawl is Python + selenium based crawler which could help to crawl addresses on https://outagemap.coned.com/external/default.html 
the input is the url(fixed), output is a file which contains addresses grepped from the website
## Install Required dependency
### Python related
1. pip install selenium
you need to install pip first, take a look at here: https://pip.pypa.io/en/stable/installing/
### Selenium related
1. download firefox(chrome cannot work, the move action cannot work well on chrome), https://www.mozilla.org/en-US/exp/firefox/new/ 
2. download firefox driver,  https://github.com/mozilla/geckodriver/releases 
3. move firefox to your PATH, or  just "mv ./geckodriver /usr/local/bin"
4. python crawler.py
