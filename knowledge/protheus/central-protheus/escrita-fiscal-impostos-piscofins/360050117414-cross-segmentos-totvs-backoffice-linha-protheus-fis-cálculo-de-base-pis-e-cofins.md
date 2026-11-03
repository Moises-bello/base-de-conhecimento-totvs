---
article_id: 360050117414
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: db7f06e27e8aaa88381679375e6758c210bfaf41eb422d8a9e9fbf04242216e0
fetched_at: '2026-06-28T22:39:36.866019+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Cálculo de base PIS
  e COFINS para veículos usados.
type: support-article
updated_at: '2021-06-22T13:25:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050117414-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-base-PIS-e-COFINS-para-ve%C3%ADculos-usados
---

**Dúvida**Como calcular a base do PIS e da COFINS sobre o lucro na venda do veículo via pedido de venda?  
  
**Ambiente**Protheus – Faturamento – A partir da versão 11.80.  
  
**Solução:**

Segue o passo a passo para calcular diferença do valor de compra para  
o valor de venda de veículos usados.  
  
MV\_CALCVEI = .T.

Utilizar um produto via documento de entrada preenchendo o número do CHASSI (B1\_CHASSI):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076302794/mceclip0.png)

Lançar uma nota de entrada com cálculo de PIS e COFINS no valor do veículo (exemplo: 10.000,00)

Gerar um pedido de venda no valor de 15.000,00 e clicar em outras ações -> veículo -> relacionar a nota de entrada.

(Ao clicar nesta opção, será apresentada a NF que foi lançada no Documento de entrada.)  
  \* Neste momento o campo V.Tot.NF.Ent(C6\_BASVEIC) será preenchido com o valor da NF de entrada.  
  
  Após relacionar o Documento de entrada com o Pedido de venda, o valor da base do PIS/COFINS **ainda não trará a diferença.**  
  
  Somente após confirmar o Pedido de venda e em seguida visualizar lo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077465453/mceclip1.png)

Boletim técnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=6076150>
