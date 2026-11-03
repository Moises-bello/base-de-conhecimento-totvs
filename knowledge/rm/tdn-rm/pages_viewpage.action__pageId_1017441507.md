---
content_hash: 2cab1531699074c5d349ee285c433a3714824389d8f776e4ef516796d47b077e
fetched_at: '2026-06-29T00:05:47.773856+00:00'
page_id: '1017441507'
product: rm
source: tdn-rm
title: Importação Empréstimos FEBRABAN / Crédito do Trabalhador - Portabilidade de
  Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1017441507
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Em casos de portabilidade do empréstimo do Crédito do Trabalhador, o número do contrato deverá ser mantido, contudo, o código do banco poderá ser alterado.

Nesse cenário, sempre que houver alteração do código do banco, essa informação deverá ser devidamente atualizada durante o processo de importação do arquivo da seguinte forma:

* + Dar baixa na linha do empréstimo atual  para manter o histórico do banco anterior.
  + Criar uma nova linha com data inicial conforme novo banco.

Dica:

Versão de liberação informada no

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios

Estando na competência de 03/2025 e importando um arquivo de 03/2025, foi alterado o banco do funcionário.

No cadastro de empréstimo está a importação do mês anterior 02/2025 com o Banco 001 e a data final do desconto em 04/2026

Importando o arquivo referente a competência onde para o mesmo contrato foi trocado o Banco para 104

A data final do desconto foi alterado para a competência do arquivo menos 1. Então como o arquivo é da competência 03/2025 a data final do desconto será 02/2025.

Criado novo cadastro com os mesmos dados do cadastro inicial mas com o Banco novo e a data da competência importada do arquivo atual

No cálculo do desconto será considerado apenas o valor desse último cadastro que está com a competência atual e data final de desconto posterior

## **03.** **TABELAS UTILIZADAS**

* PFEMPRT
* PFDESCEMPRT
