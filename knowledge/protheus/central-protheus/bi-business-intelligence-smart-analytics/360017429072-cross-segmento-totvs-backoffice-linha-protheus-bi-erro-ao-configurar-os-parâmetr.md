---
article_id: 360017429072
category: BI - Business Intelligence - Smart analytics
content_hash: 8a25bacb137e8aea91c7b87467111e1e8275ce3d538095f118c3b2efd52eeaef
fetched_at: '2026-06-28T22:37:04.178806+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Erro ao configurar
  os parâmetros do extrator bi
type: support-article
updated_at: '2022-07-27T18:15:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017429072-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Erro-ao-configurar-os-par%C3%A2metros-do-extrator-bi
---

**Dúvida**Como corrigir o erro: "*Alias does not exist:SYA* " ao configurar os parâmetros do BI?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – BI – A partir da versão 11.80  
  
**Solução**Este incidente ocorre, quando é realizado um apontamento para um banco e posteriormente este banco fica indisponível.  
Para a sua correção, é necessário a Limpeza dos dados da tabela **HYN** via **APSDU** do Banco de Dados do Protheus, para que assim possa configurar novamente o acesso ao banco.
