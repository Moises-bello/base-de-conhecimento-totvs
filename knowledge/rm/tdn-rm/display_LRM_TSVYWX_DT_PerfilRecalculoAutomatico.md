---
content_hash: 5093167b10ca9697dfe5e5c1dc0d64c376ac5e86ddf0f5e5fef8b8cb8f802da9
fetched_at: '2026-06-29T00:06:00.634628+00:00'
page_id: '196812773'
product: rm
source: tdn-rm
title: TSVYWX_DT_PerfilRecalculoAutomatico
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVYWX_DT_PerfilRecalculoAutomatico
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Recálculo Automático executado nos Relatórios* |
| **Situação/Requisito:** | *O recálculo automático chamado nos módulos de relatórios não está respeitando o filtro do perfil do usuário.* |
| **Solução/Implementação:** | *Ajustar no recálculo automático executado nos módulos de relatórios, para respeitar o filtro do perfil do usuário, no momento de fazer a seleção dos funcionários que serão processados.*  *Estava sendo recalculada a movimentação de todos os funcionários que tiveram parametrização alterada, mesmo que não constava na permissão cadastrada para o usuário logado.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSVYWX |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
