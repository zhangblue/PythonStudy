# 使用字符串

# 3.2 字符串格式化
format = "Hello,%s. %s enouth for ya?"
values=("workd","Hot")
print(format % values)

# 模板字符串
from string import Template
s=Template("A ${thing} must never ${action}")
d={}
d['thing']="gentleman"
d['action']="show his socks"
s.safe_substitute(d) #不会因缺少值或者不正确使用$字符而出错
s.substitute(d)#如果缺少值或者错误使用$则会报错