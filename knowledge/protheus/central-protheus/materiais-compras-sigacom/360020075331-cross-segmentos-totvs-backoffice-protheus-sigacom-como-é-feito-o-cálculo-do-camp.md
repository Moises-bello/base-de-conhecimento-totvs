---
article_id: 360020075331
category: Materiais - Compras (SIGACOM)
content_hash: 1ca29f37b57b8ef2c7960a0496361152b7d5e7c410331b5047cc01c618385ef8
fetched_at: '2026-06-28T22:41:07.628696+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é feito o cálculo
  do campo Data de Entrega (C7_DATPRF) de um Pedido de Compra
type: support-article
updated_at: '2026-02-11T19:19:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020075331-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-feito-o-c%C3%A1lculo-do-campo-Data-de-Entrega-C7-DATPRF-de-um-Pedido-de-Compra
---

**Dúvida**Como é feito o cálculo do campo Data de Entrega (C7\_DATPRF) de um Pedido de Compra  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
  
**Solução**

* Sistema irá carregar informação para o Pedido de compras o campo C7\_DATPRF automaticamente com a Data Base do sistema.
* Incluindo diretamente uma Solicitação de Compras, onde informará conteúdo no campo C1\_DATPRF, sistema carregará este mesmo valor para o campo C7\_DATPRF.

Existe também as parametrizações do F12 da rotina MATA161, onde existe o parâmetro MV\_PAR08, que define como o Pedido será criado.

Data de Entrega Pedido: Informa ao sistema qual data será utilizada para atualização da data de  
entrega (C7\_DATPRF) do pedido de compra.

1= DataBase + Prazo(DEFAULT)  
2= Data Necessidade

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308)
