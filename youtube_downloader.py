import pytube
import os
import subprocess

yt = pytube.YouTube(input('URL주소를 입력하세요 : '))
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, ' , ', videos[i])

cNum = int(input('화질을 선택하시오(0~21 입력) : '))

down_dir = 'c:/youtube_test'

videos[cNum].download(down_dir)
NewFileName = input('변환할 파일명을 입력하시오 : ')
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, NewFileName)
])

print('변환완료!')
