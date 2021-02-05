import psycopg2

conn = psycopg2.connect(
    database='bank',
    user='maxroach',
    sslmode='require',
    sslrootcert='certs/ca.crt',
    sslkey='certs/client.maxroach.key',
    sslcert='certs/client.maxroach.crt',
    port=26257,
    host='localhost'
)

# conn is a psycopg2 connection

with conn.cursor() as cur:
    cur.execute('INSERT INTO accounts (id, balance) VALUES (1, 1000), (2, 250)')

conn.commit()


# conn is a psycopg2 connection

with conn.cursor() as cur:
    cur.execute("SELECT id, balance FROM accounts")
    rows = cur.fetchall()
    for row in rows:
        print([str(cell) for cell in row])

# conn is a psycopg2 connection

transferAmount = 100
fromID = 1

with conn.cursor() as cur:
    cur.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s",
                (transferAmount, fromID));
conn.commit()

# conn is a psycopg2 connection

with conn.cursor() as cur:
    cur.execute("DELETE FROM accounts WHERE id = 1",
conn.commit()