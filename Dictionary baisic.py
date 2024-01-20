npc_0 = {'color': 'green', 'points': 5} #In python dictionary is built from key and value. Value can be a string, list or even different dictionary 
print(npc_0['color'].title())
print(npc_0['points'])
#Green
#5

npc_0 = {'color': 'green', 'points': 5}
npc_0['aggresive'] = 'very' #There is an option to add new key and values to the dictionary
print(npc_0)
#{'color': 'green', 'points': 5, 'aggresive': 'very'}

npc_0 = {'color': 'green', 'points': 5}
# del npc_0['color] this command will delet the key "color"

#Excersie to create an print data of user
user_data = {'name': 'tom', 'surname': 'brown', 'age': 54, 'city': 'copenhagen'}
print(user_data['name'].title())
print(user_data['surname'].title())
print(user_data['age'])
print(user_data['city'].title())
#Tom
#Brown
#54
#Copenhagen 

programming_languages = {
    'tom': 'python',
    'sara': 'c',
    'edward': 'r',
    'patrick': 'ruby',
    }
for name, language in programming_languages.items():
    print(f'The favourit languge of {name.title()} is {language.title()}')
#The favourit languge of Tom is Python
#The favourit languge of Sara is C
#The favourit languge of Edward is R
#The favourit languge of Patrick is Ruby
    
for name in programming_languages.keys(): #.keys() is presenting only keys from dictionary
    print(name.title())
#Tom
#Sara
#Edward
#Patrick
    
for name in sorted(programming_languages.keys()): #Sorted keys
    print(f'{name.title()}, thanks for sharing your experince.')
#Edward, thanks for sharing your experince.
#Patrick, thanks for sharing your experince.
#Sara, thanks for sharing your experince.
#Tom, thanks for sharing your experince.
    
for language in sorted(programming_languages.values()): #sorted and printed values 
    print (language.title())
#C
#Python
#R
#Ruby
    
rivers = {'nil': 'egypt', 'wisla': 'poland', 'thames': 'england'}
for name, country in rivers.items():
    print(f'{name.title()} is in {country.title()}')
#Nil is in Egypt
#Wisla is in Poland
#Thames is in England
    
for name in sorted(rivers.keys()):
    print(name.title())
#Nil
#Thames
#Wisla
    
