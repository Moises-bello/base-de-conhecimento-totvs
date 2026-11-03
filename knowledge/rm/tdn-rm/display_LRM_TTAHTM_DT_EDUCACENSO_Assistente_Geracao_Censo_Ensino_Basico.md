---
content_hash: 64f80fea501266027ccb63166ac6ba5e66e9c83e619672cadc495628cee676e8
fetched_at: '2026-06-29T00:06:05.383261+00:00'
page_id: '201720831'
product: rm
source: tdn-rm
title: TTAHTM_DT_EDUCACENSO_Assistente_Geracao_Censo_Ensino_Basico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAHTM_DT_EDUCACENSO_Assistente_Geracao_Censo_Ensino_Basico
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Acadêmico* |
| **Função:** | *Censo do Ensino Básico* |
| **Situação/Requisito:** | O Assistente de preparação de dados do Censo não é concluído com sucesso e apresenta a mensagem: "O índice estava fora do intervalo. Ele deve ser não-negativo e menor que o tamanho da coleção. Nome do parâmetro: index" |
| **Solução/Implementação:** | O Assistente de preparação de dados passou a descartar as disciplinas ministradas exclusivamente em cursos que não são recenseados (não possuem código do INEP) evitando assim que o processo seja interrompido. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TTAHTM* |
| **Requisito (ISSUE):** | *Informe o requisito relacionado.* |
| **Versões/Release:** | *11.83.55* |
