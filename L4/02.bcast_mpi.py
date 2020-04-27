# import mpi4py
from mpi4py import MPI

# buat COMM
COMM = MPI.COMM_WORLD

# dapatkan rank proses
rank = COMM.Get_rank()

# dapatkan total proses berjalan
total = COMM.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0 :
    broadscast = {'A' : ('AWAS VIRUS CORONA !!!'),'B' : ('#DirumahAja')}
	
# jika saya bukan rank 0 maka saya menerima pesan
else :
	broadscast = None

broadscast = COMM.bcast(broadscast, root=0)
print('Rank',rank, broadscast)