---
content_hash: add3dbd78d2edb516eccc2f7e916443379e7184f1548887a981c0678cde4660a
fetched_at: '2026-06-29T00:06:00.499528+00:00'
page_id: '196809180'
product: rm
source: tdn-rm
title: DT_Disponibilizar_informações_de_notas_e_faltas_do_aluno_na_Central_do_Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=196809180
version: 10
---

# DISPONIBILIZAR INFORMAÇÕES DE NOTAS E FALTAS DO ALUNO NA CENTRAL DO ALUNO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *TOTVS Gestão Educacional* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **EDU** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Central do Aluno.* | *Central do Aluno.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Central do Aluno** | *Central do Aluno* | |  |  | |
| **Cadastros Iniciais:** | **Cadastro de matricula no período letivo**  **Cadastro de turma disciplina .**  **Cadastro de etapas de notas e faltas na **turma/disciplina** **com a opção "exibe no portal" selecionada.**** |
| **Requisito (ISSUE):** | [PCREQ-5427](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-5427 "PCREQ-5427") |
| **País(es):** | *Todos* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Visualização das notas e faltas das disciplinas na central do aluno.

## Procedimento para Utilização

```
As notas e faltas das disciplinas com suas respectivas etapas passaram a ser visualizadas na "Central do Aluno".
```

```
Sendo assim, siga os seguintes passos:
```

**1º Passo)** Entre na visão de Alunos.

**2º Passo)** Selecione o aluno e clique no botão "Central do Aluno" .

**3º Passo)** Ao abrir a "Central do Aluno", clique no menu "Matrícula" localizado à esquerda da tela.

**4º Passo)** Escolha a matrícula no período letivo desejada, caso exista mais de uma.

**5º Passo)** Clique no menu "Notas das etapas" ou "Faltas das etapas".

**6º Passo)** Dê um duplo clique na etapa desejada para visualizar o detalhamento, seja das notas (notas das avaliações da etapa) ou seja das faltas (faltas da etapa).

Observação:

As informações exibidas na Central do Aluno relacionadas aos itens "Notas das etapas" e/ou "Faltas das etapas" respeitam a mesma informação que o aluno possui ao acessar suas notas e faltas pelo Portal. Por exemplo: apenas etapas de falta e nota que contenham o campo "Exibe no portal e na central do aluno" marcado estarão visíveis na Central do Aluno. Outro parâmetro a ser validado é: "Visível para seleção no contexto educacional do Portal", este parâmetro fica no cadastro da situação de matrícula na guia Portal Corpore.net. Caso o parâmetro que controla se a visualização de notas e/ou faltas vai ser disponibilizada após liberação do professor estiver habilitado, o parâmetro na etapa de "Disponível para os alunos" também será validado.
