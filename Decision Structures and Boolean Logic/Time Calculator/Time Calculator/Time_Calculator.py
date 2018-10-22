# Program that converts user input seconds to minutes, hour, day

print('This program converts seconds into minutes, hours, days');
seconds = int(input('Please enter the number of seconds you wish to convert: '));

if(seconds < 60 and seconds > 0):
    print('The number is', seconds, 'seconds');

elif(seconds > 60 and seconds < 3600):
    minutes = seconds/60;
    print('The seconds converted to minutes are', format(round(minutes,2)),'minutes');

elif(seconds > 3600 and seconds < 86400):
    hours = seconds/3600;
    print('The seconds converted to hours are', format(round(hours,2)),'hours');

elif(seconds > 86400):
    days = seconds/86400;
    print('The seconds converted to days are', format(round(days,2)),'days');