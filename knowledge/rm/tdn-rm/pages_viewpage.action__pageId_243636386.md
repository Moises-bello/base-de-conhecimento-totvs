---
content_hash: 95d5b2cb682019b480668531a5f483356cdef83600524c95a34327c77e737586
fetched_at: '2026-06-29T00:08:12.146472+00:00'
page_id: '243636386'
product: rm
source: tdn-rm
title: TTUWNG_DT_Cheques_Emissão_de_Cheques
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243636386
version: 121
---

# Cheques - Emissão de Cheques (sem baixar)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeria |
| **Função:** | Cheques - Emissão de Cheques (sem baixar) |
| **Situação/Requisito:** | Divergência entre as informações padrões de Tabelas Opcionais ao baixar um lançamento com o meio de pagamento Cheque, e a emissão de cheques pela visão de lançamentos financeiros. |
| **Solução/Implementação:** | Otimização realizada para utilizar o parâmetro "Na baixa de vários lançamentos, copiar tabelas opcionais apenas se forem iguais" (Baixa 1/5) para que tenha seu funcionamento estendido a Emissão de cheque pela visão de lançamentos financeiros assim como na baixa de lançamentos com meio de pagamento cheque.  Parâmetro se encontra em Contas a Pagar > Baixa > Manutenção de Baixas > Baixa 1/5.  O parâmetro pode assumir dois possíveis valores , verdadeiro (marcado) ou falso (desmarcado).  Para o parâmetro **Falso, desmarcado**:   * Ao baixar vários lançamentos em conjunto e informar o meio de pagamento cheque, será buscada as informações referente a tabelas opcionais de um lançamento, não fazendo verificação de dados iguais/diferentes; * Ao emitir cheque pela tela de visão referente a um conjunto de lançamentos, será buscada as informações referente a tabelas opcionais de um lançamento, não fazendo verificação de dados iguais/diferentes;   Para o parâmetro **Verdadeiro, marcado:**   * Ao baixar vários lançamentos em conjunto e informar o meio de pagamento cheque, será verificado para todos os valores de tabela opcional, se os valores são iguais para todos os lançamentos. Se sim, esta informação será armazenada no campo correspondente, se não, nenhum campo terá seu valor informado, não recebendo o valor do lançamento; * Ao emitir cheque pela tela de visão referente a um conjunto de lançamentos, e o selecionado "Um cheque para todos os lançamentos", será verificado, para todos os valores de tabela opcional, se os valores são iguais para todos os lançamentos. Se sim, esta informação será armazenada no campo correspondente, se não, nenhum campo terá seu valor informado, não recebendo o valor do lançamento; * Ao emitir cheque pela tela de visão referente a um conjunto de lançamentos, e o selecionado "Um cheque para cada Cliente / Fornecedor", será verificado,  para todos os valores de tabela opcional, se os valores são iguais para todos os lançamentos referente a cada cliente fornecedor correspondente. Se sim, esta informação será armazenada no campo correspondente,  se não, nenhum campo terá seu valor informado, não recebendo o valor do lançamento.   **Importante:**   * Emissão de cheques pela visão de lançamentos quando informado "Um cheque para cada lançamento" não terá seu comportamento alterado. * Emissão de cheques pela visão de lançamentos quando informado "Um cheque para cada Cliente / fornecedor" e "Informar dados apenas uma vez" não terá seu comportamento alterado. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | TTVM66 |
| **Requisito (ISSUE):** | FIN000156 |

divs
