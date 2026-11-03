---
article_id: 360025597911
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: 050ed04340f90c047f6ce1987b21f5acdbb5bba8e581375e62a392ff6ff7adc8
fetched_at: '2026-06-28T22:40:34.158492+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: MP - SIGACTB - ERRORLOG NA INCLUSÃO DO LANÇAMENTO PADRÃO (O campo CT5_EC05DB
  refira à pasta:7)
type: support-article
updated_at: '2021-04-28T15:25:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025597911-MP-SIGACTB-ERRORLOG-NA-INCLUS%C3%83O-DO-LAN%C3%87AMENTO-PADR%C3%83O-O-campo-CT5-EC05DB-refira-%C3%A0-pasta-7
---

**Ocorrência**

Na inclusão de lançamento padrão retorna errorlog:

campo CT5\_EC05DB refira à pasta:7, mas não existe. on FWFORMFIELD:PREPAREFIELDS

**Ambiente**  
Protheus – Contabilidade gerencial – A partir da versão 12  
   
 **Causa**

Este incidente ocorre porque na estrutura da (SX3) a coluna X3\_FOLDER do campo CT5\_EC05DB está direcionado para a pasta 7, que não existe na estrutura da pasta (SXA)

**Solução**Para solucionar essa ocorrência executar o UPDDISTR com SDF e SXS atualizados.
