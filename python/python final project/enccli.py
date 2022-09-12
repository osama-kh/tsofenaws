import enckey
from os.path import exists
def enc_init():
    commands = {'info' : enc_info , 'load':enc_load , 'newkey':enc_newkey , 'save':enc_save}
    return commands

def main_cli():
    commands = enc_init()
    cli_end=False
    key={}
    saved=False
    while not cli_end:
        cmd_str=input('subs>')
        cmd = cmd_str.split()
        if cmd and cmd[0] == 'done':
            cli_end = True
        if cmd and cmd [0] == 'newkey':
            key = [cmd[1],enc_newkey(),0]
            
            print('A new key called '+cmd[1]+' was created')
        if cmd and cmd [0] == 'save':
            enc_save(key,cmd[1])
            key[2]=cmd[1]
            print('Enc/Dec keys saved in '+cmd[1]+' file')
        if cmd and cmd [0] == 'load':
            if exists(cmd[1]+'.key'):
                key = enc_load(cmd[1])
                print('Key '+ key[0]+' from file '+ cmd[1]+' loaded')
            else: 
                print('no such key')
        if cmd and cmd[0] == 'enc':
            source=cmd[1]
            dest=cmd[2]
            enc_process(key,source,dest)
            print('File '+source +' was encrypted into '+dest)

        if cmd and cmd[0] == 'dec':
            source=cmd[1]
            dest=cmd[2]
            dec_process(key,source,dest)
            print('File '+source +' was decrypted into '+dest)
        
        if cmd and cmd[0] == 'info':
            enc_info(key)

            
        if not cmd :
            commands[cmd[0]](cmd[1:])


def enc_save(key,dest):
    enckey.save_key(key,dest)

def enc_load(source):
    return enckey.load_key(source)

def enc_newkey():
    new_key = enckey.new_enc_key()
    return new_key

def enc_process(key,source,dest):
    enckey.process_encryption(key,source,dest)

def dec_process(key,source,dest):
    enckey.process_decryption(key,source,dest)


def enc_info(key):
    print('current key:'+ str(key[0]))
    if (key[2] != 0):
        print('state: saved in',key[2])
    else:
        print('state: not saved')
    
    keys_list =''.join(key[1].keys())
    elements_list =''.join(key[1].values())
    print('Encryption:\n' , elements_list)
    print('decryption:\n' , keys_list)

main_cli()