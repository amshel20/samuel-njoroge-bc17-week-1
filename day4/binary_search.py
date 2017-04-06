'''First, you are to create a BinarySearch class, that inherits from the list class the following:
the __init__() takes two integers as parameters, a and b. a is the length of the
list to be created and b is the step or difference between consecutive values.
It should also initialize an instance variablelength`, that returns the number of elements in the array
Once you are done, create another method called search, it will take just one
argument which is the value you are to find. The search function should return
a dictionary object, which contains count, the number of times you function
iterated to find the index of the number in question index, the index of the
number in question The search method should implement the binary search algorithm,
each time you iterate, you should increase the count, to test how efficient your implementation is.'''


class BinarySearch(list):


    # Create a list length a and steps b
    def __init__(self, a, b):
        super(BinarySearch, self).__init__()
        self.length = a
        self.step = b
        for i in range(self.step, (self.length * self.step) + 1, self.step):
            self.append(i)


    # the binary search algorithm
    def search(self, value):
        first = 0
        last = self.length - 1
        found = False
        count = 0
        in_list = False

        #if number appears on  list set index to lowest index
        try:
            index = self.index(value)
            in_list = True
        except ValueError:
            index = -1
            in_list = False

        # compare middle element of list with target value
        while first <= last and not found and in_list and value != self[last]:
            midpoint = (first + last) // 2
            mid_value = self[midpoint]
            if mid_value == value:
                found = True
                count += 1
                index = midpoint
            else:
                if value < mid_value:
                    last = midpoint - 1
                    count += 1
                else:
                    first = midpoint + 1
                    count += 1

        # return number of iterations & index of value found in list
        return {"count": count, "index": index}
