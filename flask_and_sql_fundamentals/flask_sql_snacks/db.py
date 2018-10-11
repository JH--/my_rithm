import psycopg2


def cursor_connect():
    conn = psycopg2.connect("dbname=flask_sql_snacks")
    cur = conn.cursor()
    return cur, conn


def close(cur, conn):
    cur.close()
    conn.close()


def get_all_snacks():
    cur, conn = cursor_connect()
    cur.execute("SELECT * FROM snacks")
    snacks = cur.fetchall()
    close(cur, conn)
    return snacks


def add_snack(name, kind):
    if not name:
        return
    cur, conn = cursor_connect()
    cur.execute(
        "INSERT INTO snacks (name, kind) VALUES (%s, %s)", (name.strip(), kind.strip())
    )
    conn.commit()
    close(cur, conn)


def show_snack(id):
    cur, conn = cursor_connect()
    cur.execute("SELECT * FROM snacks WHERE id = (%s)", (id,))
    snack = cur.fetchone()
    close(cur, conn)
    return snack


def update_snack(id, new_name, new_kind):
    cur, conn = cursor_connect()
    cur.execute("UPDATE snacks SET name = (%s) WHERE id = (%s)", (new_name.strip(), id))
    conn.commit()
    cur.execute("UPDATE snacks SET kind = (%s) WHERE id = (%s)", (new_kind.strip(), id))
    conn.commit()
    close(cur, conn)


def delete_snack(id):
    cur, conn = cursor_connect()
    cur.execute("DELETE FROM snacks WHERE id=%s;", (id,))
    conn.commit()
    close(cur, conn)

