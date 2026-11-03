---
article_id: 360021565311
category: Materiais - Compras (SIGACOM)
content_hash: 5aff22f32812db6976a7524757785afd64c10a5b6fb4a84f14d0ebcf847813fb
fetched_at: '2026-06-28T22:41:07.432501+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao excluir um Conhecimento
  de Frete pela rotina MATA116, o registro na tabela SF8 não é deletado
type: support-article
updated_at: '2022-05-16T22:07:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021565311-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-excluir-um-Conhecimento-de-Frete-pela-rotina-MATA116-o-registro-na-tabela-SF8-n%C3%A3o-%C3%A9-deletado
---

**Ocorrência**Ao excluir um Conhecimento de Frete pela rotina MATA116, o registro na tabela SF8 não é deletado

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Causa**Esse incidente ocorre quando os campos no dicionário de dados das tabelas SF1 e SF8 possuem diferença de tamanho.

**Solução**Para solucionar essa ocorrência, os campos F1\_FILIAL, F1\_DOC, F1\_SERIE, F1\_FORNECE e F1\_LOJA precisam ter o mesmo tamanho dos campos F8\_FILIAL, F8\_NFDIFRE, F8\_SEDIFRE, F8\_TRANSP, F8\_LOJTRAN, respectivamente.
