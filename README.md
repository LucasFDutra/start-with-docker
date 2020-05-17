- [**English**](#English)
- [**Português**](#Português)

# English
---
# What this repository is about
Here I will describe the steps I needed to take to create a container in the docker, and how to work with it

For this, I will create an extremely simple project in nodeJS, just calling a route, I will also configure the docker to work with postgreSQL. However I will not connect the bank in my application. To see that the database also worked, I will create a connetion trough postbird, to be faster.

# What to install
- [Instale o docker e o docker compose](https://docs.docker.com/engine/install/)
- [Instale o node](https://nodejs.org/en/)
- [Instale o yarn - opcional](https://yarnpkg.com/)

> If you are a Linux user (dabian base), you can use some scripts that I put in this repository here: [my-development-environments](https://github.com/LucasFDutra/my-development-environments).

- Install node packages:
    - express
        ```sh
        $ yarn add express
        # or
        $ sudo npm install express
        ```
    - nodemon
        ```sh
        $ yarn add nodemon
        # or
        $ sudo npm install nodemon
        ```

# Files
- Node project:
    The node project comes down to a single file (index.js) that is responsable only for returning a `Hello World` when we access port 3000.
    ```js
    const express = require('express');

    const PORT = 3000;
    const HOST = '0.0.0.0';

    const app = express();

    app.get('/', (req, res) => {
        res.send('Hello world');
    });

    app.listen(PORT, HOST);
    ```

- docker files
    The docker will need tree files
    - `Dockerfile` : What is the machine settings
        ```yml
        # what we want on our machine: in this case the node, in the alpine version (as simple as possible)
        FROM node:alpine

        # where the docker machine will be located in our project
        WORKDIR /usr/app

        # Make a copy of the package.json into the docker machine
        COPY package*.json ./

        # Install packages on the docker machine according to package.json (this causes a node_modules folder to be created inside the machine)
        RUN npm install

        # copies the rest of the project
        COPY . .

        # indicates that we want to expose port 3000 on the docker machine to be accessed by our real machine
        EXPOSE 3000

        # the command to be executed by the docker machine as soon as it goes up
        # in this case it will be npm yarn start, which was defined inside the package.json
        CMD [ "yarn", "start" ]
        ```
    - `docker-compose.yml` : which indicates how the machine should work
        ```yml
        # composer version linked to your docker version (mine is version 19.03). look hear: https://docs.docker.com/compose/compose-file/
        # to see your docker version, type the command
        # $ sudo docker -v
        version: "3"

        services:
            db:
                image: postgres # passing image name
                environment: 
                    POSTGRES_PASSWORD: superSenha # passing my bank password
                    POSTGRES_USER: postgres # passing the bank user
                    POSTGRES_DB: my_db # passing the name of the bank
                ports: 
                    - "5433:5432" # the door I must access on the real machine, and the door exposed by this container
                volumes: 
                    - ./pgdata:/var/lib/postgresql/data # where the bank files will come from where they will go on the docker machine
            app:
                build: . # will start the machine, we pass the directory where the docker is
                depends_on: # makes the app container work only if the db container is working
                    - "db"
                command: "yarn start" # the command that will be executed at startup
                ports:
                    - "3000:3000" # the door I must access on the real machine, and the door exposed by this container
                volumes: 
                    - .:/usr/app # when it runs here (which is whenever there are modifications due to the nodemon) we will copy everything from . into the /usr/app folder on the docker machine

        ```
    - `.dockerignore` : used to prevent us from copying a particular file or folder into the docker
        ```yml
        # as the docker will already install the libs inside the docker machine, it is unnecessary to copy this folder there
        node_modules
        ```

- Run the command below to create and run the container
    ```sh
    $ sudo docker-compose up
    ```

# Para usar
Access `http://localhost:3000` to see that the route is working.

```
Host: localhost
Port: 5433
Username: postgres
Password: superSenha
``` 

> Note 1.: The reason for not using port 5433 on my pc, is that I have postgres installed locally, and it already uses that port.

> Note 2.: When starting your node application, make sure that it will connect to postgres only affter postgres goes up on the docker machine. You can guarantee this by generating a delay in the connection.

> Note 3.: If you want the container to stop running you need to type `$ ctrl+c` or depending on you need to type `$ sudo docker stop CONTAINER ID`, and to find the container id use `$ sudo docker ps`.

# Português
----
# Do que se trata esse repositório
Aqui eu vou descrever os passos que precisei fazer para criar um container no docker, e como trabalhar com ele.

Para tal, criarei um projeto extremamente simples em nodeJS, somente chamando uma rota. E também configurarei o docker para trabalhar com postgreSQL. Porém não irei conectar o banco na minha aplicação. Para ver que o banco de dados também funcionou, irei crie uma conexão por meio do postbird, para ser mais rápido.

# O que instalar
- [Instale o docker e o docker compose](https://docs.docker.com/engine/install/)
- [Instale o node](https://nodejs.org/en/)
- [Instale o yarn - opcional](https://yarnpkg.com/)

> Caso seja usuário de linux (base debian), pode utilizar alguns scripts que eu coloquei nesse repositório aqui: [my-development-environments](https://github.com/LucasFDutra/my-development-environments).

- Instale os pacotes do node:
    - express
        ```sh
        $ yarn add express
        # ou
        $ sudo npm install express
        ```
    - nodemon
        ```sh
        $ yarn add nodemon
        # ou
        $ sudo npm install nodemon
        ```

# Arquivos
- Projeto node:
    O projeto em node se resume a um único arquivo (index.js) que fica responsável somente por retornar uma `Hello world` quando acessarmos a porta 3000
    ```js
    const express = require('express');

    const PORT = 3000;
    const HOST = '0.0.0.0';

    const app = express();

    app.get('/', (req, res) => {
        res.send('Hello world');
    });

    app.listen(PORT, HOST);
    ```

- Arquivos do docker
    O docker precisará de três arquivos
    - `Dockerfile` : Que fica as configurações da máquina
        ```yml
        # o que queremos na nossa máquina: no caso o node, na versão alpine (mais simples possível)
        FROM node:alpine

        # em que lugar da máquina docker ficará o nosso projeto
        WORKDIR /usr/app

        # efetua uma cópia do packege.json para dentro da máquina docker
        COPY package*.json ./

        # instala os pacotes na maquina docker de acordo com o package.json (isso faz com que uma pasta node_modules seja criada dentro da máquina)
        RUN npm install

        # copia todo o restante do projeto
        COPY . .

        # indica que queremos expor a porta 3000 da máquina docker para ser acessada pela nossa máquina real
        EXPOSE 3000

        # o comando a ser executado pela máquina docker assim que ela subir
        # nesse caso será yarn start, que foi definido dentro do package.json
        CMD [ "yarn", "start" ]
        ```
    - `docker-compose.yml` : que indica como a máquina deve funcionar
        ```yml
        # versão do composer vinculada a sua versão do docker (o meu é a versão 19.03). veja aqui: https://docs.docker.com/compose/compose-file/
        # para ver sua versão do docker, digite o comando
        # $ sudo docker -v
        version: "3"

        services:
            db:
                image: postgres # passando nome da imagem
                environment: 
                    POSTGRES_PASSWORD: superSenha # passando a senha do meu banco
                    POSTGRES_USER: postgres # passando o usuário do banco
                    POSTGRES_DB: my_db # passando o nome do banco
                ports: 
                    - "5433:5432" # a porta devo acessar na máquina real, e a porta exposta por esse container 
                volumes: 
                    - ./pgdata:/var/lib/postgresql/data # de onde sairá os arquivos do banco para onde eles irão na máquina docker
            app:
                build: . # vai iniciar a máquina, passamos o diretório em que está o Dockerfile
                depends_on: # faz com que o container app só funcione se o container db estirver funcionando
                    - "db"
                command: "yarn start" # o comando que será executado na inicialização.
                ports:
                    - "3000:3000" # a porta devo acessar na máquina real, e a porta exposta por esse container
                volumes: 
                    - .:/usr/app # quando isso aqui rodar (o que é sempre que houver modificações por conta do nodemon) copiaremos tudo de . para dentro da pasta /user/app da máquina docker

        ```
    - `.dockerignore` : que serve para não deixar que copiemos um determinado arquivo ou pasta para dentro da máquina docker
        ```yml
        # como o docker já instalará as libs dentro da máquina docker, é desnecessário copiar essa pasta para lá
        node_modules
        ```

- Execute o comando abaixo para criar e rodar o container
    ```sh
    $ sudo docker-compose up
    ```

# Para usar
Acesse `http://localhost:3000` para ver que a rota está funcionando.

```
Host: localhost
Port: 5433
Username: postgres
Password: superSenha
``` 

> OBS 1.: O motivo de não ter utilizado a porta 5433 do meu pc, é que eu possuo o postgres instalado localmente, e ele já utiliza essa porta

> OBS 2.: Quando for inicializar a sua aplicação node, garanta que ela se conectará ao postgres somente depois do postgres subir na maquina docker. Pode garantir isso gerando um delay na conexão

> OBS 3.: Se quiser que o container pare de rodar você precisa digitar `$ ctrl+c` ou dependendo precisará de digitar `$ sudo docker stop CONTAINER ID`, sendo que para encontrar o id do container use `$ sudo docker ps`.