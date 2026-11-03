---
content_hash: 4a653d0ff566ba8441692cc0b88238bf6dbb110e64c9a50facd3863d3080c70a
fetched_at: '2026-06-29T00:08:48.539563+00:00'
page_id: '325852069'
product: rm
source: tdn-rm
title: 1838246 EDUCACIONAL01-3482 DT Atualização de Irmãos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=325852069
version: 93
---

# COPIAR TURMAS ENTRE PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Atualização de Irmãos* |
| **Situação/Requisito:** | *Após alterar do nome do aluno e executar o processo de "atualização de irmãos", o aluno alterado era duplicado no cadastro de irmão pois o sistema identificava esse aluno como um novo registro.* |
| **Solução/Implementação:** | *Foi alterado o processo de atualização de irmão para que o sistema começasse a validar se o irmão já existe na base, caso exista o sistema somente atualiza o nome desse registro. Também foi alterado o cadastrado do aluno para que quando existir alteração no nome do aluno essa modificação também será propagada para o cadastro de irmão.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
