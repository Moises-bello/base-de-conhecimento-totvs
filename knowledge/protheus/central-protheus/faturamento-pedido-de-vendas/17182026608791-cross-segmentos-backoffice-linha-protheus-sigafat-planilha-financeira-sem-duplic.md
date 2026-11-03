---
article_id: 17182026608791
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5a69a14495fe2894e08b11decab0ed339ef70d717dcfdb47201b618b2630ecb7
fetched_at: '2026-06-28T22:38:42.509682+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Planilha financeira
  sem duplicatas ao usar condição de pagamento tipo B
type: support-article
updated_at: '2023-08-31T19:07:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17182026608791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Planilha-financeira-sem-duplicatas-ao-usar-condi%C3%A7%C3%A3o-de-pagamento-tipo-B
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17182019236119) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**No pedido de venda a planilha financeira está sem duplicatas ao usar condição de pagamento tipo B, como solucionar?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**Esse caso é muito comum quando é alterado a tabela SE4 do padrão de "Exclusivo" para "Compartilhado" porém não é realizado a mesma coisa na tabela SEC, que é responsável pela condição de pagamento do tipo B, também de "Exclusivo" para "Compartilhado".

Ao criar uma condição de pagamento com a tabela SE4 compartilhada, de dentro da filial 01 e, incluir um pedido de venda na filial 2, pela planilha financeira as duplicatas não estarão disponíveis.

Para solucionar isto, contate seu DBA para realizar a manutenção da tabela SEC, tornando-a "Compartilhada" assim como a tabela SE4, caso a SE4 seja compartilhada.
