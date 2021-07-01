import sqlite3


def sql(user_id):
    i = 5
    all_users = []
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM users""").fetchall()
    for elem in result:
        all_users.append(elem)
    last_kaf = [i[0] for i in all_users]
    param = (max(last_kaf) + 1, user_id, i)
    con.execute("""insert into users values (?, ?, ?)""", param)
    con.commit()
    con.close()


def sql2(sagalowok, all_other):
    con = sqlite3.connect("users.db")
    param = (sagalowok, all_other)
    con.execute("""insert into basa_for_neural_network values (?, ?)""", param)
    con.commit()
    con.close()


def sql3(user_id, shablon_number, sagolowok, all_other):
    con = sqlite3.connect("users.db")
    param = (str(user_id), str(shablon_number), str(sagolowok), str(all_other))
    con.execute("""insert into all_users values (?, ?, ?, ?)""", param)
    con.commit()
    con.close()


#sql3('1', '10', 'primer_sagolowka', '[пример, введенных, данных]')
#sql2('Заголовок', 'все остальное')