---
article_id: 4407151582231
category: Materiais - Compras (SIGACOM)
content_hash: e90c128f26f4c36406a80538e62f6f4c10c19123c04ba1089d4a971e0d47b155
fetched_at: '2026-06-28T22:41:25.410787+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Valor unitário diferente
  entre a devolução de venda e sua venda original '
type: support-article
updated_at: '2021-08-26T15:06:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407151582231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Valor-unit%C3%A1rio-diferente-entre-a-devolu%C3%A7%C3%A3o-de-venda-e-sua-venda-original
---

**Dúvida** Valor unitário diferente entre a devolução de venda e sua venda original

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS  Gestão de Compras - Todas as versões  
  
**Solução**

Em determinadas situações em uma devolução de Venda feita com Desconto o Valor Unitário dessa Entrada pode ficar diferente do Valor Unitário da Saída.

O processo na entrada de uma devolução de venda, onde há tabela de preço e desconto na venda ocorre da seguinte forma:  
  
*Ao dar entrada no documento de devolução, a rotina fará um cálculo* ***(D2\_TOTAL + D2\_DESCON / D2\_QUANT),*** para descobrir o valor unitário (***D1\_VUNIT***) que deverá ser gravado, o essencial nesse caso é que o valor total da nota de entrada bata com o valor total da nota de saída.  
  
Nessa situação no tocante à valores unitários o processo da Entrada é diferente ao processo de Saída.

***Saiba Mais :***

[PÁGINA](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS) [CENTRALIZADORA](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS) [DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
