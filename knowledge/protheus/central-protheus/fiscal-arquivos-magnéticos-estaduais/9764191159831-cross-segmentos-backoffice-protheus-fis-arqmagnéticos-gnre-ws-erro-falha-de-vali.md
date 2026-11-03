---
article_id: 9764191159831
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 81e301e7302f25b3d51a1e8020aecbafd8feeed1fb70a61cc2a10b42c114c370
fetched_at: '2026-06-28T22:42:11.706481+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - ERRO:
  Falha de validação do schema TDadosGNRE'
type: support-article
updated_at: '2022-10-25T18:28:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9764191159831-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-ERRO-Falha-de-valida%C3%A7%C3%A3o-do-schema-TDadosGNRE
---

**Ocorrência** **GNRE WS** - Como corrigir o **ERRO: Falha de validação do schema TDadosGNRE ?**  
**Ambiente**TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão **12.1.25**.  
  
**Causa**Esse incidente ocorre, pois a versão da GNRE usada esta errada na configuração da rotina **FISA095**  
  
**Solução**Altere na rotina **FISA095** (opção **AMBIENTE**) a versão usada para **2.0** :

![](https://totvssuporte.zendesk.com/attachments/token/9sKQCtpMwhRCXYtYuWLJOXTQW/?name=image.png)

Obs. A versão 1.0 foi descontinuada pelo portal gnre.  
  
Segue abaixo documentação completa da rotina:

<https://tdn.totvs.com/display/public/PROT/GNREWS+-+Guia+Nacional+de+Recolhimento+de+Tributos+Estaduais+via+Webservice>
