from dataCollection import dataCollect
from dataPreprocessing import cleanText

texts = dataCollect()
para1, para2 = cleanText(texts)
print("Paragraph 1:", para1)
print("Paragraph 2:", para2)
