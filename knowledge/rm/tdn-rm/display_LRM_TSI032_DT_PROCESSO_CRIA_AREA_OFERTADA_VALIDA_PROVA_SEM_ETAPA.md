---
content_hash: a6847eee17d1388a6010e15872a16b832067708d6a619a197dc1f3eade5dd1da
fetched_at: '2026-06-29T00:06:04.930758+00:00'
page_id: '200912773'
product: rm
source: tdn-rm
title: TSI032_DT_PROCESSO_CRIA_AREA_OFERTADA_VALIDA_PROVA_SEM_ETAPA
type: documentation
url: https://tdn.totvs.com/display/LRM/TSI032_DT_PROCESSO_CRIA_AREA_OFERTADA_VALIDA_PROVA_SEM_ETAPA
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Criar área ofertada do processo seletivo* |
| **Situação/Requisito:** | *Quando a área ofertada criada possui mais de uma etapa com suas provas definidas o sistema retornava erro de validação da ordem do caderno de provas pois considerava todas as provas das etapas como uma única etapa.* |
| **Solução/Implementação:** | *Foi inserido uma validação para que se existir mais de uma etapa, verificar as provas por etapas, separando corretamente as etapas, proporcionando ao processo a execução correta quando há mais de uma etapa.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7* |
