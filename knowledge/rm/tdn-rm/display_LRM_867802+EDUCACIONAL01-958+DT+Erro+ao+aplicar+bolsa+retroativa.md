---
content_hash: 837eea63399385fd930d755e8ebdb7a49bde9af97d42cd4cfc84bebd443d47e8
fetched_at: '2026-06-29T00:08:36.914775+00:00'
page_id: '284854694'
product: rm
source: tdn-rm
title: 867802 EDUCACIONAL01-958 DT Erro ao aplicar bolsa retroativa
type: documentation
url: https://tdn.totvs.com/display/LRM/867802+EDUCACIONAL01-958+DT+Erro+ao+aplicar+bolsa+retroativa
version: 100
---

# GERAÇÃO DE LANÇAMENTOS FINANCEIROS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos financeiros |
| **Situação/Requisito:** | Ao executar o processo de bolsa retroativa para uma bolsa exclusiva para mais de uma parcela do contrato, pode ocorrer, durante o aproveitamento do crédito gerado pela parcela anterior, que devido o arredondamento do valor da bolsa, o lançamento fique com valor líquido negativo, impedindo assim a regeração do lançamento e conseguintemente a execução do processo de bolsa retroativa para o contrato em questão. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, de forma que, antes de aproveitar valores da conta corrente do aluno, o valor de bolsa exclusiva seja arredondado, conforme as regras do financeiro, afim de se evitar que  valor líquido do lançamento fique negativo, devido arredondamento da bolsa exclusiva. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
