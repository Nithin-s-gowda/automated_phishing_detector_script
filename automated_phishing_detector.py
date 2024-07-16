import re
import requests

#function to analyze URLs ofr potentially malicious domains
def check_urls(text):
    #regular expression to find URLs in the text
    urls = re.findall(r'(https?://\S+)',text)
    for url in urls:
        #simple heuristic: check if the URL uses a shortening service
        #more sophisticated checks could involve domain reputation APLs
        if "bit.ly" in url or "tinyurl.com" in url:
            print(f"potential phishing URL detected: {url}")

#function to search for phising keywords
def check_keywords(text):
    #list of common phishing keywords
    keywords = ['confirm','account','urgent','verify','update','password']
    for keyword in keywords:
        if keyword in text.lower():
            print(f"phishing keyword detected: {keyword}")

#function to check for scare tactics
def check_scare_tactics(text):
    scare_tactics_phrases = [
        'immediately','as soon as possible','at risk','secure your account','suspicious activity'
    ]
    for phrase in scare_tactics_phrases:
        if phrase in text.lower():
            print(f"potential use of scare tactics detected: {phrase}")

#main function to run our phishing detector
def phishing_detector(text):
    print("analyzing text for phising indicators...")
    check_urls(text)
    check_keywords(text)
    check_scare_tactics(text)

#example usage
if __name__ == "__main__":
    example_text = input("enter the statement: ")
    # for testing purpose you can use the below statement by removing '#'from below statements
    # """
#Dear user, we've detected suspicious activity on your account.please 
#verify your accoount immediately by visiting this link: https://bit.ly/fake-url"""
phishing_detector(example_text)