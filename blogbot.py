#coding:utf-8
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import re
import urllib
import time

# 读文件
def readTextFromFile(fileName):
    file = open(fileName)

    try:
        return file.read()

    finally:
        file.close()

# 写文件
def writeTextToFile(text, fileName):
    file = open(fileName, 'w')

    try:
        return file.write(text)

    finally:
        file.close()

# 正则查找 markdown 中的图片
def findImageUrlsInText(text):
    # 生成识别形如 ![someText](someImageUrl) 的正则
    reg = r'!\[[^\]]*\]\(([^\)]+)\)'
    imageUrlReg = re.compile(reg)

    # 正则匹配，找出所有图片链接
    imageUrls = re.findall(imageUrlReg, text)

    return imageUrls

# 从 url 下载图片到本地
def downloadImages(imageUrls):
    i = 1
    fileNames = []
    for imageUrl in imageUrls:
        print "下载中：%d / %d" %(i, len(imageUrls))

        fileName = "image%d" %i
        urllib.urlretrieve(imageUrl, fileName)
        fileNames.append(fileName)

        i += 1

    return fileNames

def uploadImages(fileNames):
    # 在此处填写你的七牛 Access Key 和 Secret Key
    accessKey = '...'
    secretKey = '...'
    q = Auth(accessKey, secretKey)

    # 七牛上的 bucket 名
    bucketName = '...'
    # 这个 bucket 的外链前缀，就是七牛后台的“外链默认域名”
    imageUrlPrefix = "http://xxxxxx.bkt.clouddn.com/"

    # 上传到七牛的文件名前缀
    fileNamePrefix = "blog" + time.strftime('%Y%m%d',time.localtime(time.time())) + "_"

    imageUrls = []
    i = 1
    for fileName in fileNames:
        print "上传中：%d / %d" %(i, len(fileNames))

        # 上传到七牛的文件名
        key = fileNamePrefix + fileName

        # 生成上传 Token
        token = q.upload_token(bucketName, key, 3600)

        # 上传
        ret, info = put_file(token, key, fileName)

        imageUrl = imageUrlPrefix + key
        imageUrls.append(imageUrl)

        i += 1

    return imageUrls


print "正在解析文件..."

blogText = readTextFromFile("blog.txt")
jianshuImageUrls = findImageUrlsInText(blogText)

print "正在下载图片..."

fileNames = downloadImages(jianshuImageUrls)

print "正在上传图片..."

qiniuImageUrls = uploadImages(fileNames)

# 替换 url
for i in xrange(0, len(jianshuImageUrls) - 1):
    jianshuImageUrl = jianshuImageUrls[i]
    qiniuImageUrl = qiniuImageUrls[i]

    blogText = blogText.replace(jianshuImageUrl, qiniuImageUrl)

print "正在写入文件..."

writeTextToFile(blogText, "newBlog.txt")

print "完成啦~"
