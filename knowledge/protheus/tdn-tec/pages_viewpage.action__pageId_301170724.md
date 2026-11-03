---
content_hash: 077fc3d6641e6c104593811772eb7816641bd03da675dd5d6cbd7399c471033c
fetched_at: '2026-07-02T19:24:23.247405+00:00'
page_id: '301170724'
product: protheus
source: tdn-tec
title: Correção - Background de coluna congelada da TCBrowse.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301170724
version: 1
---

Correção - Background de coluna congelada da TCBrowse.

|  |  |
| --- | --- |
| Situação | Quando é utilizada a função SetBlkBackColor no componente TCBrowse, sendo que a primeira coluna está congelada (nFreeze = 1), as cores das linhas dessa coluna não são alteradas como as demais. As cores da coluna congelada ficam sempre alternadas com branco. |
| Ocorrência | Necessidade de aplicar nas linhas da coluna congelada a mesma cor de fundo das linhas das demais colunas do TCBrowse. |
| Correção | Foi aplicado um ajuste para que as linhas da coluna congelada recebam a pintura de background da mesma maneira que as linhas das demais colunas. |
| Informações adicionais | * Referente ao chamado: 1120447 * Referente à ocorrência: MTEC-584 * Disponível a partir da build 7.00.131227A - 13.2.3.22 |
