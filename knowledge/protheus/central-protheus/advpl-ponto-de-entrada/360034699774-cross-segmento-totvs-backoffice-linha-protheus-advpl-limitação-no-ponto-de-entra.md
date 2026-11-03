---
article_id: 360034699774
category: ADVPL - Ponto de Entrada
content_hash: b6e77b723b7ad9250a292b875841f497baf002e46f2fab41c57ffa9ad6410260
fetched_at: '2026-06-28T22:40:11.707904+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Limitação no ponto
  de entrada TK271ROTM
type: support-article
updated_at: '2022-04-29T12:58:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034699774-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Limita%C3%A7%C3%A3o-no-ponto-de-entrada-TK271ROTM
---

**Ocorrência**Estou utilizando o ponto de entrada TK271ROTM para adicionar novas opções no menu, contudo as mesmas não estão sendo adicionadas.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Isto ocorre porque devido ao grande número de opções de operações já existentes na rotina TMKA271, o ponto de entrada limita-se a vetores menores que três posições, desta forma, atendendo ao limite de 10 opções.  
  
**Solução**Retornar um vetor com apenas duas opções para o ponto de entrada TK271ROTM ou realizar a criação de submenus.  
  
**Exemplo**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
User Function TK271ROTM()  
    Local aRotUser := {} // NÍVEL  
    Local aRotAux  := {} // SUBNÍVEL  
  
// ADIÇÃO DO PRIMEIRO NÍVEL  
    AAdd(aRotAux, {"TK271ROTM1", "U_TEMP001", 0, 7})  
    AAdd(aRotAux, {"TK271ROTM2", "U_TEMP002", 0, 7})  
    AAdd(aRotUser, {"Opções A", aRotAux, 0, 7})  
  
    // ADIÇÃO DO SEGUNDO NÍVEL  
    aRotAux := {}  
    AAdd(aRotAux, {"TK271ROTM3", "U_TEMP003", 0, 7})  
    AAdd(aRotAux, {"TK271ROTM4", "U_TEMP004", 0, 7})  
    AAdd(aRotUser, {"Opções B", aRotAux, 0, 7})  
Return (aRotUser)
```

**Saiba mais**  
[TK271ROTM - Personalização de novas rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=6787737)
