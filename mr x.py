statement=input()  # user input statement

statement=statement.casefold() # conversion of upper case in lower case


y=[]

# converting into list
for i in range (len(statement)):
    y.append(statement[i])

a=[]

vowel='aeiou' # vowel which have to find

# logic for finding vowel in sentence
for i in range (len(vowel)):
    for j in range (len(y)):
        if (y[j] in vowel[i]):
            a.append(vowel[i])

print('vowel in sentence=',a)
d=[]
for i in range (len(a)):
    s=a.count(a[i])
    d.append(s)
print('each vowel repeated as',d)
        
    
