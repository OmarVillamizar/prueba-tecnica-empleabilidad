def get_key(word):
    # Ordena una palabra, ordenandola por el valor de sus caracteres, y lo reconviert en un string para devolverlo.
    return "".join(sorted(word))

def group_anagrams(words : list[str]) -> list[list[str]]:
    anagrams = {}
    k = ""
    for w in words:
        k = get_key(w)
        #Si la llave de la pabra es nueva, se agrega.
        if k not in anagrams:
            anagrams[k] = []
        #Agrego el valor a su llave correspondiente.    
        anagrams[k].append(w)
    #return de lista de listas
    return list(anagrams.values())

case1=["eat", "tea", "tan", "ate", "nat", "bat"]
case2=[]
case3=["abc"]
case4=["abc", "abc"]
case5=["abc", "def", "ghi"]
print(group_anagrams(case1))
print(group_anagrams(case2))
print(group_anagrams(case3))
print(group_anagrams(case4))
print(group_anagrams(case5))