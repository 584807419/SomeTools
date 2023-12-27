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

[^\u4e00-\u9fa5] //匹配非中文字符

[\u4e00-\u9fa5] //匹配中文字符

^[1-9]\d*$ //匹配正整数
^[A-Za-z]+$ //匹配由26个英文字母组成的字符串
^[A-Z]+$ //匹配由26个英文字母的大写组成的字符串
^[a-z]+$ //匹配由26个英文字母的小写组成的字符串

^[A-Za-z0-9]+$ //匹配由数字和26个英文字母组成的字符串

[\u4E00-\u9FA5\\s]+ 多个汉字，包括空格
[\u4E00-\u9FA5]+ 多个汉字，不包括空格
[\u4E00-\u9FA5] 一个汉字


# regex = r"[\u4E00-\u9FA5\s\S]*?"  # 多个汉字，包括空格
regex = "'\,'([\s\S]*?)'\,'"
res = aaa


pattern = re.compile(r"{}".format(regex))
match = pattern.search(res)
print(match.groups())
