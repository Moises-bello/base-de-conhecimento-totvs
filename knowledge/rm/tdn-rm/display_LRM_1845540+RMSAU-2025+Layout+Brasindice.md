---
content_hash: b4fc871c291228cc8cf76b219f914f75ad276b326ca50df007b0d71a75035495
fetched_at: '2026-06-29T00:08:51.724901+00:00'
page_id: '338366222'
product: rm
source: tdn-rm
title: 1845540 RMSAU-2025 Layout Brasindice
type: documentation
url: https://tdn.totvs.com/display/LRM/1845540+RMSAU-2025+Layout+Brasindice
version: 1
---

# Layout Brasindice

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Atualização Brasíndice |
| **Situação/Requisito:** | Ao importar arquivo, sistema apresentava erro de tamanho esperado ultrapassado. |
| **Solução/Implementação:** | A rotina foi atualização para atender a atualização do Layout Brasíndice que passou o tamanho do código laboratório de três para quatro dígitos. Tal atualização foi refletida nas tabelas do banco de dados e nos campos correspondentes na aplicação. Além disso, foi criado um *check* *box*, para que o usuário possa indicar qual tipo de arquivo está sendo importado. |
