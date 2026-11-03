---
content_hash: 1d91d46ee308043196fc53c8f4de5fa5a788a40a01cdea3b1001d1d5bf738c12
fetched_at: '2026-06-29T00:10:25.044386+00:00'
page_id: '501452995'
product: rm
source: tdn-rm
title: 5279100 FISCAL01-8337 DT Eventos Tributários - Grupo Dedução - Percentual limite
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501452995
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Fiscal |
| Função: | Cadastro de Evento Tributário |
| Ticket: | 5279100 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8337 |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que vinculou uma Conta Contábil no grupo de Deduções do Evento Tributário IRPJ   
informando o Percentual Limite para dedução. Porém, ao realizar a simulação e a apuração do tributo   
o sistema desconsidera o percentual limite e considera o valor total da Conta Contábil.

## **03. SOLUÇÃO**

Foi verificado que o sistema não esta preparado para tratar o Percentual Limite quando a origem do Item

do Evento Tributário e diferente de Lalur Parte B.

Foi realizado um ajuste no Cadastro de Evento Tributários para não deixar colocar   
Percentual Limite de Dedução/Compensação quando a origem do Item de Evento for   
diferente de Lalur Parte B.  
Isto porque quando se informa este Percentual nesta condição causa inconsistência de  
valores no Encerramento do Período de Apuração/Simulação.

Obs.: Iremos fazer um estudo para implementar um Melhoria no Encerramento do   
Período de Apuração para ai sim poder informar esta Percentual para qualquer   
tipo de Origem.
