import json 

input_text = open('story.txt')
text = input_text.readlines()
text = ''.join(text)
text = text.replace('\n', '')

print(text)