---
article_id: 4417323582231
category: Faturamento - Integrações
content_hash: a6c3586722c481e57b06624097285f46aa5e19a8f025fc62172e3c3a26f429f1
fetched_at: '2026-06-28T22:38:26.432272+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - O XML  do pedido
  de vendas não passa para pasta lidos com uso do integrador de XML
type: support-article
updated_at: '2021-12-28T14:07:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417323582231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-O-XML-do-pedido-de-vendas-n%C3%A3o-passa-para-pasta-lidos-com-uso-do-integrador-de-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**  
O que fazer para que o XML do pedido de vendas sai da pasta inn para pasta lidos com uso do integrador de XML?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- a partir da release 12.1.25.  
  
**Solução**

Para que haja a leitura correta do XML pelo Schedule do Configurador, e o xml sai da pasta inn para a pasta lidos é necessário que estejam configurados os dois jobs abaixo em conjunto:

* **Colautoread**: Responsável pela leitura do XML e gravação na **CKO**.(Transfere os registros da pasta IN para a pasta LIDOS).
  + Informar recorrência: Definir o tempo em que os XML serão importados e gravados, o ideal é deixar sempre ativo.
* **MA411JOB**: Job de Importação dos Pedidos de Venda.

Configuração do Schedule:

**Colautoread**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417306599831/mceclip0.png)

**MA411JOB**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417316256535/mceclip1.png)**

**Obs:** O JOB **SCHEDCOMCOL** é para tratamento do Importador XML de nota de entrada, se ele estiver ativo o JOB **Colautoread,** somente haverá importação de XML de documento de entrada, desta forma, mesmo que tenha XML para pedido de venda , só haverá a importação para a pasta lidos , se o JOB **MA411JOB** estiver configurado**.**

**Saiba Mais sobre Importador XML no Faturamento: [Importador XML - Guia de Referência - Faturamento - P12](https://tdn.totvs.com/x/5zzuIw)**
