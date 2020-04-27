# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
angka = random.randint(1,100)

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    sum = 0
    for i in range (1,size):
        nilai = comm.recv(source = i, tag = 1)
        print(nilai)
        sum = sum + nilai['send']
    print("Total = ", sum)
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    nilai = {'rank' : rank, 'dest' : 0, 'send' : angka}
    comm.send(nilai,dest=0,tag=1)
