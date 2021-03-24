one = float(input("Pls, enter the first number: "))
two = float(input("Pls, enter the second number: "))
three = float(input("Pls, enter the third number: "))
four = float(input("Pls, enter the fourth number: "))
one_gr = one + two
two_gr = three + four
answ = one_gr/two_gr
print("You enter: {0}, {1}, {2}, {3}. ".format(one,two,three,four,answ))
print("Task: ({0} + {1})/({2} + {3}).".format(one,two,three,four,answ))
print("Answer: %.2f." % (answ))