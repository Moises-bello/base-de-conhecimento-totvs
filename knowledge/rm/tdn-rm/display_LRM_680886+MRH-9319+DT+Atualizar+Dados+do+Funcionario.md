---
content_hash: 214c4a453dd01d3730808b91f63638efc93a0588f36d45b97f803592da4a621b
fetched_at: '2026-06-29T00:08:31.197155+00:00'
page_id: '273295038'
product: rm
source: tdn-rm
title: 680886 MRH-9319 DT Atualizar Dados do Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/680886+MRH-9319+DT+Atualizar+Dados+do+Funcionario
version: 109
---

# ATUALIZAR DADOS DO FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Atualizar dados do funcionário |
| **Situação/Requisito:** | O sistema apresenta erro ao salvar qualquer alteração no cadastro da chapa “052015000658” Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados. Código da Informação: [98f4e2a0e6d84ed8fc0c1238f25a6d5f] |
| **Solução/Implementação:** | Realocado a chamada do método SetarProps() que estava no bindingSource\_AfterRead() para dentro do FopFuncionarioForm\_Load(), pois estava gerando um problema AcceptChanges() na Lib. |
| **Tickets relacionados:** | * [680886](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22680886%22 "680886") |

divs
