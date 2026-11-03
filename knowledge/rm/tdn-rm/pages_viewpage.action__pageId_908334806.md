---
content_hash: a53bf1b764850b72d347e3f40d408506a3df5aea27ef28ac926502e1b14aedd6
fetched_at: '2026-06-29T00:12:03.382384+00:00'
page_id: '908334806'
product: rm
source: tdn-rm
title: FISCAL01-24905 - Nova Declaração Módulo de Inclusão de Tributos (MIT) - Tela
  de Geração da Rotina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=908334806
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | MIT |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24905 |

## **02. SITUAÇÃO/REQUISITO**

Através da IN RFB nº 2.237/2024, a Receita Federal unifica a DCTF e a DCTFWeb. Com a mudança, a DCTFWeb passa a ser denominada Declaração de Débitos e Créditos Tributários Federais.

A partir de 1º de janeiro de 2025, os débitos atualmente declarados na DCTF PGD passarão a ser declarados na DCTFWeb mensal, por intermédio do **Módulo de Inclusão de Tributos - MIT**. Ele funcionará como uma nova escrituração geradora de DCTFWeb, assim como o eSocial, a EFD-Reinf.

## **03. SOLUÇÃO**

Foi criado um novo processo que pode ser acessado nas obrigações acessórias, federais.

Ao informar os parâmetros na tela do processo é gerado um arquivo no formato JSON na pasta escolhida.

Disponível à partir da biblioteca 12.1.2406
