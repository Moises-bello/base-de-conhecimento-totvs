---
article_id: 20152414287255
category: Portal de Gestão de Capital Humano
content_hash: 51e69338da109d88f4a85b25dfd15ce18053bdb8fce026e9d7935aaf1325054a
fetched_at: '2026-06-28T22:42:59.004179+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - Portal GCH - O parâmetro MV_DFECHAD bloqueia solicitações
  de abono
type: support-article
updated_at: '2023-12-27T20:02:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20152414287255-RH-Linha-Protheus-Portal-GCH-O-par%C3%A2metro-MV-DFECHAD-bloqueia-solicita%C3%A7%C3%B5es-de-abono
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20152414209175) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O parâmetro MV\_DFECHAD bloqueia solicitações de abono  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão Capital Humano - Todas as versões  
  
**Solução**O parâmetro **MV\_DFECHAD** tem referência ao Portal GCH, no que tange ao **bloqueio apenas das marcações de Ponto Eletrônico**, ele estabelece a quantidade de dias que o período de apontamento ficará fechado para manutenção, após o término do parâmetro MV\_DABERTO.  
  
Exemplo:  
Período **01/11/2023 A 30/11/2023**  
**MV\_DABERTO = 20**  
**MV\_DFECHAD = 11**  
  
Dos dias **01/12/2023 a 20/12/2023**, o sistema deverá permitir a inclusão da marcação de ponto e dos abonos, e de 21/12/2023 a 31/12/2023, o período estará **fechado para manutenção das marcações de ponto**, no Portal GCH  
  
**Para solicitações de abono, o Sistema não irá realizar o bloqueio**, apenas com a rotina de Marcação de Ponto.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20152465461015)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20152465467671)  
  
**Saiba Mais  
[Artigos Sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)**
