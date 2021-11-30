import asyncio
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
        # 获取链接
        self.aio_redis_conn = await self.get_async_redis_conn(redis_host=kwargs.get('redis_host'),
                                                              redis_port=kwargs.get('redis_port'),
                                                              redis_db=kwargs.get('redis_db'),
                                                              redis_pwd=kwargs.get('redis_pwd'))
        # 使用
        while 1:
            msg = await self.aio_redis_conn.set('temp_key', 'test string')
            print(f'set {msg}')
            msg = await self.aio_redis_conn.get('temp_key')
            print(f'get {msg}')
            await asyncio.sleep(5)
            if __name__ == "__main__":
                break


if __name__ == '__main__':
    # 异步工具使用方法示例
    demo_ins = Demo(TASK_NUMBER=1, redis_host='10.1.90.29',
                    redis_port='6379',
                    redis_db=15,
                    redis_pwd='lhdna2016')
    print('start')
