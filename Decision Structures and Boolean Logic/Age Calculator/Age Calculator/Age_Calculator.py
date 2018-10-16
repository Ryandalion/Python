# Function takes user's age and tells them if they are an infant, child, teen, or adult
# 1 year old or less = INFANT
# 1 ~ 13 year old = CHILD
# 13 ~ 20 = TEEN
# 20+ = ADULT

userAge = int(input('Please enter your age: '));

if userAge < 0 or userAge > 135:
    print('Please enter a valid age');
else:
    if userAge <= 1:
        print('You are an infant');
    elif userAge > 1 and userAge < 13:
        print('You are a child');
    elif userAge >= 13 and userAge <= 20:
        print('You are a teen');
    elif userAge >= 20:
        print('You are an adult');
