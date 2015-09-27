import bs4
import urllib2
import re
from alchemyapi import AlchemyAPI
import json

alchemyapi = AlchemyAPI()

# Input handling shared by Sekhar Mekala.

text_extracted = ''

while True:
  try:
     print "\n\n Input the URL to analyze.".center(50," ")
     print "Hit ENTER for the URL to be parsed:"
     url = raw_input("\nInput the URL OR Press ENTER for default URL==>")

     if url == '': url = "https://www.cfa.harvard.edu/news/2015-19" # this is the default
     page = urllib2.urlopen(url)
  except:
     print "\n\nIncorrect URL / Connection problem"
  else:
     break

# Processing with BeautifulSoup

soup = bs4.BeautifulSoup(page.read())
page.close() # Does closing the page matter here or is this just good practice?

paragraphs = soup.findAll('p') # Finding all of the "p" tags

# Text from the p tags is processed and collected as a string variable

for p in paragraphs:
    f = re.sub(r"\[.*\]","", p.text.encode("utf-8")) # regex
    # text_extracted = text_extracted + p.text.encode("utf-8")
    text_extracted = text_extracted + f

web_text = text_extracted

print '\n\n'
print "URL Source: " + url
print web_text
print '\n\n'

print '#### Top 10 Keywords ####'.center(80," ")

response = alchemyapi.keywords('text', web_text, {'sentiment': 1}) # From example.py of alchemyapi module

# Processing the XML

if response['status'] == 'OK':

    print '\n'
    print "Keyword".center(50," ") + "Relevance".center(10," ") + "Sentiment".center(10," ")
    print "="*80 # underline
    i = 0
    for keyword in response['keywords']: # loop to specify top ten based on relevance
        i += 1
        if i > 10: break
        if 'score' in keyword['sentiment']:
           print keyword['text'].encode('utf-8').center(50, " ") + str(keyword['relevance']).center(10, " ") + str(keyword['sentiment']['type']).center(10, " ")
        else:
           print keyword['text'].encode('utf-8').center(50, " ") + str(keyword['relevance']).center(10, " ") + str(keyword['sentiment']['type']).center(10, " ")
else:
    print 'Error in keyword extaction call: ' + response['statusInfo']
