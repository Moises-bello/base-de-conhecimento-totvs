---
content_hash: 9444302f4057cfc4fc85e3ccd8b4369ce5e573b69d64f97b0d235fb9ee7461da
fetched_at: '2026-06-29T00:09:53.673044+00:00'
page_id: '440855350'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-3899 DT Erro na Contabilização do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440855350
version: 84
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Contabilização por competência |
| **Situação/Requisito:** | Conforme analise, a contabilização de um contrato era realizada por parte do TOTVS Gestão Educacional, mas que porém nenhuma informação era processada pelo evento contábil e enviada para o TOTVS Gestão Contábil. Por consequência, a coluna IDOPERACAO da tabela SPARCELACONT era preenchido com valor null e assim a competência não era listada na visão de "contabilização" do contrato e nem processada novamente pelo processo de contabilização por competência. |
| **Solução/Implementação:** | Foi desenvolvida melhorias no Log do processo "Gera Contabilização" orientando o usuário a estornar a(s) competência(s) contabilizada(s) com IDOPERACAO nulo.. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
