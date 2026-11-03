---
content_hash: 3f07cb53f31989734fad110fd043eb79575a092a93b232aa84204d1ad1c982e8
fetched_at: '2026-06-29T00:06:23.393317+00:00'
page_id: '224101583'
product: rm
source: tdn-rm
title: TU0264_DT_Verificacao_Formula_Pensao_Letra_Minuscula
type: documentation
url: https://tdn.totvs.com/display/LRM/TU0264_DT_Verificacao_Formula_Pensao_Letra_Minuscula
version: 120
---

# VERIFICAÇÃO DA FÓRMULA DE PENSÃO NÃO CONSIDERA LETRAS MINÚSCULAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Quando a função de fórmula VALORCODCALCULO, passando como parâmetro a CODCALCULOCORRENTE, é utilizada em uma fórmula de pensão informada dentro do cadastro do dependente, a execução da fórmula entra em recursividade, resultando em um travamento do processo.*  *Isto ocorre porque o evento de CC 13 irá calcular a fórmula do dependente, que por sua vez, chama o cálculo do CC 13, que novamente chama a fórmula do dependente... e assim entra em loop.*  *Já existia no sistema um tratamento para detectar a ocorrência desta situação, e exibir uma mensagem de erro para o usuário. Entretanto estava sendo tratado somente as funções com letras maiúsculas.* |
| **Solução/Implementação:** | *Ajuste na consistência de utilização das funções VALORCODCALCULO e CODCALCULOCORRENTE na fórmula de pensão, informada dentro do cadastro do dependente, para exibir a mensagem de erro para o usuário, independente de utilização de letras maiúsculas ou minúsculas.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TU0264* |
| **Requisito (ISSUE):** | N/A*.* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
