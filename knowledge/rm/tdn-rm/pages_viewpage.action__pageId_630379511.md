---
content_hash: 780b2319306234b700f6a24c901b174968099de54d8d1a60b75ba6d2af643498
fetched_at: '2026-06-29T00:11:05.366214+00:00'
page_id: '630379511'
product: rm
source: tdn-rm
title: FISCAL01-15864 - DT - Divergência Inscrição Estadual = ISENTO no xml de NF-e
  e Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=630379511
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Nota Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15864 |

## **02. SITUAÇÃO/REQUISITO**

REINF pelo RM, ao enviar R-1000 sem informar inscrição estadual (campo vazio) retorna a inconsistência: "Falha ao processar o evento de identificador 1 e tipo R-1000:

Ocorreu um erro ao configurar os dados da filial no TSS Inscrição Estadual da Filial não informada!"

## **03. SOLUÇÃO**

Ao executar o Processo para Enviar NF-e, se a Inscrição Estadual do Destinatário estiver como “ISENTO”, a mesma será convertida em um campo vazio e processado com sucesso.

Foi realizado essa tratativa para manter a mesma compatibilidade da REINF.
