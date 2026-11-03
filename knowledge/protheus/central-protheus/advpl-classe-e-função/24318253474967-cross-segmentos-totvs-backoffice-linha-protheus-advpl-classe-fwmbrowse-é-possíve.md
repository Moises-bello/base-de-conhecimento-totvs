---
article_id: 24318253474967
category: ADVPL - Classe e Função
content_hash: 7ebe07f89c25780bbd33290bb0680452edfa67b2101460b628e0909ce53e841d
fetched_at: '2026-06-28T22:40:21.656913+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL- Classe FWMBrowse
  - É possível alterar a cor da linha de fundo do texto ou da fonte?
type: support-article
updated_at: '2024-06-21T13:07:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24318253474967-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWMBrowse-%C3%89-poss%C3%ADvel-alterar-a-cor-da-linha-de-fundo-do-texto-ou-da-fonte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24318253435799) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível alterar a cor da linha de fundo do texto ou da fonte utilizando algum método da classe FWMBrowse?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Solução**

A classe *FWMBrowse*possui um método para alterar a cor da fonte e outro para alterar a cor da linha de fundo do texto. São eles:

SetBlkBackColor -> Indica a cor de fundo para a linha atual.

SetBlkColor -> Indica a cor de fonte para a linha atual.

**Exemplo**

```
[...]  
  
bColor := ({||CLR_BLACK})  
oBrowse:SetBlkBackColor(bColor)  
  
  
bColor1 := ({||CLR_GREEN})  
oBrowse:SetBlkColor(bColor1)  
  
[...]
```

![Gravar_2024_06_20_14_34_22_179.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24318274525335)

**Saiba Mais**

[FWMBrowse](https://tdn.totvs.com/display/public/framework/FwBrowse)
