## a = 'hello' #capitalize
## b = 'tom' #uppercase
## c = 'LAURA' #lowercase
## question = 'How are you' #change o in e
## age_question = 'How old are you?' #use the correct method to create a string for each word
## print(a, b, c, question, age_question)
a,b,c = 'hello','tom','LAURA'
d = a.capitalize()
e = b.upper()
f = c.lower()
a=d
b=e
c=f
question = 'How are you'
g= question.replace('o', 'e')
age_question = 'How old are you?'
h=age_question.split()
print(a,b,c,g,h)