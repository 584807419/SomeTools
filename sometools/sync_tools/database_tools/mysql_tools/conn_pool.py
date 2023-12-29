import MySQLdb
from dbutils.pooled_db import PooledDB
from MySQLdb.cursors import DictCursor
from sometools.sync_tools.base import Base


# pip install mysqlclient -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install DBUtils -i https://pypi.tuna.tsinghua.edu.cn/simple
# 使用dbutils的PooledDB连接池，操作数据库。
# 这样就不需要每次执行sql后都关闭数据库连接，频繁的创建连接，消耗时间
# PooledDB 提供线程间可共享的数据库连接，并自动管理连接。一般来说，PooledDB 的数据库连接耗时更稳定，大多数情况下都推荐使用。
# import sys
# from MySQLdb.converters import conversions
# def mysqlclient_converters():
#     from MySQLdb.constants import FIELD_TYPE
#     conversions[FIELD_TYPE.BIT] = lambda x: 1 if int.from_bytes(x, byteorder=sys.byteorder, signed=False) else 0
#     return conversions


class MysqlPoolMixIn(Base):
    def __init__(self, *args, **kwargs):
        super(MysqlPoolMixIn, self).__init__(*args, **kwargs)

    def get_sync_mysql_conn(self, host='localhost', port=3306, user='root', passwd='', db='my_site', charset='utf8mb4',
                            mincached=10, maxcached=20, maxshared=20, maxconnections=40, blocking=False, maxusage=0,
                            setsession=None, ping=1, ):
        # MySQLdb连接池
        pool = PooledDB(
            mincached=mincached,  # 连接池初始化的总连接数，默认值为 0，不初始化任何连接，推荐使用 10。
            maxcached=maxcached,  # 连接池中最大的空闲连接数量，默认值为 0，无限制，推荐使用 20。
            maxshared=maxshared,  # 最大的共享连接数，默认值为 0，所有连接都为独占，推荐使用 20。
            maxconnections=maxconnections,  # 连接池的最大连接数，硬性限制，默认值为0，无限制，推荐使用 40。
            blocking=blocking,  # 决定连接数达到上限时的行为。设置为 True 时会进入等待状态知道连接数降低；设置为 False 时会直接报错，默认值为 False，推荐使用默认值。
            maxusage=maxusage,  # 单个连接被复用的次数，达到次数之后会关闭并重新打开连接，默认值为 0，无限制，推荐使用默认值。
            setsession=setsession,  # 连接使用前自动执行的 SQL 语句。默认值为 NULL，推荐使用默认值。
            ping=ping,
            # ping: 控制使用 ping() 方法检测连接的方式，（0 = 不检查；1 = 默认，从连接池获取的时候进行检查；2 = 创建游标时检查；4 = 执行查询时检查； 7 = 全部检查，包含 1，2，4 的所有场景），推荐使用默认值。
            creator=MySQLdb,
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset,
            cursorclass=DictCursor,
            # conv=mysqlclient_converters()
        )
        return pool

    def get_sync_mysql_conn_without_pool(self):
        # 简单使用
        import MySQLdb
        from MySQLdb.cursors import DictCursor
        import json


        localhost_conn = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='lh_news_spider',
            charset='utf8mb4'
        )
        aa_set = set()
        localhost_cur = localhost_conn.cursor(DictCursor)

        # sql = f"select * from lh_ns_info where data_source = '中国证券监督管理委员会' and news_type = 37;"
        sql = f"select * from lh_rule_operation_relation a left join lh_data_rule b on a.rule_id=b.id where a.is_valid = 1 and a.datasource_id = 1 and a.data_position = 1 and a.operation_id is NULL order by a.order asc"
        localhost_cur.execute(sql)
        raw = localhost_cur.fetchall()
        rec_count = len(raw)
        data_hash_map = json.loads(raw[0][0])
        data_hash_map = json.loads(raw[0][0])


