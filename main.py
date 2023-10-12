#Matias Fernandez
#2023-09-22

#definir la fonction "word count"
def word_count():
    #demande au utilisateur de ecrire un text
    text = str(input("ecrie ton texte:"))
    #compter le nombre de mot
    return(print(len(text.split())))
#commencer la fonction
word_count()
