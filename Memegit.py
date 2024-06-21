meme_dict= {'XD':'emogi que representa una risa muy fuerte', 
            'POSER':'Fan por moda',
            'CHAMBA':'Trabajar',
            'FANBOY':'fan ciego'}

for i in range(5):
    word = input('que palabra quieres aprender?').upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('aun faltan agregar elementos al diciionario ')
    

