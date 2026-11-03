---
content_hash: 1390f0823ce8f154ed8d2e0c500138f7b83d56bc269fa7c2d933879e7edb01b8
fetched_at: '2026-06-29T00:08:43.265441+00:00'
page_id: '302416091'
product: rm
source: tdn-rm
title: 1362558 FINANCEIRO01-2538 DT Baixar Lançamento Financeiro via WS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=302416091
version: 97
---

# BAIXA DE LANÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | Ao realizar a execução do arquivo XML de baixa do DataProcess “FinTBCBaixaDataProcess” através do ExecuteWithXmlParams, informando um IDLAN inexistente na base de dados, o sistema retorna a seguinte mensagem de erro: “Incorrect syntax near ')'. Mais detalhes do processamento(log) se encontram no Gerenciamento de Jobs. Id do Job = 12475603 - Id. de Execução= 1 “. |
| **Solução/Implementação:** | Ajuste no serviço de itens de baixa para tratar casos em que é passado idlan não existente via WS. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |

divs
