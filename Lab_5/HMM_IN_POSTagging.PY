train_data = [
    [("the", "DET"), ("cat", "NOUN"), ("sat", "VERB")],
    [("the", "DET"), ("dog", "NOUN"), ("barked", "VERB")],
    [("a", "DET"), ("dog", "NOUN"), ("sat", "VERB")]
]

from collections import defaultdict
import math

transition = defaultdict(lambda: defaultdict(int))
emission = defaultdict(lambda: defaultdict(int))
start_prob = defaultdict(int)
tag_counts = defaultdict(int)

for sentence in train_data:
    prev_tag = None
    for i, (word, tag) in enumerate(sentence):
        tag_counts[tag] += 1
        emission[tag][word] += 1

        if i == 0:
            start_prob[tag] += 1
        else:
            transition[prev_tag][tag] += 1

        prev_tag = tag

def normalize(d):
    total = sum(d.values())
    return {k: v / total for k, v in d.items()}

start_prob = normalize(start_prob)

for tag in emission:
    emission[tag] = normalize(emission[tag])

for prev in transition:
    transition[prev] = normalize(transition[prev])


print("Start Prob:", start_prob)
print("Emission:", emission)
print("Transition:", transition)