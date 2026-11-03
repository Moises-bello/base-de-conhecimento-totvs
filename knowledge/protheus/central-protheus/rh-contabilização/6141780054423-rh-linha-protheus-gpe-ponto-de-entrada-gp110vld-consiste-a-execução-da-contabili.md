---
article_id: 6141780054423
category: RH - Contabilização
content_hash: 8f9232c4efa108aba63ca08762abbada2f38e371c65cb1052bd3f0dbf6f58db3
fetched_at: '2026-06-28T22:43:46.023378+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP110VLD - Consiste a Execução
  da Contabilização da Folha de Pagamento
type: support-article
updated_at: '2025-07-21T18:22:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6141780054423-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP110VLD-Consiste-a-Execu%C3%A7%C3%A3o-da-Contabiliza%C3%A7%C3%A3o-da-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20668243690263) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como utilizar o Ponto de Entrada GP110VLD?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução****01. VISÃO GERAL**

Ao dar início à execução da rotina de contabilização, são efetuadas consistências, como por exemplo, se a folha de pagamento está fechada e, assim, proceder com a contabilização. Através desse ponto de entrada, é possível completar esse tipo de validação e determinar a continuidade do processo ou a sua finalização.

**02. PROGRAMA FONTE**

GPEM110.PRX

**03. SINTAXE**

GP110VLD - Consiste a Execução da Contabilização da Folha de Pagamento ( ) --> lRetono

Retorno

**lRetono**

(logico)* .T. Aborta o processo e não realiza a contabilização. F. - Continua a execução da rotina de contabilização

**Observações:**

Esse ponto de entrada é executado após a realização das consistências padrões para a execução do processo de contabilização mas antes do seu início de fato.

Exemplos

#INCLUDE 'RWMAKE.CH'  
#INCLUDE 'PROTHEUS.CH'USER   
  
FUNCTION GP110VLD()  
Local lRet:= .F.//Somente permite a contabilização do mês no mês da data base.   
IF Month(dDataBase) <>Val(Substr(cMesAnoCtab,1,2))    
lRet:= .T.Endif    
  
Return(lRet)

Variáveis

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |

**Saiba Mais:**  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
