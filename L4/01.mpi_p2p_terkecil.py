#Import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    for i in range(1, size):
        sendMessage = ("pesan")
        comm.send(sendMessage, dest=i)
        print('rank', rank, 'mengirim', sendMessage, 'ke rank', i)

# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    recvMessage = comm.recv(source=0)
    print('rank', rank, 'menerima', recvMessage, 'dari rank',0)

	