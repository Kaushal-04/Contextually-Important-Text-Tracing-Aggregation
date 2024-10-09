from collections import Counter

def aggregate_entities(entities):
    entity_counts = Counter([ent[0] for ent in entities])
    return entity_counts.most_common()
