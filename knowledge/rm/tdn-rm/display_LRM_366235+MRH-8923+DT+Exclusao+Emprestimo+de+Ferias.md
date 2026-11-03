---
content_hash: 579214b6f1f16907c690c1666a9c222f112caff46702acb763eb58c8fe4fd5c1
fetched_at: '2026-06-29T00:08:30.339168+00:00'
page_id: '272424921'
product: rm
source: tdn-rm
title: 366235 MRH-8923 DT Exclusao Emprestimo de Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/366235+MRH-8923+DT+Exclusao+Emprestimo+de+Ferias
version: 108
---

# EXCLUSÃO AUTOMÁTICA DO EMPRÉSTIMO DE FÉRIAS NO CANCELAMENTO DE MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cancelamento de Movimento* |
| **Situação/Requisito:** | Quando é utilizado o recurso de "Lançamento automático de empréstimo de férias", onde é cadastrado um empréstimo para o funcionário equivalente ao líquido do recibo de férias, ao efetuar o cancelamento do movimento marcando a opção “Atualiza cadastro de empréstimo”, não está sendo excluído o registro do empréstimo inserido pelo processo. |
| **Solução/Implementação:** | No módulo de Cancelamento do Movimento, quando for marcada a opção “Atualiza cadastro de empréstimo”, excluir o registro do empréstimo inserido pelo processo de Lançamento das Férias, conforme configuração na pasta Férias/Empréstimo do Parametrizador. |
| **Tickets relacionados:** | MRH-8923 |

divs
