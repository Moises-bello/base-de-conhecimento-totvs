---
content_hash: 69f51699dd6cfaf67d3b3e412b0e72ccbc270649d02f31933f1741a381e561f6
fetched_at: '2026-06-29T00:08:38.320395+00:00'
page_id: '285647952'
product: rm
source: tdn-rm
title: 837119 EDUCACIONAL01-883 DT Erro na Geracao de Movimento de NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/837119+EDUCACIONAL01-883+DT+Erro+na+Geracao+de+Movimento+de+NFS-e
version: 101
---

# GERAÇÃO DE MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de movimento em regime de caixa |
| **Situação/Requisito:** | Ao gerar movimento em regime de caixa para um boleto oriundo de uma parcela do Educacional, o sistema sempre envia o código de serviço, conforme o tributo do produto no município da filial que está gerando o movimento, mesmo que o movimento esteja parametrizado para não editar município por item. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de movimento, permitindo ao sistema, que o código de serviço do produto no município seja carregado pelo TOTVS Gestão de Estoque, Compras e Faturamento, conforme parametrização do movimento. Se o movimento estiver parametrizado para editar município por item, o sistema buscará o código do serviço com base na tributação do item. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
