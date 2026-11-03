---
content_hash: 2e3286d2ee7fdfa5f4b4aeb7c41bcb9f1e6d19a8b6f9e8a5171d9eda8fd99733
fetched_at: '2026-06-29T00:08:34.898841+00:00'
page_id: '274851375'
product: rm
source: tdn-rm
title: 664785 FOPCALCULO01-113 Cancelamento Com Insuficiencia de Saldo
type: documentation
url: https://tdn.totvs.com/display/LRM/664785+FOPCALCULO01-113+Cancelamento+Com+Insuficiencia+de+Saldo
version: 114
---

# CANCELAMENTO DE MOVIMENTO COM DESCONTOS DE PERÍODOS ANTERIORES POR INSUFICIÊNCIA DE SALDO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cancelamento de Movimento |
| **Situação/Requisito:** | Quando existe no envelope descontos lançados pelo grupo de eventos através da opção “Lançar Verbas com insuficiência de saldo do mês ou período anterior”, e este envelope é cancelado, o status do desconto na ficha financeira, aba “Verbas c/ insuficiência de Saldo” continua como 1-Descontado.  Com isso, não é possível efetuar o lançamento desse valor novamente em um novo processamento do grupo de eventos. |
| **Solução/Implementação:** | Gravar as informações do envelope de lançamento dos descontos guardados por insuficiência de saldo, para que em um eventual cancelamento do movimento, o evento possa ser identificado na ficha financeira, na aba “Verbas c/ insuficiência de Saldo”, e o seu status seja retornado para "0- Não Descontado". |
| **Tickets relacionados:** | FOPCALCULO01-113 |

divs
