# -*- coding: utf-8 -*-
"""ContohAplikasiRL_TiffanM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19NbvF54yaJUezQLS1OSlnkHSJvHvOh-Y
"""

#Meng-inisialisasi kamus untuk menyimpan sub-masalah
memo_dict = {}

def fibonacci(n):
    #Jika jawaban untuk urutan fibonacci ke-n sudah ada dalam kamus, maka jawaban harus dikembalikan
    if(n in memo_dict):
        return(memo_dict[n])
    if n <= 2:
        return (1)
    else:
      #Simpan jawaban urutan fibonacci ke-n ke dalam kamus untuk digunakan lebih lanjut nantinya
        memo_dict[n] = (fibonacci(n-1)+fibonacci(n-2))
        return(memo_dict[n])
if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))