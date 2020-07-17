# Auto-Submit 某学校自动报表提交
## 使用说明

使用前请先安装Chrome浏览器

并且按照你的浏览器版本 下载以下驱动放入根目录。

http://npm.taobao.org/mirrors/chromedriver/



打开script.py

填写配置

```
### 配置区 ###
config_sheng = 1 #省的编号 请注意这个城市编号从0开始算,为填报时选择的顺序
config_shi = 1 #市的编号
config_xian = 1 #县的编号
username = 1 #账号
password = 1 #密码
drivername = "./chromedriver" #驱动文件路径
howtime = 19 #几点提交
phone = 13676763333 #联系电话,如果你的手机号自动填写了 请在下面注释提交手机的代码

speed_for_page = 20 #每一页加载的时间
speed_for_load = 10 #每一个选项加载的时间
url = 'https://域名/mobile/index.html' #请自己填写域名
#############
```

执行命令python3 script.py

