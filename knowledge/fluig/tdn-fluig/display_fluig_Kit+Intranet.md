---
content_hash: 23b9d10b64a706cbd6f6a54298b236d455260774f2185bcb2be202d83c182438
fetched_at: '2026-06-28T21:35:19.075795+00:00'
page_id: '189313181'
product: fluig
source: tdn-fluig
title: Kit Intranet
type: documentation
url: https://tdn.totvs.com/display/fluig/Kit+Intranet
version: 94
---

# Índice

4true.\*ndicenone

# Objetivo do Componente

---

O Kit Intranet oferece widgets, técnicas e código de referência para desenvolvedores na plataforma fluig nas tarefas mais comuns, como:

* Desenvolvimento de Widgets utilizando a SuperWidget;
* Utilização do fluig Style Guide;
* Salvar e recuperar preferências de Widgets;
* Controle de instâncias de Widgets;
* Exibir dados de Documentos do ECM;
* Consultar e exibir dados de formulários;
* Obter dados a partir de um ERP;
* Receber e enviar dados utilizando REST

Importante

O Kit Intranet deixou de ser oferecido pela Fluig Store e agora pode ser obtido diretamente através do diretório Git do Fluig. Faça o *download* do pacote **[neste *link*](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse)** para a atualização Fluig 1.8.1.

