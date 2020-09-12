favorite_languages={'Rakesh':'python', 'suresh':'java', 'Dinesh':'ruby'}
print (favorite_languages['Rakesh'])
print(favorite_languages['suresh'])
print("#################")
for k, v in favorite_languages.items():
#    print (f"\nkey: "{k})
#    print (f"value: "{v})
    print("Key: "+ k)
    print("value: "+ v)
print("#################")

for name in favorite_languages.keys():
    print (name)

print("##################")

for name, language in favorite_languages.items():
    print (name.title() + "\'s favorite lang is " + language)
