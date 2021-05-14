from sometools import Common_tools


class Demo(Common_tools):
    def __init__(self, *args, **kwargs):
        # kwargs['log_file_rec'] = True
        # kwargs['log_file_name'] = 'ConsumptionService'
        super(Demo, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    demo_ins = Demo()
    demo_ins.uuid1 = 'uuid1'
    demo_ins.uuid2 = 'uuid2'


    # 将输入的任何类型的日期字符串类型转化为datetime.datetime类型的日期对象(北京时间UTC+8)(Converts any type of date string type entered to a date object of type datetime.datetime)(beijing time UTC+8)
    demo_ins.logger().info(f"{demo_ins.str_to_obj('2012-12-12 12:12:12')}{type(demo_ins.str_to_obj('2012-12-12 12:12:12'))}")
    demo_ins.logger().info(f"{demo_ins.str_to_obj('11-May-2021 07:03 EDT')}{type(demo_ins.str_to_obj('11-May-2021 07:03 EDT'))}")

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
    demo_ins.logger().exception(f"{Demo.get_pinyin('中国外汇交易中心')}")

    demo_ins.logger().info(f"繁体转简体 眾議長與李克強會談->{Demo.traditional_chinese_to_simplified('眾議長與李克強會談')}")
    demo_ins.logger().info(f"简体转繁体 众议长与李克强会谈->{Demo.simplified_chinese_to_traditional_chinese('众议长与李克强会谈')}")
