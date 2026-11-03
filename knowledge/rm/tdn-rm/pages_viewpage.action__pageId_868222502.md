---
content_hash: 2116d7c11b4e178956fdaf75b07d62f6965d88525f9795b5a4af062eac458126
fetched_at: '2026-06-29T00:11:56.673526+00:00'
page_id: '868222502'
product: rm
source: tdn-rm
title: DT - Reprogramação Salarial - Log de Movimento x Distribuição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=868222502
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Reprogramação Salarial |
| País: | Brasil |
| Ticket | [19937807](https://totvssuporte.zendesk.com/agent/tickets/19937807 "View ticket on the Zendesk portal"); [19891119](https://totvssuporte.zendesk.com/agent/tickets/19891119 "View ticket on the Zendesk portal") |
| Issue | [DRHCALCRM-6568](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6568); [DRHCALCRM-6582](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6582) |

## **02. VERSÃO**

Este requisito estará disponível a partir do release 12.1.2410

Atenção

Devido a alteração na estrutura da tabela PFMOVENSINOLOG, esta solução somente será liberada no release 12.1.2410. Os valores calculados anteriormente não terão alteração na  PFMOVENSINOLOG, permanecendo com valor arredondado

## **03.****SITUAÇÃO/REQUISITO**

Atualmente o produto não apresenta valores iguais no “Log do Movimento de Ensino” e na “Distribuição do Movimento de Ensino” ao realizar uma reprogramação salarial, sendo que no log de movimento de ensino os valores são arredondados e na distribuição do movimento de ensino os valores contemplam 4 casas decimais, realizando o arredondamento no final após somar os valores de cada distribuição.

Este comportamento ocorre, pois na Tabela PFMOVENSINOLOG o tipo de campo não permitia inserir valores com mais de 2 casas decimais, o que forçava o arredondamento.

## **04.****SOLUÇÃO**

Foi alterado o tipo do campo VALORMENSAL da tabela PFMOVENSINOLOG para que tenha a mesma precisão numérica do campo VALORMENSAL da tabela PFMOVENSINO para que ambas possam suportar uma precisão de até 4 decimais e facilitando assim a conferência dos valores distribuídos no processo de reprogramação salarial.

Para isto, foi necessário criar um script de banco de dados para alinhar a precisão numérica entre as tabelas PFMOVENSINOLOG e PFMOVENSINO quanto ao campo VALORMENSAL, fazendo com que a diferença de centavos não ocorra novamente.   
  
Como podemos observar no exemplo abaixo:  
  
**log da distribuição de horas do Movimento de ensino:**  
  
  
**Distribuição das horas do Movimento de ensino:** 

## **05. ASSUNTOS RELACIONADOS**
