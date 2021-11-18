# Memeriksa huruf yang sama antara dua kalimat atau kata

def count(str1,str2):
    set_string1 = set(str1)
    set_string2 = set(str2)

    matched_characters = set_string1 & set_string2
    # print("No. of matching characters are : " + str(len(matched_characters)) )
    print(matched_characters)

str1 = "abcdef"
str2 = "defghia"
print(count(str1,str2))