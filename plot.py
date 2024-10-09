import matplotlib.pyplot as plt

def plot_aggregated_entities(aggregated_entities):
    labels, values = zip(*aggregated_entities)
    plt.bar(labels, values)
    plt.xlabel('Entities')
    plt.ylabel('Count')
    plt.title('Aggregated Contextually Important Entities')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
