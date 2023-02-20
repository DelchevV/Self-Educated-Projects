import random


def pick_song():
    songs = [
        'https://www.youtube.com/watch?v=rsPsQu7ACBI&ab_channel=%F0%9D%96%B1%F0%9D%96%A4%F0%9D%96%A3%F0%9D%96%A2%F0%9D%96%A8%F0%9D%96%B3%F0%9D%96%B8',
        'https://www.youtube.com/watch?v=vOXZkm9p_zY&ab_channel=ImagineDragonsVEVO',
        'https://www.youtube.com/watch?v=Gm8unaZk-2o&ab_channel=%D0%9C%D0%9E%D0%9B%D0%95%D0%A6',
        'https://www.youtube.com/watch?v=aJQSS0AJxng&ab_channel=DeepVibes'
    ]
    song=random.choice(songs)
    return song