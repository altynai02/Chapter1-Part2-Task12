# 12. Given a string that may or may not contain a letter of interest. Print the
# index location of the first and last appearance of f. If the letter f occurs
# only once,then output its index. If the letter f does not occur, then do not
# print anything.
# Don't use loops in this task.

any_string = input("Enter something with letter f: ")
if "f" in any_string:
    first_f = any_string.find("f")
    last_f = any_string.rfind("f")
    print(first_f, last_f)
else:
    print("-_-")