import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

# DB 생성 (오토 커밋)
conn = sqlite3.connect("./DB/2021-05-17_DeepLearning.db", isolation_level=None)
# 커서 획득
c = conn.cursor()
# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("select * from attendance")

c.close()