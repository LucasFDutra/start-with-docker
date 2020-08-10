# O que é docker

O docker é uma ferramenta que nos permite criar container para nossas aplicações.

## O que seria um container?

Um container é nada mais do que um processo, e dentro desse processo você terá uma aplicação rodando com todas as suas dependências isoladas do sistema operacional. Pensando assim pode até parecer que o docker é como uma máquina virtual feita no virtual box. Afinal temos ai um sistema que consegue rodar coisas isoladamente dentro do nosso próprio sistema operacional de forma totalmente isolada. Mas não é a mesma coisa. Tem aqui um diagrama da própria documentação para nos ajudar a entender as diferenças.

<div style="display:flex; flex-direction:row; align-items:center; justify-content:space-between">
    <img src='./images/figura_01.png' width=30%/>
    <img src='./images/figura_02.png' width=30%/>
</div>


Pelas imagens, vemos uma certa semelhança entre os dois processos, porém vemos claramente que a diferença é que o docker não precisa subir todo um sistema operacional para cada container, ele utiliza dos recursos de OS da própria OS hospedeiro, enquanto a VM precisa sempre subir todo um sistema operacional e ainda precisa do Hypervisor para fazer a conexão com a infraestrutura da máquina.

A vantagem disso é que uma imagem docker é muito leve. Ela pode ser criada contendo somente o mínimo necessário para rodar a aplicação que deseja, enquanto um VM precisa ter todo um sistema operacional por trás.

Mas como já deve imaginar, se a máquina docker utiliza o sistema host como fonte de recursos, o sistema host pode ser windows, linux ou mac? tanto faz? A resposta é não. O docker foi feito para rodar com sistemas linux, logo seu melhor desempenho é com linux. Porém isso não significa que não de para utilizar ele com outros sistemas, tem como instalar o docker para todas os sistemas.


## O que é uma imagem docker?

Uma imagem docker é nada mais do que resultado de um container montado. Ou seja, uma vez que você criar um container e subir o código necessário para sua aplicação rodar, você pode gerar uma imagem do seu container e utilizá-la depois.

## Mas como criar uma container??

Bom, todo container é feito a partir de uma imagem pré-existente. E se quiser buscar imagens para utilizar, eu recomendo ir no site do [docker hub](https://hub.docker.com/) para isso (na verdade você será obrigado a utilizá-lo). Lá é onde ficam hospedadas as imagens que a comunidade foi criando ao longo do tempo, e é a partir de lá que o docker puxa uma imagem para você instalar na sua máquina.

Lá você vai encontrar imagens do ubuntu, do postgres, mysql, ngix, php, python, ruby... E tudo quanto é coisa que você imaginar.

Mas como eu disse antes, uma imagem sempre é construída em cima de outra, logo quando vemos uma imagem do postgres, provavelmente o que aconteceu foi que quem a criou se baseou em uma imagem de uma máquina ubuntu e então instalou dentro dela o postgres, gerou uma imagem disso e colocou ela no docker hub. E é assim que o processo funciona, você precisa pegar uma imagem que mais se assemelha ao que você deseja utilizar, e então vai adicionando coisas a ela.


## Mas quais as vantagens de se utilizar docker??
Bem, o objetivo pelo qual o docker foi inventado foi para igualar os ambientes de desenvolvimento. Evitando o famoso "mas na minha máquina funciona", afinal agora a imagem docker é uma só entre todo o time, logo não tem nem jeito de alguma coisa acontecer diferente entre máquinas. Afinal com a mesma imagem, sempre teremos as mesmas coisas instaladas e sempre nas mesmas versões, e sempre na mesma base de sistema operacional. Logo não importa se utiliza windows, linux ou mac, o container é sempre o mesmo.

Outra grande vantagem de utilizar uma imagem para desenvolver é que você configura todo seu sistema de desenvolvimento com literalmente um comando (desde que a imagem já esteja pronta). 

E caso queira instalar alguma coisa na sua máquina para ver como funciona, ou trabalhar com essa determinada tecnologia será bem mais simples instalá-la com o docker, afinal é só pegar uma imagem, que já está configurada, e que nem se quer vai realmente estar na sua máquina, afinal o container está isolado. Logo não existe o problema de conflito entre bibliotecas do sistema e de uma aplicação, e nem aquele probleminha chato que a gent passa ao desinstalar alguma coisa que tem um dependência comum com outras aplicações e durante a desinstalação essa dependência é apagada e de repente você está sem interface gráfica (quem nunca fez isso quando começou a fuçar em uma distro linux)


> Para entender o que é docker você também pode buscar diretamente na documentação do mesmo, por esse [link](https://docs.docker.com/get-started/).


# Como instalar essa maravilha

Novamente a documentação está [aqui](https://docs.docker.com/get-docker/) para te ajudar, caso tenha qualquer problema siga a mesma.

A instalação do docker deve ser seguida da instalação do docker-compose, que mais para frente explicarei o que é

## Linux

```shell
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo groupadd docker
sudo usermod -aG docker $USER
su $USER
```

## MAC
aparentemente é só fazer o [download](https://docs.docker.com/docker-for-mac/install/) que está na página do docker e mandar instalar.

## Windows
Na página do docker também temos um [download](https://docs.docker.com/docker-for-windows/install/) disponível em forma de executável, mas necessita algumas configurações de virtualização. Então recomendação pessoal: Não instale o docker para windows normalmente, utilize o WSL para instalar o docker, afinal ele precisará do linux para rodar normalmente, então é melhor instalar o WLS do que tentar utilizar algum tipo de virtualização. Para isso eu recomendo ver esse video [aqui](https://www.youtube.com/watch?v=g4HKttouVxA) que mostra como fazer isso além de dar uma explicação do porque fazer dessa forma.
