# -*- coding: utf-8 -*-
import html

from sometools.sync_tools.base import Base


class HtmlMixIn(Base):
    def __init__(self, *args, **kwargs):
        super(HtmlMixIn, self).__init__(*args, **kwargs)

    @staticmethod
    def html_escape(html_str: str) -> str:
        # 转义
        return html.escape(html_str)

    @staticmethod
    def html_unescape(html_str: str) -> str:
        # 还原
        return html.unescape(html_str)


if __name__ == '__main__':
    print(HtmlMixIn().html_escape("""'& < >\"'"""))
    print(HtmlMixIn().html_unescape("&#x27;&amp; &lt; &gt;&quot;&#x27;"))


