#Parcial hecho por Freddy Castro
from facebook_scraper import get_posts
import csv

face = csv.writer(open('geekworldsv.csv', 'w'))
face.writerow(['POST_ID', 'TEXTO', 'LIKES'])

for post in get_posts('geekworldsv', pages=10, ):
    #Imprimir datos
    print(post['post_id'], post['text'], post['likes'], post['time'], sep=' - ')
    try:
        face.writerow([post['post_id'], post['text'], post['likes'], post['time'], ])
    except:
        None

#¿Que publicaciones tuvieron mayor aceptacion?
