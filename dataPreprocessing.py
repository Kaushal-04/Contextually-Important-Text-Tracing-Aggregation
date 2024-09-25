import re
def cleanText(texts):
    texts = re.sub(r'\s+',' ',texts)
    texts = re.sub(r'\d+','',texts)
    texts = texts.lower()
    return texts