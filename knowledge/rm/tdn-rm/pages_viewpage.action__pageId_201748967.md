---
content_hash: 7f9fc2734605a593e6cee9d0d5b493a0140ac3b3136177822d1ccf4fc44977cd
fetched_at: '2026-06-29T00:06:08.519972+00:00'
page_id: '201748967'
product: rm
source: tdn-rm
title: TTCWDF_DT_Consulta_Acervo_Retorna_Erro_Quando_Local_Com_Espaço_Final
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201748967
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Pesquisa no Acervo* |
| **Situação/Requisito:** | *Quando é feita uma busca por assunto que retorna publicações que tenham no local o nome de uma cidade com espaço no final, o sistema gera erro na busca e não retorna nenhuma publicação.* |
| **Solução/Implementação:** | *Foi adicionado um tratamento para o local da publicação, para retirar os espaços no começo e no final caso existam, assim é feita a montagem corretamente da referência que será exibida no retorno da pesquisa na tela.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