Já para as atualizações inferiores e até a 1.8.0 faça o download **[neste *link*](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse?at=refs%2Ftags%2F1.5.13_A_1.8.0)**. E confira mais informações sobre a instalação na seção de [Instalação/Atualização](http://tdn.totvs.com/display/fluig/Kit+Intranet#KitIntranet-Instala%C3%A7%C3%A3o/Atualiza%C3%A7%C3%A3o) abaixo.

# Widgets

---

Veja o exemplo em nosso repositório [aqui](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse/kitintranet.zip).

## Widget Aniversariantes

Não deixe passar em branco o aniversário de ninguém: veja os aniversariantes do mês, com destaque para os aniversariantes do dia.

Atualmente podemos listar os aniversariantes utilizando duas formas de consulta, uma é através da criação de registros de formulários diretamente no fluig e a outra é pela integração com o ERP RM.

**Registro de Aniversariantes diretamente no fluig**

11Passo 1

* Adicione a widget de aniversariantes na página de sua preferência.

2Passo 2

* Clique em "Link do formulário" para acessar os registros de aniversariantes.

3Passo 3

* Clique em **Novo** e depois em **Registro de formulário** para inserir um novo registro.

4Passo 4

* Preencha o formulário com as informações do aniversariante.

**[Aqui](https://git.fluig.com/projects/SAMPLES/repos/datasets/browse/dataset-cardservice-create)** temos um exemplo (**dataset-cardservice-create**) que lê a tabela de funcionários do ERP e cria registros de formulário no formulário de aniversariantes do Kit Intranet.

**Integração com o RM**

Na widget de aniversariantes, selecione RM e preencha as informações de acesso ao serviço de consulta do ERP.

Atenção!

A *widget* precisa ser configurada com o usuário mestre do RM ou outro usuário com as mesmas permissões.

## Widget Organograma Corporativo

Veja a estrutura organizacional da sua empresa, buscando as informações de seu ERP.

Este widget irá acessar os serviços do TOTVS RM, .

## Widget Notícias

Aposente murais de notícias e comunicados por e-mail: publique notícias e faça comunicados para toda sua empresa de forma moderna, de forma online.

Após a instalação do Kit Intranet, siga os procedimentos abaixo para criar novas notícias.

Procedimentos1Passo 1

* Edite a página qual a widget de Notícias foi adicionada, e conforme mostra a imagem abaixo clique no link do formulário.

2Passo 2

* Clique em **Novo** e depois em **Registro de formulário** para inserir uma nova notícia.

3Passo 3

* Preencha o formulário com o conteúdo da notícia.

Observação

As imagens contidas nas *widgets* não possuem um tamanho padrão fixo pois elas são responsivas, ou seja, se adaptam ao tamanho do monitor em que a *widget* está sendo visualizada.

Quando as notícias são pré-visualizadas na lista da widget, a imagem de cada notícia é redimensionada para ser exibida em uma prévia. Sua largura em miniatura possui 120 px.

Ao clicar em uma determinada notícia, a mesma é aberta em uma nova tela, neste caso a imagem é redimensionada de maneira responsiva de acordo com o tamanho do monitor.

## Widget Convênios

Facilite a consulta e visualização do catálogo de convênios que os funcionários de sua empresa tem acesso, evitando que convênios desatualizados continuem sendo divulgados.

## Widget Slideshow

Adicione um slideshow de imagens em suas páginas ou comunidades, possibilitando exibir imagens a partir de uma pasta publicada no ECM ou então de uma conta do Instagram.

Fique atento!

A resolução ideal é para as imagens no widget Slideshow é de **1024 x 576 pixels**. Porém, dependendo da resolução do monitor, a resolução da imagem pode mudar. Caso precise de um tamanho maior, basta redimensioná-la mantendo a mesma proporção.

**Opções da widget Slideshow:**

Para ter acesso as opções da widget a pagina deve estar em modo de edição. Uma vez em edição  a widget de slideshow apresenta as opções:

* **Integração via Instagram:** Integre a widget com o Instagram para exibir imagens deste serviço no Slideshow.

* **Gerar Novo Token de Acesso**: Exibido apenas quando a integração com o Instagram está ativada. Redireciona o usuário para o portal do desenvolvedor do Instagram, onde o procedimento de geração de token deve ser realizado.

Acesse a documentação  para obter informações sobre como realizar a integração.

* **Integração via pasta do sistemas:** Neste caso o usuário deverá informa a pasta no sistema que contem as imagens a serem exibidas, esta opção também possibilita mostrar a legenda das imagens através da opção "Mostrar título nas imagens" conforme figura.

* **Estender Imagens:**Em ambas opções de integração da widget, existe a opção de "Estender as imagens". Habilitando este item as imagens irão ocupar toda a área da widget. Dependendo da resolução da imagem, esta opção pode deixar a imagem distorcida. A altura máxima suportada é de 400px, a largura irá depender da tela do monitor do usuário.

* **Redimensionar:** Enquadra imagens com tamanho maior que o disponível no Slideshow para evitar que sejam exibidas apenas parcialmente no widget.

## Widget Cardápio

Divulgue qual serão as opções disponíveis para umas das melhores horas do dia: comer! Para cada opção, inclua o nome, descrição e, se quiser, adicione uma foto.

Após a instalação do Kit Intranet, siga os procedimentos abaixo para adicionar novos registros no cardápio.

11Passo 1

* Edite a página qual a widget de Cardápio foi adicionada, e conforme mostra a imagem abaixo clique no link do formulário.

2Passo 2

* Clique em **Novo** e depois em **Registro de formulário** para inserir um novo item no cardápio.

3Passo 3

* Preencha as informações do formulário com o conteúdo do cardápio.

# Instalação e atualização do Kit Intranet

---

Siga os passos descritos abaixo para instalar e configurar propriamente o componente.

0.5falsesamplesfadetrue1Download

**Download**

* Faça o *download* do Kit Intranet gratuitamente através [deste link](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse/kitintranet.zip).

2Instalação/Atualização

**Instalação/Atualização**

* Faça login no fluig como usuário administrador

* Clique em **Painel de Controle** → agrupador **Personalização** → **Importar e Exportar Páginas**

* Importe o artefato "kit-intranet.zip" obtido na etapa anterior

* Verifique se a página "Intranet" foi criada na barra de menu lateral.

3Exemplos para desenvolvedores

* Verifique [aqui](http://tdn.totvs.com/display/fluig/Widgets) como desenvolver seus próprios *widgets* a partir dos exemplos dessa página.

## Conexão aos serviços RM

Algumas widgets podem obter dados a partir de serviços SOAP de uma instancia do ERP RM versão 11.40 ou superior.

Para conhecer e saber como utilizar estes serviços, utilize a [Documentação de Integração](http://wikihelp.totvs.com.br/WikiHelp/CON3/INT.Integracao.aspx).

## Suporte a aplicativos Mobile

Agora as widgets de Aniversariantes, Notícias, Cardápio, Convênios e Organogramas podem ser visualizadas também nos aplicativos mobile, basta seguir as etapas abaixo.

Habilitar Widget Mobile1Editar Página

Com usuário administrador acessa a opção **Editar página**.

2Selecionar as widgets 

Na parte superior direita da widget que deseja habilitar a visualização em aplicativos móveis, clique no ícone ao lado do cadeado.

3Publicar a página

Publique as alterações e acesse a página a partir do aplicativo móvel.

### Webservices RM

Os widgets Aniversariantes e Organograma fazem acesso a serviços do ERP RM utilizando o protocolo SOAP, conforme os detalhes abaixo:

#### Widget Aniversariantes

Mount Point: /wsDataServer/IwsDataServer

DataServerName: RhuPessoaData

| Campo | Descrição |
| --- | --- |
| birthDay | Dia do nascimento |
| birthMonth | Mês do nascimento |
| fullName | Nome completo |

[Aqui](https://git.fluig.com/projects/SAMPLES/repos/datasets/browse/dataset-cardservice-create) temos um exemplo que lê a tabela de funcionários do ERP e cria registros de formulário no formulário de aniversariantes do Kit Intranet

#### Widget Organograma organogramaRM

Mount Point: /wsDataServer/IwsDataServer

DataServerName: FopSubordinadosData

| Campo | Descrição |
| --- | --- |
| userCode | Código do usuário no RM |
| email | Email do usuário |
| name | Nome do usuário |

# Desenvolvimento sobre a plataforma

---

Para modificar o comportamento dos *widgets* do Kit Intranet de modo que se adequem melhor a sua situação, pode-se tomar como base o guia para [criar um widget que busque conteúdo](http://tdn.totvs.com/pages/viewpage.action?pageId=185735401).
