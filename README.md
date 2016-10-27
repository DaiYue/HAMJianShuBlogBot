把简书博客里的图片传到七牛上，然后替换图片链接的 python 脚本。

## 环境准备
这个脚本在 python 2.7.1 下运行通过。图床用的是七牛云存储。

七牛的 python sdk 需要安装 requests，没装的朋友可以在 terminal 里运行 `sudo easy_install -U requests` 来安装。

## 用法

1. 把源码下载到本地
2. 填写源码中的以下部分：
    ```
    # 在此处填写你的七牛 Access Key 和 Secret Key
    accessKey = '...'
    secretKey = '...'
    q = Auth(accessKey, secretKey)

    # 七牛上的 bucket 名
    bucketName = '...'
    # 这个 bucket 的外链前缀，就是七牛后台的“外链默认域名”
    imageUrlPrefix = "http://xxxxxx.bkt.clouddn.com/"
    ```
2. 把 blog.txt 里的文本替换成自己的博客内容
3. 在 terminal 中切换到脚本根目录，运行：`python blogbot.py`，会看到以下输出：
    ```
    $ python blogbot.py 
    正在解析文件...
    正在下载图片...
    下载中：1 / 4
    下载中：2 / 4
    下载中：3 / 4
    下载中：4 / 4
    正在上传图片...
    上传中：1 / 4
    上传中：2 / 4
    上传中：3 / 4
    上传中：4 / 4
    正在写入文件...
    完成啦~
    ```
5. 新生成的博客就在脚本根目录下的 `newBlog.txt` 里。拿去用吧：）

## 代码讲解

代码非常简单，[我的这篇博客](http://www.jianshu.com/p/ac1db9114cc4)里有简短的解释。

Enjoy~
