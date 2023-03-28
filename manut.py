import sqlite3

banco = sqlite3.connect("numeros", check_same_thread=False)

cursor = banco.cursor()

cursor.execute("CREATE TABLE numeros(id_numero, comprador, telefone, vendedor)")
for i in range(200):
    cursor.execute(f"INSERT INTO numeros VALUES ({i+1}, NULL, NULL, NULL)")
    banco.commit()