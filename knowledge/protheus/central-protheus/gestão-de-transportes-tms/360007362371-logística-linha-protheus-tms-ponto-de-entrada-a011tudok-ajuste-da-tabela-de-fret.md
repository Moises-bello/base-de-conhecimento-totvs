---
article_id: 360007362371
category: Gestão de Transportes (TMS)
content_hash: f7e2b6fe43d077db3a47816fedcee3cc5f71f8518c963869fa63b547a294ed66
fetched_at: '2026-06-28T22:45:29.526566+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada A011TUDOK Ajuste da Tabela
  de Frete
type: support-article
updated_at: '2022-06-20T17:05:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007362371-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-A011TUDOK-Ajuste-da-Tabela-de-Frete
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura:**00:00:40 min **Dúvida**Como implementar o ponto de entrada **A011TUDOK** - Ajuste da Tabela de Frete?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **A011TUDOK** está localizado no fonte **TMSA011** - Ajuste da Tabela de Frete e permite ao usuário efetuar validações antes da gravação da rotina.  
  
**Programa** **Fonte**: TMSA011.PRW  
  
**Sintaxe**: A011TUDOK - Ajuste da Tabela de Frete ( [ Nill ] ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | Nill |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  
**lRet**

(logico)* Caso o retorno seja (.F.) não permite gravar o ajuste.

**Exemplos**:  
  
User Function A011TUDOK()

Local lRet := .T.

lRet := .F.

MsgAlert('Bloqueado a gravação do Ajuste')
