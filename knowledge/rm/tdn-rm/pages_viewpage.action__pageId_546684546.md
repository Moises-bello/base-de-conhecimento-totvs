---
content_hash: c6966d7e7ebf4a3974225b9af14ab08567119963ee71e1c7c6bf1acdd3f2d731
fetched_at: '2026-06-29T00:10:41.963435+00:00'
page_id: '546684546'
product: rm
source: tdn-rm
title: 6293846 FISCAL01-10521 DT VAF/DAMEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546684546
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | VAF/DAMEF |
| Ticket: | 6293846 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10521 |

## **02. SITUAÇÃO/REQUISITO**

Na geração da VAF DAMEF o valor de ST decorrente das entradas deve ser gerado em Exclusões da VAF.  
Segue parecer da consultoria tributária:

Parcela do ICMS Retido por Substituição Tributária: informar o valor do ICMS-ST das entradas, inclusive do ICMS-ST que tenha sido destacado na nf. pelo fornecedor substituído somente para o reembolso do adquirente;

## **03. SOLUÇÃO**

Inclusão do CFOP 1.403. e 2.403 na Linha Exclusão Substituição Tributaria do relatório.
