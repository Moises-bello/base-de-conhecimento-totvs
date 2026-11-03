---
content_hash: 4106d8b80607d66cb5e5d7edb4a2ff1010f797a840eb13d5eaa7488eb3c17a98
fetched_at: '2026-06-29T00:10:52.113631+00:00'
page_id: '570063753'
product: rm
source: tdn-rm
title: 9133423 FISCAL01-13648 - DT Erro no registro C120 do SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/9133423+FISCAL01-13648+-+DT+Erro+no+registro+C120+do+SPED+Fiscal
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | TOTVS Backoffice |
| Segmento: | Linha RM |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 9133423 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13648 |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que ao gerar um arquivo do SPED Fiscal e importá-lo no PVA é apresentado erro no registro C120 referente as informações de importação solicitando obrigatoriedade do preenchimento. Segundo o cliente a NF é de devolução simbólica de peso, a mesma está parametrizada com CFOP 3.201, que segundo Nota Técnica 2010.007, de acordo com o cliente, seguindo as instruções da Nota Técnica, não é necessária informação da DI e por esse motivo não deve ser gerado o registro C120. De acordo com o mapeamento de campo essa informação é uma consistência para geração do mesmo.

## **03. SOLUÇÃO**

Ao gerar um arquivo do SPED Fiscal, foi acrescentada uma condição para que o Registro C120 seja gerado somente se o Número do Documento de Importação (DI) estiver preenchido, caso contrário será informado no Log da rotina que o registro não foi gerado.
