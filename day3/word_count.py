def words(input):

    # empty dictionary to hold solution
    solution = {}

    #test the input type
    if type(input) == str:

        # split the input phrase to sub_strings
        sub_strings = input.split()

        for count in sub_strings:
            # already exists in our dictionary
            if count in solution:
                #make dictionary convert integer string to integer
                if count.isdigit() == True:
                    count = int(count)
                # increment value if more than one sub_strings exist
                    solution[count] += 1

                #treat it as a string
                else:
                # increment value by one if they exist
                    solution[count] += 1

                #does not exist in our dictionary
            else:
                 # if key is a integer
                if count.isdigit() == True:
                    count = int(count)
                    solution[count] = 1
                else:
                    solution[count] = 1
        # return populated solution with names and count as key values
        return solution
