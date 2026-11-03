---
content_hash: 8b0f57af1625668439785c72867e15304aeda204d5a860684c24f5f03be2f413
fetched_at: '2026-06-29T00:11:13.363293+00:00'
page_id: '659610741'
product: rm
source: tdn-rm
title: FISCAL01-17241 DT - Reabertura do Período de INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=659610741
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Abertura de Período de Apuração |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17241 |

## **02. SITUAÇÃO/REQUISITO**

Ajustar a Validação da Reabertura do Período de INSS.

Cliente precisa reabrir período de INSS, com períodos posteriores já encerrados, além da EFD-Reinf também encerrado.  
"Podemos seguramente remover as validações da EFD-Reinf e dos Períodos de Apuração Posteriores  
encerrados, apenas para o INSS. Desta forma o Cliente conseguirá abrir apenas o Período de Apuração de  
Janeiro/2020 e realizar a inclusão do novo Lançamento. Quando necessário ele poderá abrir o período de  
Apuração do INSS sem reabrir a EFD-Reinf."

## **03. SOLUÇÃO**

Foi removido duas travas para o encerramento do período de apuração do INSS:  
● Não precisa mais reabrir períodos posteriores para reabrir um determinado período;  
● Não precisa mais reabrir o evento R5011 para reabrir o período INSS.
