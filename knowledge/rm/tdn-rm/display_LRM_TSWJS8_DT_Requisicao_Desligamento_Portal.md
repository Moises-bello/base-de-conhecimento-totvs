---
content_hash: 6c44d62bcf4212908897fbe1faf282ae7945a7757d6dfea2ae78b1f8f3a89baf
fetched_at: '2026-06-29T00:06:00.875074+00:00'
page_id: '196813362'
product: rm
source: tdn-rm
title: TSWJS8_DT_Requisicao_Desligamento_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWJS8_DT_Requisicao_Desligamento_Portal
version: 4
---

# Requisição de Desligamento (Portal)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Gestão de Pessoas* |
| **Função:** | *Requisição de Desligamento (Portal)* |
| **Situação/Requisito:** | *Na lookup de funcionário do portal (web), caso o usuário logado fosse chefe em mais de uma coligada e possuí-se filtros de perfis em mais de uma coligada,*  *a lookup só pegava o filtro da coligada atual, limitando os resultados que eram retornados.* |
| **Solução/Implementação:** | *Foi adicionado o mesmo tratamento que havia na tela de Equipe/Subordinados, para buscar os filtros de perfil de todas as coligadas em que o usuário é chefe.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSWJS8* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
