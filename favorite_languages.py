# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
favorite_languages = {}
favorite_languages['jen2'] =['python', 'ruby']
favorite_languages['sarah2'] = ['c']
favorite_languages['edward2'] = ['ruby']
favorite_languages['phil2'] = ['python']
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())