---
content_hash: 5e04f364ce800e6cfe2cdbfe5997c571d4f1aadaa6d87e993d850012e0550160
fetched_at: '2026-06-29T00:11:26.752314+00:00'
page_id: '720341586'
product: rm
source: tdn-rm
title: DT - Cálculo de Média com evento de Salário Composto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=720341586
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Cálculo de Média |
| País: | Brasil |
| Ticket: | [#10202627](https://totvssuporte.zendesk.com/agent/tickets/10202627 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-860](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-860) |

## **02. SITUAÇÃO/REQUISITO**

Quando um funcionário possui um evento que compõe salário e o mesmo pertece a um grupo de médias, ao fazer o cálculo de 13º Salário, Férias, Aviso prévio, Rescisão e Licenaç Maternidade é considerado o ultimo salário hora para o cálculo de média. Porém, quando o evento não faz mais parte da composição salarial é considerado o valor lançado na Ficha Financeira sem fazer a atualização do valor hora atual.

## **03. SOLUÇÃO**

Foi criado o parametro '**Média de evento salário composto em meses anteriores deve atualizar valor com salário atual**' em Configuraçãoes | Parametrizador | Folha Normal | Cálculo 1/2 que, quando marcado irá considerar o valor do salário hora do cadastro do funcionário para o calculo de média de um evento que fazia parte da composição salarial.

Parâmetro Marcado, Parâmetro Desmarcado, Passo 03, Passo 04passo1,passo2

Histórico de Salário do Funcionário:

yespasso1

Com parâmetro Marcado:

Para o evento 0253 considerou o salário hora do Funcionário. Os demais eventos considerou o salário hora da composição salarial de cada evento:

nopasso2

Com o Parâmetro Desmarcado:

Para o evento 0253 considerou os valores lançados na Ficha Financeira. Os demais eventos considerou o salário hora da composição salarial de cada evento:

## **04. DEMAIS INFORMAÇÕES**

O parâmetro foi tratado para todos os cálculos de média configurado nos grupos de média do sindicato.

## **05. ASSUNTOS RELACIONADOS**
