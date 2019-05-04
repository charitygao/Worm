#使用lxml库
from lxml import etree
text = '''
<div>
<ul>
<li class="red"><h1>red flowers</h1></li>
<li class="yellow"><h1>yellow flowers</h1></li>
<li class="white"><h1>white flowers</h1></li>
<li class="black"><h1>black flowers</h1></li>
<li class="blue"><h1>blue flowers</h1>
</ul>
</div>
'''
html = etree.HTML(text)
print (html) #Lxml 库解析数据为 Element对象

result = etree.tostring(html)
print (result) #lxml库解析数据 可以自动修正html

html1 = etree.parse('flower.html')
result1 = etree.tostring(html,pretty_print=True)
print (result1)
