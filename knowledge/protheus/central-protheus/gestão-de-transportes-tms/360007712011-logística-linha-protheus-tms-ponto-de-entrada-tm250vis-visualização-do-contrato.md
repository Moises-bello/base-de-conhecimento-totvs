---
article_id: 360007712011
category: Gestão de Transportes (TMS)
content_hash: 48c381dfcaab4c471868eb7d50679c032ab548571c3c1545fa8bf3df5a25189c
fetched_at: '2026-06-28T22:45:32.280156+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250VIS Visualização do
  Contrato Complementar
type: support-article
updated_at: '2023-10-26T21:26:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007712011-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250VIS-Visualiza%C3%A7%C3%A3o-do-Contrato-Complementar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18591822426135)** Tempo aproximado para leitura: **00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM250VIS** - **Visualização do Contrato Complementar**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250VIS** está localizado na rotina de geração de contrato complementar e é executado na confirmação da geração/visualização do contrato complementar.  
  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250VIS - Visualização do Contrato Complementar ( [ nOpcx ] ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | nOpcx |  |  | Caracter |  |  | Número da opção selecionada |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  
**lRet**

(logico)* Se o retorno for ".F." o contrato complementar NÃO será gerado.

**Exemplos**:  
  
*User Function* **TM250VIS**()

Local nOp := ParamIXB[1]

Local lRet:= .F.

Aviso('Ponto TM250VIS','Opção: '+Str(nOp),{'OK'})

If nOp == '4'

lRet:= .T.

End If

Return lRet

**Variáveis**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |
