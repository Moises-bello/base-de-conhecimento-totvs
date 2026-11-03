---
content_hash: 2acf0e355a1a3ce6ee4e49bb0b276671b3ad130cf997532e51eb6765033543ff
fetched_at: '2026-06-29T00:08:26.266353+00:00'
page_id: '271170370'
product: rm
source: tdn-rm
title: MRH-3836 DT Mov Pensao Ferias Transferido
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3836+DT+Mov+Pensao+Ferias+Transferido
version: 112
---

# MOVIMENTO DE PENSÃO DE FÉRIAS TRANSFERIDO PARA A NOVA CHAPA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão por Transferência* |
| **Situação/Requisito:** | *Quando o funcionário é transferido um dia após o retorno das férias e as mesmas são pagas no mês caixa anterior, são lançados os eventos Base de Cálculo (CC's 335 a 339) na chapa demitida e os eventos de férias são transferidos para a chapa ativa.*  *Porém os movimentos dos dependentes são transferidos também para a chapa ativa, com referência de pagamento no mês anterior a transferência (mesmo mês de pagamento das férias).*  *Como a DIRF tem que detalhar o desconto de pensão por dependente, estes valores não estão sendo levados nem na chapa demitida, pois não existem mais, e nem na chapa ativa, pois a data de pagamento é anterior a data de transferência.* |
| **Solução/Implementação:** | *No processo de transferência, quando é marcada a opção para transferir movimento mensal, verificar se existe pensão alimentícia de férias pagas no mês caixa anterior, e neste caso manter o registro de movimentação da pensão no dependente da chapa demitida.* |
| **Chamados relacionados:** | MRH-3836 |
| **Requisito (ISSUE):** | MRH-3836 |

divs
