---
content_hash: ee5ce96426782ca4de77a6397ca01804595f1a8899a0cb3e554ef93bb43a8610
fetched_at: '2026-06-28T21:35:22.560521+00:00'
page_id: '237394476'
product: fluig
source: tdn-fluig
title: Alta disponibilidade e balanceamento de carga do Fluig ESB
type: documentation
url: https://tdn.totvs.com/display/fluig/Alta+disponibilidade+e+balanceamento+de+carga+do+Fluig+ESB
version: 50
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

# Índice

true.\*ndicenone

# Objetivo

---

Este guia tem como finalidade, descrever de forma objetiva, passo a passo, todos os procedimentos necessários para a configuração do produto Fluig ESB para suportar alta diponibilidade e balanceamento de carga.

# Público alvo

---

A configuração de alta disponibilidade e balanceamento de carga devem ser realizada por profissionais com experiência em instalação de aplicativos e com conhecimentos de ambiente de rede.

# Pré-requisitos

---

Antes da instalação consulte as documentações de  [dimensionamento](http://tdn.totvs.com/display/fluig/Dimensionamento+fluig+ESB) e [configuração de banco de dados](http://tdn.totvs.com/pages/viewpage.action?pageId=120784259) para garantir que o ambiente onde o Fluig ESB será instalado está homologado.

### Fluig ESB Server

É obrigatório a utilização da mesma versão do F**luig ESB Server (versão 12.2.x ou superior)** em todos os servidores identificados no guia como “ESB Server Cluster Node” ou “ESB Server Cluster Master” para utilização em Alta Disponibilidade e Balanceamento de carga respectivamente.

Este documento não cobre o procedimento de instalação e configuração do Fluig ESB Server. Para obter mais detalhes sobre a instalação do produto, verifique o documento **.**

É obrigatória a sincronização dos relógios em todos os servidores que utilizem o **F****luig ESB Server** em ambiente de Alta disponibilidade. Para isso é recomendado utilizar o protocolo NTP. O guia de instalação e configuração pode ser localizado em: [NTP.br](http://NTP.br). Para redes Windows® também pode ser utilizado o Active Directory®.

### TOTVS | License Server

Cada instância do **Fluig ESB Server** deve possuir uma licença disponível no **License Server** para sua correta execução e inicialização.

Para que não seja necessário utilizar o servidor de licenças, é obrigatório que os diagramas executados nas instâncias do **Fluig ESB Server** contenham somente componentes do tipo **TOTVSReceiver** e **TOTVSSender** para a troca de mensagens entre soluções TOTVS.

### TOTVS | Developer Studio

É obrigatório a utilização do **TOTVS | Developer Studio** (11.x ou superior) em conjunto com o **Fluig ESB Plugin** (versão 12.x ou superior) instalado.

O **TOTVS | Developer Studio** éutilizado para a criação dos mapas de integração que serão executados nos **Fluig ESB Servers** configurados em Cluster bem como realizar a configuração dos **Fl****uig ESB Server Cluster Nodes.**

Este documento não cobre o procedimento de instalação e configuração do **TOTVS | Developer Studio**. Para obter mais detalhes sobre a instalação do produto, verifique o procedimento de instalação no endereço <http://ds.totvs.com>.

### Banco de Dados

Visando garantir a alta disponibilidade da base de dados, recomenda-se que este também esteja sob um cluster quando utilizado no cenário de alta disponibilidade do **Fluig ESB Server**. (vide documentação do banco de dados utilizado).

# Alta Disponibilidade

---

### Cenário 1 - Alta Disponibilidade

### Definição

Um sistema de alta disponibilidade é um sistema resistente a falhas de software e energia, cujo principal objetivo é manter os serviços online o máximo de tempo possível.

### Descrição do cenário

O cenário apresenta três instâncias do **Fluig ESB Server** configuradas para trabalhar de forma sincronizada formando assim um só **Fluig ESB Server Virtual**. Todas as instâncias do **Fluig ESB Server** são configurados para compartilhar o mesmo banco de dados. O Monitoramento das mensagens poderá ser realizado utilizando o , acessível a partir de qualquer uma das instâncias do cluster **Fluig ESB Server.**

### Fluig ESB Server – Nomenclatura das instâncias

* MÁQUINA 1: Fluig ESB Server Cluster Node 1

* MÁQUINA 2: Fluig ESB Server Cluster Node 2

* MÁQUINA 3: Fluig ESB Server Cluster Node 3

# Configuração das instâncias Fluig ESB

---

### Fluig ESB Server Cluster Nodes

0.5falsesamplesfadetrue1Passo 1

Inicie as instâncias do **Fluig ESB Server Cluster Node** das máquinas 1, 2 e 3;

2Passo 2

Abra o **TOTVS Developer Studio** e acesse a perspectiva **“TOTVS ESB”**;

3Passo 3

Na view **“ESB Servers”**, efetue um clique com o botão direito do mouse e selecione a opção **“Novo grupo de Servidores”** para configurar um novo grupo de servidores chamado **Fluig ESB Cluster**;

  
4Passo 4

Configure o acesso ao servidor da máquina 1. Para isso efetue um clique com o botão direito do mouse sobre o grupo de servidor **“Fluig ESB Cluster”** e selecione a opção **ESB → ESB Server**.

true5Passo 5

Informe na opção “Nome Servidor” o valor Maquina 1, e em **“Host”** e **“Port”** o IP e a porta em que está executando o **Fluig ESB**. Clique no botão **“Finish”** para confirmar.

true6Passo 6

Abra o arquivo de configuração da máquina 1, efetuando um duplo clique sobre o seu nome na view **“ESB Servers”**.

true7Passo 7

Configure o banco de dados do **Fluig ESB Server** da máquina 1 para utilizar o banco de dados que será compartilhado por todas as instâncias **Fluig ESB Server**. Neste exemplo utilizaremos um banco de dados MySQL Server 5.5, com acesso ao schema “**esbcluster**”. A configuração é feita acessando a aba “Database Configuration” na configuração **Fluig ESB Server.**

true8Passo 8

Acesse a aba **“Cluster Configuration”**;

true9Passo 9

Na opção “Cluster Name”, informe o nome da máquina na caixa de texto **“Name”**. Digite **“ESBClusterNode1”**;

true10Passo 10

Habilite a opção **“Enable High-Avaliability”**;

true11Passo 11

Alimente a tabela **“Cluster Nodes HA”** com os endereços IP e Porta dos respectivos **Fluig ESB Servers 2** e **3**.

* Clique no botão “+” para adicionar um novo servidor;

* Na opção **“Hostname/IP”** informe o IP do **Fluig ESB Server** que irá executar na máquina 2;

* Na opção **“Port”** informe a porta do ESB na máquina remota;

* Repita o processo para configurar o **Fluig ESB Server** Cluster Node 3, informando seu respectivo IP e Porta.

* A configuração deverá ficar como a imagem abaixo:

true12Passo 12

Clique no botão **“Salvar”** para confirmar as configurações.

true13Passo 13

O console do **Fluig ESB Server** deve apresentar o resultado conforme a imagem abaixo:

true14Passo 14

Reinicie o **Fluig ESB Server Cluster Node** da máquina 1.

true15Passo 15

Repita os passos a partir do item 4 para configurar os servidores 2 e 3.

Atenção

Quando chegar o momento de configurar o item 9 novamente para os servidores 2 e 3, tome o cuidado de:

* As referências a configuração da “maquina 1” devem ser entendidas como **“maquina 2”** quando estiver configurando a máquina 2.
* As referências a configuração da “maquina 1” devem ser entendidas como **“maquina 3”** quando estiver configurando a máquina 3.
* Na opção **“Name”** do **Custer Name**, informe **ESBClusterNode2** e **ESBClusterNode3** para os servidores das máquinas 2 e 3 respectivamente.
* No servidor **ESBClusterNode2**, informar os endereços IP e porta dos servidores 1 e 3
* No servidor **ESBClusterNode3**, informar os endereços IP e porta dos servidores 1 e 2.

# Criação e deploy dos diagramas de integração nas instâncias Fluig ESB

---

### Criação dos diagramas

Para que o **Fluig ESB** funcione corretamente com a configuração em cluster de alta disponibilidade, é necessário que o mesmo diagrama execute simultaneamente nas instâncias do cluster para que ocorra o resultado esperado. Dessa maneira, quando algum das máquinas que faz parte do cluster venha a ficar indisponível, o diagrama continuará a ser executado pelos demais nós do cluster.

Para criar um novo diagrama vamos utilizar o **TOTVS | Developer Studio** com o plugin do **Fluig ESB.**

0.5falsesamplesfade1Passo 1

Abra o **TOTVS | Developer Studio** e acesse a perspectiva **“Fluig ESB”**;

2Passo 2

Na view **“ESB Navigator”**, efetue um clique com o botão direito do mouse e selecione a opção **“New → ESB Project”** para criar um novo projeto de diagramas do **Fluig ESB**.

3Passo 3

Na view **“ESB Navigator”**, efetue um clique com o botão direito do mouse e selecione a opção **“New → ESB Project”** para criar um novo projeto de diagramas do **Fluig ESB**. Clique em **“Finish”** após informar o nome do projeto, seu título e uma descrição.

4Passo 4

Na view **“ESB Navigator”**, efetue um clique com o botão direito do mouse sobre o projeto **“ESBCluster”** e selecione a opção **“New → ESB Diagram”** para criar um novo diagrama do **Fluig ESB**. Clique em **“Finish”** após informar o nome do diagrama.

5Passo 5

Crie um diagrama **WSChannelReceiver → FileSender** conforme o exemplo abaixo:

6Passo 6

Configure as propriedades do componente WSChannelReceiver conforme o exemplo abaixo:

7Passo 7

Configure as propriedades do componente **FileReceiver** conforme o exemplo abaixo. É importante ressaltar que a propriedade **“Directory”** deve apontar para um diretório de rede ou storage.

8Passo 8

Salve o diagrama clicando sobre o botão “Salvar” ou “Salvar todos”.

9Passo 9

Efetue o **“deploy”** do diagrama para o servidor da máquina 1, clicando com o botão direito do mouse sobre o diagrama aberto, e selecionando a opção **“Deploy to ESB Server...”**.

10Passo 10

Efetue o **“deploy”** do diagrama para o servidor da máquina 1, clicando com o botão direito do mouse sobre o diagrama aberto, e selecionando a opção **“Deploy to ESB Server...”**.

11Passo 11

Repita o processo de deploy a partir do passo 9 para as máquinas 2 e 3.

12Passo 12

Reinicie os serviços do ESB nas três máquinas. O Fluig ESB configurado para alta disponibilidade estará funcionando.

# **Considerações sobre o ambiente de alta disponibilidade**

---

### Teste de execução

Para testar o funcionamento do **Fluig ESB** em alta disponibilidade, utilize o aplicativo SoapUI para gerar um cliente *web service* que envie mensagens para os nodos do ESB.

O SoapUI possui uma versão *open source* e pode ser baixado através do endereço <http://www.soapui.org/>.

Baixe e instale o SoapUI.

Antes de criarmos um projeto de testes no SoapUI, precisamos obter o endereço WSDL dos serviços Web do **Fluig ESB**. Para isso, acesse a URL abaixo através de qualquer navegador de internet:

[http://[ip-do-servidor]:[porta]/ws](http://ip-do-servidorporta), onde:

**ip-do-servidor =** endereço IP da máquina 1

**porta =** 8085 – porta padrão do serviço web

0.5falsesamplesfade1Passo 1

Em nosso exemplo vamos acessar a URL: <http://10.80.69.173:8085/ws/>. A página abaixo deve ser carregada, e o link selecionado deve ser acessado para exibir o WSDL dos serviços do Fluig ESB.

2Passo 2

O WSDL deve ser exibido no navegador de internet para o endereço <http://10.80.69.173:8085/ws/esb/ESBWebService?wsdl> conforme a imagem abaixo. Copie a URL deste endereço para utilizar no **SoapUI**.

3Passo 3

De posse do endereço do WSDL dos serviços do **Fluig ESB**, execute o **SoapUI**, e crie um novo projeto clicando no menu **File → New soapUI Project**, conforme a figura abaixo:

4Passo 4

Na opção **“Project Name”** informe: Teste Maquina 1 Na opção **“Initial WSDL/WADL”** informe o endereço WSDL dos serviços do **Fluig ESB.** Clique no botão “OK” para confirmar a criação do projeto.

5Passo 5

Repita o processo de criação para os endereços das máquinas 2 e 3 a partir do **passo 4**, bastando somente modificar o endereço IP da respectiva máquina durante a criação do projeto no **SoapUI.**

6Passo 6

Após o **passo 5**, o SoapUI deve conter 03 projetos para podermos enviar mensagens para cada um dos nós do cluster.

7Passo 7

Para enviar uma mensagem de teste ao **Fluig ESB Server** da máquina 1, abra o projeto **“Teste Maquina1”**, expanda o método **“sendMessage”** e efetue um duplo clique no **“Request 1”**.

8Passo 8

Será aberta uma janela para iniciar um teste de requisição ao serviço “sendMessage” do Fluig ESB, conforme apresenta a imagem abaixo:

9Passo 9

Altere o envelope SOAP da requisição para que envie a mensagem **“Mensagem Teste ao TOTVS | ESB Cluster”** para o componente **WSChannelSender**. Para isso altere o conteúdo dos elementos **<message/>** e **<queue/>**, e clique no botão **“Submit request to specified endpoint URL”** conforme a imagem abaixo:

10Passo 10

O ESB deve responder conforme as imagens abaixo:

11Passo 11

Acesse o diretório **y:\temp\resources** confira que um arquivo foi adicionado com o conteúdo **“Mensagem Teste ao TOTVS | ESB Cluster”**.

12Passo 12

Repita o mesmo processo com os projetos das máquinas 2 e 3 para validar o funcionamento do ambiente de cluster.

### Considerações funcionamento dos componentes do Fluig ESB em ambiente de cluster de alta disponibilidade

Quando configurado como Cluster de alta disponibilidade, o **Fluig ESB** irá trabalhar melhor com componentes do tipo **“Receiver”** que sejam considerados **“Ativos”** caso o cenário de integração deva ter somente um ponto de entrada centralizado. Com isso, o Fluig ESB é capaz de realizar a leitura de um único repositório de entrada para processar as mensagens.

Componentes **“Receiver”** ativos são aqueles que possuem a capacidade de trabalhar buscando mensagens de repositórios através de agendamento pela opção **“Interval”**.

Contudo, é necessário que o intervalo de agendamento na opção **“Interval”** seja **“diferenciado”** entre os Receivers das máquinas que trabalham em alta disponibilidade.

Isso significa que o mesmo diagrama deve executar em todos os nós do cluster, mas o intervalo de *pooling* deve ser diferente entre eles.

Para isso, o diagrama pode ser replicado no **TOTVS | Developer Studio** para cada máquina, onde a única diferença é o intervalo de leitura do componente Receiver do tipo ativo. Basta copiar e colar o projeto .esb original informando um novo nome na aba **“ESB Navigator”**.

Para o exemplo em questão, os diagramas ficariam dispostos conforme a imagem abaixo no TOTVS | Developer Studio:

Segue abaixo a lista de componentes do tipo **Receiver** do **Fluig ESB “Ativos”**, indicados para trabalhar com cluster de Alta Disponibilidade:

* **FILEReceiver**

* **FTPReceiver**

* **MAILReceiver**

* **JMSReceiver**

* **HTTPReceiver**

* **TOTVSReceiver (somente DATASULReceiver)**

Para utilizar diagramas em cluster de alta disponibilidade que utilizem componentes Receiver do tipo passivo, é recomendado utilizar a configuração de cluster de *Load Balancing* (balanceamento de carga), onde é adicionado mais um **Fluig ESB Server Cluster Proxy** para redirecionar o processamento das mensagens para os componentes Receivers do tipo passivo.

Esta configuração é exemplificada no próximo capítulo.

# Balanceamento de Carga

---

### Cenário 2 - Balanceamento de carga

### Definição

Esse tipo de cluster tem como função controlar a distribuição equilibrada do processamento. Requer um monitoramento constante na sua comunicação e em seus mecanismos de redundância, pois se ocorrer alguma falha, haverá uma interrupção no seu funcionamento. É composto por um conjunto de servidores Fluig ESB configurados para receber a distribuição de carga de um servidor **Fluig ESB** **Master**, permitindo ao máximo a divisão da carga do ambiente para o usuário através de políticas de balanceamento de carga.

### Descrição do cenário

O cenário apresenta três instâncias do Fluig ESB Server configuradas para trabalhar de forma independente. Todas as instâncias do **Fluig ESB Server** são configuradas para compartilhar o mesmo banco de dados, e recebem a carga da rede através de um servidor **Fluig ESB Master** (com servidor de banco de dados isolado das demais instâncias), que pode dividir a carga através de dois tipos de políticas:

**1. ROUND ROBIN**  
Política utilizada quando a capacidade de processamento das máquinas que receberão a distribuição de carga é desconhecida. Com esta política habilitada, o **Fluig ESB Cluster Master** dividirá a carga igualmente entre os demais Fluig ESB Servers de destino.

**2. WEIGHTED ROUND ROBIN**  
Política utilizada quando a capacidade de processamento das máquinas que receberão a distribuição de carga é conhecida e diferente. Isso significa que o Fluig ESB Cluster Master poderá enviar cargas diferenciadas de acordo com o servidor de destino. Com esta política habilitada, o **Fluig ESB Cluster Master** poderá ser configurado para enviar rajadas de requisições diferenciadas entre os demais Fluig ESB Servers de destino.

O monitoramento das mensagens poderá ser realizada utilizando o Fluig ESB Monitor acessível a partir de qualquer uma das instâncias do Fluig ESB Server.

### Fluig ESB Server – Nomenclatura das instâncias

* **MÁQUINA *LOAD BALANCING*:** TOTVS | ESB Server Cluster Master 1

* **MÁQUINA 1:** TOTVS | ESB Server Node 1

* **MÁQUINA 2:** TOTVS | ESB Server Node 2

* **MÁQUINA 3:** TOTVS | ESB Server Node 3

# Configuração das instâncias Fluig ESB

---

### Fluig ESB Server Nodes

Para configurar as quatro máquinas com o Fluig ESB Server, siga os passos descritos no [item 4.4](http://tdn.totvs.com/display/fluig/Alta+disponibilidade+e+balanceamento+de+carga+do+fluig+ESB#AltadisponibilidadeebalanceamentodecargadofluigESB-fluigESBServer%E2%80%93Nomenclaturadasinst%C3%A2ncias) até o passo 7 para cada uma das instâncias do Fluig ESB.

Atenção

Ao configurar o novo servidor na view “Servers” para o Cluster Master (Proxy de balanceamento de carga), informe na propriedade **“Server Name”** o valor **“Maquina Cluster Master (Proxy)”**.

Não é necessário configurar as três instâncias como federação de cluster de alta disponibilidade. Após o processo de criação dos servidores no **TOTVS | Developer Studio**, a view **“Servers”** deverá estar conforme a imagem abaixo:

Para configurar a máquina Fluig ESB Server (Maquina Cluster Master) que irá trabalhar como **Proxy de balanceamento de carga**, siga os passos adicionais abaixo:

0.5falsesamplesfade1Passo 1

Acesse a aba **“Cluster Configuration”**;

2Passo 2

Na opção “Cluster Name”, informe o nome da máquina na caixa de texto **“Name”**. Digite **“ESBClusterMaster1”**;

3Passo 3

Habilite a opção **“Enable Load Balancing”**;

4Passo 4

Selecione a política desejada:

* *Round Robin* (padrão) ou
* *Weighted Round Robin*
5Passo 5

Vamos configurar a opção ***Weighted Round Robin***. Informaremos que a máquina 1 irá receber uma rajada de 1 mensagem, a máquina 2 uma rajada de 4 mensagens e o servidor 3 uma rajada de 8 mensagens.

6Passo 6

Para isso, informe o seguinte valor no campo **“Distribution Ratio”**: 1:4:8

7Passo 7

Salve a configuração e reinicie o **Fluig ESB Cluster Master (Proxy)**

8Passo 8

O console do **Fluig ESB Server** deve apresentar o resultado conforme a imagem abaixo:

# Criação e deploy dos diagramas de integração nas instâncias Fluig ESB

---

### Criação dos diagramas

Para que o Fluig ESB funcione corretamente com a configuração em cluster de balanceamento de carga, não é necessário que o mesmo diagrama execute simultaneamente nas instâncias do cluster para que ocorra o resultado esperado.

Cada máquina contendo uma instância do Fluig ESB Server pode conter diagramas diferenciados, mas para efeitos didáticos assumiremos que todas as máquinas irão executar o mesmo diagrama.

Somente a instância do Fluig ESB Server configurado como cluster master em balanceamento de carga irá executar um diagrama diferente, com o objetivo de distribuir a carga entre os demais Fluig ESB Servers.

Para confeccionar os diagramas das 03 máquinas que executam o Fluig ESB Server, execute os **passos** **1 a 12** a partir do **[item 6.1](http://tdn.totvs.com/display/fluig/Alta+disponibilidade+e+balanceamento+de+carga+do+fluig+ESB#AltadisponibilidadeebalanceamentodecargadofluigESB-Cria%C3%A7%C3%A3oedeploydosdiagramasdeintegra%C3%A7%C3%A3onasinst%C3%A2nciasfluigESB) (Criação dos diagramas).**

Siga os passos abaixo para criar o diagrama que deve executar na máquina Fluig ESB Server Master:

0.5falsesamplesfade1Passo 1

Conforme descrito no passo 4 do item 6.1, crie um novo diagrama do Fluig ESB com o nome **“LoadBalancingDiagram.esb”**

2Passo 2

Configure o diagrama conforme o exemplo abaixo: **(01 FileReceiver** enviando para **03 WSSenders)**

3Passo 3

Configure as propriedades do componente **FileReceiver** conforme o exemplo abaixo:

4Passo 4

Configure as propriedades do componente **WSSenderMaquina1** conforme o exemplo abaixo:

a. Na opção **“WSDL Path”** informe: <http://ip_maquina_1:8085/ws/esb/ESBWebService?wsdl> (informando o endereço IP da máquina 1 no lugar de “ip\_maquina\_1”);

b. Clique no botão **“List Operations”**

c. No combo “Operation”, selecione a opção **“sendMessage”**

d. Adicione um parâmetro com o nome **“message”** do tipo **“ESBMessage”** na coluna **“Data Type”** e com o campo **“value”** em vazio

e. Adicione mais um parâmetro com o nome **“queue”** do tipo **“Text”** contendo o valor **“WSChannelReceiver”** no campo **“value”**.

f. A configuração deverá ficar conforme a imagem abaixo:

5Passo 5

Efetue a mesma configuração para os componentes **WSSenderMaquina2** e **WSSenderMaquina3** levando em consideração somente o endereço IP do campo **WSDL Path**, que deve apontar para IP correspondente a máquina 2 e a máquina 3.

6Passo 6

Salve o diagrama clicando em um dos botões **“Save”** ou **“Save All”**

7Passo 7

Efetue deploy do diagrama para o servidor **Fluig ESB Cluster Master** (Proxy) conforme descrito a partir do item 9 na página 15.

# Considerações sobre o ambiente de balanceamento de carga

---

### Teste de execução

Para testar o funcionamento do Fluig ESB em balanceamento de carga, basta reiniciar todas instâncias do Fluig ESB, e disponibilizar 13 arquivos texto no diretório **C:\TEMP\RESOURCES.**

O **Fluig ESB Cluster Master (Proxy)** deverá distribuir a carga da seguinte maneira:

* Máquina 1 – receberá 1 arquivo

* Máquina 2 – receberá 4 arquivos

* Máquina 3 – receberá 8 arquivos

Caso deseje alterar a política de distribuição da configuração de balanceamento de carga para **ROUND ROBIN**, efetue a alteração na configuração da instância Fluig ESB de proxy, salve e reinicie o servidor Fluig ESB Cluster Master (Proxy).

Ao postar novamente 13 arquivos no diretório **C:\TEMP\RESOURCES**, o resultado será:

* Máquina 1 – receberá 5 arquivos

* Máquina 2 – receberá 4 arquivos

* Máquina 3 – receberá 4 arquivos

Sendo que a máquina 1 receberá o 1º e o último arquivo da instância **Fluig ESB** configurada como proxy de balanceamento de carga.

Observações

Não utilizamos o **SoapUI** nos testes pois a instância Fluig ESB configurada para balanceamento de carga faz exatamente a mesma função, enviando via *web services* o conteúdo dos arquivos TXTs lidos do diretório **C:\TEMP\RESOURCES.**

### Considerações funcionamento dos componentes do Fluig ESB em ambiente de cluster de alta disponibilidade

Quando configurado como Cluster de balanceamento de carga, o Fluig ESB irá trabalhar com quaisquer tipo de componentes.

Na configuração de balanceamento de carga, podemos ter diagramas diferentes, cada um executando em um Nodo respectivo. Isso é possível, pois ficará a cargo do **Fluig ESB Cluster Master1** redirecionar a carga para cada instância dos Fluig ESB Server Nodes (máquinas 1, 2 e 3).

É importante lembrar que este capítulo não está configurando as instâncias dos Fluig ESB Server Nodes com alta disponibilidade. Caso uma das instâncias venha a ficar indisponível, o processamento dessa instância ficará indisponível até que ela volte a ficar online.
