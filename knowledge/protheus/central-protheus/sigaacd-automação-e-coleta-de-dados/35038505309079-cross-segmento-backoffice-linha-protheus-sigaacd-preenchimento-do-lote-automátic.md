---
article_id: 35038505309079
category: SIGAACD - Automação e Coleta de Dados
content_hash: 6a6fc4b7158a24a7f3eed2aca99c06ef3e382863bc275b21c5d655a21dbe3298
fetched_at: '2026-06-28T22:39:13.761624+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Preenchimento do lote
  automático na rotina ordem de separação ACDV166
type: support-article
updated_at: '2025-09-18T17:31:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35038505309079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Preenchimento-do-lote-autom%C3%A1tico-na-rotina-ordem-de-separa%C3%A7%C3%A3o-ACDV166
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35038485297559) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Utilizamos o **coletor de dados ACD via telnet** para realizar a separação de **Ordem de Separação (OS)**.  
Precisamos que o **lote** seja preenchido automaticamente no momento da separação.  
O lote já está disponível no campo **CB8\_LOTECT**.

Existe algum ponto de entrada que permita trazer essa informação?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35038806189975)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Para que o número do lote seja preenchido automaticamente na separação realizada pelo ACD, é possível utilizar **customização**.

Neste caso, pode-se implementar a lógica no **ponto de entrada A166TELA**, que permite personalizar o comportamento da tela da separação.

Dessa forma, o sistema pode recuperar o valor gravado em **CB8\_LOTECT** e apresentá-lo automaticamente no momento da separação, eliminando a necessidade de digitação manual do lote pelo usuário.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como personalizar a tela da Ordem de Separação (ACDV166)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8906519642007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-personalizar-a-tela-da-Ordem-de-Separa%C3%A7%C3%A3o-ACDV166)

**Saiba Mais**:

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como personalizar a tela da Ordem de Separação (ACDV166)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8906519642007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-personalizar-a-tela-da-Ordem-de-Separa%C3%A7%C3%A3o-ACDV166)
