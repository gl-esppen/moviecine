# Moviecine

## Especificações Principais:
* Python 2.7
* Django 1.11.10
* Django REST FRAMEWORK


## Instalação:

* Recomenda-se utilizar o virtualenvwrapper para trabalhar melhor no projeto:


    $ pip install virtualenvwrapper

    $ /usr/local/bin/virtualenvwrapper.sh 

    $ echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bash_profile

    $ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile 

    $ source ~/.bash_profile  



* Após fazer a instalação, podemos seguir com o setup do ambiente e a instalação dos pacotes necessários:


    $ mkvirtualenv moviecine

    $ workon moviecine

    $ make install
   

## Iniciando a Aplicação:
 
    $ make run

## Acessando Django API REST:

##### Urls base:
* /api/filmes/
* /api/ator/


## Sugestão de Arquitetura:

* Configurando o sistema 
- SUPERVISOR
Ferramenta para garantir que o gunicorn permaneça ativo e registra os logs de erro.

- Fabric
Ferramenta para automação de deploys.


* Otimizando o acesso
- EC2
    Instancia para aplicação, com integração de outros serviços para otimizar acesso e fluxo de dados.
	
	- Auto Scaling
        Detecta o volume de carga de acesso baseado em um alarme configurado, inicia uma nova instancia e coloca no Load Balance


    - Load Balance
        Configuração de máquinas secundárias para distribuição de carga com a instancia principal, de forma a evitar sobrecarga devido ao alto volume de acesso diário e simultaneo.

- RDS
    Banco de dados Postgres da aplicação

- S3
    Armazenamento de arquivos estáticos e de mídias.    


- CloudWatch
    Monitoramento das máquinas de processos com alertas personalizados (Ex: Database CPU)







