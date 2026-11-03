---
article_id: 360052192973
category: BI - Business- Intelligence - Workflow
content_hash: 582487f9ebaa93e80a0abf1e03c57021aac29f4b18cb48a8de83edbd3b4b0e88
fetched_at: '2026-06-28T22:37:03.052829+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Lentidão ao disparar
  a lista de e-mails do processo de Workflow
type: support-article
updated_at: '2022-07-27T18:27:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052192973-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Lentid%C3%A3o-ao-disparar-a-lista-de-e-mails-do-processo-de-Workflow
---

**Ocorrência**O Disparo de Workflow da empresa está abrindo um processo de envio para cada conta de e-mail da lista de contatos. Tal ação está demandando muitas horas de processamento.  
Como proceder para que o envio se torne único para todos os e-mails listados?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – Workflow – A partir da versão 12.1.17  
  
**Causa**A lentidão ocorre pois a forma de envio dos e-mails do Workflow está configurada como **"Individualmente"** dentro Configurador do Protheus. Desta forma, é criado um processo por vez de disparo para cada conta dentro da lista.  
  
**Solução**Neste caso, quando existe uma lista de e-mails para disparo, o ideal é alterar a forma de envio para **"Em Lote"** dentro do Configurador do Protheus, criando apenas um processo que enviará o mesmo e-mail para todas as contas cadastradas da lista.  
Para alterar esta configuração, acesse o **Configurador** e dentro da Aba **"Workflow"**, escolha a opção **"Parâmetros de Workflow"**. Será apresentado as duas opções de envio: **1-Em Lote** ou **2-Individualmente**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081999773/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080903934/mceclip0.png)
