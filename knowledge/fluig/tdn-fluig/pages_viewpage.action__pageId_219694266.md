---
content_hash: 00e3d9b9bb16348423354c0cc9f3b9c4bf635d373c06e600a3d165d1e7f5d016
fetched_at: '2026-06-28T21:35:19.662497+00:00'
page_id: '219694266'
product: fluig
source: tdn-fluig
title: Edição colaborativa com Google Drive
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219694266
version: 78
---

* [Objetivo](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-Objetivo)
* [Pré-requisitos](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-Pr%C3%A9-requisitos)
* [Edição colaborativa com Google Drive](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive)
  + [Download do pacote](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-Downloaddopacote)
  + [Instalação do componente](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-Instala%C3%A7%C3%A3odocomponente)
* [Configurando o seu Google Drive](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-ConfigurandooseuGoogleDrive)
* [Habilitar edição colaborativa na plataforma](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-Habilitaredi%C3%A7%C3%A3ocolaborativanaplataforma)
* [Edição de conteúdo após a conclusão da configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Edi%C3%A7%C3%A3ocolaborativacomGoogleDrive-Edi%C3%A7%C3%A3odeconte%C3%BAdoap%C3%B3saconclus%C3%A3odaconfigura%C3%A7%C3%A3o)

# Objetivo

---

Este guia tem o objetivo de apresentar os passos necessários de configuração para uso da edição colaborativa no TOTVS Fluig Plataforma.

# Pré-requisitos

---

