# encoding='utf-8'

aaa = """<a href='javascript:void(0)' encode-open='/UpFiles/zqjghj/zqjghj_46f83333-2625-42a7-9afc-d7e96aeb7c26.pdf'>关于对天津房地产集团有限公司的监管函</a>"""

import re

# string = aaa.replace('\r', '').replace('\n', '').replace('\t', '')
# match = re.search(r'wzwsfactor\|\d+', string, re.I)   # 匹配字符串不区分大小
# print(match)
# print(match.group())
# print(string[553:568])




# match = re.search('data_callback\(\[([\d\D]+?|\s+?|[\r\n]+?)\]\)', aaa, re.S)   # 匹配字符串不区分大小
# match = re.search('data_callback\((.*|\n*)\)', aaa, re.S)   # 匹配字符串不区分大小
# print(match)
# print(type(match.group(1)))
# print(match.group(1))


# comment = re.compile('data_callback\((.*|\n*)\)', flags=re.S)
# print(comment.findall(aaa))

res = aaa
regex = "'>([\s\S]*?)</a>"
res1 = re.search(regex, res).group(1)
print(res1)
