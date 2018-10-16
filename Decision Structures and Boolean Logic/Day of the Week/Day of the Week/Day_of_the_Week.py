#Function that asks the user to enter a number which corresponds with a day of the week, if user enters a number that is not valid an error message will appear

const_min = 0; # Min number of days in a week
const_max = 7; # Max number of days in a week

userDay = int(input('Enter a number and I will tell you which day it corresponds with: '));

if userDay < const_min or userDay > const_max:
    print('Invalid input. Please enter a number between 1 and 7');

else:
    if userDay == 1:
         print('You entered Monday');
    elif userDay == 2:
        print('You entered Tuesday');
    elif userDay == 3:
        print('You entered Wednesday');
    elif userDay == 4:
        print('You chose Thursday');
    elif userDay == 5:
        print('You chose Friday');
    elif userDay == 6:
        print('You chose Saturday');
    elif userDay == 7:
        print('You chose Sunday');