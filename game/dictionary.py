import requests

def validate_word(palabra):
    try:
        url = f"https://dle.rae.es/data/search?w={palabra}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "resultados" in data:
            for resultado in data["resultados"]:
                if resultado.get("id") == "w":
                    return True
    except Exception as e:
        pass  # Ignorar errores de solicitud
    
    return False

while True:
    print("Si desea saltar el turno, presione Enter")
    word = input("Ingrese una palabra: ")
    
    if not word:
        break
    
    if validate_word(word):
        print(f"'{word}' existe ")
    else:
        print(f"'{word}' no existe ")