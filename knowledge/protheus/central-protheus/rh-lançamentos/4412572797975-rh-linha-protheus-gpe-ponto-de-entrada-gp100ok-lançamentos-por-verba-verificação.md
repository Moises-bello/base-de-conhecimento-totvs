---
article_id: 4412572797975
category: RH - Lançamentos
content_hash: 260f3593bc1e75311aaa00cd40e69e4ab0743c529f9c9f12136e155f3b5afc75
fetched_at: '2026-06-28T22:43:31.393940+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP100OK - Lançamentos por Verba
  / Verificação Adicional
type: support-article
updated_at: '2025-08-04T20:50:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412572797975-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP100OK-Lan%C3%A7amentos-por-Verba-Verifica%C3%A7%C3%A3o-Adicional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26080975043863) Tempo aproximado para leitura: **02:00:00 min** **Dúvida**Utilização do Ponto de Entrada GP100OK  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | *Microsiga Protheus®.* |
| **Segmento:** | *Serviços.* |
| **Módulo:** | *SIGAGPE.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *GPEA100.* | *Manipulacao de Lançamentos por Verba.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *GPEA590* | *Lançamentos por Verba.* | |
| **Chamados Relacionados** | *TVVHM2.* |
| **Tabelas Utilizadas:** | *RGB - Lançamentos* |

### **Ponto de Entrada**

|  |  |
| --- | --- |
| **Descrição:** | *Este Ponto de Entrada tem como objetivo permitir validações extras nas linhas de lançamentos nas rotinas de Inclusão/Alteração de Lançamentos Por Verbas.*  *Validação será feita no momento do LinhaOK, verificando se a linha posicionada atende às validações.*  *Deve retornar verdadeiro (.T.) se linha for válida, permitindo alterar foco para próxima linha ou salvar registros.*  *Deve retornar falso (.F.) caso linha não atender à validação realizada, impedindo retirada de foco da linha ou gravação dos registros.* |
| **Localização:** | *SIGAGPE - Atualizações - Lançamentos - Por Verba* |
| **Eventos:** | *Lançamentos por Verba* |
| **Programa Fonte:** | *GPEA100.prx* |
| **Função:** | *GPEA100* |
| **Retorno:** | Lógico (.T. ou .F.) |

**Exemplo:**

**GP100OK**

|  |
| --- |
| `USER FUNCTION GP100OK()`      `Local lRet  := .T.`  `Local nX    := 0`  `Local nY    := 0`  `Local nPosDeleted   := GdFieldPos( "GDDELETED" )`  `Local nPosValor     := GdFieldPos("RGB_VALOR")`  `Local nPosHorasC    := GdFieldPos("RGB_HORAS")`  `Local nPosDtRef     := GdFieldPos("RGB_DTREF")`  `Local nPosMat       := GdFieldPos("RGB_MAT")`    `/*Neste exemplo, verifico se a verba editada em questão é uma verba específica que escolhi. Caso seja essa verba, realizo a validação para não permitir alteração no lançamento.*/`  `If cCod == "013"`  `For nX := 1 to Len(aCols)`  `nY := aScan(aColsAnt, { |x| x[nPosMat] == aCols[nX][nPosMat] })`  `If aCols[nX][nPosDeleted] == .T. //se verba esta como deletada`  `MsgAlert("Verba não pode ser deletada.","ATENCAO")`  `aCols[nX][nPosDeleted] := .F.`  `lRet := .F.`  `ElseIf aCols[nX][nPosValor] != aColsAnt[nY][nPosValor] .OR. aCols[nX][nPosDtRef] != aColsAnt[nY][nPosDtRef]`  `MsgAlert("Verba não pode ser alterada.","ATENCAO")`  `lRet := .F.`  `aCols[nX][nPosValor] := aColsAnt[nY][nPosValor]`  `aCols[nX][nPosDtRef] := aColsAnt[nY][nPosDtRef]`  `EndIf`  `Next nX`  `EndIf`    `Return ( lRet )` |

**Saiba Mais**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=244742667>
