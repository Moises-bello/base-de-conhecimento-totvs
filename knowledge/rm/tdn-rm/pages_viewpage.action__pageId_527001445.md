---
content_hash: 2ba818c595b48d76b14a8e203c004bd294e9089928318c879f1014f73cbaa5ac
fetched_at: '2026-06-29T00:10:32.518178+00:00'
page_id: '527001445'
product: rm
source: tdn-rm
title: DT Rematricula revitalizada - Ensino básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527001445
version: 13
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Rematrícula |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-11728  EDUCACIONAL01-11729  EDUCACIONAL01-13458  EDUCACIONAL01-13460 |

## **02. SITUAÇÃO/REQUISITO**

O processo de rematrícula do ensino básico necessitava de uma revitalização para melhorar a usabilidade da tela e também para otimizar o processamento.

## **03. SOLUÇÃO**

Foi criado uma nova tela otimizada além de vários ajustes no processo para ganhar em performance, foi também implementado a possibilidade de utilizar o fracionamento de jobs.

Nesta tela é possível visualizar quem é o próximo período letivo e pré-visualizar os alunos que serão considerados na rematrícula.

Ao clicar na pré-visualização de alunos irá ser aberto a lista de alunos que serão considerados para a rematrícula. Dependendo do filtro efetuado na tela principal da rematrícula, o número de alunos poderá ser muito grande, ocasionando uma lentidão ao trazer os alunos.

Importante

Não é possível remover ou adicionar alunos por meio desta tela de pré-visualização, ela traz todos os alunos que mediante filtro da tela principal da rematrícula.

### Multi Contexto

Foi implementando a possibilidade de utilizar a rematrícula para múltiplos contextos. Ao clicar no botão de seleção dos contextos irá abrir uma tela com os contextos disponíveis para seleção mediante filtro.

Os contextos que serão exibidos, serão os que possuem:

* Permissão no contexto.
* Permissão no item de rematrícula no contexto.
* Relação de cadastro (de-para) entre períodos letivos entre o contexto logado e os outros contextos.

Ao marcar os contextos e clicar no botão **Selecionar contextos** todos os contextos que foram selecionados serão considerados na execução da rematrícula.

Seleção do contexto logado

Lembrando que, para considerar o contexto logado na rematrícula, o mesmo deve ser selecionado nesta tela, ou seja, se não selecionar o contexto logado, o mesmo não será considerado na rematrícula.

Este comportamento de abrir uma tela de seleção de contextos está disponível nos patches 12.1.27.182, 12.1.28.115 e release 12.1.29.

A utilização da funcionalidade de multi contexto requer algumas regras:

* Possuir permissão no perfil para utilizar o multi contexto:
* Os contextos que poderão ser utilizados devem possuir a mesma apresentação, ou seja, só serão utilizados contextos do tipo "ensino básico".
* O usuário que está executando a operação deve possuir permissão nos perfis quanto na funcionalidade de rematrícula nos contextos que serão utilizados.
* As relações de cadastro entre coligadas e filiais devem existir para os itens "período letivo", "situação" e "turno".

Ao executar o processo todas as relações de cadastro (período letivo, situações de matrícula, e turno) serão validadas se existem para cada contexto. Com isso, o contexto que estiver com as relações de cadastro criadas o mesmo será executado a rematrícula, caso não exista alguma relação de cadastro para o contexto, ele não será considerado na rematrícula.

### Filtros

Foram implementados filtros para a rematrícula, estes filtros são complementares aos dados básicos como período letivo e situações da matrícula, porém não será possível utilizar os três filtros, será permitido somente a utilização de um deles.

##### Filtro genérico

* Filtra conforme a visão de matrículas de alunos.

##### Filtro por Período letivo / Matriz Aplicada

* Filtra utilizando o período letivo informando juntamente com a matriz aplicada.

Observações

Não é permitido utilizar este filtro quando a opção de multi contexto for utilizada.

##### Filtro por Consulta SQL

* Permite a utilização de uma consulta SQL obedecendo as informações mínimas para filtrar os alunos.

**Observação**: é necessário selecionar os campos CODCOLIGADA, RA da tabela SALUNO, NOME da tabela PPESSOA, IDPERLET e CODSTATUS da SMATRICPL

Observações

Não é permitido utilizar este filtro quando a opção de multi contexto for utilizada.

Informações Complementares

---
