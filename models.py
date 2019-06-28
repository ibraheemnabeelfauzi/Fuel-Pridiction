import sqlite3

ROOT = path.dirname(path.relpath((__file__)))

def create_post(clientLocation, companyProfitMargin, SeasonRateFluctuation, CompetitorRate):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cusor()
    cur.execute('insert into posts (clientLocation, companyProfitMargin, SeasonRateFluctuation, CompetitorRate) values(?, ?, ?, ?)', (clientLocation, companyProfitMargin, SeasonRateFluctuation, CompetitorRate)
    con.commit()
    con.close()

    def get_posts():
         con = sql.connect(path.join(ROOT, 'database.db'))
         cur = con.cursor()
         cur.execute('select * from posts')
         posts = cur.fetchall()
         return posts