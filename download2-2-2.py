import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = 'http://blogfiles13.naver.net/20130112_203/maya5450_1357932569167MadYa_JPEG/e19e56365dc299bb89bcc2bd3344e916_sSWcWy1CfVqSib9il97RfpMZqGvGqKZ.jpg'
htmlURL = 'http://google.com'

savePath1 = 'c:/test1.jpg'
savePath2 = 'c:/index.html'

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()
saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print('다운완료')
