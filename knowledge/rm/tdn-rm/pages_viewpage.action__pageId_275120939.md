---
content_hash: 7cacf4b82421c65716872d1fee3d173c82125700eaab359ff345ec84ee8b5d0d
fetched_at: '2026-06-29T00:08:35.250555+00:00'
page_id: '275120939'
product: rm
source: tdn-rm
title: 840450 EDUCACIONAL01-824 DT Evolução Vincular / Desvincular Pessoa com Cli/For
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=275120939
version: 97
---

# Vincular / Desvincular Cli / For

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Processo de vinculação / desvinculação do cliente / fornecedor com Pessoa |
| **Situação/Requisito:** | Atualmente o processo não permite selecionar mais de uma pessoa |
| **Solução/Implementação:** | Evolução no processo de Vincular / Desvincular cliente fornecedor a Pessoa para que seja possível executar o processo para várias Pessoas simultaneamente, ou seja, selecionar mais de um registro.  Comportamento:  **1º Selecionando apenas um registro**  O usuário deverá informar pontualmente qual será o código do cliente / fornecedor que será gerado (comportamento já aplicado antes da evolução).  **2º Selecionando mais de um registro**  Será necessário informar um código default de máscara baseado na máscara parametrizada no módulo TOTVS Gestão Financeira.  O código default respeitara a seguinte regra:  Caracteres válidos:  #   Somente números  l   Somente letras  L   Somente letras  a   Letras e números  A   Letras e números, converte pra maiúscula quando letra  Separadores:. , - : /"  Exemplo:  Máscara do Financeiro: L####  Código default correspondente a máscara: P####  Ao gerar o código o sistema vai criar o código assim: P0001, P0002.... |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
