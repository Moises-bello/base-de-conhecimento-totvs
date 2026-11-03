---
content_hash: 9f97ad6932d1d5c5df5eb76721baa4d3ddb6b74d598647a88dddf1d8c992cb30
fetched_at: '2026-06-29T00:10:42.288508+00:00'
page_id: '547238421'
product: rm
source: tdn-rm
title: EDUCACIONAL01-13593 DT Máscara no cadastro do curso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547238421
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Cadastro de curso |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-13593 |

## **02. SITUAÇÃO/REQUISITO**

No cadastro do curso existe o campo de máscara da turma, o mesmo está considerando os colchetes na contagem do número de caracteres da máscara. Entretanto, estes caracteres apenas indicam uma sessão, com isso, não devem ser contados no número de caracteres da máscara.

## **03. SOLUÇÃO**

Foi feita uma melhoria para desconsiderar colchetes na contagem do número de caracteres na máscara da turma no cadastro do curso. Além disso, foi colocado um ícone informativo ao lado do campo da máscara identificar todas as possíveis funções para usar na máscara.

Caso a máscara informada gerar um código de turma maior que 20 caracteres (número de caracteres do código de turma) uma mensagem será exibida ao usuário informando que a máscara irá extrapolar o código da turma.
