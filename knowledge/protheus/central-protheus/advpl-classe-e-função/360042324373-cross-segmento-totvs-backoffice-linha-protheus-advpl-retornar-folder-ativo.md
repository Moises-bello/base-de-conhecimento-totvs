---
article_id: 360042324373
category: ADVPL - Classe e Função
content_hash: f09d04577668ecc2d8cf37cca0427fcd12dadcf9a67b3dcddedfe1889709dcb1
fetched_at: '2026-06-28T22:40:17.980555+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Retornar Folder
  ativo
type: support-article
updated_at: '2022-01-03T21:07:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042324373-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retornar-Folder-ativo
---

**Dúvida**Como retornar folder ativo em rotinas MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.23  
  
**Solução**Pode- se utilizar o método**[GetFolderActive](https://tdn.totvs.com/display/PROT/FWFormView)()**.  
Neste deve-se passar dois parâmetros: **cID** e **nType**.

Para obter o ID, utilizamos o **[FwViewActive](https://tdn.totvs.com/display/PROT/FWViewActive)(),** o objeto retornado possui o array **AFOLDERS** e na posição 1,1 "AFOLDERS[1][1]", é obtido o ID, o segundo parâmetro pode ser 1 ou 2 dependendo da necessidade, no exemplo utilizado, retornaremos o folder na rotina **FATA300**, aba "Produto", a instrução neste caso foi:

```
oView := FwViewActive()  
aFolder := oView:GetFolderActive(OVIEW:AFOLDERS[1][1],2 )
```

**Saiba Mais**

[FWFormView](https://tdn.totvs.com/display/PROT/FWFormView)

[FWViewActive](https://tdn.totvs.com/display/PROT/FWViewActive)
