 通过scrapy爬取生物序列
 遇到js动态渲染的数据无法正常抓取
 安装scrapinghub/splash作为浏览器渲染引擎，参考博客: https://www.cnblogs.com/Minlwen/p/10491424.html
 
 ```
 1. 先根据keyword拿到第一个url-A(可以直接正常解析)
 2. 再根据url-A拿到其中要的文本(需要动态渲染获取)
 3. 通过csv包，写入文件中 data/data.csv
 

 4. 通过手动添加main.py文件可以debug scrapy爬虫框架
```

 
 
 
 
