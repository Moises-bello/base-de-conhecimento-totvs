---
article_id: 360027459352
category: ADVPL - Classe e Função
content_hash: 033be26378c60ac01d1670a708626a3ced7a94ae40421cdc3cfa89949b222bc4
fetched_at: '2026-06-28T22:40:19.441022+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função para obter
  matricula no Vinculo Funcional
type: support-article
updated_at: '2022-01-10T21:51:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027459352-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-para-obter-matricula-no-Vinculo-Funcional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Qual função para obter o numero da matricula, no Vinculo Funcional no Configurador -> Cadastro de usuário.   
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Poderá utilizar a função PswRet(),  pois o retorno desta função é um array onde a posição 22 tem as informações, como mostra a documentação no portal TDN: [PswRet - Informações do último usuário](http://tdn.totvs.com/pages/releaseview.action?pageId=267792734)  
  
" [1][22] C     Empresa, filial e matricula"
