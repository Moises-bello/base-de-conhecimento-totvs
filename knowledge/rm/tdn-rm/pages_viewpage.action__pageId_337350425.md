---
content_hash: 002f14a59e703ba8237cb7aee9227b3915897c4c26bc24ffd78983cf389e5e3f
fetched_at: '2026-06-29T00:08:51.587263+00:00'
page_id: '337350425'
product: rm
source: tdn-rm
title: NFS-e RJ - TAG <tipotrib> gerada incorretamente.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337350425
version: 86
---

# NFS-e - RJ

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Retorno de autorização da NFS-e |
| **Situação/Requisito:** | Está sendo apresentada a seguinte mensagem de inconsistência no processo de envio da nota fiscal para a Prefeitura do Rio de Janeiro:  **" \*Enviar NFS-e: Erro no envio da NFS-e\***  **\*TSS - Erro na validação desta nota.\***  **\*\*Element 'tipotrib': [facet 'enumeration'] The value '0' is not an element of the set**  **{'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'}** |
| **Solução/Implementação:** | Ajustado o envio de NFS-e para que gere a tag “tipotrib” de acordo com a regra que deveria ser gerada, de acordo com a especificação. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | [1676403](https://totvssuporte.zendesk.com/agent/tickets/1676403 "Open ticket in Zendesk Support") |
| **Requisito:** | -- |

divs
