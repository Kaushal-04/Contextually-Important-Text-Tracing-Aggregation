from dataCollection import dataCollect
from dataPreprocessing import cleanText


data = dataCollect()

texts = [cleanText(text) for text in data]
print(texts)
