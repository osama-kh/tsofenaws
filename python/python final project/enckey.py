import random,string,ast
def new_enc_key():
    alphabet = list(string.ascii_lowercase)
    shuffeld_alphabet = list(string.ascii_lowercase)
    random.shuffle(shuffeld_alphabet)
    key = dict(zip(alphabet, shuffeld_alphabet))


    return key

def save_key(key,dest):
    file1 = open(dest+'.key',"w")
    file1.write(str(key))
    file1.close



def load_key(source):
    d={}
    with open(source+'.key') as f:
        data = f.read()
    d = ast.literal_eval(data)

    return d


def process_encryption(key,source,dest):
    enc_data=""
    main_key = key[1]
    with open(source) as s:
        data= str(s.read())
        for i in range(len(data)):
            if(data[i]==" "):
                enc_data += " "
            else:
                enc_data += main_key[data[i]]
            
        
    file1 = open(dest,"w")
    file1.write(enc_data)
    file1.close

def process_decryption(key,source,dest):
    dec_data=""
    main_key = key[1]
    keys_list =list(main_key.keys())
    elements_list =list(main_key.values())

    
    
    with open(source) as s:
        data= str(s.read())
        for i in range(len(data)):
            if(data[i]==" "):
                dec_data += " "
            else:
                value = elements_list.index(data[i])
                dec_data += keys_list[value]
            
        
    file1 = open(dest,"w")
    file1.write(dec_data)
    file1.close
