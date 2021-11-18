# Memeriksa apakah sebuah kata termasuk palindrome atau tidak

def isPalindrome(s):
    return s == s[::-1]
 
# Driver code
s = "kakak"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

# algoritma sebagai berikut 
# 1 buat fungsi python yang memiliki return bahwa string awal sama dengan string yang dibalik => syntax string dibalik string[::1]
# 2 buat string yang berisi kalimat yang akan dicek
# 3 buat variabel yang menjadi objek dari fungsi nomor 1
# 4 cek jika nomor 3 palindrome cetak yes
# 5 cek jika tidak cetak no 