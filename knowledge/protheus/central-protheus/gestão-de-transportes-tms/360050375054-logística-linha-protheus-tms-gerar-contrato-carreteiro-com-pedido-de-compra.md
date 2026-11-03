---
article_id: 360050375054
category: Gestão de Transportes (TMS)
content_hash: 4eb77539fb065a767a79608b4d96c14000f94953f9127d3f99584b12280a1d85
fetched_at: '2026-06-28T22:45:29.250935+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Gerar contrato carreteiro com pedido de
  compra
type: support-article
updated_at: '2025-07-01T18:39:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050375054-Log%C3%ADstica-Linha-Protheus-TMS-Gerar-contrato-carreteiro-com-pedido-de-compra
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33183003261591)***Tempo aproximado para leitura: **00:01:20 min****Dúvida**Como gerar o contrato de carreteiro com pedido de compra no **SIGATMS - Gestão de Transportes**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Este tipo de contrato é utilizado quando o contratado é pessoa jurídica e cobra a transportadora por meio de um documento fiscal.  
  
É necessários verificar os itens:

* O parâmetro **MV\_TMSGRPC - Gera Pedido de Compras**, deve estar configurado com a opção **.T.;**
* No parâmetro **MV\_PRDCTC - Produto para geração do pedido de compras pessoa jurídica**, informar um produto para **pessoa jurídica**, cadastrado na tabela **SB1 - Produtos**;
* No parâmetro **MV\_PRDCTF - Produto para geração do pedido de compras pessoa física**, informar um produto para **pessoa física**, cadastrado na tabela **SB1 - Produtos**.
* **MV\_GERTIT** - Identifica se o Contrato de Carreteiro deverá gerar Contas a Pagar, deve estar configurado com a opção **.T..**

Acesse **Atualizações/Terceiros/Contrato Fornec - TMSA800,** o campo **Gera Ped Co - DUJ\_GERAPC** deve estar definido como **1 - Sim** e no grid, o campo **Ger.Tit.Con. - DVG\_GERTIT** como **2 - Não.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33183003265431)

Após a geração do contrato o sistema gera o pedido de forma automática. É possível consultar o número do pedido visualizando o contrato.  
  
Na aba **Ped. Comp** é possível visualizar os detalhes do pedido.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078559353)
