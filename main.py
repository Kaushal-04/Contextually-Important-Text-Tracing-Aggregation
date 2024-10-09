from dataCollection import dataCollect
from dataPreprocessing import cleanText
from ner import extract_entities
from vectorize import vectorize_text
from aggregate import aggregate_entities
from plot import plot_aggregated_entities

def main():
    text_data = dataCollect()

    print("Preprocessing text : ")
    tokens = cleanText(text_data)
    print(f"Tokens: {tokens}\n")

    print("Extracting entities : ")
    entities = extract_entities(text_data)
    print(f"Entities: {entities}\n")

    print("Vectorizing text : ")
    df = vectorize_text(text_data)
    print("TF-IDF Vectorized DataFrame:")
    print(df, "\n")

    print("Aggregating entities : ")
    aggregated_entities = aggregate_entities(entities)
    print(f"Aggregated Entities: {aggregated_entities}\n")

    print("Plotting aggregated entities : ")
    plot_aggregated_entities(aggregated_entities)

if __name__ == "__main__":
    main()
