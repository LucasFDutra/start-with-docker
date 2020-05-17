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