---
content_hash: e871f1e5f9b91034119a305855d0646e3ca46acbcf6d9a7f7133304a5c144f55
fetched_at: '2026-06-29T00:06:08.523660+00:00'
page_id: '201748969'
product: rm
source: tdn-rm
title: TTFRWC_DT_Consulta_Acervo_Retorna_Erro_Quando_Local_Com_Espaço_Final
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201748969
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
| **Versões/Release:** | *12.1.8* |
