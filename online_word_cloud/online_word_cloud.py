import crawler5
import cloud

brower=crawler5.crawler('http://weibo.com')
brower.log_in()
#nums=eval(input('输入爬取的页数：'))
sears=input('输入爬虫关键词：')+'/'
sears=sears.split('/')
#sears=input('输入爬虫关键词：').split('/')
brower.get_outcomes(1,sears)
#brower.get_outcomes(nums,sears)
cloud=cloud.data()
cloud.read_pinglun()
cloud.mood()
cloud.ciyun()
brower.brower.quit()