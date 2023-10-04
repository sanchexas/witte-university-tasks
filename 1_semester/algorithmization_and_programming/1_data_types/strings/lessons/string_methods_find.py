languages = "Языки: Python, PHP, SQL, HTML, Java."
langs_position = languages.find(": ")
print(langs_position)

languages = languages[langs_position + 2:]
print(languages)

second_language_start_position = languages.find(", ") + 2
second_language_end_position = languages.find(", ", second_language_start_position)
second_language = languages[second_language_start_position:second_language_end_position]
print(second_language)