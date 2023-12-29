import psycopg2
from psycopg2 import extras

from sometools.sync_tools.base import Base


# 然后可以使用 extras 模块中的各种功能，例如


class PgPoolMixIn(Base):
    def __init__(self, *args, **kwargs):
        super(PgPoolMixIn, self).__init__(*args, **kwargs)

    def get_sync_conn(self):
        conn = psycopg2.connect(database="mydatabase", user="myusername", password="mypassword", host="localhost",
                                port="5432")
        cur = conn.cursor(
            cursor_factory=extras.DictCursor)  # 在使用 extras.DictCursor 时，查询结果返回的确实是元组（tuple）类型，其中每个元组的元素都是字段名和对应的值。
        cur = conn.cursor(
            cursor_factory=extras.RealDictCursor)  # 在查询时立即将结果转换为字典类型,查询结果将以列表的形式存储在 result 变量中，每个列表元素都是一个字典，其中键是字段名，值是对应的值
        cur.execute("SELECT * FROM mytable")

        result = cur.fetchall()

        print(result)
