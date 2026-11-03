---
content_hash: 1c0d755f21dc5f30ecfee4329cc8342a24eb0cfbff01a7e78438f46ad26c6207
fetched_at: '2026-06-29T00:06:26.986892+00:00'
page_id: '227541296'
product: rm
source: tdn-rm
title: TUFIFJ_DT_Lancamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFIFJ_DT_Lancamento_Financeiro
version: 121
---

# Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | Folha de pagamento |
| **Função:** | *Lançamento Financeiro* |
| **Situação/Requisito:** | Ao gerar Guia de INSS marcando para seja feito também o lançamento financeiro, sistema retorna mensagem de erro: O Valor do rateio deve ser maior que zero  Foi verificado que a mensagem ocorre devido a ter uma funcionária com licença maternidade no mês com o valor líquido de lançamento negativo devido a dedução da licença maternidade, porém o valor total do lançamento é positivo. |
| **Solução/Implementação:** | Otimizado lançamento financeiro da guia de INSS de forma que, ao encontrar centro de custo com valor negativo, o sistema irá abater esse valor negativo da seguinte maneira:   * Primeiro o sistema tentará abater o valor de forma proporcional entre os rateios existentes no lançamento * Se não for possível o abatimento proporcional, o sistema tentará encontrar um rateio de valor maior ou igual ao valor negativo e abaterá desse valor     Em ambos os casos será enviada uma mensagem de aviso ao cliente informando a chapa que contém valor negativo e se o valor foi abatido proporcional ou qual o centro de custo que teve seu valor abatido |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUFIFJ TUILK5 |
| **Requisito (ISSUE):** |  |

divs
