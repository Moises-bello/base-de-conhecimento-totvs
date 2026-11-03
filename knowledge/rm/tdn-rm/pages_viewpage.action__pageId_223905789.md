---
content_hash: d7387cf0736955acbe1587cedb4212cb4ab89eb808fd84c7f4922ef63533a112
fetched_at: '2026-06-29T00:06:21.919226+00:00'
page_id: '223905789'
product: rm
source: tdn-rm
title: TTYCMW_DT_Contabilização_Contrato_Baixa_Por_Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223905789
version: 119
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
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
