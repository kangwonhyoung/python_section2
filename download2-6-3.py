from bs4 import BeautifulSoup
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fd = open('cars.html', encoding='utf-8')
soup = BeautifulSoup(fd, 'html.parser')

def car_func(selector):
    print('car_func', soup.select_one(selector).string)


#람다식
car_lambda = lambda q : print('car_lambda', soup.select_one(q).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")

print('car_func', soup.select("li")[3].string)
print('car_func', soup.select('li'[3]).string)
