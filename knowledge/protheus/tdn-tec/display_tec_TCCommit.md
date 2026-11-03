---
content_hash: e56ec9670ffdb3b26a788b43f944d8f70bf0971e7e283d8d80e9871b0026c520
fetched_at: '2026-07-02T19:24:22.455170+00:00'
page_id: '270075307'
product: protheus
source: tdn-tec
title: TCCommit
type: documentation
url: https://tdn.totvs.com/display/tec/TCCommit
version: 2
---

TCCommit

Realiza o controle de transação no DBAccess

## Sintaxe

false, [ xParam ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nOption | numérico | Numero relacionado a ação do TCCommit | X |  |
| xParam | qualquer | Compatibilidade. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| uRet | nil | Sempre retorna nulo. |

## Observações

trueAtenção

É necessário fazer a chamada do TCCommit(1) no inicio da transação e TCCommit(4) após o termino da transação

Valores possiveis para o primeiro parametro da função:

| nOption | Descrição |
| --- | --- |
| 1 | Inicializa uma transação |
| 2 | Realiza o commit da transação |
| 3 | Realiza o rollback da transação |
| 4 | Finaliza a Transação |

## Exemplos

cppEclipsetruefalse( DBAppend( .F. ) )
(cT1)->FIELD\_NAME := "Inteiro"
(cT1)->FIELD\_TYPE := "Int"
(cT1)->( DBCommit() )
(cT1)->( DBAppend( .F. ) )
(cT1)->FIELD\_NAME := "Character"
(cT1)->FIELD\_TYPE := "char"
(cT1)->( DBCommit() )
DBCloseArea()
TCCommit(2) // Realiza o commit
TCCommit(4) // Finaliza a Transação
TCUnlink()
RETURN
]]>

## Veja também
