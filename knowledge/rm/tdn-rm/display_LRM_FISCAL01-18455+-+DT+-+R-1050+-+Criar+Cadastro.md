---
content_hash: 25aefd84c6537b3bfbcaeaf653ca80aa33abec203646d192bd4a2198b0dc32f9
fetched_at: '2026-06-29T00:11:27.546838+00:00'
page_id: '726531296'
product: rm
source: tdn-rm
title: FISCAL01-18455 - DT - R-1050 - Criar Cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18455+-+DT+-+R-1050+-+Criar+Cadastro
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18455 |

## **02. SITUAÇÃO/REQUISITO**

De forma semelhante ao Evento R-1070 (Anexo ao R-1000) deve ser criado um cadastro para o Evento R-1050

Neste cadastro deve ser possível informar uma Filial do tipo SCP, além da data inicial e final.

O Cadastro do Evento não poderá ser excluído, a não ser que o status seja Inconsistente, Rejeitado ou Não Transmitido.

A data fim da operação é opcional caso o evento R-1000 não informe esta data.

Ao ser incluído o cadastro deve assumir o status "Não Transmitido".

## **03. SOLUÇÃO**

Implementado o cadastro do registro.

Imagem

Disponível a partir da biblioteca 12.1.2205
