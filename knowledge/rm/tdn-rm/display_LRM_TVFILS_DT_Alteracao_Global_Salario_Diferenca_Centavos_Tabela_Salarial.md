---
content_hash: 7e3c77af64b34bd8bbd090e5e889e0c16445ca84d457fe5ecc0bc5bc41cac496
fetched_at: '2026-06-29T00:08:13.284251+00:00'
page_id: '243661805'
product: rm
source: tdn-rm
title: TVFILS_DT_Alteracao_Global_Salario_Diferenca_Centavos_Tabela_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/TVFILS_DT_Alteracao_Global_Salario_Diferenca_Centavos_Tabela_Salarial
version: 117
---

# ALTERAÇÃO GLOBAL DE SALÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração Global de Salário com Tabela Salarial* |
| **Situação/Requisito:** | A rotina de alteração salarial está apresentando diferença para alguns funcionários.   O valor lançado para o cadastro do funcionário apresenta diferença a menor do valor informado na tabela salarial, as diferenças estão entre 1 e 2 centavos. |
| **Solução/Implementação:** | Ajustado o cálculo da alteração global de salário quando utiliza tabela salarial. Foi alterado o número de casas decimais para melhorar a precisão do cálculo do percentual de aumento. |
| **Chamados relacionados:** | *TVFILS* |

divs
