# 马赛克图片制作

通过搜索引擎进行图片爬虫，可以爬取原图（目前实现 百度的爬虫），然后使用opencv进行图片处理

## 环境需要（需要安装的库）

1. Python 3.X
2. pip install scrapy==1.6 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
3. pip install selenium -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
4. pip install requests -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
5. pip install opencv-python -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
6. pip install tqdm  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

## 使用方法

1. 运行reptiles_imgs/main.py文件，进行图片爬取，图片会保存在images文件夹下
2. 运行\production\main.py文件，程序会以production\example文件夹里的1.jpg为模板生成马赛克图片
3.  生成的图片会出现在\output文件里
4. 完成

## 需要注意
1. 推荐使用Chrome浏览器
2. 请在Chrom浏览器的“帮助” -> “关于Google Chrome(G)”中查询当前浏览器版本，例如“版本 75.0.3770.100（正式版本） （64 位）”表示当前主版本为75.
3. 可以到 http://npm.taobao.org/mirrors/chromedriver/ 下载对应主版本的chromedriver，并放在driver目录下

## 如果喜欢这个小程序，请star一下，特别感谢！

