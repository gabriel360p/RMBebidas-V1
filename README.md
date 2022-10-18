# RMBebidas-V1.6
Feito em treinamento com python usando django, meu primeiro projeto django usando mysql.

--- Configurando a conexão com Banco de dados Mysql ---

1 - Em settings.py, procure por:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

2 - E depois mude para: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'nomeBanco', # Nome do banco (existe um arquivo .sql na pasta do projeto chamado 'rmdrinks', onde possui o código sql feito por mim para ser usado nesse projeto. E só rodar ele no workbench, que o banco vai ser criado.
        'HOST':'127.0.0.1',
        'PORT':'3306', # Porta padrão do msql
        'USER':'user', # Seu usuario root do mysql
        'PASSWORD':'senha', #Sua senha root do mysql
    }
}

3 - Depois disso, dê o seguinte comando:
python manage.py makemigrations && python manage.py migrate && python manage.py inspectdb > rmbebidas/models.py && python manage.py runserver

4 - Depois da configurações do banco, o usuário de acesso padrão criado pelo próprio banco é:
Email: admin@admin
Senha: root
(Esse usuário não é o mesmo usuário da área administrativa do Django, esse é necessário ser criado por você)
