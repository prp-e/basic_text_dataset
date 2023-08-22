import json 

input_text = open('story.txt')
text = input_text.readlines()
text = ''.join(text)
text = text.replace('\n', '')

dataset = {}
dataset['text'] = text

dataset = json.dumps(dataset)

final_set = open('dataset.jsonl', 'w')
final_set.write(dataset)

print('created')