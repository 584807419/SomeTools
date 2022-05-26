import asyncio
import datetime
import platform

if not (platform.system() == 'Windows'):
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())  # 使用 uvloop 来替换 asyncio 内部的事件循环。

from sometools.async_tools import CommonAsyncTools


class Demo(CommonAsyncTools):
    def __init__(self, *args, **kwargs):
        super(Demo, self).__init__(*args, **kwargs)
        # 事件循环
        task_number = kwargs.get('TASK_NUMBER')
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(self.ready(**kwargs)) for _ in range(task_number)]
        if platform.system() == 'Windows':
            loop.set_debug(True)
        loop.run_until_complete(asyncio.wait(tasks))

    async def ready(self, **kwargs):
        # 1. redis示例
        self.aio_redis_conn = await self.get_async_redis_conn(redis_host='xx.xx.xx.xx',
                                                              redis_port='6379',
                                                              redis_db=1,
                                                              redis_pwd='xxx')
        msg = await self.aio_redis_conn.set('temp_key', 'test string')
        print(f'redis set {msg}')
        msg = await self.aio_redis_conn.get('temp_key')
        print(f'redis get {msg}')
        # await asyncio.sleep(5)

        # 2. 布隆过滤示例
        to_filter_url = 'https://zhuanlan.zhihu.com/p/376305519'
        _is_filted = await self.aio_is_bloom_filter_contains(to_filter_url)
        print(f'布隆过滤 是否存在：{_is_filted}')
        res = await self.aio_bloom_filter_insert(to_filter_url)
        print(f'布隆过滤 插入：{res}')
        _is_filted = await self.aio_is_bloom_filter_contains(to_filter_url)
        print(f'布隆过滤 是否存在：{_is_filted}')

        # 3. mysql orm 示例
        from sometools.async_tools.database_tools.mysql_tools.async_mysql_orm import Model, StringField, TextField, \
            IntegerField, DateTimeField
        # 创建连接池
        db_conn_pool = await self.create_db_conn_pool(
            DATABASE_HOST='localhost',
            DATABASE_PORT=3306,
            DATABASE_USER='root',
            DATABASE_PWD='root',
            DATABASE_DB='db_name_xxxx',
            DATABASE_CHARSET='utf8mb4',
            DATABASE_AUTOCOMMIT=True,
            DATABASE_MAX=10,
            DATABASE_MIN=1,
        )

        # 创建模型
        class BondPrices(Model):
            __db_conn_pool__ = db_conn_pool
            __table__ = "bond_prices"
            id = IntegerField(primary_key=True)
            trade_time = DateTimeField()
            trade_data = TextField()
            page_name = StringField(ddl='varchar(45)')
            is_valid = IntegerField()
            data_source = StringField(ddl='varchar(100)')
            verify_md5 = StringField(ddl='varchar(40)')
            clean_status = IntegerField()
            create_at = DateTimeField()
            update_at = DateTimeField()

        print('检查表是否存在')
        data_array = await BondPrices.table_exists('erqqwrwfdsa')
        if data_array == 1:
            print('表存在')
        else:
            print('表不存在')

        print('直接执行sql语句')
        data_array = await BondPrices.execute_sql('select * from bond_prices')
        if data_array:
            for data_hashmap in data_array:
                print(data_hashmap)
        print('增加')
        bond_price_data = BondPrices(trade_time=datetime.datetime.now(),
                                     trade_data='dadad',
                                     page_name='保存pagename',
                                     data_source='单顺荣',
                                     is_valid=1,
                                     verify_md5='123456789',
                                     clean_status=2,
                                     create_at=datetime.datetime.now(),
                                     update_at=datetime.datetime.now(),
                                     )
        insert_res = await bond_price_data.save_db_date()
        if insert_res:
            print(f'插入数据成功，主键是{insert_res}')

        print('修改')
        bond_price_data = BondPrices(id=4,
                                     trade_time=datetime.datetime.now(),
                                     trade_data='dadad',
                                     page_name='愤忿忿忿忿忿忿忿忿忿忿',
                                     data_source='单顺荣',
                                     is_valid=1,
                                     verify_md5='123456789',
                                     clean_status=2,
                                     create_at=datetime.datetime.now(),
                                     update_at=datetime.datetime.now(),
                                     )
        insert_res = await bond_price_data.update_db_date()
        if insert_res:
            print(f'修改数据成功，影响行数是{insert_res}')

        print('删除')
        data_array = await BondPrices.select_by_where(id=3)
        if data_array:
            remove_res = await data_array[0].remove_db_date()
            print(f'删除数据成功，影响行数是{remove_res}')

        print('查询')
        data_array = await BondPrices.select_by_where(id=3, page_name='报价行情', limit=1)
        if data_array:
            data_hashmap = dict(data_array[0])
            print(data_hashmap.get('verify_md5'))


if __name__ == '__main__':
    # 异步工具使用方法示例
    demo_ins = Demo(TASK_NUMBER=1)
    print('end')
