---
content_hash: 5d726719ba8d933586eea64af0f6936593282982dc66f3192a2740c81038a7ba
fetched_at: '2026-06-29T00:08:38.506554+00:00'
page_id: '285660473'
product: rm
source: tdn-rm
title: 680625 FINANCEIRO01-10 Contabilização de extrato em baixa por cheque com mútuo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285660473
version: 101
---

# APLICAÇÃO DEFAULT CONTÁBIL PARA GERAR CONTABILIZAÇÃO DE EXTRATO EM BAIXA POR CHEQUE COM MÚTUO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Contabilização de extrato criado via baixa de lançamento financeiro. |
| **Situação/Requisito:** | Ao baixar um lançamento utilizando meio de pagamento cheque com conta caixa parametrizada para gerar contabilização de mutuo e parametrizar na coligada destino que a contabilização do extrato irá obter os defaults contábeis da tabela opcional o sistema não encontra a conta contábil emitindo mensagem de não fechamento dos valores das partidas. |
| **Solução/Implementação:** | Foi alterado o processo de baixa para carregar os dados do cheque informado pelo meio de pagamento e enviando os mesmo corretamente para a geração dos lançamentos contábeis do extrato de caixa pelo evento parametrizado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 680625. |
| **Requisito:** | FINANCEIRO01-10 |

divs
