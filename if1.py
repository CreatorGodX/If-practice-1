#if pracitce
age = input('how old are you?: ')
age = int(age)

if age < 14 and age >= 7:
    print ('you must be a Elementary school student')
elif age >= 14 and age < 16:
    print ('you must be a jumior high school student')
elif age >= 16 and age < 18:
    print ('you must be a senior high school student')
elif age >= 18 and age < 22:
	print ('you must be a university student')
else:
    print ('you are a social person')




