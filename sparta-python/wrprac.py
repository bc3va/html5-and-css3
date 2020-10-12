from PIL import Image
import numpy as np
from wordcloud import WordCloud

text = ''
with open("kakao.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        result = line.split(',"')
        if len(result) == 3:
            text += result[2].replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('이모티콘','').replace('사진','').replace('"','')

# print(text)

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='/System/Library/Fonts/AppleSDGothicNeo.ttc', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")