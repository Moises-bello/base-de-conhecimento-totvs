---
content_hash: 7499267a487db28f2880bac0bc999ba751a89b3e3acb06202180f2f80d28246b
fetched_at: '2026-06-29T00:08:37.138024+00:00'
page_id: '284874796'
product: rm
source: tdn-rm
title: 801569 CONTROLADORIA01-214 DT Relatório Balancete
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284874796
version: 102
---

# Relatório Balancete

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Balancete |
| **Situação/Requisito:** | Ao emitir o relatório balancete marcando a opção: Quebra por Filial o relatório demora aproximadamente 1 hora para gerar e quando este gera é apresentada a mensagem a seguir: A matriz interna não pode expandir para maiores que Int32.MaxValue elementos. |
| **Solução/Implementação:** | Ajuste na geração do Balancete quando se marca a opção de quebra por Filial para que a lista (Contas x Filiais) gerada seja quebrada sempre que ultrapassar 1 milhão de elementos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
