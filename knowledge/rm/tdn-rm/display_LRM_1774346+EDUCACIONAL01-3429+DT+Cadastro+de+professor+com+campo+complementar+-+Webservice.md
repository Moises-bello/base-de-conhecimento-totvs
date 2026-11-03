---
content_hash: e3a66da119f00d465e725a43044321f9ebffc5cc606ee0c577693ec805218250
fetched_at: '2026-06-29T00:08:47.718104+00:00'
page_id: '320375395'
product: rm
source: tdn-rm
title: 1774346 EDUCACIONAL01-3429 DT Cadastro de professor com campo complementar
  - Webservice
type: documentation
url: https://tdn.totvs.com/display/LRM/1774346+EDUCACIONAL01-3429+DT+Cadastro+de+professor+com+campo+complementar+-+Webservice
version: 94
---

# CADASTRO DE PROFESSORES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Cadastro de professores |
| **Situação/Requisito:** | Ao tentar realizar o cadastro de um professor o sistema apresenta a mensagem "  A chapa do funcionário associado ao professor deve ser informada." e o cadastro não é realizado. |
| **Solução/Implementação:** | Verificamos que o XML enviado não continha todas as informações necessárias para a definição do contexto.  É necessário que sejam informados os códigos da coligada, filial e tipo de curso.  Foi encontrado, também, uma inconsistência na atualização de campos complementares via webservice que foi corrigida.  Segue link da documentação criada para utilização do webservice para o cadastro de professor:  Link: [Cadastro Professor - Webservice](http://tdn.totvs.com/x/XYkYEw) |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
