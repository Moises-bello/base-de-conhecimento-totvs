---
article_id: 360019180652
category: NFe - Nota Fiscal Eletrônica
content_hash: e8c8ffd3c90ad668e64ce992f6a99eb0da1cc34748d6f11d07173bdd260b71ac
fetched_at: '2026-06-28T22:40:06.874328+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Impressão de Carta
  de Correção Eletrônica ( CCe / CC-e)
type: support-article
updated_at: '2025-08-12T00:51:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019180652-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Impress%C3%A3o-de-Carta-de-Corre%C3%A7%C3%A3o-Eletr%C3%B4nica-CCe-CC-e
---

## **01.  VISÃO GERAL.**

Essa documentação visa apresentar o processo de configuração do parâmetro MV\_CCEPDF, assim como o envio da carta de correção em .PDF via e-mail pelas interfaces: TSSMANAGER, TSSMONITOR e TSSINTERFACE.

## **02. Configurar parâmetro**

**Configuração do parâmetro utilizando o TSSMANAGER.**

| Ação | Descrição |
| --- | --- |
| Acesse a rotina *TSSMANAGER.* |  |
| Acesse o menu *configurar.* |  |
| Altere o valor conforme sua necessidade. |  |
| Clique em *Confirmar* e salve os parâmetros. |  |
| Parâmetro salvo. |  |

## **03.  Envio da carta de correção em .PDF**

**Enviando a carta de correção pelo TSSMONITOR.**

| Campo | Descrição |
| --- | --- |
| Campo | Descrição |
| --- | --- |
| Acesse a rotina *TSSMONITOR.* |  |
| Acesse a Rotina*Nf-e* em *Eventos.* |  |
| Preencha o filtro conforme seus documentos de carta de correção. |  |
| Selecione o documento desejado e através do menu de *outras ações* selecione *Enviar E-mail.* |  |
| Preencha conforme as suas informações e clique em enviar.  **Importante:**Caso seja marcado o checkbox *Anexar Cc-e PDF* o e-mail será enviado  ignorando o parâmetro MV\_CCEPDF. |  |
| Na opção *Reenviar E-mail* o comportamento segue o que for configurado  no parâmetro MV\_CCEPDF. |  |

## **04.  TABELAS UTILIZADAS**

* SPED000 ( Parâmetros).
