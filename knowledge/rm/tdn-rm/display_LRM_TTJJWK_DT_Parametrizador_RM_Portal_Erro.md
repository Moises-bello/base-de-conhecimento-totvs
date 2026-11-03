---
content_hash: 9f94180c32eb1f210fbebe6eeb1b995ee42237e0be706394e3b32c490ec7aacf
fetched_at: '2026-06-29T00:06:11.923317+00:00'
page_id: '204965719'
product: rm
source: tdn-rm
title: TTJJWK_DT_Parametrizador_RM_Portal_Erro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJJWK_DT_Parametrizador_RM_Portal_Erro
version: 2
---

# PARAMETRIZADOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parametrizador RM Portal* |
| **Situação/Requisito:** | *Ao criar um novo parâmetro do RM Portal e reparametrizar ocorre o erro: O índice estava fora dos limites da matriz* |
| **Solução/Implementação:** | *Alterado serviço que ajustava os parâmetros já existentes do RM Portal. Não estava tratando quando o parâmetro não estava preenchido.* |
| **Chamados relacionados:** | TTJJWK |
| **Versões/Release:** | *11.82.41* |
