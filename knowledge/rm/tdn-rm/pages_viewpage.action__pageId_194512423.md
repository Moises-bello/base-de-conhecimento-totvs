---
content_hash: c98403bf40ea90080eadba4e4c0ddb3f50a8d98e971524f8dad2c104275405e0
fetched_at: '2026-06-29T00:06:00.153024+00:00'
page_id: '194512423'
product: rm
source: tdn-rm
title: ER_PCREQ-5427_Disponibilizar_informações_de_notas_e_faltas_do_aluno_na_Central_do_Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=194512423
version: 10
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Gestão Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | R\_EDU011 | **IRM1** | PCREQ-5426 |
| **Requisito1** | PCREQ-5427 | **Subtarefa1** | [PDR\_EDU\_EDU011-493](http://jira.totvs.com.br/browse/PDR_EDU_EDU011-424) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir o usuário visualizar as notas e faltas das disciplinas em suas etapas, por meio da Central do Aluno.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Especificação de produto:  $/RM/Documentos/Edu-Educacional/Especificações/Aluno/Especificação - Alunos.docx | [Alteração] | “Currículo e Oferta”->“Alunos” (Botão “Central do Aluno”) | - |

Na Central do Aluno, será possível visualizar as notas e faltas das disciplinas nas respectivas etapas referentes à matrícula do Aluno no período letivo. Para tal, foram adicionados dois novos grids na opção **Matrícula**, sendo o primeiro referente a etapa de notas e a segunda, a etapa de faltas. Caso o usuário selecione uma etapa de nota (duplo *click*) da disciplina no grid de notas, serão exibidas as notas das avaliações daquela etapa. O mesmo ocorrerá para o grid de faltas, que exibirá o detalhamento das faltas daquela disciplina e etapa.

Os dados a compor a grid de notas serão:

* Nome da Filial
* Código da turma
* Código da disciplina
* Nome da disciplina
* Situação na disciplina
* Notas das etapas... (ver protótipo)

Os dados a compor a grid de faltas serão:

* Nome da Filial
* Código da turma
* Código da disciplina
* Nome da disciplina
* Situação na disciplina
* Falta das etapas...(ver protótipo)

Os dados a compor a grid de notas de avaliação da etapa serão:

* Avaliação
* Data da avaliação
* Valor da avaliação
* Nota obtida
* Data de devolução

Os dados a compor a grid de faltas da etapa serão:

* Dia da semana
* Data da aula
* Inicio
* Fim
* Justificada?
* Abono falta?
* Motivo

As informações exibidas na Central do Aluno relacionadas aos itens "Notas das etapas" e/ou "Faltas das etapas" respeitam a mesma informação que o aluno possui ao acessar suas notas e faltas pelo Portal. Por exemplo: apenas etapas de falta e nota que contenham o campo "Exibe no portal e na central do aluno" marcado estarão visíveis na Central do Aluno. Outro parâmetro a ser validado é: "Visível para seleção no contexto educacional do Portal", este parâmetro fica no cadastro da situação de matrícula na guia Portal Corpore.net. Caso o parâmetro que controla se a visualização de notas e/ou faltas vai ser disponibilizada após liberação do professor estiver habilitado, o parâmetro na etapa de "Disponível para os alunos" também será validado.

### Protótipo de Tela

**Protótipo 01**

* Notas e faltas das etapas das disciplinas

**Protótipo 02**

* Notas de avaliação da etapa da disciplina

**Protótipo 03**

* Faltas da etapa da disciplina

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
