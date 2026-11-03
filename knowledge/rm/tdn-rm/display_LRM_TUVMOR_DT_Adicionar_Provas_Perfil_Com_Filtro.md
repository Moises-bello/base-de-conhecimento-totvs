---
content_hash: 32b1b7f1e535ef2a1581d99710f40bada3adb1558708a2ed56f381a1f9a1781b
fetched_at: '2026-06-29T00:08:07.215160+00:00'
page_id: '237373930'
product: rm
source: tdn-rm
title: TUVMOR_DT_Adicionar_Provas_Perfil_Com_Filtro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVMOR_DT_Adicionar_Provas_Perfil_Com_Filtro
version: 114
---

# PROVAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Adicionar provas com um perfil que utiliza filtros.* |
| **Situação/Requisito:** | *Quando um usuário possui filtro de perfil na tabela BPROVA o sistema retorna um erro impedindo a inclusão de provas pois é gerado com código de prova já existente.* |
| **Solução/Implementação:** | *Foi identificado que o processo utilizava o filtro do usuário para gerar o código da prova, e como era utilizado o filtro o sistema não retornava todos os códigos assim ocasionando a geração de um código de prova que já existe. Foi feito a remoção do filtro no momento de gerar o código e o problema não ocorreu mais.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
