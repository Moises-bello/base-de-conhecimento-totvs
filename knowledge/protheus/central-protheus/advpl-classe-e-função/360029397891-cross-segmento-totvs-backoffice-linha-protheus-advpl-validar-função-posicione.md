---
article_id: 360029397891
category: ADVPL - Classe e Função
content_hash: ee68e9bbaecffb4a9d2597665d5a91e4f5e314dbab586f83ac1d280df10c6760
fetched_at: '2026-06-28T22:40:18.207476+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Validar função Posicione
type: support-article
updated_at: '2025-12-22T12:51:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029397891-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Validar-fun%C3%A7%C3%A3o-Posicione
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: ***00:05:00 min*** **Dúvida**Estou usando a função posicione e a descrição do primeiro item e replica para os demais.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030702611/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**

Neste caso o índice não consegue diferenciar o item posicionado.

Para validar a utilização do posicione primeiramente é verifique se o índice existe e se as chaves estão corretas, uma outra opção é criar uma user function e debugando a função verifique se os valores do parâmetro utilizado na **[Posicione](http://tdn.totvs.com/pages/viewpage.action?pageId=25165872)**estão corretos ***"XFILIAL("SA1") + SC9->C9\_CLIENTE + SC9->C9\_LOJA"*** valide chumbando os valores ***"'01' +  '000001' + '01'"***

***Posicione("SA1",1,XFILIAL("SA1") + "000001" + "01", "A1\_NOME")***

```
User Function VLDPosicione  
local cNome  := "  
  
DbSelectArea("SA1")  
SA1->(DbSetOrder(1))  
  
cNome  := Posicione("SA1",1,XFILIAL("SA1") + "CLI000" + "01", "A1_NOME")  
  
Return cNome
```

**obs**.: Valido para todas versões do protheus.
