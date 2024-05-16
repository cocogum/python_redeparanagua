# Projeto COCOGUM

### Instalando o Projeto


#### Clonar o Projeto
'git clone https://github.com/cocogum/python_redeparanagua/tree/main/redeparanagua_admin'

#### Instalar dependencias 
'pip install -r requirements.txt'

#### Alterar configurações da BD no arquivo ~setting.py
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_da_ BD',
        'HOST': 'host_da_BD',
        'PORT': ~porto_da_BD',
        'USER': 'usuario_BD',
        'PASSWORD': 'senha_BD'
    }
}
'''

#### Migrar banco de dados
'python manage.py maigrate'

#### Iniciar o servidor
'python manage.py runserver'