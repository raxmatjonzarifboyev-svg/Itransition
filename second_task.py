import hashlib
import zipfile
import math

path=r"C:\Users\Asus\Downloads\task2.zip"
email='raxmatjonzarifboyev@gmail.com'
def get_hex(data:bytes):
    h=hashlib.sha3_256()
    h.update(data)
    context=h.hexdigest()
    return context 

def get_file(file_path:str):
    hex=[]
    with zipfile.ZipFile(file_path,'r') as zf:
        files=zf.infolist()
        
        for i in files:
            if i.is_dir():
                continue
            data=zf.read(i.filename)
            hash=get_hex(data)
            hex.append(hash)
        return hex
    
def sorted_key(info):
    return math.prod([int(ch,16) +1 for ch in info] )
    
def full_solve(file_path,email):
    
    ad=get_file(file_path)
    ad.sort(key=sorted_key)
    joined=''.join(ad)
    joined=joined+email.lower()

    result=hashlib.sha3_256(joined.encode('utf-8')).hexdigest()

    return result

if __name__=='__main__':
   
   a=full_solve(path,email)
   print(a)





