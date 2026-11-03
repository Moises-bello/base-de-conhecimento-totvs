---
content_hash: 9b4aea0d7951d2236292d2b7ffeccb18d0069c402aeb3c6d214a86cf2e3e0a86
fetched_at: '2026-06-29T00:11:20.668954+00:00'
page_id: '687734985'
product: rm
source: tdn-rm
title: DT - Histórico Salarial Futuro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687734985
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Histórico Salarial Futuro |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | Histórico Salarial Futuro:  Transferência de Funcionários: [DRHCALCRM-2559](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2559) |

## **02. SITUAÇÃO/REQUISITO**

Sistema não permitia realizar a alteração do salarial para uma data futura sem que alterasse o valor do salário no cadastro de funcionário.

## **03. SOLUÇÃO**

Criado o parâmetro "Utiliza controle de alteração salarial futura" ao marcá-lo o sistema irá  passará a armazenar as alterações salariais futuras no cadastro Histórico Salarial Futuro.

Realizado tratamento na transferência individual e coletiva dos funcionários para alertar ao usuário da necessidade de excluir ou efetivar a alteração salarial futura nas chapas origem ou destino do funcionário transferido.

## **04. DEMAIS INFORMAÇÕES**
