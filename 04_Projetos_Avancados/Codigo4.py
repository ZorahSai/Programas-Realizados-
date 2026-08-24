#Utilizando Hash para proteger uma Senha
import bcrypt

def gerar_hash_seguro(senha_puro_texto):
    senha_bytes = senha_puro_texto.encode('utf-8')

    salt = bcrypt.gensalt()

    senhas_hash = bcrypt.hashpw(senha_bytes, salt)
    return senhas_hash

def verificar_senha(senha_digitada, hash_armazenado):
    senha_bytes = senha_digitada.encode('utf-8')
    
    if bcrypt.checkpw(senha_bytes, hash_armazenado):
        return True
    else:
        return False


