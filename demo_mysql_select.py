import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ahmed",
  password="Ahmed_123",
  database="db"
)

cursor = mydb.cursor()
cursor.execute("select user from users")
n = 0
f = open("users.txt", "a")
for x in cursor:
    n = n+1
    user = str(x)
    f.write(f"{user}\n")
    print(f"user {n} added to the list")
f.close()
print(f"{n} users added to users.txt")
