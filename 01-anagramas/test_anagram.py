import pytest
from anagram import group_anagrams

# --- Función auxiliar para comparar resultados ---
# Como el orden de los grupos y el orden dentro de ellos no importa, 
# esta función normaliza ambos para que el assert no falle injustamente.
def normalize(result):
    return sorted([sorted(group) for group in result])

# --- TUS CASOS ORIGINALES ---

def test_case1():
    case = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert normalize(group_anagrams(case)) == normalize(expected)

def test_case2_empty():
    assert group_anagrams([]) == []

def test_case3_single():
    assert group_anagrams(["abc"]) == [["abc"]]

def test_case4_duplicates():
    # Palabras idénticas deben terminar en el mismo grupo
    assert group_anagrams(["abc", "abc"]) == [["abc", "abc"]]

def test_case5_no_anagrams():
    case = ["abc", "def", "ghi"]
    expected = [["abc"], ["def"], ["ghi"]]
    assert normalize(group_anagrams(case)) == normalize(expected)

# --- 5 CASOS EXTRA (EDGE CASES) ---

def test_case6_case_sensitivity():
    # Python es sensible a mayúsculas, 'Amor' y 'roma' tendrían llaves distintas
    case = ["Amor", "roma", "mora"]
    result = group_anagrams(case)
    # Según tu lógica actual, "Amor" estará solo y "roma"/"mora" juntos
    assert len(result) == 2 

def test_case7_different_lengths():
    # Palabras con mismas letras pero distinta cantidad no son anagramas
    case = ["aaa", "aa", "a"]
    expected = [["aaa"], ["aa"], ["a"]]
    assert normalize(group_anagrams(case)) == normalize(expected)

def test_case8_spaces():
    # Los espacios cuentan como caracteres en el ordenamiento
    case = ["a b", "ba ", "b a"]
    # "a b" y "b a" son anagramas (espacio en medio), "ba " tiene el espacio al final
    # Pero al ordenar, todos resultan en " ab"
    assert len(group_anagrams(case)) == 1

def test_case9_numeric_strings():
    case = ["123", "321", "456"]
    expected = [["123", "321"], ["456"]]
    assert normalize(group_anagrams(case)) == normalize(expected)

def test_case10_long_anagrams():
    case = ["anagrama", "amaragan", "nagaramas"]
    # Las primeras dos coinciden, la tercera tiene una 's' extra
    result = group_anagrams(case)
    assert len(result) == 2