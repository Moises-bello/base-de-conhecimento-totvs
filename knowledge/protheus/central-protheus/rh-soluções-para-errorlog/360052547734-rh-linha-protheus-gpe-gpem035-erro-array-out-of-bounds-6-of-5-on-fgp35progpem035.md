---
article_id: 360052547734
category: RH - Soluções para error.log
content_hash: a17abaf1c3a31d136d16115f7a49fe75f4a4b74981be4823afdd70fff67aa658
fetched_at: '2026-06-28T22:44:08.942704+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - GPEM035 - Erro: Array out of bounds [6] of [5]  on
  FGP35PRO(GPEM035.PRW) 30/04/2020 16:22:40 line : 1396'
type: support-article
updated_at: '2025-08-22T18:08:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052547734-RH-Linha-Protheus-GPE-GPEM035-Erro-Array-out-of-bounds-6-of-5-on-FGP35PRO-GPEM035-PRW-30-04-2020-16-22-40-line-1396
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34377767993623)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**No módulo SIGAGPE, ao tentar realizar a rotina GPEM035 ocorre inconsistências no eSocial gerando error log: ***Array out of bounds [6] of [5] on* FGP35PRO(GPEM035.PRW) 30/04/2020 16:22:40 line : 1396.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal– A partir da versão 12.  
  
**Causa**Esse incidente ocorre pois existem inconsistências no complemento cadastral do SIGATAF tabelas C1E e CR9.  
  
**Solução**Verifique na rotina TAFA050 a configuração do complemento cadastral que mais se enquadre no seu cenário conforme documentações abaixo:  
  
TAF - SIGATAF - Complemento cadastral (TAFA050) - Mudança da amarração de N:1 para 1:1  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996074](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996074&sa=D&source=hangouts&ust=1598118724976000&usg=AFQjCNEBK9UBFmUeiedzEsIIpBK23Yd1Ig)     
  
TAF - SIGATAF - Complemento cadastral (TAFA050) - Amarração 1:1  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043508233](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043508233&sa=D&source=hangouts&ust=1598118724976000&usg=AFQjCNH7z2iSK_nswg286GGzWrIsTUBoew)     
  
**Saiba mais  
[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**
