---
content_hash: b6730a3be1af3966c96480f59570acd64bc13c519c551261783d2d4e88535413
fetched_at: '2026-06-29T00:06:24.278650+00:00'
page_id: '224115681'
product: rm
source: tdn-rm
title: Aplicação RM no Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224115681
version: 123
---

# Aplicação RM no IDENTITY

|  |  |
| --- | --- |
| **Produto:** | IDENTITY |
| **Passo a passo:** | **Objetivo:**  O objetivo deste guia é apresentar como criar as aplicações do RM no Identity.  **Introdução:** Criando a aplicação   Após ingressar no identity, acesse o menu "Ações", "", preencha o campo "" com o nome do aplicativo que deseja criar e clique em . Observações  Para poder criar a aplicação é necessário que o usuário possua a permissão de **"Administrador Corporativo".**     deckSerá exibido um menu  com 3 guias, onde serão cadastrados os dados do aplicativo.  Visão GeralVisão Geral **Guia Visão Geral**  Onde serão inserido os dados básicos da aplicação.   EntrarEntrar **Guia Entrar**  Onde serão preenchido os dados do protocolo de comunicação, e o endereço do servidor que será responsável por responder as requisições de login.       ProvisionarProvisionar **Guia Provisionar**     Observação Quando o provisionamento estiver configurado no modo Push, as alterações realizadas através do IDENTITY são realizadas instantaneamente. Neste modelo é necessário expor a porta HTTP do RM.    Quando o provisionamento estiver  configurado no Modo Pull, as alterações realizadas através do IDENTITY só entrarão em vigor após o processamento da fila do IDENTITY. Neste modelo não é necessário estar com a porta HTTP exposta externamente.   Observações: Para utilizar a integração do RM.exe e Portal RM é necessário criar **uma aplicação para cada sistema**.  Configuração **Modo de Login** de cada aplicação:  **RM EXE :**  **Portal RM :** |

divs
