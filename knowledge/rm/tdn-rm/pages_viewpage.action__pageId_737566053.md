---
content_hash: 89e4a23f8b6dd311a0130b87c50c4fe0d03eb2a6b4b51a3be8f1ebe424601d15
fetched_at: '2026-06-29T00:11:31.400923+00:00'
page_id: '737566053'
product: rm
source: tdn-rm
title: DT-S-2240 -Tag <nrInsc> passa a verificar o histórico de seção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=737566053
version: 3
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-2240-Condições Ambientais do Trabalho-Agentes Nocivos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-5632](https://jiraproducao.totvs.com.br/browse/DRHROTRM-5632) |

## **02. SITUAÇÃO/REQUISITO**

Quando um funcionário tem uma transferencia entre CNPJs, se gerarmos o XML para uma data antes à transferencia, a descrição da seção é apresentada conforme histórico de seção do funcionário, mas <nrInsc> busca a seção atual. 

## **03. SOLUÇÃO**

Tratativa no evento S-2240 nas tags <tpInsc> e <nrInsc> do grupo infoAmb para verificar o histórico de seção do funcionário.
