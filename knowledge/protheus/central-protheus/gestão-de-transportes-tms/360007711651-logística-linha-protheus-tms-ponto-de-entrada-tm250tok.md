---
article_id: 360007711651
category: Gestão de Transportes (TMS)
content_hash: 961567687267c094c5faac27f87d37d5c1c5fcb9f4b14bce3d25564c59d215b9
fetched_at: '2026-06-28T22:45:32.270907+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250TOK
type: support-article
updated_at: '2024-02-19T16:57:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007711651-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250TOK
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM250TOK**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250TOK** está localizado no fonte **TMSA250** - **Contrato** **de** **Carreteiro,** e é chamado antes de exibir a tela de **Exclusão do Contrato de Carreteiro**.  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250TOK ( < Nil> ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | Nil |  |  | Array of Record |  |  | Nenhum |  |  |  |  |  | X |  |  |  |  |

**Retorno**:  
  

**lRet**

(logico)* .T. - Exclui o Contrato de Carreteiro
* .F. - Não exclui o Contrato de Carreteiro

**Observações**: Ao executar este Ponto de Entrada o arquivo **DTY -** Contrato de Carreteiro está posicionado.  
  
**Exemplos**:  
  
*User Function* TM250TOK()

*MsgAlert* ('Este Contrato de Carreteiro Não poderá ser excluido', 'Atencao')

Return .F.
