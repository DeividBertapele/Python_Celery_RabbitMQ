# Python_Celery_RabbitMQ

## Usando um modelo de processamento distribuído baseado em filas. ( As tarefas com celery. )

Instalar biblioteca:

- pip install celery
- pip intall flower

---------------------------------------------------------
Usando Docker para instalar RabbitMQ: 

- docker run -d -p 5672:5672 rabbitmq 

ou

- https://registry.hub.docker.com/_/rabbitmq/

---------------------------------------------------------

Para verificar se está rodando na aplicação no comando shell:

- celery -A tasks worker --loglevel=INFO

outro comando shell:

- flower celery -A tasks


---------------------------------------------------------
Links citados para acessar as documentações:

Documentação do celery: https://docs.celeryq.dev/en/stable/index.html

Download do RabbitMQ: https://www.rabbitmq.com/download.html

