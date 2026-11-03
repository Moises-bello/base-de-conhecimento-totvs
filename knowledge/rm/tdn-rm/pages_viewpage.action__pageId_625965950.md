---
content_hash: daa95a096982e20326f46a987f78215c180a6e54a688d865390d5611e7c398fb
fetched_at: '2026-06-29T00:11:04.292038+00:00'
page_id: '625965950'
product: rm
source: tdn-rm
title: DT - Agrupamento para Salário Composto (Educacional)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625965950
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Totvs Folha de Pagamento |
| Função: | Agrupamento para Salário Composto (Educacional) |
| País: | Brasil |
| Ticket: | [11599201](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D%20%3D%20%2211599201%22) |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-13780](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-13780) |

## **02. SITUAÇÃO/REQUISITO**

No lançamento de eventos, através do módulo Folha Educacional | Agrupamento Salarial | Educacional para determinados registros, o sistema também lançava o evento para outros registros que não estavam no filtro aplicado.

## **03. SOLUÇÃO**

Foi criado em 'Configurar colunas' o campo 'Id. Turma' para melhor visualização dos eventos lançado de acordo com a relação entre o evento, professor,disciplina e turma.

## **04. DEMAIS INFORMAÇÕES**

Quando é efetuado o lançamento do evento, ele é lançado para turma/disciplina. O professor recebe o evento lançado por estar vinculado à turma/disciplina. No caso,  
se lançarmos o evento para uma determinada turma/disciplina será lançado para todos professores vinculados à ela, mesmo que não possua aulas semanais na turma/disciplina.

## **05. ASSUNTOS RELACIONADOS**

* [Agrupamento Salarial (RM Classis Net)](https://tdn.totvs.com.br/pages/editpage.action?pageId=452719886)
