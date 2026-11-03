---
article_id: 360001045987
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 9cbd9f8ce75e65348ac6ad6f378c5634d84303e677874272ff30b6e62befa28e
fetched_at: '2026-06-28T22:38:45.462876+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP-FAT- array out of bounds ( 1 of 0 )  on MA460PROC
type: support-article
updated_at: '2021-04-28T15:13:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001045987-MP-FAT-array-out-of-bounds-1-of-0-on-MA460PROC
---

**Ocorrência**

Ao faturar uma nota fiscal gera o erro:

array out of bounds ( 1 of 0 )  on **MA460PROC**(MATA461.PRX) 07/03/2018 15:05:56 line : 1396

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro se dava com o uso do campo  **F4\_VLRZERO**=="1", com o parâmetro **mv\_paisloc**="BRA" e o preço de venda igual a 0, onde não estava carregando as informações no array **aPvlNfs** do **mata461**, ocasionando o error.log.  
   
 **Solução**  
 Para solucionar essa ocorrência, aplique o pacote da **ocorrência 44** - [Principais Pacotes de Correção - Faturamento - SIGAFAT ( A410Limpa, NNR, \_FWMBPICTVAR, CHECKNEWX, MPUSERACCOUNT, BEFOREEXECUTE, Work area not, MATA030, CFILTERNATIVE, FEFO, Vencimento Lote, AFY811, FATJOBNFE, ACOLSCCUT, MARESDOFAT, Gatilho, C5\_MENNOTA)](http://tdn.totvs.com/pages/viewpage.action?pageId=235334710)
