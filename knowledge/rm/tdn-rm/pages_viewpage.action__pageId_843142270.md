---
content_hash: 06d68b1c4f8a646f5bff5730fd17bfaa457d6e4bd5df126e9dff7ba483d25258
fetched_at: '2026-06-29T00:11:50.585422+00:00'
page_id: '843142270'
product: rm
source: tdn-rm
title: FISCAL01-22724 - Consolidação dos Valores PIS/COFINS em um único Período de
  Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=843142270
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Encerramento Período Apuração PIS/COFINS |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-22724 |

## **02. SITUAÇÃO/REQUISITO**

Implementação da Consolidação dos Valores PIS/COFINS em apenas um dos Períodos de Apuração

## **03. SOLUÇÃO**

Configuração dos Parâmetros de Rotina

A configuração do tributo principal deve ser realizada conforme abaixo:

Incluir(Cadastrar) dois Parâmetros no Anexo de Parâmetros da Rotina.

Com a Chave **APURACAO\_PIS** ou **APURACAO\_COFINS** e o valor deverá ser código do tributo

Exemplo:

Chave = APURAR\_PIS / Valor = "PIS"

Chave = APURAR\_COFINS / Valor = "COFINS"

obs.: O Valor deve ser igual ao Código do Tributo do Período de Apuração que se deseja fazer os Calculos da Consolidação PIS/COFINS.

Encerramento do Período

Alterar o processo de encerramento do Período de Apuração para reconhecer os parâmetros configurados onde:

* **Se** a base estiver configurada para utilizar o novo cálculo do PIS e COFINS. Deverá ser validado a existência do parâmetro APURAR\_XXX

* + **Se** o Parâmetro não estiver cadastrado, O Período deve ser encerrado informando um Alerta ao usuário. Este comportamento afetará todos os períodos de apuração dos tributos PIS e COFINS.
  + **Se** o parâmetro estiver cadastrado
    1. Quando não for o tributo principal: o período deve ser encerrado sem alertas e erros, mas na mensagem de sucesso, deve ser informado que o cálculo será realizado no período principal (informar o código do tributo).
    2. Quando for o tributo principal: Deverá proceder com a Apuração normalmente, apresentando erros e alertas quando necessário.
* **Se** Se a base não estiver configurada para utilizar o novo cálculo, o comportamento antigo deverá ser mantido.

Disponível à partir da biblioteca 12.1.2402
