---
article_id: 4412257148055
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: a66d71175b68da6298ae5f364c8b3e3a01d2ca920b96800014d836748e67a479
fetched_at: '2026-06-28T22:39:44.509441+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem: Um
  ou mais campos obrigatórios não foram preenchidos Vlr R$'
type: support-article
updated_at: '2021-11-04T20:50:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412257148055-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Vlr-R
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **01:30 min****Ocorrência**Ao tentar gravar o **Adiantamento de P.O.** dentro do **Controle de Cambio (EICAP100)**, o sistema retorna a seguinte mensagem: **Um ou mais campos obrigatórios não foram preenchidos. Vrl R$. Falha na gravação automática do Título!**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412243675543/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Causa**A mensagem é apresentada pois não foi encontrado dentro do Módulo Financeiro (SIGAFIN) rotina Cotação **(MATA090),** a cotação do dia para a moeda utilizada no processo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412256185367/mceclip1.png)  
 **Solução**Neste caso, será necessário cadastrar a cotação do dia para a moeda utilizada dentro do Módulo Financeiro rotina MATA090, após tal ação refazer o Adiantamento da PO.  
  
**Saiba mais**  
[Pagamento Antecipado para a P.O.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000091867-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Pagamento-antecipado-para-a-purchase-order?source=search)
