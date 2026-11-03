---
article_id: 22544038642071
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8909eb3fd26a90703822a238ef3f4ee4619b65dba6587e79ef487388d56ab17c
fetched_at: '2026-06-28T22:38:39.763240+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Desconto no rodapé do pedido
  de venda (MATA410)
type: support-article
updated_at: '2024-04-04T12:41:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22544038642071-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Desconto-no-rodap%C3%A9-do-pedido-de-venda-MATA410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22544084790039) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como saber de onde vem o desconto do rodapé do pedido de venda?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**É possível visualizar os descontos do pedido de venda pelo rodapé:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22544038605719)

**Caso não esteja conseguindo identificar de onde vem o desconto, cheque:**

**1 -** Veja se há preenchimento dos campos de desconto de indenização:

* "%Indenizacao (C5\_PDESCAB)"
* "Indenizacao (C5\_DESCONT)"  
    
  OBS 1: (Não levam valor aos campos "Valor desconto (C6\_VALDESC)" e "% Desconto (C6\_DESCONT)" mas conta como desconto no rodapé).

**2 -** Veja se há preenchimento nos campos de desconto em cascata do cabeçalho:

* "Desconto (C5\_DESC/1/2/3/4)"

**3 -** Veja se há preenchimento no desconto dos itens:

* "Valor desconto (C6\_VALDESC)"
* "% Desconto (C6\_DESCONT)"

**4 -** Veja se o parâmetro "MV\_NDESCTP' está falso. Se estiver, é considerado desconto (nos campos do tópico 3) a diferença entre o "preço de lista (C6\_PRUNIT)" e o "preço de venda (C6\_PRCVEN)".

OBS 2: Veja se a decimais dos campos "preço de lista (C6\_PRUNIT)" e o "preço de venda (C6\_PRCVEN)" são iguais, se não forem, essa diferença das decimais podem ser levadas como desconto, exemplo:

* MV\_NDESCTP = .F.
* "Preço de lista (C6\_PRUNIT)" = 100.00335
* "Preço de venda (C6\_PRCVEN)"C6\_PRCVEN = 100.00

**Resultado:** Desconto no rodapé do pedido de vendas no valor "R$0.00335" por conta subtração (C6\_PRUNIT - C6\_PRCVEN).

**Saiba mais:**

[FAT0035 - Descontos, acréscimos e arredondamentos no Faturamento](https://tdn.totvs.com/x/KE1tDQ)

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Funcionamento do parâmetro MV\_NDESCTP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019243511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-NDESCTP)
