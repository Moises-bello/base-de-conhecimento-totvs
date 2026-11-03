---
article_id: 21678177657367
category: Faturamento - Cadastros
content_hash: 4348b9b109e5e90d4b779fde730e8bace69dbeea4f316624a8ea289011e65b12
fetched_at: '2026-06-28T22:38:36.774342+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento
  Tipo 5
type: support-article
updated_at: '2024-03-04T18:54:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678177657367-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21678177642519) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como criar uma condição de pagamento do tipo 5?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Recomendado para condições de complexidade baixa;

**Exemplo em vídeo de como criar (How To Tutorial):**

Determina-se os dias até o primeiro vencimento, a quantidade de parcelas e a carência entre elas.

![](https://tdn.totvs.com/download/attachments/240310845/551.png?version=2&modificationDate=1664248874943&api=v2)

**Cadastrando:**

E4\_CODIGO = (critério do usuário)

E4\_TIPO = 5

E4\_COND = 30,4,30

![](https://tdn.totvs.com/download/attachments/240310845/a.png?version=2&modificationDate=1664248888810&api=v2)

**Resultado:**

Os pagamentos serão efetuados da seguinte forma:

* 1ª parcela paga 30 dias após a emissão do documento de saída.
* 2ª parcela paga 30 dias após o vencimento da parcela anterior.
* 3ª parcela paga 30 dias após o vencimento da parcela anterior.
* 4ª parcela paga 30 dias após o vencimento da parcela anterior.

**GIF Exemplo do resultado da simulação utilizando uma condição de pagamento Tipo 5 (Tipo 5 - E4\_TIPO = “5”):**

![](https://tdn.totvs.com/download/attachments/240310845/tipo5.gif?version=1&modificationDate=1656449113893&api=v2)

**Saiba mais:**

[**Todas as Condições de Pagamento (MATA360)**](https://tdn.totvs.com/x/PdpSDg)
