---
content_hash: d44edb9cd5d3d2562c436ca3b674302fb12975845b84c359d8984ca9aaa2ede5
fetched_at: '2026-06-29T00:06:15.633514+00:00'
page_id: '211059579'
product: rm
source: tdn-rm
title: TTOHRT_DT_Integração_Cupom_Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=211059579
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Integração de Cupom Fiscal em Modo Server |
| **Situação/Requisito:** | Existe um cupom fiscal no sistema onde o movimento se encontra quitado (baixa lançamento vencimento emissão). Ao  importar o arquivo de integração onde este cupom será cancelado o sistema não permite que o movimento seja cancelado  apresentando mensagem informando que o movimento esta quitado e por isso não pode ser cancelado. |
| **Solução/Implementação:** | Ajuste na importação do arquivo de integração para que o lançamento seja estornado antes do cancelamento do  movimento. |
| **Conversores e Parâmetros:** | NA |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | NA |
| **Versões/Release:** | 12.1.9 |
| **Versão Corrigida:** | NA |
| **Versão Expedida:** | NA |

divs
