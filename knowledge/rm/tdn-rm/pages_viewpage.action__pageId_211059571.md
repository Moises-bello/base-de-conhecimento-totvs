---
content_hash: 071ecdcdbb0655e270a2a3ed28a4675ad8f87e9f70b4a8afa5424a31fdf8853f
fetched_at: '2026-06-29T00:06:15.629176+00:00'
page_id: '211059571'
product: rm
source: tdn-rm
title: TSYIZQ_DT_Integração_Cupom_Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=211059571
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
| **Versões/Release:** | 11.82.42 |
| **Versão Corrigida:** | NA |
| **Versão Expedida:** | NA |

divs
