def check_anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()
    if str1_list == str2_list:
        print(1)
    else:
        print(0)


check_anagram(input(), input())



