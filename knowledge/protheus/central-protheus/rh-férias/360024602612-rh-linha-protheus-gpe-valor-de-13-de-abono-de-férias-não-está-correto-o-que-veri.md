---
article_id: 360024602612
category: RH - Férias
content_hash: 02e8e5772442e0786a7ed4cd6cabd16e0a8f90ee1726ceb28785f6c50b725e7b
fetched_at: '2026-06-28T22:43:59.254331+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Valor de 1/3 de abono de férias não está correto
  o que verificar
type: support-article
updated_at: '2025-08-28T18:27:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024602612-RH-Linha-Protheus-GPE-Valor-de-1-3-de-abono-de-f%C3%A9rias-n%C3%A3o-est%C3%A1-correto-o-que-verificar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31453075762199)Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**O valor de 1/3 de abono de férias não está correto, o que deve ser verificado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O valor de 1/3 de abono de férias não ficará correto quando houver no calculo das férias verbas informadas(Geradas) pelo usuário e está verba não ter identificador de calculo.

Sistema irá somar o valor da verba informado no calculo das férias e não no calculo de 1/3 de abono, por não ter identificador, sistema não tem como realizar a separação do valor em férias e abono.

No padrão o sistema não consegue realizar a separação pois a verba auxilio moradia não tem identificador de calculo.  
  
As verbas informadas neste momento, e que não possuem identificador de cálculo, e que possuem a configuração do campo **'Ref. Férias' (RV\_REFFER)** como '**Sim**', irão compor o salário do funcionário ref. ao cálculo de Férias.

**Saiba Mais**

[RH - Linha Protheus - GPE - Recibo de férias com abono](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053273833-RH-Linha-Protheus-GPE-Recibo-de-f%C3%A9rias-com-abono)  
[RH - Linha Protheus - GPE - Como alterar a data de pagamento das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063518933-RH-Linha-Protheus-GPE-Como-alterar-a-data-de-pagamento-das-f%C3%A9rias)  
[RH - Linha Protheus - GPE - Cálculo de abono pecuniário antes ou depois dos dias de Gozo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023266111-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-abono-pecuni%C3%A1rio-antes-ou-depois-dos-dias-de-Gozo-das-f%C3%A9rias)
