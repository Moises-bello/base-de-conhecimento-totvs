---
article_id: 360025171871
category: ADVPL - Ponto de Entrada
content_hash: c7ad59b7f808a489834ae45a4e205703d4ae03bdf3894d0d868bf99acb5d6ad8
fetched_at: '2026-06-28T22:40:12.843550+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Problemas ao utilizar
  o PE FA100GET (MF100GRV1e MF100GRV4)
type: support-article
updated_at: '2021-12-30T17:16:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025171871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Problemas-ao-utilizar-o-PE-FA100GET-MF100GRV1e-MF100GRV4
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Ocorrência**No módulo Financeiro, ao confirmar Movimento Bancário (FINA100), na opção de transferência entre contas  utilizando o ponto de entrada **FA100GET** o sistema apresenta mensagem (**MF100GRV1e** **MF100GRV4**)   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12  
  
**Causa**Esse incidente ocorre, pois o campo **E5\_MOEDA**, na versão 11, tinha tamanho de 3 caracteres, e na versão 12 o campo é de tamanho 2  
  
**Solução**  
Para solucionar essa ocorrência, utilize o exemplo abaixo.

```
#include "rwmake.ch"   
User function FA100Get ()  
  
Local aTeste :={}  
 Aadd( aTeste, {"341" })// BANCO ORIGEM   
 Aadd( aTeste, {"22 " })// AGENCIA ORIGEM   
 Aadd( aTeste, {"000001 " })// CONTA ORIGEM  
 Aadd( aTeste, {"0000000001" })// NATUREZA ORIGEM   
 Aadd( aTeste, {"237" })// BANCO DESTINO   
 Aadd( aTeste, {"0002 " })// AGENCIA DESTINO   
 Aadd( aTeste, {"000002 " })// CONTA DESTINO  
 Aadd( aTeste, {"0000000001" })// NATUREZA DESTINO   
 Aadd( aTeste, {"CH" })// TIPO MOV ----------- Neste campo que houve a alteração.  
 Aadd( aTeste, {"999 " })// NUMERO DOC  
 Aadd( aTeste, {1000 })// VALOR  
 Aadd( aTeste, {"TESTE " })// HISTORICO   
 Aadd( aTeste, {"OSASCO " })//BENEFICIARIO  
  
Return aTeste
```
