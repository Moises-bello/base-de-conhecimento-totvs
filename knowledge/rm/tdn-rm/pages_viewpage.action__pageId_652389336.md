---
content_hash: 9404bd6969790a75cbb166f6776a2f1e8a200589413d0a27f09bc4e388e0782c
fetched_at: '2026-06-29T00:11:12.350306+00:00'
page_id: '652389336'
product: rm
source: tdn-rm
title: FISCAL01-15905 DT - Processo de Integração com Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652389336
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Gerar Lançamento Financeiro Guias ISS |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15905 |

## **02. SITUAÇÃO/REQUISITO**

Implementar conforme Solicitado

## **03. SOLUÇÃO**

Durante a Integração da Guia de ISS com o Financeiro, foi adicionado uma opção na tela do Processo "Utilizar Cliente/Fornecedor do Município".

Ao marcar esta opção, o campo referente ao Cli/For deve ser desabilitado e o processo deverá considerar o Município preenchido nos Dados Fiscais do Município.

Caso algum município não tenha o Cli/For preenchido, deverá ser informado no log uma mensagem informando que as guias não foram integradas

porque o cli/for do município não foi preenchido.
