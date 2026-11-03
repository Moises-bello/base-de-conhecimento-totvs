---
article_id: 360054270134
category: RH - Dissídio
content_hash: 12cdc82164db62af723095d5dad7e9e0ded93d15fa2f6ae6a92956bab0723431
fetched_at: '2026-06-28T22:43:43.308017+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o mnemônico P_LMEDFERD
type: support-article
updated_at: '2025-08-05T19:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054270134-RH-Linha-Protheus-GPE-Como-funciona-o-mnem%C3%B4nico-P-LMEDFERD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16997545336215) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como funciona o mnemônico **P\_LMEDFERD**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
O mnemônico P\_LMEDFERD define como será realizado o cálculo da diferença de médias no dissídio retroativo.  
Caminho rotina **>Atualizações > Definições de cálculos > Mnemônicos (GPEA300)**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093845713)

Para sua parametrização, informa **.T.** ou **.F.**

**-> Mnemônico P\_LMEDFERD = .T.** para definir que na apuração da média de férias no cálculo do dissídio retroativo será aplicado o % de reajuste do dissídio diretamente nas verbas de média de férias, ou seja, não será feito a reapuração das médias de férias no cálculo do dissídio.

-> **Mnemônico P\_LMEDFERD = .F.** será realizada a reapuração das médias , porém as médias só serão reajustadas se as verbas que as geraram na folha original forem reajustadas. Por exemplo, se as médias foram calculadas por conta da existência de determinada verba de Hora Extra, e essa verba de Hora Extra foi reajustada pelo dissídio, as médias também devem ser alteradas. Se as médias foram geradas por conta de uma verba de valor fixo ou lançadas sem cálculo automático do sistema para composição do valor, no cálculo do dissídio, as médias não sofrerão alteração. 

**Saiba Mais**

[RH - Dissidio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
