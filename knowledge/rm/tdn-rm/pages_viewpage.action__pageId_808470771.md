---
content_hash: d71da59c3b0df19e09bc6e3578d6a8b4b662408f42cb645d934a8b38f15fd6a5
fetched_at: '2026-06-29T00:11:44.010453+00:00'
page_id: '808470771'
product: rm
source: tdn-rm
title: FISCAL01-21442 - DT - Erro retorno transmissão Reinf MS1254
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808470771
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Reinf |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21419 |

## **02. SITUAÇÃO/REQUISITO**

O sistema está se perdendo na geração/transmissão dos eventos Reinf, quando a opção "Centralizado", no cadastro dos Parâmetros de Processos EFD-Reinf esta habilitado, e consta lançamentos do mesmo cliente, período, mas para filiais diferentes da filial matriz.

## **03. SOLUÇÃO**

Tag "nrInscEstab" do evento 4010 passa a ser gerado apenas com o CNPJ da filial em que foi criado o lançamento, tendo em vista que este evento não possui geração centralizada. Logicamente, isto se aplica independentemente de o parâmetro "Centralizado" estar marcado ou não.

Disponível a partir da biblioteca 12.1.2302
