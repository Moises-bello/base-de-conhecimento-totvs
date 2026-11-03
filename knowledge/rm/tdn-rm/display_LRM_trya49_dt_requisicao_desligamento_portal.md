---
content_hash: 005ffce1cddd2650fda442b76bc2a4d085ab7eaad7537b54fddff966de1d7c2e
fetched_at: '2026-06-29T00:06:00.638801+00:00'
page_id: '196812885'
product: rm
source: tdn-rm
title: trya49_dt_requisicao_desligamento_portal
type: documentation
url: https://tdn.totvs.com/display/LRM/trya49_dt_requisicao_desligamento_portal
version: 3
---

# Requisição de Desligamento (Portal)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Totvs Gestão de Pessoas* |
| **Função:** | *Requisição de Desligamento (Portal)* |
| **Situação/Requisito:** | *Na lookup de funcionário do portal (web), caso o usuário logado fosse chefe em mais de uma coligada e possuísse filtros de usuários em mais de uma coligada,*  *a lookup somente acatava o filtro da coligada atual, limitando os resultados que eram retornados.* |
| **Solução/Implementação:** | *Foi adicionado o mesmo tratamento que havia na tela de Equipe/Subordinados, para buscar os filtros de perfil de todas as coligadas em que o usuário é chefe.* |
| **Chamados relacionados:** | TRYA49 |
| **Versões/Release:** | *11.82.40* |
