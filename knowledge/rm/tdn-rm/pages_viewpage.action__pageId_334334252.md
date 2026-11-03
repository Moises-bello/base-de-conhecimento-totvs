---
content_hash: eb4e2a212e9dcbe1d7c7da63164d04718c808db00d4d9f2b50c168c648c84523
fetched_at: '2026-06-29T00:08:50.390360+00:00'
page_id: '334334252'
product: rm
source: tdn-rm
title: 01. Parametrização inicial para a integração entre o TOTVS Folha de pagamento
  e o TAF (TOTVS Automação Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334252
version: 2
---

Partindo do princípio de que o usuário já possui o TAF (TOTVS Automação Fiscal) instalado em seu ambiente, vamos abordar inicialmente quais seriam as parametrizações necessárias dentro do módulo de Folha de Pagamento para garantir que a integração entre os dois produtos seja realizada com sucesso.

O primeiro ponto a ser levantado é o conceito utilizado para integração, levando em consideração que a comunicação entre os dois produtos será realizada via**WebServices**. Esta solução é utilizada na integração de sistemas e na comunicação entre aplicações distintas, ela fornece recursos para que novas aplicações possam interagir com aquelas que já existem e que sistemas desenvolvidos em plataformas diferentes sejam compatíveis.

Para parametrizar o produto, o usuário deve acessar o módulo de Folha de Pagamento através da nova MDI e seguir os caminhos apresentados nas imagens abaixo:

* Acesse o módulo de Folha de pagamento, clique na aba **"Configurações"** e em seguida**"Parametrizador"**:

* Ao acessar o **Parametrizador**, clique na opção **06.07-eSocial** e avance:

* Avance até a **Etapa - eSocial: Integração com o TAF**:

Na "**Etapa - eSocial: Integração com o TAF**"são apresentados os campos para que o usuário informe a URL WebService que será configurada após a instalação do TAF, o Usuário, a Senha e o Código da Filial.

Observações sobre os campos:

**URL Webservice:** Caminho do serviço de acesso ao TAF.

**Usuário:** Usuário para autenticação do  TAF. 

**Senha:** Senha para autenticação do TAF. 

**Código da Filial:** Informar o Código da Filial cadastrada no TAF, este código de filial irá identificar qual é a empresa cadastrada no TAF que receberá as informações da coligada do módulo de Folha de Pagamento.

**OBS:** Ao realizar os testes de instalação com a versão 12.1.17 do TAF, é necessário informar apenas a URL Webservice, o Usuário padrão "admin" e o Código da Filial para realizar a integração, outras validações serão implementadas em releases futuros. 

**Importante! As funcionalidades estão disponíveis no sistema somente a partir da versão 12.1.17.**
