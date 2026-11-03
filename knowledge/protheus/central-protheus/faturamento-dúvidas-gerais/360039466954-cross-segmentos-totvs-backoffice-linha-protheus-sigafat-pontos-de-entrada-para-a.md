---
article_id: 360039466954
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 0b16cbfdeda0230c6d748ce87fe1f37de7f199893e5e3d928888b234280d06c8
fetched_at: '2026-06-28T22:38:30.110931+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Pontos de entrada
  para alteração do cadastro do cliente
type: support-article
updated_at: '2025-10-09T23:37:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466954-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-para-altera%C3%A7%C3%A3o-do-cadastro-do-cliente
---

**Dúvida**

Quais os pontos de entrada na alteração do cadastro de cliente?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - a partir da release 12.1.27.

**Solução**

A partir da de **04/04/22**, o **mata030** foi descontinuado e em seu lugar, passou a utilizar o **crma980** ativando o parâmetro **mv\_mvcsa1** como .T.

Desta forma, os pontos utilizados para alteração do cliente mudaram para o formato em mvc, segue o de-para dos pontos e entradas para utilização:

De M030PALT ---> Para: CRMA980  ID **MODELCOMMITTTS -**  <https://tdn.totvs.com/x/-rO6J> 

**De M030ALT ----> Para :**CRMA980  ID **MODELCOMMITTTS -**  <https://tdn.totvs.com/x/-rO6J> 

**De MALTCLI -----> Para:** CRMA980  ID **MODELCOMMITTTS -**  <https://tdn.totvs.com/x/-rO6J> 

**De MA030TOK ----> Para:** CRMA980  ID **FORMPOS-** <https://tdn.totvs.com/x/-rO6J>-Inclusão e Alteração

Obs: Caso necessite criar o listbox para a opção posição do cliente, existente em outras ações, pode se utilizar o Ponto de entrada **FC010LIST**: **<https://tdn.totvs.com/pages/releaseview.action?pageId=6071494>**
