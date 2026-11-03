---
article_id: 34946721989143
category: Materiais - Compras (SIGACOM)
content_hash: bd4ede95cd27369e1ef8c5bdcfa4f96c3ccb5df1a6ddf52688c6d994b4d4d10c
fetched_at: '2026-06-28T22:41:09.015835+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Manter dados originais
  da Nota Fiscal ao vincular um pedido de compras no Importador XML - MV_XMLXPED
type: support-article
updated_at: '2025-12-29T18:52:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34946721989143-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Manter-dados-originais-da-Nota-Fiscal-ao-vincular-um-pedido-de-compras-no-Importador-XML-MV-XMLXPED
---

**Dúvida**  
Como manter os dados originais da Nota Fiscal ao vincular um pedido de compras no Importador XML? Ao tentar vincular um pedido de compra numa nota proveniente do Importador XML, o sistema gera o help ***"Para notas provenientes do TOTVS Colaboração o vínculo de pedidos deverá ser feito por item"*** . O que fazer para solucionar esse help.

**Ambiente**  
Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Solução**  
O help em questão é gerado quando o parâmetro **MV\_XMLXPED** está habilitado e existe alguma informação do pedido que está divergente da nota. Sendo assim, para preservar os dados originais da nota, não permite o vínculo e gera o help.

O parâmetro **MV\_XMLXPED** configurado como .T., permite efetuar o vínculo de pedidos de compra por item na classificação da nota de entrada gerada a partir do Monitor do Importador XML (COMXCOL) sem sobrepor os itens originais da nota, assim, é garantida a integridade dos itens das notas recebidas do fornecedor.

Ao utilizar a funcionalidade de vínculo de pedidos por Item de Pedido [F6], ocorrerá a ligação do item do pedido selecionado com o item da nota elegida mantendo as informações originais da nota do fornecedor (Produto, Quantidade, Valor unitário, Valor total). Os demais campos de valores de impostos serão recalculados de acordo com o TES do pedido, se houver, ou o TES informado no momento da classificação.

Na tentativa de utilizar a funcionalidade de vínculo de pedidos por Pedido [F5], é exibida a mensagem “TOTVS Colaboração. Para notas provenientes do TOTVS Colaboração o vínculo de pedidos deverá ser feito por item” evidenciando que esta opção não está disponível para ser utilizada em notas provenientes do TOTVS Colaboração para que os itens da nota não sejam sobrepostos pelos itens do pedido, ou seja, o vínculo deverá ser feito por Item de Pedido.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
