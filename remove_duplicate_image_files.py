import sys
import os
import hashlib

allduplicates = []

def chunk_reader(fobj, chunk_size=1024):
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    count = 0
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            count = 0
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk)
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
                if duplicate:
                    count += 1
                    print("Duplicate found:\n %s and %s" % (full_path, duplicate))
                    allduplicates.append(duplicate)
                else:
                    hashes[file_id] = full_path
            print("\n**********************************************************")
            print("\nTotal duplicates in {} : {}".format(dirpath,count))
            print("\n**********************************************************")

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print("Please pass the paths to check as parameters to the script")

for imgname in allduplicates:
    os.remove(imgname)
    # print(imgname)