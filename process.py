import json 

input_text = open('story.txt')
text = input_text.readlines()

new_text = []
for line in text:
    if line.strip():
        print(line)

dataset = {}
dataset['text'] = text

dataset = json.dumps(dataset)

final_set = open('dataset.jsonl', 'w')
final_set.write(dataset)

print('created')