---
content_hash: 2fb779e75396bf7972d36d300d6d3e02bdcb16ab6aeee971ddb0a4364026db31
fetched_at: '2026-06-28T21:35:22.621243+00:00'
page_id: '238034195'
product: fluig
source: tdn-fluig
title: Componentes desenvolvidos sobre a plataforma Fluig ESB
type: documentation
url: https://tdn.totvs.com/display/fluig/Componentes+desenvolvidos+sobre+a+plataforma+Fluig+ESB
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

# Índice

4true.\*ndicenone

# Objetivo

---

O sistema Fluig ESB possui diversos componentes que poderão ser utilizados para montar uma integração entre aplicativos. Porém, em alguns casos se faz necessário o uso de alguns componentes desenvolvidos sobre a plataforma para definir tarefas que não são suportados pelos componentes padrão. Ex.: conexão a base de dados, tratamento de arquivos textos, etc.

O objetivo desse tutorial é demonstrar como fazer uso dos componentes *CustomReceiver* e *CustomSender* bem como o desenvolvimento das classes que serão executadas.

# Pré-requisitos

---

O editor Java para construir as classes necessárias é o Eclipse na versão Luna com o JDK (*Java Development Kit*) instalado e configurado. Porém, outros editores e ambientes também podem ser utilizados para o desenvolvimento Java.

# Construção dos componentes

---

A construção dos componentes segue três etapas:

1. Criação do projeto Java no Eclipse
2. Criação do projeto e diagrama no TDS + Plugin Fluig ESB
3. *Deploy* no Fluig ESB

## Projeto Java no Eclipse

samples1Passo 1

Com o Eclipse aberto na perspectiva Java, deve-se criar um novo projeto Java. Isso é feito acessando o menu **File **→** New... → Java Project**. Aparecerá uma tela, semelhante à exibida abaixo, solicitando um nome para o projeto bem como opções relacionadas à compilação do projeto. Para concluir clique no botão **Finish**.

Em seguida o projeto aparecerá no painel esquerdo da área de trabalho do Eclipse denominado de **Package** **Explorer** em uma estrutura padrão para projetos Java. Nesse momento, o usuário deverá referenciar o projeto ao pacote **esb-component-binding-custom-XX.XX.jar** onde XX.XX é o número da versão do ESB. Esse pacote encontra-se na instalação do Fluig ESB, na pasta lib/esb.

2Passo 2

Para fazer essa referência, deve-se clicar com o botão direito em cima do projeto Java e selecionar a opção de menu **Build Path **→** Add External Archives...** Em seguida selecionar o arquivo **esb-component-binding-custom-XX.XX.jar.** O resultado será conforme a imagem abaixo com o pacote JAR sob o item **Refereced Libraries.**

Nesse momento, o usuário estará apto a criar as classes tipo Java para serem executadas pelo componente *CustomReceiver* e/ou *CustomSender.* Cada componente deverá implementar uma interface específica para que possa ser identificada e executada pelo Fluig ESB. Nos próximos passos são apresentadas as interfaces que deverão ser implementadas para cada componente.

3Passo 3

**CustomReceiver **→** com.totvs.esb.components.custom.CustomReceiver**: Essa interface possui um método *receiveMessage* com apenas um parâmetro do tipo Properties. Esse parâmetro é um arquivo que contêm informações de propriedades para aplicativos Java. É configurado nas propriedades do componente *CustomReceiver* no momento da diagramação e será detalhado mais adiante.

O método *receiveMessage* deverá retornar a mensagem gerada em array bidimensional de bytes (**byte[][]**) para repassar ao próximo componente. Cada posição do array retornado será uma mensagem diferente a ser enviada ao fluxo do Fluig ESB. Ex.: **byte[0][]** será considerada uma mensagem diferente da posição **byte[1][]**.

4Passo 4

**Custom Sender **→** com.totvs.esb.components.custom.CustomSender**: Essa interface também possui apenas um único método denominado *sendMessage*. Nesse método a mensagem pode ser processada e definido um retorno em byte[] para o próximo componente no fluxo do ESB, se necessário. Os parâmetros que são utilizados:

