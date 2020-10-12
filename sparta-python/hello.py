import dload

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver') # 웹드라이버 파일의 경로
driver.get("https://www.google.com/search?q=%EB%B9%84%EB%B0%80%EC%9D%98+%EC%88%B2+%EC%A0%84%ED%98%9C%EC%A7%84&tbm=isch&ved=2ahUKEwjR4tCa0ZzsAhUTvJQKHW13BGcQ2-cCegQIABAA&oq=%EB%B9%84%EB%B0%80%EC%9D%98+%EC%88%B2+%EC%A0%84%ED%98%9C%EC%A7%84&gs_lcp=CgNpbWcQA1D8IlibLmDpL2gBcAB4AYABfIgBxAuSAQQwLjEzmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=oaN6X5GOM5P40gTt7pG4Bg&bih=718&biw=1149")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#islrg > div.islrc > div > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img,f'imgs_homework/{i}.jpg')
    i += 1


driver.quit() # 끝나면 닫아주기