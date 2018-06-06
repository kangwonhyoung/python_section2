import sys
import io
from urllib.parse import urljoin

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

baseURL = 'http://test.com/html/a.html'
print('>>', urljoin(baseURL, '../b.html'))
