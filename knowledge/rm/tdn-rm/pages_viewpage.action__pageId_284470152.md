---
content_hash: 5477a0748e3b63bae18dccf9ca12b27d956d61b1566faa21a6c4314969f2f4e3
fetched_at: '2026-06-29T00:08:36.239776+00:00'
page_id: '284470152'
product: rm
source: tdn-rm
title: 415970 FOPROTINAS01-88 DT Tipo de Anotação Código 0(zero)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284470152
version: 102
---

# Parametrizador

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Parametrização do RM Portal para os tipos de anotações. |
| **Situação/Requisito:** | Ao acessar um grupo de acesso em: “Configurações > Parametrizador > RM Portal > Grupo de acesso” RM portal o sistema apresenta mensagem: “O índice estava fora dos limites da matriz.”. |
| **Solução/Implementação:** | Ao acessar o Parametrizador do RM Portal o sistema passa a retirar da listagem de anotações pessoais o código de anotação zero, somente da listagem de opção e não data tabela dinâmica. Neste casso o sistema emitirá a seguinte mensagem: "Foi Removido da Lista de 'Anotações' a anotação de código 0(Zero). Para correta funcionalidade, deve ser excluído da tabela de Anotações Pessoais o código zero." "O Parametrizador desabilitará as anotações pessoais até o cadastro da tabela dinâmica ser ajustado." O sistema então passa a bloquear a listagem de anotações pessoais. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 415970 |
| **Requisito:** |  |

divs
