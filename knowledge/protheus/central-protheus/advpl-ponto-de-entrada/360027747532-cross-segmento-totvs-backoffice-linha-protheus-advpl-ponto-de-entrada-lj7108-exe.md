---
article_id: 360027747532
category: ADVPL - Ponto de Entrada
content_hash: 5a4e65fdf02eb0b0e6b38c2e56c0f11587d42f0aa0db89a65807acd8ab77100b
fetched_at: '2026-06-28T22:40:11.830821+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  lj7108 executado diversas vezes
type: support-article
updated_at: '2022-03-14T11:43:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027747532-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-lj7108-executado-diversas-vezes
---

**Ocorrência**O ponto de entrada LJ7108 está sendo chamado diversas vezes após o preenchimentos de alguns campos.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**O ponto de entrada LJ7108 é chamado cada vez que um campo tem o seu conteúdo alterado, assim sendo, o preenchimento de um campo, pode disparar diversos gatilhos e a cada alteração o ponto será chamado novamente.  
  
**Solução**Para considerar apenas uma chamada do ponto de entrada LJ7108 (em casos de exibição de caixas de diálogo), pode ser criada uma variável estática no fonte que mantenha o controle de exibição.  
  
Exemplo

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// VARIÁVEL DE CONTROLE  
Static MP_CONTROL As Logical  
  
// ALTERA O CÓDIGO PADRÃO DA TABELA DE PREÇO (MV_TABPAD)  
User Function LJ7108()  
    Local cTabRet := PARAMIXB[1] // CÓDIGO DA TABELA DE PREÇO (MV_TABPAD)  
    Local aPosCpo := PARAMIXB[2] // ITEM PARA VALIDAÇÃO  
  
    // VERIFICA SE É A PRIMEIRA EXECUÇÃO  
    If (MP_CONTROL == NIL)  
        // RETORNA A TABELA DESEJADA  
        cTabRet := IIf(MsgYesNo("YES=T01 | NO=T02"), "T01", "T02")  
  
        // ATRIBUI VALOR LÓGICO  
        MP_CONTROL := .T.  
    EndIf  
Return (cTabRet)
```

  
**Saiba mais**  
[MP - Como funciona o parâmetro MV\_TABPAD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004642292)  
[LJ7108 - Permite alterar o código da tabela de preço (MV\_TABPAD)](http://tdn.totvs.com/pages/viewpage.action?pageId=286721110)
