import json 

input_text = open('basic_farsi.txt')
text = input_text.read()


new_text = text.replace('\n', '')

print(new_text)

dataset = {}
dataset['text'] = new_text

dataset = json.dumps(dataset)

final_set = open('farsi_dataset.jsonl', 'w')
final_set.write(dataset)

print('created')