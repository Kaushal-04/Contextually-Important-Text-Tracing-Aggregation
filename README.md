# Contextually-Important-Text-Tracing-And-Aggregation
<h3>1. Install the necessary libraries</h3>
spacy, nltk, pandas, scikit-learn, matplotlib, seaborn, plotly, gensim, transformers <br> 
<b>cmd command</b> "pip install spacy nltk pandas scikit-learn matplotlib seaborn plotly gensim transformers"
<h3>2. Data Collection</h3>
Use web Scaping tool like "BeautifulSoup"
<h3>3. Data Preprocessing</h3>
Text Cleaning
<h3>4. NER(Named Entity Recognition)</h3>
Download : python -m spacy download en_core_web_sm
<h3>4. Vectorization</h3>
Using TfidfVectorizer from scikit-learn.
<h3>4. Aggregation</h3>
Aggregate the named entities extracted from the text and provide a count of how many times each entity occurs. This can help in understanding the prominence of certain entities within the given text, making it easier to identify key subjects or topics discussed.
<h3>4. Visualization</h3>
Visualize the frequency of contextually important entities extracted from the text. The bar chart provides a clear and immediate understanding of which entities are most prominent, making it easier to analyze the data visually.

<h3>4. Example</h3>
    texts = """
    Apple Inc. is looking at buying U.K. startup for $1 billion. 
    The deal would mark the company's first acquisition in Europe. 
    Tim Cook, CEO of Apple, stated that this acquisition is part of the company's strategy to expand its presence in the region.
    """
    
![My Image](https://github.com/Kaushal-04/Contextually-Important-Text-Tracing-Aggregation/blob/main/ScreenShot/Plot.png)
