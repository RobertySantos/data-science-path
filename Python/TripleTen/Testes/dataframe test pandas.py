import pandas as pd

atlas = [  
        ['France', 'Paris'],  
        ['Russia', 'Moscow'],  
        ['China', 'Beijing'],  
        ['Mexico', 'Mexico City'],  
        ['Egypt', 'Cairo']  
]

world_map = pd.DataFrame(atlas, columns= ['Country','Capital'])
new_names = []
for value in world_map.columns:
    new_names.append(value.lower())
world_map.columns = new_names

world_map.rename(columns = {'country':'COUNTRY'}, inplace= True)

def replace_wrong_genres(wrong_genres,correct_genre):
    for genres in wrong_genres:
       world_map['capital'].replace(genres,correct_genre, inplace=True)
    return

replace_wrong_genres(['Cairo'],'Cairos')


print(world_map)