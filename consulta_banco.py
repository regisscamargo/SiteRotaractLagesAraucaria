import sqlite3

banco = sqlite3.connect("numeros", check_same_thread=False)

cursor = banco.cursor()


def cria_banco():
    cursor.execute("CREATE TABLE numeros(id_numero, comprador, telefone, vendedor)")
    for i in range(300):
        cursor.execute(f"INSERT INTO numeros VALUES ({i+1}, NULL, NULL, NULL)")
        banco.commit()
# abc = cursor.execute("SELECT * FROM numeros")

# for i in abc:
#     print(i)


def consulta(nro_consultado):
    query = cursor.execute(f"SELECT comprador FROM numeros WHERE id_numero={nro_consultado}")
    return query


def livres():
    lista = []
    query = cursor.execute("SELECT id_numero  FROM numeros WHERE comprador = ''")
    for i in query:
        lista.append(i[0])
    return lista


def insere_dados(nro_consultado_dados, comprador, telefone, vendedor):
    cursor.execute(f"UPDATE numeros SET comprador='{comprador}', telefone='{telefone}', vendedor='{vendedor}' WHERE id_numero={nro_consultado_dados}")
    banco.commit()
