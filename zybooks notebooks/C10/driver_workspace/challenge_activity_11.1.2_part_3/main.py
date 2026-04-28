import persons
import colors
import clothing
import search
one_sentence = input()
has_color = search.find(one_sentence, colors.search_list)
has_person_and_clothing = search.find(one_sentence, persons.search_list) and search.find(one_sentence, clothing.search_list)
if has_color:
    print("The sentence mentions a color.") 
if has_person_and_clothing:
    print("The sentence mentions a person and a piece of clothing.")