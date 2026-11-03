---
article_id: 360025656012
category: Originação de Grãos (OG)
content_hash: 16aaed29cc18752ed514b28639b325051a450db28b6cf5a34b8f9227a6632b68
fetched_at: '2026-06-28T22:45:43.365481+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Problema ao confirmar o romaneio
type: support-article
updated_at: '2025-06-17T20:43:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025656012-Agro-Linha-Protheus-AGR-Problema-ao-confirmar-o-romaneio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20593725254423)***Tempo aproximado para leitura: **00:00:50 min****Dúvida**Ao tentar efetuar a confirmação de um romaneio de Devolução de Remessa, na rotina de **Romaneio com Pesagem - OGA250**, não aparecem as notas para selecionar. Como proceder para solucionar esse problema?   
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - A partir da versão 12  
  
**Solução**Esse problema ocorre porque não há saldo nas notas na tabela **SB6** e, certamente, isso aconteceu porque a Entrada para Devolução foi efetuada por meio da rotina **MATA103** em vez de ser efetuada pelo próprio **Originação**, pois se uma **Entrada é efetuada pelo Originação**, a Saída também necessita ser feita dessa forma e vice-versa.
