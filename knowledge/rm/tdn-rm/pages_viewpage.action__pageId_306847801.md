---
content_hash: 071396b79ef513b7e6322c92f611b72b0ae0b8088505d503fa8dfd739784b88a
fetched_at: '2026-06-29T00:08:43.824425+00:00'
page_id: '306847801'
product: rm
source: tdn-rm
title: 1420008 FINANCEIRO01-2890 Retorno bancário boleto registrado online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=306847801
version: 99
---

# RETORNO BANCÁRIO DE BOLETO REGISTRADO ONLINE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Retorno bancário. |
| **Situação/Requisito:** | Cliente utiliza a integração bancária com registro online e em alguns casos após fazer o registro do título nessa modalidade o banco envia um arquivo de retorno referente ao registro (mesmo não existindo uma remessa). Assim, após importação do mesmo, o status do boleto passa de **Registrado online** para **Registrado**, perdendo-se o histórico de que o título foi registrado online. |
| **Solução/Implementação:** | Caso o registro venha como registrado no retorno bancário mas o mesmo já se encontrado registrado online o campo **Status da Remessa** do boleto não será alterado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1420008. |
| **Requisito:** | FINANCEIRO01-2890. |

divs
