# raplace or chaining

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Mohan").replace("<|Date|>","21 September 2050"))