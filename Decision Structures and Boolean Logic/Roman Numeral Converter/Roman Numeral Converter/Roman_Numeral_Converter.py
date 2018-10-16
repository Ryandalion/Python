# Function converts a number to a roman numeral

userNum = int(input('Please enter a literal number between 1 ~ 10 you wish to convert to a Roman numeral: '));

if userNum < 0 or userNum > 10:
    print('Please enter a number between 1 and 10');
else:
    if userNum == 1:
        print('I');
    else:
        if userNum == 2:
            print('II');
        else:
            if userNum == 3:
                print('III');
            else:
                if userNum == 4:
                    print('IV');
                else:
                    if userNum == 5:
                        print('V');
                    else:
                        if userNum == 6:
                            print('VI');
                        else:
                            if userNum == 7:
                                print('VII');
                            else:
                                if userNum == 8:
                                    print('VIII');
                                else:
                                    if userNum == 9:
                                        print('IX');
                                    else:
                                        if userNum == 10:
                                            print('X');

