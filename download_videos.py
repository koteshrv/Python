from bs4 import BeautifulSoup
import urllib.request, progressbar

pbar = None

def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()
    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

source = input('Enter url here: ')
html_page = urllib.request.urlopen(source)
soup = BeautifulSoup(html_page, "html.parser")
home_page = source[:20]
for link in soup.findAll('a')[1:]:
    video = link.get('href')
    video_name = video.split('/')[-1]
    print(video_name)
    url = home_page + video
    print('Downloading ' + video)
    urllib.request.urlretrieve(url, video_name, show_progress) 
