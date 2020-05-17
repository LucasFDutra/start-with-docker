# Do que se trata esse repositório
Aqui eu vou descrever os passos que precisei fazer para criar um container no docker e como trabalhar com ele.

Para tal, criarei um projeto extremamente simples em nodeJS, somente chamando uma rota.

# O que instalar
- [Instale o docker e o docker compose](https://docs.docker.com/engine/install/)
- [Instale o node](https://nodejs.org/en/)
- [Instale o yarn - opcional](https://yarnpkg.com/)

Caso seja usuário de linux (base debian ubuntu), pode utilizar alguns scripts que eu coloquei nesse repositório aqui: [my-development-environments](https://github.com/LucasFDutra/my-development-environments). Eu utilizo ele para agilizar minhas instalações de ambientes de desenvolvimento.

- Instale os pacotes do node:
    - express
        ```sh
        yarn add express
        # ou
        sudo npm install express
        ```
    - nodemon
        ```sh
        yarn add nodemon
        # ou
        sudo npm install nodemon
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
        res.send('Hello world slkdfjçla');
    });

    app.listen(PORT, HOST);
    ```

- Arquivos do docker
    O docker precisará de 3 arquivos
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
        # nesse caso será npm start, que foi definido dentro do package.json
        CMD [ "npm", "start" ]
        ```
    - `docker-compose.yml` : que indica como a máquina deve funcionar
        ```yml
        # versão do composer vinculada a sua versão do docker (o meu é a versão 19.03). veja aqui: https://docs.docker.com/compose/compose-file/
        # para ver sua versão do docker, digite o comando
        # $ sudo docker -v
        version: "3"

        services:
            app:
                build: . # vai iniciar a máquina, passamos o diretório em que está o Dockerfile
                command: npm start # o comando que será executado na inicialização
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
    docker-compose up
    ```

- Acesse `http://localhost:3000`

> Se quiser que o container pare de rodar você precisa digitar `sudo docker stop CONTAINER ID` 
> rode `sudo docker ps` para ver o id do container