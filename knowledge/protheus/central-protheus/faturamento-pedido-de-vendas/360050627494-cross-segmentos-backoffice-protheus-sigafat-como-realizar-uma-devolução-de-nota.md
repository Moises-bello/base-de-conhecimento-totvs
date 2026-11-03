---
article_id: 360050627494
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8ac365ec1cc4a33a8f744271fb3d57a486a8a8114c578108f87dda2843b5227e
fetched_at: '2026-06-28T22:38:39.732001+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como realizar uma Devolução
  de Nota com Complemento de Preço na entrada
type: support-article
updated_at: '2026-03-05T18:21:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050627494-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-realizar-uma-Devolu%C3%A7%C3%A3o-de-Nota-com-Complemento-de-Pre%C3%A7o-na-entrada
---

**Dúvida**

Como realizar uma Devolução de Nota com Complemento de Preço na entrada?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Para realizar a devolução de uma compra que possui uma Nota Fiscal de Complemento vinculada na entrada, é necessário realizar a devolução de cada item separadamente no Pedido de Vendas (uma linha para a nota de compra original e outra linha para a nota de complemento).  
  
1 - O Tipo de Pedido continuará a ser D;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079015013)

2 - Para a linha referente à NF de Complemento, utilize uma TES com o campo Qtd. Zerada (`F4_QTDZER`) configurado como "1 - Sim";

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102153453)​

3 - Caso o valor ou a quantidade a ser devolvida seja diferente do total da nota original, é necessário validar os campos de divergência para que o sistema realize o vínculo corretamente:

* **D1\_VALDEV:** Preencha com o valor exato que está sendo devolvido (caso seja parcial).
* **D1\_QTDEDEV:** Preencha com a quantidade exata que está sendo devolvida.

**Observação:** O preenchimento correto dos campos `D1_VALDEV` e `D1_QTDEDEV` é essencial para que o saldo da nota de entrada seja baixado corretamente (isso vale para qualquer tipo de devolução de compras).

**Saiba mais:**

* [Configuração e informações sobre a devolução de uma nota de compra](https://tdn.totvs.com/x/g0FtDQ)
