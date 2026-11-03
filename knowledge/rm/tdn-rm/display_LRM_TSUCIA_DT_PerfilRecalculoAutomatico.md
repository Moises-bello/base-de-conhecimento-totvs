---
content_hash: 618e69911468f41a9757676bee6929370c40ba06c8d3d07fea046d97945027f3
fetched_at: '2026-06-29T00:06:00.543264+00:00'
page_id: '196811070'
product: rm
source: tdn-rm
title: TSUCIA_DT_PerfilRecalculoAutomatico
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUCIA_DT_PerfilRecalculoAutomatico
version: 4
---

# Perfil no Recálculo Automático

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Recálculo Automático executado nos Relatórios* |
| **Situação/Requisito:** | *O recálculo automático chamado nos módulos de relatórios não está respeitando o filtro do perfil do usuário.* |
| **Solução/Implementação:** | *Ajustar no recálculo automático executado nos módulos de relatórios, para respeitar o filtro do perfil do usuário, no momento de fazer a seleção dos funcionários que serão processados.*  *Estava sendo recalculada a movimentação de todos os funcionários que tiveram parametrização alterada, mesmo que não constava na permissão cadastrada para o usuário logado.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSUCIA |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.39, 11.82.40* |
