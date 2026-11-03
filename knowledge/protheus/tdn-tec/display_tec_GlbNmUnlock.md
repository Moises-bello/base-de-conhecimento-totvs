---
content_hash: 8441bf4745ee084bd679c4383eadde7d385c32b344a0d91e06b36dd0378fad6c
fetched_at: '2026-07-02T19:24:21.599118+00:00'
page_id: '268799847'
product: protheus
source: tdn-tec
title: GlbNmUnlock
type: documentation
url: https://tdn.totvs.com/display/tec/GlbNmUnlock
version: 2
---

GlbNmUnlock

Libera um bloqueio de um identificador nomeado obtido pela função GlbNmLock().

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cText | caractere | Indica o nome do identificador de bloqueio. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lLck | lógico | Retorna .T. caso o identificador de bloqueio tenha sido liberado com sucesso para o processo atual. Para isso, o identificador precisa existir na lista de bloqueios, e o processo atual deve ter sido o responsavel por realizar o bloqueio. Caso contrário a função retorna .F. |

## Observações

* O escopo do identificador nomeado é a instância atual do serviço e/ou processo executável do TOTVS | Application Server, sem fazer distinção por Environment em execução.

## Exemplos

cppEclipsetruefalse

## Abrangência

TOTVS | Application Server 7.00.131227A, com data de geração superior a 07/11/2016

## Veja também
