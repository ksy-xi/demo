import requests
import time
开始=int(input("请输入初始页"))
结束=int(input("请输入结束页"))
for n in range(开始,结束+1):
    网址=f"https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax?q=python&page={n}&pagesize=20&district=100000&salaryrange="
    标头={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "referer":"https://yiqifu.baidu.com/g/aqc/joblist?q=python"
        }
    请求=requests.get(网址,headers=标头)
    # print(请求)
    # print(请求.text)
    转化=请求.json()
    # print(转化)
    for i in 转化["data"]["list"]:
        # print(i)
        名字=i["jobName"]
        # print(名字)
        消去=名字.replace("<em>"," ").replace("</em>"," ")
        # print(消去)
        salary=i["salary"]
        company=i["company"]
        edu=i["edu"]
        with open("招聘信息.txt","a",encoding="utf-8")as f:
            f.write("岗位名称"+消去+"\n")
            f.write("岗位薪资"+salary+"\n")
            f.write("公司名称"+company+"\n")
            f.write("学历"+edu+"\n")
            time.sleep(1)
    # print("--------------------------下载完成")
    # 招聘网站的链接 https://yiqifu.baidu.com/g/aqc/joblist
    # 分析网页：找到数据在哪里
    # 网页中 数据分为两种类型：
    # 静态数据   图片-jpg png 格式
    # 动态数据   视频  从服务器实时获取的数据
    #提供一个更简单的方法拿到需要的数据
    #动态数据 按F12 开发者工具  找到 查看网络  响应  就可以一次性的获取需要的动态数据
    #=======================================
    #标头信息：
    #user-agent： 用户模拟浏览器的身份 去访问  目的：伪装
    #referer : 说明一下请求来源页面的URL