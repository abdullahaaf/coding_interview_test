# Memeriksa jumlah huruf yang sama antara dua kalimat atau kata

def count(str1,str2):
    set_string1 = set(str1)
    set_string2 = set(str2)

    matched_characters = set_string1 & set_string2
    # print("No. of matching characters are : " + str(len(matched_characters)) )
    print(matched_characters)

str1 = "abcdef"
str2 = "defghia"
print(count(str1,str2))

# Algoritma
# 1 buat sebuah fungsi dengan 2 parameter string
# 2 didalam fungsi nomor 1, ubah kedua string tersebut kedalam tipe data set => set(string)
# 3 dengan menggunakan set intersection, buat sebuah variabel yang menggabungkan kedua string yang telah menjadi set => set(string1) & set(string2)
# 4 untuk mengetahui ada berapa huruf yang sama, gunakan fungsi len(variabel_nomor_3)