---
article_id: 360007203292
category: Gestão de Transportes (TMS)
content_hash: a9c87e73f63dfd9c0fda5ab3345807becd2edf348b740c8387f8f6ecfd585ac4
fetched_at: '2026-06-28T22:45:29.627555+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040BICM Alteração da
  base de ICMS na cotação de frete
type: support-article
updated_at: '2022-01-18T17:46:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007203292-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040BICM-Altera%C3%A7%C3%A3o-da-base-de-ICMS-na-cota%C3%A7%C3%A3o-de-frete
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como implementar o ponto de entrada **TM040BICM** **Alteração da base de ICMS na cotação de frete**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040BICM** é utilizado no processo de cotação de frete, na atualização da composição do frete. Permite alterar o valor da base do **ICMS** **- Imposto sobre Circulação de Mercadorias e Serviços**, tendo como parâmetros, o valor atual dessa base e os códigos da região origem, destino e devedora, semelhante ao ponto de entrada **TM040ICM**.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040BICM - Alteração da Base de ICMS na Cotação de Frete ( < nBasICM> , [ cCdrOri ], [ cCdrDes ], [ cCliDev ], [ cLojDev ] ) --> nBasICM  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| nBasICM | Numérico | Valor atual da base de icms |  | X |  |
| cCdrOri | Array of Record | Código da região de origem |  |  |  |
| cCdrDes | Array of Record | Código da região de destino |  |  |  |
| cCliDev | Array of Record | Cliente devedor |  |  |  |
| cLojDev | Array of Record | Loja do cliente devedor |  |  |  |

**Retorno:**  
nBasICM  
             (numerico)  
             valor alterado da base de icms  
  
**Exemplos**:  
User Function TM040BICM()  
Local nBasICM := PARAMIXB[1]   
Local cCdrOri := PARAMIXB[2]  
Local cCdrDes := PARAMIXB[3]  
Local cCliDev := PARAMIXB[4]  
Local cLojDev := PARAMIXB[5]//-- Manutenção do valor do nBasICM  
Return nBasICM  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
| nBasICM | Numérico | Local | Sim | valor alterado da base de icms |
|  | Array of Record | Global | Não |  |
