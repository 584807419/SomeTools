from common_tools import Common_tools


class Demo(Common_tools):
    def __init__(self, *args, **kwargs):
        super(Demo, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    demo_ins = Demo()
    demo_ins.logger.info(f"{demo_ins.str_to_obj('2012-12-12 12:12:12')}{type(demo_ins.str_to_obj('2012-12-12 12:12:12'))}")
