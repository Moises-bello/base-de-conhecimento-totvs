---
article_id: 360000583388
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: eccd2d2ca55fa99a44a743a9bc7e19490d0f79dae5ec743421b98cf5a1fcb633
fetched_at: '2026-06-28T22:38:45.113508+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT- Como utilizo ExecAuto
  para preparação da nota de saída
type: support-article
updated_at: '2026-05-17T13:30:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583388-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-utilizo-ExecAuto-para-prepara%C3%A7%C3%A3o-da-nota-de-sa%C3%ADda
---

**Dúvida**Como utilizo ExecAuto para preparação da nota de saída ?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT -todas as versões.  
  
**Solução**

A rotina de preparação de documento de Saída (**Mata460a/Mata461**)possui um execauto desenvolvido recentemente através da função **MANFS2NFS**, utilizada para a geração do Documento Fiscal de Saída a partir de um Documento Fiscal de Origem. conforme Documento Técnico : **[MANFS2NFS - Geração automática de Documento Fiscal de Saída (ExecAuto)](https://tdn.totvs.com/x/lZoIIg)**

Também foi implementado o execauto para geração da nota  através do pedido de venda, **MAPVLNFS**, função utilizada para a geração do **Documento Fiscal de Saída** a partir de itens do **Pedido de Venda,** conforme Documento Técnico**:  [MAPVLNFS - Geração de Documento de Saída a partir de itens do Pedido de Venda](https://tdn.totvs.com/x/gEt5Ig)**

**IMPORTANTE :**A função **MaPvlNfs** não é responsável por validar os bloqueios dos itens liberados (**SC9**). Desta forma, a customização se torna responsável pela verificação dos bloqueios de **Estoque** (**C9\_BLEST**) e **Crédito** (**C9\_BLCRED**), conforme regra de negócio implementada pelo desenvolvedor.
