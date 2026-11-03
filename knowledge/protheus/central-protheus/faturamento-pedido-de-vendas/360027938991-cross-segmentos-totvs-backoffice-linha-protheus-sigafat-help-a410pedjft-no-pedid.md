---
article_id: 360027938991
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 60245d4db36c69de93632311d74554a33991e53f31d6a95f96275b4b90bd0531
fetched_at: '2026-06-28T22:38:41.137458+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help A410PEDJFT
  no Pedido de Vendas (MATA410)
type: support-article
updated_at: '2022-09-14T17:20:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027938991-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410PEDJFT-no-Pedido-de-Vendas-MATA410
---

**Ocorrência**

O sistema apresenta o Help A410PEDJFT na inclusão/alteração de um pedido.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da versão 11.80.  
  
**Solução**

O Help **A410PEDJFT** indica que a quantidade que está tentando inserir no pedido (**C6\_QTDVEN**) é menor do que a quantidade já faturada neste pedido (**C6\_QTDENT**).

* **Na Alteração do Pedido**:  
  Ao tentar alterar um pedido **faturado parcialmente**, caso ele tente diminuir a quantidade (**C6\_QTDVEN**) para um número **menor** que o já faturado (**C6\_QTDENT**), o sistema exibe o Help A410PEDJFT informando que a quantidade informada no pedido não pode ser menor que a quantidade faturada.  
  Neste caso a quantidade (C6\_QTDVEN) precisa ser maior ou igual à quantidade já faturada (C6\_QTDENT).
* **Na inclusão do Pedido**:  
  Verifique se o número do pedido que está alterando já existe em seu sistema, caso ocorra algum problema de numeração, o sistema pode sugerir uma numeração que já existe na base.   
  Faça um teste alterando o número do Pedido manualmente para a numeração correta (número que seja superior ao maior já incluído na base). E só então, registre no grid o produto e quantidade.  
  Caso esteja com um problema na numeração automática dos pedidos realize o procedimento da FAQ publicada no TDN: **[FAT0046 Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/x/P4YKDg)**
