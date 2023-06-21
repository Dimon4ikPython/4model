def palindrome(string):
    string = string.lower().replace(" ", "")
    string_reverse = string[::-1]
    if string == string_reverse:
        print("True")
    else:
        print("False")

palindrome("Лепс спел")