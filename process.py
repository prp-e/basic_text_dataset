import json 

input_text = open('story.txt')
text = input_text.readlines()

new_text = []
for line in text:
    if not line.isspace():
        if line.rstrip():
            new_text.append(line)

new_text = ' '.join(new_text)
new_text = new_text.replace('\n', '')

print(new_text)

dataset = {}
dataset['text'] = new_text

dataset = json.dumps(dataset)

final_set = open('dataset.jsonl', 'w')
final_set.write(dataset)

print('created')