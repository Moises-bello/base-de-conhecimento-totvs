---
content_hash: 535f324145a2a2184c9bf32c7d1cc6411bdbc688b61261c4ca9ef81165bb9d3f
fetched_at: '2026-06-29T00:08:05.972820+00:00'
page_id: '236424871'
product: rm
source: tdn-rm
title: TUNJZZ_DT_Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236424871
version: 121
---

# Parâmetros

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Financeira* |
| **Função:** | Parâmetros |
| **Situação/Requisito:** | Geração de dois boletos com status em aberto, caso um lançamento baixado parcialmente com flag não gerar outro boleto, seja cancelado com a flag marcada. |
| **Solução/Implementação:** | Criado validação no parâmetro do Totvs Gestão Financeira Ambiente | Parâmetros | Gestão Financeira | 02.02 – Contas a Receber | Baixa a receber | Não Gerar outro boleto para lançamento após a baixa parcial para que ao selecionar esta opção, seja verificado se existe Lançamentos com boletos parcialmente baixados, e seja exibida a mensagem: "Existem lançamentos parcialmente baixados com boletos em aberto ou parcialmente baixados. A Alteração desse parâmetro, pode causar o não cancelamento do boleto gerado por baixa parcial, e com isso o cancelamento deverá ser feito manualmente." |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito (ISSUE):** | FIN000012 |

divs
