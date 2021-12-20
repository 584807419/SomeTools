# 工具箱中的工具都是开箱即用的，不依赖特别的数据、配置和业务逻辑
__author__ = 'zhangkun'

from sometools.async_tools.redis_tools import AsyncIoRedisMixIn
from sometools.async_tools.bloom_filter import AioBloomFilterMixIn


class CommonAsyncTools(AsyncIoRedisMixIn, AioBloomFilterMixIn):
    def __init__(self, *args, **kwargs):
        super(CommonAsyncTools, self).__init__(*args, **kwargs)