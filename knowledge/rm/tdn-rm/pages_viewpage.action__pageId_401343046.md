---
content_hash: 17df869940c261f0ba7c9d01c8b604573ce83d5b00f9d0978b55dfa09a90fce7
fetched_at: '2026-06-29T00:09:10.593674+00:00'
page_id: '401343046'
product: rm
source: tdn-rm
title: 3506871 FINANCEIRO01-8534 DT Exclusão de lançamentos financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=401343046
version: 1
---

# Exclusão de lançamentos financeiros

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Exclusão de lançamentos financeiros. |
| **Situação/Requisito:** | Ao tentar excluir um lançamento financeiro com status cancelado, o sistema está validando se o usuário tem permissão para poder cancelar os itens de baixa. |
| **Solução/Implementação:** | Ajustado o serviço de exclusão de itens de baixa, para poder verificar se o usuário tem permissão de excluir itens de baixa. Dessa forma, ao tentar excluir lançamentos que já estão cancelados e que  possuam itens de baixa, caso possua permissão de excluir itens de baixa o lançamento será excluído. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
