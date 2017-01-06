Python中的包
包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的Python的应用环境。
考虑一个在Phone目录下的pots.py文件。这个文件有如下源代码：
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def Pots():
   print "I'm Pots Phone"
   
同样地，我们有另外两个保存了不同函数的文件：
Phone/Isdn.py 含有函数Isdn()
Phone/G3.py 含有函数G3()
现在，在Phone目录下创建file __init__.py：
Phone/__init__.py
当你导入Phone时，为了能够使用所有函数，你需要在__init__.py里使用显式的导入语句，如下：
from Pots import Pots
from Isdn import Isdn
from G3 import G3
当你把这些代码添加到__init__.py之后，导入Phone包的时候这些类就全都是可用的了。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入 Phone 包
import Phone
 
Phone.Pots()
Phone.Isdn()
Phone.G3()
以上实例输出结果：
I'm Pots Phone
I'm 3G Phone
I'm ISDN Phone

python的每个模块的包中，都有一个__init__.py文件，有了这个文件，我们才能导入这个目录下的module。

其实，__init__.py里面还是可以有内容的，我们在导入一个包时，实际上导入了它的__init__.py文件。
我们可以再__init__.py文件中再导入其他的包，或者模块。
[python]
import readers 
import writers 
import commands 
import users 
import meta 
import auth 
import admin 

这样，当我们导入这个包的时候，__init__.py文件自动运行。帮我们导入了这么多个模块，我们就不需要将所有的import语句写在一个文件里了，也可以减少代码量。
不需要一个个去导入module了。
