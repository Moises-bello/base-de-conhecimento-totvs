---
content_hash: c650259b1913010007d2cac3d3bd91050742d9fc77e28d2c0ad1e9e570dd6a7e
fetched_at: '2026-06-29T00:08:34.737291+00:00'
page_id: '274838108'
product: rm
source: tdn-rm
title: 602032 FINANCEIRO01-346 Retorno Cobrança Boleto Duplicado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274838108
version: 98
---

# RETORNO DE COBRANÇA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Retorno de cobrança. |
| **Situação/Requisito:** | Ao realizar um retorno de cobrança cujo arquivo possui duas linhas para o mesmo boleto (pagamento total em duplicidade) e a opção "Gerar um extrato para todos os lançamentos" está marcada o lançamento fica com status parcialmente baixado ao invés de baixado, além de criar um novo boleto com valor zerado. |
| **Solução/Implementação:** | A opção "Gerar um extrato para todos os lançamentos" não pode ser usada para arquivo que contenha retorno duplicado de boletos pois nesse caso é necessário não é possível a criação de um único extrato para diferentes baixas de um mesmo boleto. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 602032. |
| **Requisito:** | FINANCEIRO01-346. |

divs
