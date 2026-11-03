---
article_id: 4412582221719
category: RH - Lançamentos
content_hash: 1d7b36b118d8da145b1c930b2d21ca0b9cc713d75445f89ab95549d857c1230a
fetched_at: '2026-06-28T22:43:31.377590+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP090OK - Validação Adicional
  em Lançamentos Mensais / Por Funcionário
type: support-article
updated_at: '2025-04-17T17:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412582221719-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP090OK-Valida%C3%A7%C3%A3o-Adicional-em-Lan%C3%A7amentos-Mensais-Por-Funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26080821188759) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Utilização do ponto de entrada GP090OK  
  
**Ambiente**[TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Este Ponto de Entrada tem como objetivo a verificação extra nas rotinas de Inclusão/Alteração/Exclusão de Lançamentos Mensais.

Validação será feita no momento do LinhaOK, verificando se a linha posicionada atende às validações.

Deve retornar verdadeiro (.T.) se linha for válida, permitindo alterar foco para próxima linha ou salvar registros.

Deve retornar falso (.F.) caso linha não atender à validação realizada, impedindo retirada de foco da linha ou gravação dos registros.

Feita atualização para permitir a passagem pelo PE também quando a linha está com estado de Deletada. Validando assim, todas as linhas: incluídas, alteradas e deletadas.

**Localização** : Atualização / Lançamentos / Por Funcionário (GPEA090)

**Fonte**: GPEA090.PRX

**Retorno:** Lógico (.T. ou .F.)

**Parâmetros** :

| Nome | Tipo | Descrição |
| --- | --- | --- |
| PARAMIXB | Array of Record | Contém o array com as informações da linha que está sendo validada. |

**Exemplo**

**GP090OK - P12**

USER FUNCTION GP090OK()  
  
Local lRet := .T.  
Local nX := 0  
Local nY := 0  
Local nPosDeleted := GdFieldPos( "GDDELETED" )  
Local nPosValor := GdFieldPos("RGB\_VALOR")  
Local nPosHorasC := GdFieldPos("RGB\_HORAS")  
Local nPosDtRef := GdFieldPos("RGB\_DTREF")  
  
If Len(aColsAnt) > 0  
       For nX := 1 to Len(aCols)  
             nY := aScan(aColsAnt, { |x| x[2] == aCols[nx][2] })  
             If aCols[nx][2] == "013" .AND. aCols[nx][nPosDeleted] == .T. //se verba esta como deletada  
                  MsgAlert("Verba não pode ser deletada - GP090OK","ATENCAO")  
                  aCols[nx][nPosDeleted] := .F.  
                  lRet := .F.  
            ElseIf nY > 0 .AND. (aCols[nx][nPosValor] != aColsAnt[ny][nPosValor] .OR. aCols[nx][nPosDtRef] != aColsAnt[ny][nPosDtRef])  
                  aCols[nx][nPosValor] := aColsAnt[ny][nPosValor]  
                  aCols[nx][nPosDtRef] := aColsAnt[ny][nPosDtRef]  
                  MsgAlert("Verba não pode ser alterada - GP090OK","ATENCAO")  
             EndIf  
       Next nX  
EndIf  
  
Return (lRet)

BASE TDN*: <https://tdn.totvs.com/display/public/PROT/DT_PE_GP090OK_Lancamentos_Mensais_Verificacao_Adicional>*

**Saiba mais:**

[RH - Lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781734-RH-Lan%C3%A7amentos)
