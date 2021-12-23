# SomeTools

一些常用工具

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=plastic)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/SomeTools.svg?style=plastic)](https://pypi.org/project/SomeTools/)
[![wheel](https://img.shields.io/pypi/wheel/SomeTools.svg?style=plastic)](https://pypi.org/project/SomeTools/)
[![pyversions](https://img.shields.io/pypi/pyversions/SomeTools.svg?style=plastic)](https://pypi.org/project/SomeTools/)
[![Downloads](https://pepy.tech/badge/SomeTools?style=plastic)](https://pepy.tech/badge/SomeTools)

---------------------------------------------

一些方便日常使用的工具

* 将输入的任何类型的日期字符串类型转化为datetime.datetime类型的日期对象
* 移除一个字符串中的回车换行空格制表符等内容
* 将中文字符转为其拼音的首字母
* 更加方便的日志记录工具
* 繁体简体中文汉字转换工具
* redis创建连接同步、异步工具
* 正则表达式提取字符串中的中文内容工具


## Installation

``` bash
$ pip install SomeTools -i https://pypi.python.org/simple
```


## Getting Started

### 1.同步工具使用

``` pycon
from sometools import Common_tools


class Demo(Common_tools):
    def __init__(self, *args, **kwargs):
        # kwargs['log_file_rec'] = True
        # kwargs['log_file_name'] = 'ConsumptionService'
        super(Demo, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    demo_ins = Demo()

    # 将输入的任何类型的日期字符串类型转化为datetime.datetime类型的日期对象(北京时间UTC+8)(Converts any type of date string type entered to a date object of type datetime.datetime)(beijing time UTC+8)
    demo_ins.logger(uuid1='uuid1', uuid2='uuid2').info(
        f"{demo_ins.str_to_obj('2012-12-12 12:12:12')}{type(demo_ins.str_to_obj('2012-12-12 12:12:12'))}")
    demo_ins.logger().info(
        f"{demo_ins.str_to_obj('11-May-2021 07:03 EDT')}{type(demo_ins.str_to_obj('11-May-2021 07:03 EDT'))}")

    # 移除一个字符串中的回车换行空格制表符等内容(Remove carriage return, newline space tabs, etc., from a string)
    temp_str = 'abc abc \n abc \r'
    demo_ins.logger().info(f"before clean string{temp_str}")
    temp_str = Demo.clean_string('abc abc \n abc \r')
    demo_ins.logger().info(f"after clean string{temp_str}")

    # 将中文字符转为其拼音的首字母(Convert Chinese characters to the first letter of their pinyin)
    demo_ins.logger().info(f"{Demo.get_pinyin('中国外汇交易中心')}")

    # 更加方便的日志记录工具(More convenient logging tool)
    demo_ins.logger().info(f"{Demo.get_pinyin('中国外汇交易中心')}")
    demo_ins.logger().debug(f"{Demo.get_pinyin('中国外汇交易中心')}")
    demo_ins.logger().warning(f"{Demo.get_pinyin('中国外汇交易中心')}")
    demo_ins.logger().error(f"{Demo.get_pinyin('中国外汇交易中心')}")

    # 中文繁体简体互转
    demo_ins.logger().info(f"繁体转简体 眾議長與李克強會談->{Demo.traditional_chinese_to_simplified('眾議長與李克強會談')}")
    demo_ins.logger().info(f"简体转繁体 众议长与李克强会谈->{Demo.simplified_chinese_to_traditional_chinese('众议长与李克强会谈')}")

    # url编码解码
    demo_ins.logger().info(f"url编码->{Demo.url_encode('https://www.baidu.com/s?wd=中国')}")
    demo_ins.logger().info(f"url解码->{Demo.url_decode('https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD')}")

    # redis使用
    redis_conn = demo_ins.get_sync_redis_conn(redis_host='10.1.90.29',
                                              redis_port='6379',
                                              redis_db=15,
                                              redis_pwd='lhdna2016'
                                              )
    msg = redis_conn.set('temp_key1', 'test string1')
    demo_ins.logger().info(f"redis set {msg}")
    msg = redis_conn.get('temp_key1')
    demo_ins.logger().info(f"redis get {msg}")

    # 正则提取中文
    temp_str = demo_ins.extract_one_chinese("""downloadPdf1('http://www.sse.com.cn/disclosure/bond/announcement/company/c/2021-03-22/4135530025747110334559080.pdf','厦门建发股份有限公司2021年面向专业投资者公开发行可续期公司债券（第一期）发行公告','2021-03-22','1015','pdf');""")
    demo_ins.logger().info(f"正则提取单个中文 {temp_str}")
    temp_str = demo_ins.extract_multi_chinese("""downloadPdf1('http://www.sse.com.cn/disclosure/bond/announcement/company/c/2021-03-22/4135530025747110334559080.pdf','厦门建发股份有限公司2021年面向专业投资者公开发行可续期公司债券（第一期）发行公告','2021-03-22','1015','pdf');""")
    demo_ins.logger().info(f"正则提取多个中文 {temp_str}")

    # 图片处理
    temp_aa = demo_ins.img_blurred(r'E:\Users\Administrator\Documents\SomeTools\win11_sunrise.jpg')
    print(f"图片模糊后路径{temp_aa}")
    temp_aa, img_path = demo_ins.img_generate_verification_code(r'E:\Users\Administrator\Documents\SomeTools\Arial.ttf', r'E:\Users\Administrator\Documents\SomeTools\\')
    print(f"根据字符串{temp_aa}生成验证码{img_path}")
```


### 2.异步工具使用

``` pycon
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
```