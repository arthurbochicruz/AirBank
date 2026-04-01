import sqlite3

conexao = sqlite3.connect('db/banco.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contas_bancarias(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    titular TEXT NOT NULL,
    saldo REAL NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT NOT NULL UNIQUE
)
""")

def inserir_usuario(titular, idade, saldo, cpf):
    cursor.execute("""
    INSERT INTO contas_bancarias (titular, idade, saldo, cpf)
    VALUES (?, ?, ?, ?)
    """, (titular, idade, saldo, cpf))

    conexao.commit()
    print("Usuário salvo!")

cursor.execute(""" SELECT * FROM contas_bancarias """)
contas = cursor.fetchall()

def encapsulating_data():
    for conta in contas:
        id, titular, idade, saldo, cpf = conta
        print(f"""
                Id: {id}
                Titular: {titular}
                Idade: {idade}
                Saldo: {saldo}
                CPF: {cpf}
            """)

def deleteUsers(id_user):
    
    cursor.execute(""" SELECT * FROM contas_bancarias WHERE id = ? """, (id_user,))
    userChosenToBeDeleted = cursor.fetchone()
    
    if userChosenToBeDeleted is None:
        print('Usuário não encontrado, não foi possivel deletar!')
        return None   
    
    DeletedUserData = {
    "id":   userChosenToBeDeleted[0],
    "titular":  userChosenToBeDeleted[1],
    "idade":    userChosenToBeDeleted[3],
    "saldo":    userChosenToBeDeleted[4],
    "cpf":  userChosenToBeDeleted[4]
    }

    cursor.execute("""DELETE FROM contas_bancarias WHERE id = ?""", (id_user,))
    conexao.commit()
    return DeletedUserData

def updatingBalance(user_for_update, user_value_for_update):
    cursor.execute(""" SELECT * FROM contas_bancarias WHERE id = ? """, (user_for_update,))
    userChosenUpdated = cursor.fetchone()
    
    if userChosenUpdated is None:
        print('Usuário não encontrado, não foi possivel atualizar!')
        return None   
    
    cursor.execute("""UPDATE contas_bancarias SET saldo = ? WHERE id = ?""",
                   (user_value_for_update, user_for_update,))
    conexao.commit()

    cursor.execute(""" SELECT * FROM contas_bancarias WHERE id = ? """, (user_for_update,))
    userChosenUpdated = cursor.fetchone()

    UserDataUpdated = {
        "id": userChosenUpdated[0],
        "titular": userChosenUpdated[1],
        "saldo": userChosenUpdated[2],
        "idade": userChosenUpdated[3],
        "cpf": userChosenUpdated[4]
    }

    return UserDataUpdated
