---
content_hash: 851a46396bcc70c7b2bc916cc887ecf39c4050c60870442e9e89f09b7f1655f6
fetched_at: '2026-06-29T00:11:48.674287+00:00'
page_id: '825301229'
product: rm
source: tdn-rm
title: FISCAL01-22016 - REINF - MS1256 - frmTribut
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-22016+-+REINF+-+MS1256+-+frmTribut
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-22016 |

## **02. SITUAÇÃO/REQUISITO**

Corrigir a geração do campo frmTribut.

Está sendo considerado somente o cadastro do tributo e não do Cli/For

## **03. SOLUÇÃO**

Ajustada a geração do campo frmTribut conforme descrito na documentação do evento R-4020.

É considerado o cadastro do Cli/For caso a forma de tributação não esteja preenchida no tributo.

A opção “Nenhuma forma de tributação definida” (00) no tributo é considerada como não preenchimento.

Disponível a partir da biblioteca 12.1.2306
