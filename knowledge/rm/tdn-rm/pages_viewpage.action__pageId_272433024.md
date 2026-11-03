---
content_hash: cf354605709ddfd977f16a988e1a777d6a01c8f06e457d0b1ccfa95b8b6170a3
fetched_at: '2026-06-29T00:08:30.465294+00:00'
page_id: '272433024'
product: rm
source: tdn-rm
title: 551556 MRH-8346 DT Cadastro Geração Encargos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272433024
version: 108
---

# ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Encargos |
| **Situação/Requisito:** | Ao gerar o encargo tipo 8 - Provisão de FGTS de 13o. salário o sistema não esta respeitando o parâmetro "Abate adiantamento" quando o mesmo se encontra desmarcado, desta forma o sistema está sempre abatendo o valor do adiantamento na geração do encargo. |
| **Solução/Implementação:** | Foi criado um novo parâmetro chamado "Não abate adiantamento de 13º" pois o parâmetro anterior funcionava somente para o encargo do tipo 7 -Provisão de 13o. salário , desta forma foi preciso criar um novo parâmetro para atender a solicitação desejada. E o sistema não abater o valor de adiamantamento. |
| **Tickets relacionados:** | * [551556](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22431042%22 "431042") |

divs