* É necessário que a plataforma tenha acesso externo (a partir da internet) para utilizar esta funcionalidade

  Os endereços [https://www.google.com](https://www.google.com.br) e [https://www.googleapis.com](https://www.google.com/url?q=https://www.googleapis.com&sa=D&source=hangouts&ust=1562088363335000&usg=AFQjCNFpM2yt1vy3OeOd5Q-tIVpTXqA4nw) devem estar liberados na rede.
* A edição em modo colaborativo depende da extensão do arquivo. Arquivos em PDF, por exemplo, não são editáveis, e devem ser convertidos para posterior edição.

# Edição colaborativa com Google Drive

---

A plataforma disponibiliza o recurso de edição colaborativa de documentos, por meio do Google Drive. Para utilizar esse recurso, é necessário instalar e configurar um componente específico, conforme orientações abaixo.

## Download do pacote

* Para baixar o componente, acesse o [Portal do Cliente](http://suporte.totvs.com)[.](http://suporte.fluig.com/)
* Clique em ***Download*** (essa é a mesma página onde está disponível a mais recente atualização da plataforma).
* Selecione o produto **Fluig**, acesse o diretório **FLUIG STORE** e selecione**FLUIG**.
* Faça o *download* do arquivo **FLUIG-COLLABORATION-GOOGLEDRIVE.**

## Instalação do componente

Descompacte o arquivo em uma pasta de sua preferência, que aqui chamaremos de **<Diretorio\_EdicaoColaborativa>.**

false0.5falseComponentefadetrue1Passo1

* Acesse a plataforma com o perfil de administrador e em seguida acesse : **Painel de Controle** → agrupador **Aplicativos** → **Central de componentes**.

2Passo 2

* Acione a opção **Escolher arquivo**, navegue até a pasta descompactada e selecione o arquivo **application-collaboration-googledrive-ear.ear**.

3Passo 3

* Acione a opção **Enviar** e aguarde aproximadamente 1 minuto para a finalização do processo de publicação do componente;
* Reinicie os serviços fluig\_RealTime, fluig\_Indexer e fluig.
4Passo 4

* Após reiniciar os serviços, faça uma busca na página de componentes por **collaboration.**
* Selecione **ecm\_collaboration\_admin** e acione o botão **Ativar**.
* Selecione **ecm\_collaboration\_edit** e acione o botão **Ativar.**

5Passo 5

* Acesse **Painel de Controle →** agrupador **Aplicativos**. Uma nova opção de menu chamada **Edição Colaborativa** estará disponível .

6Passo 6

* Ao clicar na opção **Edição Colaborativa** será apresentada a tela abaixo.

false

A URL de redirecionamento será utilizada na configuração do **[Aplicativo WEB](http://tdn.totvs.com/pages/viewpage.action?pageId=219694266#GoogleDrive-8)** do Google no próximos passos.

7Passo 7

* Reiniciar os serviços da plataforma.

# Configurando o seu Google Drive

---

Para que seja possível a integração entre o TOTVS Fluig Plataforma e o Google Drive será necessário realizar os passos abaixo.

0.5falseGoogle Drivefadetrue1Passo 1

* Acesse a URL [https://console.developers.google.com.](https://console.developers.google.com) Caso não esteja logado no Google, realize o login e crie um projeto, seguindo um dos exemplos abaixo:
  + Credenciais > Criar
  + Criar projeto
2Passo 2

* Após avançar, escolha um nome para o seu projeto.
* Em seguida, clique em **Criar**.

3Passo 3

* Agora você pode aguardar a criação do projeto e acompanhar pela notificação.

 

* Após a criação, selecionar o projeto e em sequência clicar em **Ir para visão geral de APIs**, conforme a imagem:

* Ou você pode acessar diretamente a URL [https://console.developers.google.com.](https://console.developers.google.com/)
4Passo 4

* Após criar o projeto, você será direcionado para a página abaixo.
* Selecione a opção **Biblioteca** no menu lateral esquerdo.

5Passo 5

* Na página exibida, selecione a opção **Drive API**, na categoria G Suite APIs.

6Passo 6

* Acione o botão **Ativar**, caso essa tela apareça. Se não pule para o passo 7.

7Passo 7

* Com a API ativada, clique no botão **Criar credenciais**.

8Passo 8

* Precisamos de credenciais do tipo **ID do cliente OAuth** para realizar a integração, portanto este passo pode ser ignorado clicando no botão **Cancelar**.

9Passo 9

* Agora clique no botão **Criar credenciais** e selecione a opção **ID do cliente OAuth**.

10Passo 10

* Clique em **Configurar a tela de consentimento**.

11Passo 11

* Informe um nome de sua preferência e acione **Salvar**.

12Passo 12

* Aqui você terá que adicionar o **Nome** do cliente e a **URL de redirecionamento.**

false

A URL de redirecionamento autorizada deve ser cadastrada com a **URL de redirecionamento** recuperada no [Passo 6](http://tdn.totvs.com/pages/viewpage.action?pageId=219694266#Componente-6) da instalação do componente.

13Passo 13

* Após criar o **Aplicativo WEB** serão apresentadas as chaves OAuth para serem cadastradas no TOTVS Fluig Plataforma.

14Passo 14

* Você também pode personalizar seu app de edição colaborativa acessando a opção de menu **Credenciais** na aba **Tela de consentimento OAuth.**

* Aproveite para adicionar o logo da plataforma.

As telas acima podem apresentar diferenças em relação ao que está demonstrado, devido a constantes atualizações da Google.

# Habilitar edição colaborativa na plataforma

---

Após realizar as configurações necessárias no Google Drive, é necessário fazer as configurações no TOTVS Fluig Plataforma para completar a integração entre a plataforma e o Google Drive.

0.5falseConfiguração fluigfadetrue1Passo 1

* Acesse **Painel de Controle >** agrupador **Aplicativos > Edição Colaborativa** e adicione as chaves OAuth adquiridas no [Passo 13](http://tdn.totvs.com/pages/viewpage.action?pageId=219694266#GoogleDrive-13) da configuração do Google Drive.

2Passo 2

* Após cadastrar as chaves e habilitar o Google Drive, acesse os Documentos e selecione um documento que deseja editar.

3Passo 3

* Selecione a opção **Google Drive**.

4Passo 4

* Será apresentada a tela abaixo onde será necessário acionar a opção **Permitir**.

5Passo 5

* Com isso, o documento estará disponível para ser editado no **Google Drive** colaborativamente por usuários que tenham permissão de edição no documento.

# Edição de conteúdo após a conclusão da configuração

---

Após realizar as configurações necessárias no Google Drive e no TOTVS Fluig Plataforma, o passo a passo para editar o conteúdo desejado pode ser consultado na documentação .

É possível editar pelo Google Drive apenas documentos que possuem uma das seguintes extensões suportadas pelo recurso:

* Documentos: doc, docx, odt;

* Planilhas: xls, xlsx, ods;

* Apresentações: ppt, pptx, odp.
