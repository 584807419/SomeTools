# encoding='utf-8'

aaa = """downloadPdf1('http://www.sse.com.cn/disclosure/bond/announcement/company/c/2021-03-22/4135530025747110334559080.pdf','厦门建发股份有限公司2021年面向专业投资者公开发行可续期公司债券（第一期）发行公告','2021-03-22','1015','pdf');"""

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
regex = "downloadPdf1\('([\s\S]*?)'\,"
res1 = re.search(regex, res).group(1)
print(res1)
