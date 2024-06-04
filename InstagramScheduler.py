from instagrapi import Client
from pywebio import start_server
from pywebio.input import file_upload, input_group, input, select
from pywebio.output import put_text, put_success, put_error
import schedule
import time
from plyer import notification
import os
import json

# Variáveis globais
videos = {}
cl = Client()  # Inicialização global do cliente

# Função para publicar mídia
def publicar_midia(media_type, media_path, caption):
    try:
        print(f"[DEBUG] Tentando publicar a mídia {media_path} com a legenda '{caption}'")
        if media_type == "video":
            media = cl.video_upload(media_path, caption)
        elif media_type == "image":
            media = cl.photo_upload(media_path, caption)
        else:
            raise Exception("Tipo de mídia desconhecido")

        if media:
            media_id = media.dict().get('id')
            media_url = f"https://www.instagram.com/p/{media.dict().get('code')}/"
            msg = f"A mídia {media_path} foi publicada com sucesso no Instagram! Link: {media_url}"
            print(msg)
            notification.notify(
                title="Publicação no Instagram",
                message=msg,
                timeout=10
            )
        else:
            raise Exception("Erro desconhecido na publicação.")
    except Exception as e:
        error_msg = f"[DEBUG] Ocorreu um erro ao publicar a mídia {media_path}: {e}"
        print(error_msg)
        notification.notify(
            title="Erro na Publicação no Instagram",
            message=error_msg,
            timeout=10
        )

# Função para agendar postagens
def agendar_postagens(videos):
    for horario, detalhes in videos.items():
        print(f"[DEBUG] Agendando postagem para {horario} com os detalhes: {detalhes}")
        schedule.every().day.at(horario).do(publicar_midia, detalhes["media_type"], detalhes["media_path"], detalhes["caption"])

# Função para a interface web
def app():
    global videos
    put_text("Configuração de Postagens Automáticas no Instagram")

    # Solicitar credenciais do usuário
    credenciais = input_group("Login no Instagram", [
        input("Nome de Usuário:", name="user_name", required=True),
        input("Senha:", name="password", type="password", required=True),
    ])

    # Login no Instagram
    try:
        global cl
        if credenciais['proxy']:
            cl.set_proxy(credenciais['proxy'])
        cl.login(credenciais['user_name'], credenciais['password'])
        put_success("Login realizado com sucesso!")
    except Exception as e:
        put_error(f"Erro ao fazer login: {e}")
        return

    # Criar o diretório 'uploads' se não existir
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    for horario in ["18:53",'18:58']:  # Adiciona os horários desejados aqui
        data = input_group(f"Configuração para {horario}", [
            select("Tipo de Mídia:", ["video", "image"], name="media_type"),
            input("Legenda:", name="caption"),
            file_upload("Selecione a mídia:", accept="video/*,image/*", name="media")
        ])

        media_path = f"uploads/{data['media']['filename']}"

        with open(media_path, 'wb') as f:
            f.write(data['media']['content'])

        videos[horario] = {
            "media_type": data['media_type'],
            "media_path": media_path,
            "caption": data['caption']
        }

    # Salvar as postagens em um arquivo JSON para persistência
    with open('postagens.json', 'w') as f:
        json.dump(videos, f)

    agendar_postagens(videos)
    put_success("Postagens agendadas com sucesso!")

    # Manter o loop de agendamento em execução
    while True:
        schedule.run_pending()
        print("[DEBUG] Executando tarefas agendadas...")  # Mensagem de debug para o loop principal
        time.sleep(1)

# Iniciar o servidor web
if __name__ == "__main__":
    start_server(app, port=8081)  # Alterado a porta para qual voce desejar se a 8080 nao estiver disponivel
