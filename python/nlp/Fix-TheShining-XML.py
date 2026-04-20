import re

def merge_dialogues(match):
        speaker_part = match.group(1)
        dialogues = re.findall(r'<dialogue>(.*?)</dialogue>', match.group(2), re.DOTALL)
        merged_dialogue = ' '.join(dialogues)
        return f'{speaker_part}<dialogue>{merged_dialogue}</dialogue>\n'

with open("../../regex/shinningDialogue.xml", "r") as file:
    text = file.read()
    pattern = re.compile(r'(<speaker>.*?</speaker>\s*)((<dialogue>.*?</dialogue>\s*)+)',
    re.DOTALL)
    new_text = pattern.sub(merge_dialogues, text)
    with open('TheShining_fixed.xml', 'w') as file:    file.write(new_text)
    print ("Dialogues merged successfully. Check 'TheShining_fixed.xml' for the result.")