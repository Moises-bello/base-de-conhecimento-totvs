---
content_hash: adef837c55822b4b7088c44176cd6f8b2c1a1b6fd86f91baeecde56800ac294c
fetched_at: '2026-06-29T00:08:30.998093+00:00'
page_id: '272711392'
product: rm
source: tdn-rm
title: MEDU-3214_DT_Geracao_Lancamentos_Aproveitamento_Conta_Corrente
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-3214_DT_Geracao_Lancamentos_Aproveitamento_Conta_Corrente
version: 111
---

# GERAÇÃO DE LANÇAMENTOS COM APROVEITAMENTO DE CONTA CORRENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Função:** | *Regeração de lançamentos cancelados com aproveitamento em conta corrente* |
| **Situação/Requisito:** | Ao tentar regerar um lançamento com aproveitamento de valores em conta corrente o sistema está apresentando erro devido a tentativa de geração de um lançamento com valor negativo.  O erro estava ocorrendo devido a falta de parametrização dos valores opcionais de cobrança retroativa para aproveitamento desses valores. |
| **Solução/Implementação:** | *Foi realizado um ajuste no sistema para impedir a execução do processo de geração de lançamento quando ão houver parametrização dos valores opcionais de cobrança retroativa. Quando essa situação ocorrer, será gerado um erro informando a falta de parametrização.*  *Como essa parametrização não pode ser realizada após a movimentação da conta corrente, foi realizado um ajuste para permitir sua alteração caso o campo esteja vazio.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | EDUCACIONAL01-45 |
| **Requisito (ISSUE):** | *N/A* |

divs

96785
