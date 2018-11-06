from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen2'] = 'python'
favorite_languages['sarah2'] = 'c'
favorite_languages['edward2'] = 'ruby'
favorite_languages['phil2'] = 'python'
for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:"+ language.title())