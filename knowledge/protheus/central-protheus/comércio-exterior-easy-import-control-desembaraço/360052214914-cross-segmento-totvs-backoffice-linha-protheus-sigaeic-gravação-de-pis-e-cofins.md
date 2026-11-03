---
article_id: 360052214914
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: a3b03086f8579c41613047e0a3d6091c9bdbd58f11eb6cad5874bb2d4e616903
fetched_at: '2026-06-28T22:39:50.079205+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Gravação de PIS
  e Cofins do processo Conta e Ordem
type: support-article
updated_at: '2022-04-27T20:56:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052214914-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Grava%C3%A7%C3%A3o-de-PIS-e-Cofins-do-processo-Conta-e-Ordem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Ao gerar o documento de entrada não esta sendo gravado os valores de PIS e COFINS, como resolver?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Para gravação dos valores de PIS e Cofins é necessário configurar o parâmetro **MV\_EIC0027**, conforme boletim: [EIC0011\_Impostos\_no\_processo\_de\_importação\_por\_Conta\_e\_Ordem](http://tdn.totvs.com/pages/releaseview.action?pageId=271871355)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085355413/mceclip0.png)

Após configuração do parâmetro MV\_EIC0027 , verifique se possui os campos EIW\_PERPIS e EIW\_PERCOF para gravação da alíquota, caso não tenha efetue a configuração conforme boletim:    
[9372516 DTRADE-4868 DT PIS/Cofins processo conta e ordem](https://tdninterno.totvs.com/pages/releaseview.action?pageId=556400260)  
E os campos D1\_VALIMP5 e D1\_VALIMP6 como usado por todos os módulos.
