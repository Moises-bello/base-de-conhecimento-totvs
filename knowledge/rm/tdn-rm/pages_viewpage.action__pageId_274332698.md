---
content_hash: a2cfd2409b0ab67bae5a502bc75c18516f4bb29ae8f08096528eab349f2d3ef0
fetched_at: '2026-06-29T00:08:33.890635+00:00'
page_id: '274332698'
product: rm
source: tdn-rm
title: 854570 FINANCEIRO01-729 Baixar com valor a maior um Título do Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274332698
version: 97
---

# BAIXA DE TÍTULO DO PROTHEUS NO RM COM VALOR A MAIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa de títulos do Protheus no RM. |
| **Situação/Requisito:** | Ao baixar com valor a maior um Título do Protheus gerado a partir de integração com o TOTVS Incorporação o TOTVS Gestão Financeira procede como esperado e baixa totalmente o título, acomodando a diferença de valor a maior no valor de integração PROTHEUS ARREDONDAMENTO MAIOR. Porém, na baixa, o Valor Original foi subtraído deste valor a maior, gerando uma diferença nos valores de baixa passados ao TOTVS Incorporação, deixando a parcela Parcialmente Baixada, quando deveria ficar como Quitada. |
| **Solução/Implementação:** | Ajustado o processo de baixa para nessa situação não subtrair do Valor Original a diferença encontrada seja a maior ou menor. O valor deve ser usado apenas para inclusão do valor de integração PROTHEUS ARREDONDAMENTO MAIOR ou Ajustado o processo de baixa para nessa situação não subtrair do Valor Original a diferença encontrada seja a maior ou menor. O valor deve ser usado apenas para inclusão do valor de integração PROTHEUS ARREDONDAMENTO MENOR . |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 854570. |
| **Requisito:** | FINANCEIRO01-729. |

divs
