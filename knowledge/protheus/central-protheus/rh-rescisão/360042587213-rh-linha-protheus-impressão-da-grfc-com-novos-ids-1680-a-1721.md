---
article_id: 360042587213
category: RH - Rescisão
content_hash: ac7d3863e57dfb4afce4eb4cc05400b51322400a649d25db00dd07674c99dbf6
fetched_at: '2026-06-28T22:43:50.958545+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - Impressão da GRFC com novos ID´s 1680 a 1721
type: support-article
updated_at: '2025-06-12T12:09:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042587213-RH-Linha-Protheus-Impress%C3%A3o-da-GRFC-com-novos-ID-s-1680-a-1721
---

**Ocorrência**Para conferir os valores gerados referente a **aviso prévio e multa na GRRF**, é utilizada a impressão da GRFC - (Guia de Recolhimento Rescisório do FGTS e Contribuição Social).

A GRFC não esta considerando os novos Identificadores de calculo, 1680 a 1721.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Causa**A impressão da GRFC utiliza a rotina IMPGRFC.PRX que foi atualizada para considerar os novos IDS:

**Solução**Compile o rdmake IMPGRFC.PRX disponível no link abaixo para as versões anteriores a release 12.1.33:  
<https://suporte.totvs.com/portal/p/10098/download#detail/947506>

Para releases a partir da 12.1.33 o ambiente deve ser atualizado com a expedição contínua, pois o fonte agora é padrão (GPER994):  
<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>
