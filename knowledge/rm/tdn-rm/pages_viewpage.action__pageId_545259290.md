---
content_hash: 0661e93560af7115fa0eab4d9f651c825b848f988034ac43b1416d1e9764212a
fetched_at: '2026-06-29T00:10:38.886791+00:00'
page_id: '545259290'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Web - Acesso a DataServers
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545259290
version: 6
---

Visando proteger os dados de acesso externo e atendendo a lei geral de proteção dos dados(LGPD), optamos por proteger esse acesso através de permissão de perfil de usuário e em alguns casos retirar possibilidade de acesso externo. Segue abaixo maiores informações:

Foi criado a tag de nome '**Acesso Irrestrito aos Dados dos Web Services**' que por padrão virá bloqueada. Ao permitir acesso a esta tag você esta liberando para que o usuário tenha acesso a todos os dados através de WebServices.

AcessoDataServerstrueAcessoPermissão de Acesso |Cadastro de Perfis

Para liberar a permissão de acesso a nova tag criada, acesse o aplicativo de **Globais** através do menu principal clicando em  '**Serviços Globais**'>> Segurança>> **Perfis**.

1. Em **Sistema** selecione '**Incorporação**'.
2. Selecione o perfil desejado e edite.
3. Vá na aba **Acesso a Menus**.
4. Clique em Recolher tudo.
5. Navegue nos menus em: **Incorporação**>> **Incorporação(Portal)**;
6. **WebServices**>> Selecione '**Acesso Irrestrito aos Dados dos Web Services**' e clique em **Permitir acesso**.

Orientamos que libere a permissão de acesso somente para o perfil associado ao usuário que irá fazer o consumo de webservice.

Saiba mais sobre permissões de acesso: [Segurança - Perfis](https://tdn.totvs.com/pages/releaseview.action?pageId=146182940)

MensagensMensagens |Mensagens

Caso a tag não esteja liberada para consumo externo as mensagens abaixo podem ser apresentadas ao tentar consumir o dataserver via webservie.

* O dataserver será retornado vazio.
* Ocorreu um erro ao efetuar a leitura da visão: Não é possível encontrar a tabela 0.
* Ocorreu um erro ao efetuar a leitura da visão: O método ou a operação não está implementada.
* Ocorreu um erro ao efetuar a leitura da visão: Esse DataServer não está disponível via webservice por questões internas de regra de negócio.

Esta funcionalidade esta disponível a partir da versão 12.1.28.
