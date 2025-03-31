import requests
import time

def gerar_perfil():
    while True:
        try:
            # Mostramos los mensajes de espera en bucle
            print("Criando usuário...", end="\r", flush=True)
            time.sleep(2)  # Simula un retraso de 2 segundos

            print("Espere um momento...", end="", flush=True)
            time.sleep(2)  # Otro retraso de 2 segundos

            # Hacemos la solicitud a la API
            response = requests.get('https://randomuser.me/api/')
            response.raise_for_status()  # Si hay un error, se lanza una excepción

            # Si la solicitud fue exitosa, salimos del bucle
            break  # Rompe el bucle

        except requests.exceptions.HTTPError as err:
            # Si ocurre un error, mostramos el error y volvemos a intentar
            print(f"\nErro ao acessar a API: {err}")
            time.sleep(2)  # Espera antes de intentar nuevamente

    # Procesamos la respuesta si fue exitosa
    data = response.json()
    usuario = data['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    telefone = usuario['phone']
    pais = usuario['location']['country']
    cidade = usuario['location']['city']

    print(f"\nNome do usuário: {nome}")
    print(f"Email: {email}")
    print(f"Telefone: {telefone}")
    print(f"País: {pais}")
    print(f"Cidade: {cidade}")
    print("Perfil criado com sucesso!")  # Mensaje de éxito

if __name__ == '__main__':
    gerar_perfil()