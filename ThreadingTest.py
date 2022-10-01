import string
import threading
import concurrent.futures
import time
import requests
import random
NUM_THREADS = 16

'''
Free to download and use image URLs
'''
IMG_URLS = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

def test_func(seconds : int) -> None:
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print(f'Done Sleeping {seconds}')
    
def download_img(url : string, threaded : bool) -> None:
    img_bytes = requests.get(url).content
    img_name = url.split('/')[3]
    img_name = f'{img_name}_{"Non_" if not threaded else ""}Threaded.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded')

    
'''
Testing speed up when using threads to download a list of High Res Images 

Threading (16) - 24.2seconds
Non Threading - 26.6seconds

Not the speed up I was expecting - it may be due to implementation being correct, or using an incorrect amount of threads. 
Where the overhead of thread creation and deletion outweighs the speed up (This seems unlikley)
''' 
def main(threading : bool):
    start = time.perf_counter()

    if threading:     
        with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            executor.map(download_img, IMG_URLS, [True]*len(IMG_URLS))
    else:
        for url in IMG_URLS:
            download_img(url, False)


    print('Downloaded all Images :)')
    print(f'({"Threaded" if threading else "Non_Threaded"}) Finished in {time.perf_counter() - start:.2f} second(s)')
    

if __name__ == "__main__":
    main(threading=True)
    main(threading=False)
    
    