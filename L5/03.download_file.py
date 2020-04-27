# Import os, requests, threading, urllib, time
import os
import requests
import threading
import urllib.request, urllib.error, urllib.parse
import time

# Url file yang akan di download
url = "https://apod.nasa.gov/apod/image/1901/LOmbradellaTerraFinazzi.jpg"

# Membagi jumlah data yang akan di download
def buildRange(value, numsplits):
    lst = []
	
    # Perulangan untuk membagi jumlah data
    for i in range(numsplits):
        if i == 0:
            lst.append('%s-%s' % (i, int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
        else:
            lst.append('%s-%s' % (int(round(1 + i * value/(numsplits*1.0),0)), int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
    return lst

# Membagi buffer dan jumlah thread saat download
class SplitBufferThreads(threading.Thread):
    """ Splits the buffer to any number of threads
        thereby, concurrently downloading through
        ny number of threads.
    """

    # Membagi buffer 
    def __init__(self, url, byteRange):
        super(SplitBufferThreads, self).__init__()
        self.__url = url
        self.__byteRange = byteRange
        self.req = None

    # Request url
    def run(self):
        self.req = urllib.request.Request(self.__url,  headers={'Range': 'bytes=%s' % self.__byteRange})

    # Mendapatkan file data dan dibaca    
    def getFileData(self):
        return urllib.request.urlopen(self.req).read()

# Fungsi utama dengan membagi download menjadi 3 thread
def main(url=None, splitBy=3):
    start_time = time.time()

    # Jika tidak terdapat url
    if not url:
        print("Please Enter some url to begin download.")
        return

    # Jumlah byte yang akan di download
    fileName = url.split('/')[-1]
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)
    print("%s bytes to download." % sizeInBytes)
    if not sizeInBytes:
        print("Size cannot be determined.")
        return

    # Pembagian thread
    dataLst = []
    for idx in range(splitBy):
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx]
        bufTh = SplitBufferThreads(url, byteRange)
        bufTh.start()
        bufTh.join()
        dataLst.append(bufTh.getFileData())

    content = b''.join(dataLst)

    # Mengecek apakah file sudah didownload
    if dataLst:
        if os.path.exists(fileName):
            os.remove(fileName)
        print("--- %s seconds ---" % str(time.time() - start_time))
        with open(fileName, 'wb') as fh:
            fh.write(content)
        print("Finished Writing file %s" % fileName)

if __name__ == '__main__':
    main(url)