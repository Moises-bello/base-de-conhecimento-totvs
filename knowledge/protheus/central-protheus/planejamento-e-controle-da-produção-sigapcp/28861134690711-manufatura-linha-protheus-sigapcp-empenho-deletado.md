---
article_id: 28861134690711
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 289989296ad5788ba1d0d9133e4d81f163129a2a64eda1a0ec7e980bae2e30ad
fetched_at: '2026-06-28T22:42:42.240327+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Empenho deletado
type: support-article
updated_at: '2025-01-23T11:11:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28861134690711-Manufatura-Linha-Protheus-SIGAPCP-Empenho-deletado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28861103247255) Tempo aproximado para leitura: **00:00:58 min** **Dúvida**Ao incluir uma **OP - Ordem de Produção** na rotina **MATA650 - Ordens de Produção**, mesmo o produto da OP possuindo estrutura, os empenhos estão deletado. Por quê isso ocorre?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Todas as versões  
  
**Solução**

O empenho pode vir deletado por alguns fatores, dentre eles os mais habituais são:

1 . O componente não ser válido, porque a data de início prevista para a OP, registrada no campo **C2\_DATPRI - Previsão Ini** está fora dos valores especificados nos campos **Dt Inicio** e **Dt Fim** no cadastro da estrutura na rotina **PCPA200 - Estrutura**;

2. A **OP** foi aberta para uma determinada revisão e o componente não é valido nesta revisão.
