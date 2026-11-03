---
content_hash: a065b96d9ae7e982baeb42c0723df772c4d0da0a3c3ab1a54fa11e60407dc0d7
fetched_at: '2026-06-29T00:08:06.986672+00:00'
page_id: '236599965'
product: rm
source: tdn-rm
title: DT_FRAME_HTML_-_NOTIFICATION_E_REPORTS
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_FRAME_HTML_-_NOTIFICATION_E_REPORTS
version: 115
---

# [REQ-10084](http://jira.totvs.com.br/browse/PDR_FRW_FRW002-211)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Framework* |
| **Módulos:** | *Lib, Rpt e Con* |
| **Requisito (ISSUE):** | [PCREQ-10031](http://jira.totvs.com.br/browse/PVR_R_V12-499?jql=cf%5B10500%5D%20%3D%20PCREQ-10087) |

## Descrição

      Mecanismo para a execução de processos e relatórios via THF (totvs-html-framework) com integração com o Fluig. Esse mecanismo também proporciona a integração com qualquer sistema, visto que foi implementado utilizando um serviço RESTful.

      Com essa mudança, teremos os seguintes benefícios:

* Será possível agendar a execução de processos em aplicativos criados com o THF (TOTVS HTML Framework).
* A execução de relatórios também será disponibilizada via THF.
* Qualquer aplicativo que suporte comunicação via HTTP e que construa mensagens no padrão definido pelo THF poderá agendar a execução de processo e relatórios do CorporeRM.
* Os relatórios produzidos pelo novo gerador poderão ser exportados diretamente para o GED.
* Poderá ser enviado notificações para o Fluig quando da execução de qualquer processo no CorporeRM.

## Importante

**Para maiores detalhes sobre as implementações a serem feitas, favor acessar o documento de especificação: <http://tdn.totvs.com/display/LRM/ER_PCREQ-10087_FRAME_HTML_-_NOTIFICATION_E_REPORTS>**

divs
