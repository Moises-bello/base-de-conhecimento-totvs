---
content_hash: b7b582fca981f10f348882ce8048ede28e0f449c70cc5138127087f9aa72fe0e
fetched_at: '2026-06-29T00:06:22.352212+00:00'
page_id: '223915077'
product: rm
source: tdn-rm
title: TTYEBS_DT_Contabilização_Contrato_Baixa_Por_Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223915077
version: 123
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | Ao gerar contabilização por competência para um contrato, em que suas parcelas estão geradas e baixadas por acordo, o sistema, passa a contabilizar o valor total do contrato de forma incorreta. As rotinas para geração de lançamentos, que são utilizadas pela simulação de valores, não trata lançamentos baixados por acordo. fazendo com que o sistema tente calcular um valor original para eles. Como o sistema não encontra parcelas para dividir os créditos, o valor inteiro do contrato é atribuído como o valor original do lançamento. |
| **Solução/Implementação:** | *Foi realizada otimização do processo de contabilização por competência para quando o contrato possuir todas as suas parcelas calculadas por crédito e com lançamentos financeiros gerados e baixados por acordo.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
