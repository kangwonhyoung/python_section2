import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = 'http://www.encar.com'

mem = req.urlopen(url)

#print(type(mem))
#print(type({}))
#print(type([]))
#print(type(()))

#print('geturl', mem.geturl())
#print('status', mem.status)#200 정상, 404 없는, 403 접근거절 내부망 외부망 등, 500 서버자체에 error
#print('headers', mem.getheaders())
#print('info', mem.info())
#print('code', mem.getcode())
#print('read', mem.read(50),decode('utf=8'))#가져올 양을 선택 50, decode는 자주 붙여씀, euc=kr ....

print(urlparse('http://www.encar.com?test=test'))
