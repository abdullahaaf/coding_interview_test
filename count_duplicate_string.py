# Problem memeriksa jumlah huruf yang duplikat dan total berapa kali huruf tersebut muncul dalam sebuah kalimat

chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "loremipsumsitdoloramet"

count = {}
for s in check_string:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

for key in count:
  if count[key] > 1:
    print (key, count[key])

# algoritma nya sebagai berikut :

# 1 buat string a - z
# 2 buat string kalimat yang akan diperiksa abjad duplikat nya
# 3 buat dictionary kosong yang menampung key abjad dan value jumlah abjad yang ada di string nomor 2
# 4 looping pada string nomor 2
# 5 jika key abjad sudah ada di dictionary, tambahkan value +=1
# 6 jika key abjad belum ada di dictionary, inisialisasi value menjadi 1
# 7 looping key pada dictionary nomor 3 => looping ini diluar dari blok looping nomor 4
# 8 jika value dari key abjad lebih dari 1, maka cetak key dan value dari key tersebut