* **byte[] message:** Mensagem que o componente *CustomSender* recebe do componente anterior.
* **Properties props:** Arquivo de propriedades para aplicativos Java. É configurado nas propriedades do componente *CustomSender* no momento da diagramação e será detalhado mais adiante.
* **Map<String, Object> args:** Mapa de propriedades específicas da mensagem.

5Passo 5

Com as classes devidamente desenvolvidas e compiladas sem erros, o próximo passo envolve exportar o projeto Java para o formato JAR. Trata-se de um empacotamento especial das classes para ser executado dentro de algum aplicativo Java. Para empacotar, deve-se acessar o painel Package Explorer, clicar com o botão direito em cima do projeto e acessar o menu **Export**... Uma tela semelhante ao da esquerda se abrirá e o usuário deverá selecionar a opção **Java **→** JAR file**. Após selecionar a opção, clica-se em **Next**.

6Passo 6

A próxima tela permitirá que o usuário selecione qual a pasta e os arquivos do projeto em que se deseja exportar para o arquivo JAR. A única opção que o usuário terá que configurar é o caminho e o nome do arquivo que será gerado com as classes exportadas. A configuração é realizada através do campo **JAR file**, conforme destacado na figura abaixo. Pressione **Finish** para finalizar a operação e o arquivo será gerado no diretório especificado.

## Projeto TDS + Plugin Fluig ESB

samples1Passo 1

Dentro do TDS, com o plugin Fluig ESB devidamente instalado, deve-se acionar o menu **Window → Open Perspective → Other...**,e selecionar a perspectiva TOTVS ESB e clicar em OK. A área de trabalho irá ser atualizada e no painel esquerdo para o **ESB Navigator** que conterá os projetos com os diagramas do ESB.

Em um projeto desejado, deve-se copiar o arquivo JAR resultante da etapa anterior para dentro do projeto em uma pasta de sua preferência. Nesse exemplo, utilizou-se a pasta resources. Para realizar a cópia, basta selecionar o arquivo em um navegador de arquivos do sistema operacional (Ex.: Windows Explorer, Nautilus, etc.) e arrastar para dentro do TDS na pasta resources. Ou ainda, pode selecionar o arquivo e pressionar Ctrl + C (Copiar), selecionar a pasta resources no TDS e pressionar Ctrl + V (Colar).

2Passo 2

Com isso, o usuário deverá criar um diagrama utilizando os componentes **CustomReceiver** e **CustomSender**, com as propriedades demonstradas nas figuras a seguir.

3Passo 3

As propriedades que devem ser preenchidas para os componentes são:

* Jars Folder: Pasta onde se encontra o arquivo JAR copiado para o projeto. No exemplo, o campo deverá ser a pasta resources.
* Class Name: Nome completo da classe que será executada. Conforme exemplo, para o componente **CustomReceiver** será **com.samples.esb.MyCustomReceiver**. Para o componente **CustomSender** será **com.samples.esb.MyCustomSender.**
* Properties: Trata-se de um campo opcional, caso precisar fazer uso de um arquivo tipo .properties que possui propriedades para aplicativos Java. No exemplo, utilizou-se um arquivo denominado **props.properties** situado na pasta raiz do projeto. As propriedades contidas no arquivo serão repassadas como parâmetro para os métodos implementados, conforme visto anteriormente.

Com essas configurações, o diagrama está pronto para ser executado pelo servidor Fluig ESB.

## Deploy no Fluig ESB

Para que o diagrama seja ativado no Fluig ESB, o mesmo deverá ser publicado. Para tanto, o Fluig ESB deverá estar em execução. Com o serviço do ESB “no ar”, o usuário deverá abrir o diagrama dos componentes Custom (arquivo .esb), clicar no meio do diagrama com o botão direito e acessar o menu Deploy to ESB Server... e seguir os procedimentos de publicação.

Para habilitar a execução do diagrama o usuário deverá reiniciar o serviço do Fluig ESB. Não é necessário enviar manualmente os arquivos correlatos (.jar, .properties, etc.) pois o processo de *deploy* se encarrega de enviar esses arquivos. Na figura abaixo tem-se o resultado da execução do diagrama mencionado no Fluig ESB.
