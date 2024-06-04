Instagram Automatic Posting Bot

Este projeto é um bot para postagem automática no Instagram, permitindo que os usuários agendem postagens de fotos e vídeos com legendas personalizadas. Utiliza a biblioteca instagrapi para interagir com a API do Instagram e pywebio para a interface web.

Funcionalidades

Login no Instagram: Permite que os usuários façam login com seu nome de usuário e senha.

Agendamento de Postagens: Usuários podem agendar postagens para horários específicos.

Upload de Fotos e Vídeos: Suporta upload de mídia diretamente pela interface web.

Notificações: Envia notificações locais quando uma postagem é realizada com sucesso ou ocorre um erro.

Requisitos

Python 3.6+

Instagrapi

PyWebIO

Schedule

Plyer


Instalação

1 - Clone o repositório:

git clone https://github.com/Brendo-will/InstagramScheduler.git

cd instagram-automatic-posting-bot

2- Crie um ambiente virtual e ative-o:

python -m venv venv

source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3- Instale as dependências:

pip install -r requirements.txt

Utilização

Acesse http://localhost:8081 em seu navegador.

Insira suas credenciais do Instagram para fazer login.

Configure suas postagens agendadas selecionando o tipo de mídia, adicionando uma legenda e fazendo upload do arquivo.

As postagens serão agendadas para os horários especificados.

Estrutura do Projeto

InstagramScheduler.py: Script principal que executa o servidor web e gerencia o agendamento de postagens.

requirements.txt: Lista de dependências do projeto.

uploads/: Diretório onde as mídias carregadas são armazenadas.

app.log: Arquivo de log que registra as atividades e erros do bot.

Melhorias Futuras

Suporte para autenticação de dois fatores (2FA).

Suporte a diferentes fusos horários para o agendamento de postagens.

Interface web mais responsiva e intuitiva.

Implementação de carregamento assíncrono para uploads de mídia.
