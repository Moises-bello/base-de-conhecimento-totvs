---
article_id: 360025359392
category: Materiais - Compras (SIGACOM)
content_hash: ac2d5c5833cd658bc60b8dc24ce0f0779717ca945aef5e4316c9141e9b9013f7
fetched_at: '2026-06-28T22:41:08.900160+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A100NOCLAS ao
  tentar excluir um Documento de Entrada (MATA103)
type: support-article
updated_at: '2022-05-12T21:19:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025359392-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A100NOCLAS-ao-tentar-excluir-um-Documento-de-Entrada-MATA103
---

**Ocorrência**Help **A100NOCLAS** ao tentar excluir um Documento de Entrada (MATA103)

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Causa**

No módulo Compras, ao excluir uma nota fiscal através da rotina Documento de Entrada (MATA103) é apresentado o assistente **A100NOCLAS**.

Esse incidente ocorre pois a nota a ser excluída não foi classificada.  
  
**Solução**Para notas não classificadas a exclusão deverá ser realizada pela rotina Pré-nota de entrada (MATA140).
