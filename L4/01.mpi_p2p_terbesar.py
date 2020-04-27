# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == size-1:
    data = "pesan"
    for i in range(size-1):
        comm.send(data,dest=i)
        print('rank', rank, 'mengirim', data, 'ke rank', i)

# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    data = comm.recv(source = size - 1)
    print('rank', rank, 'menerima', data, 'dari rank', size-1)