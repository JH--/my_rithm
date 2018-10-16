import psycopg2


def cursor_connect():
    conn = psycopg2.connect("dbname=flask-sql")
    cur = conn.cursor()
    return cur, conn


def close(cur, conn):
    cur.close()
    conn.close()


def get_all_toys():
    cur, conn = cursor_connect()
    cur.execute("SELECT * FROM toys")
    toys = cur.fetchall()
    close(cur, conn)
    return toys


def add_toy(name):
    if not name:
        return
    cur, conn = cursor_connect()
    cur.execute("INSERT INTO toys (name) VALUES (%s)", (name,))
    conn.commit()
    close(cur, conn)


def show_toy(id):
    cur, conn = cursor_connect()
    cur.execute("SELECT * from toys where id = (%s)", (id,))
    toy = cur.fetchone()[1]
    close(cur, conn)
    return toy


def update_toy(id, new_name):
    cur, conn = cursor_connect()
    cur.execute("UPDATE toys SET name = (%s) where id = (%s)", (new_name, id))
    conn.commit()
    close(cur, conn)


def delete_toy(id):
    cur, conn = cursor_connect()
    cur.execute("DELETE FROM toys where id = (%s)", (id,))
    conn.commit()
    close(cur, conn)
