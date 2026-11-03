---
article_id: 360007724111
category: Gestão de Transportes (TMS)
content_hash: b1c7d63986d54e285527b1d9a233135b0a29b6bbd754d2affb68e52d468b03e3
fetched_at: '2026-06-28T22:45:32.342605+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM310FFL
type: support-article
updated_at: '2023-02-28T14:23:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007724111-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM310FFL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM310FFL**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões

**Solução**O ponto de entrada **TM310FFL** está localizado na função **TMSA310Grv** - **Gravação,** ao adicionar atividade no *array* **aServic**, caso o retorno do ponto de entrada seja verdadeiro, então é adicionado no *array*.  
  
**Programa** **Fonte**: TMSA310:PRW  
  
**Sintaxe**: TM310FFL ( [ PARAMIXB[1] ], [ PARAMIXB[2] ] ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | PARAMIXB[1] |  |  | Caracter |  |  | Filial da atividade |  |  |  |  |  |  |  |  |  |  |
|  | PARAMIXB[2] |  |  | Caracter |  |  | Código da atividade |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  

**lRet**

(logico)* .T. - Adiciona atividade para outras filiais  
  .F. - Não adiciona atividade para outras filiais

**Exemplos**:  
  
*User Function* TM310FFL()

Local lRet := .T.

Local cFilAti := PARAMIXB[1]

Local cCodAti := PARAMIXB[1]//Validações de usuário

*Return lRet*
