---
content_hash: 39ec618542834728f825547b92831d38e6eefdebcb14bbef60e60936fc8b63fe
fetched_at: '2026-06-29T00:06:16.875497+00:00'
page_id: '212900946'
product: rm
source: tdn-rm
title: ER_PCREQ-8591_ Informações_Mudança_Turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212900946
version: 7
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [R\_EDU\_EDU015](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_EDU_EDU015 "R_EDU_EDU015") | **IRM1** | [PCREQ-8590](http://jira.totvs.com.br/browse/PCREQ-8590) |
| **Requisito1** | [PCREQ-859](http://jira.totvs.com.br/browse/PCREQ-8590)1 | **Subtarefa1** | PDR\_EDU015-3 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Detalhar as alterações na funcionalidade de mudança de turma do TOTVS Educacional para o contexto de Ensino Superior.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Mudar turma | Alteração | Currículo e Oferta | Aluno  Anexo: Matrícula no Período Letivo  Processo: Mudar turma | - |
|  |  |  |  |

### **Mudança de Turma - Atualmente**

Durante o processo de mudança de turma, contexto do Ensino Superior, no passo “Seleção de disciplinas”, o sistema disponibiliza uma visualização no formato de árvore (*Treeview*): as disciplinas, turmas disciplinas e caso exista, as subturmas.

Os dados das entidades são exibidos ao usuário do sistema da seguinte maneira:

**Disciplina** / Código da Disciplina – Nome da Disciplina

**Turma Disciplina** / Código da Turma

**Subturma** / Código da subturma

### 

### **Mudança de Turma - Proposto**

Durante a mesma etapa de “Seleção de disciplinas”, o sistema para o contexto de Ensino Superior irá disponibilizar novos dados referente as disciplinas, turmas disciplinas, e subturmas visando agilizar o processo de escolha.

Novas colunas referente as disciplinas que serão disponibilizadas:

* + Número de Créditos (Número de Créditos – SDISCIPLINA ou SDISCGRADEALUNO);
  + Carga Horária (Carga horária – SDISCIPLINA ou SDISCGRADEALUNO);
  + Período (Código do Período – SPERIODO ou SPERIODOALUNO).

Novas colunas referente as turmas/disciplinas que serão disponibilizadas:

* + Curso (Nome do Curso – SCURSO);
  + Habilitação (Nome da Habilitação – SHABILITACAO);
  + Grade (Nome da Grade – SGRADE);
  + Turno (Nome do Turno da Turma/Disciplina – STURNO);
  + Campus (Caso exista campus vinculado a Turma Disciplina, será exibido o nome do campus – SCAMPUS).
  + Número de Vagas (calculado pelo sistema, baseado nos parâmetros da turma/disciplina);
  + Tipo da turma - presencial, a distância ou semipresencial (tipo – STURMADISC);
  + Data de início (STURMADISC);
  + Data de fim (STURMADISC);
  + Nome da filial vinculada a turma disciplina (nome – GFILIAL);
  + Nome professor (Nome – PPESSOA);
  + Horário da turma/disciplina (SHORARIOTURMA);

Novos dados referentes as subturmas que serão disponibilizadas:

* + Horário da subturma (SHORARIOTURMA);

Os novos dados serão apresentados da seguinte maneira:

**Disciplina** / Código da disciplina - Nome da Disciplina - Número de Créditos - Carga Horária - Período

**Turma Disciplina** / Código da Turma – Nome do Campus - Nome do Curso – Nome da Habilitação – Nome da Grade – Nome do Turno – Número de Vagas – Tipo – Data de Início – Data de Fim – Nome da Filial

**Professores da Turma/Disciplina** / Nome do professor

**Horário da Turma/Disciplina** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Subturma** / Código da subturma

**Horário da Subturma** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Horários Subturma**

Serão exibidos os horários da subturma somente se o parâmetro do TOTVS Educacional, “Utilizar turma/disciplina e subturma com horários independentes” (Secretaria > Geral 2/5) estiver selecionado.

**Turma Livre**

É importante ressaltar que Turmas Livres serão apresentadas somente com o código da turma, o nome do campus, nome do turno, número de vagas, tipo da turma, data de início, data de fim e nome da filial.

Os novos dados serão apresentados da seguinte maneira:

**Disciplina** / Código da disciplina - Nome da Disciplina - Número de Créditos - Carga Horária - Período

**Turma Disciplina** / Código da Turma – Nome do Campus - Nome do Turno – Número de Vagas – Tipo – Data de Início – Data de Fim – Nome da Filial

**Horário da Turma/Disciplina** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Subturma** / Código da subturma

**Horário da Subturma** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Currículo Individual**

Alunos com currículo individual, serão apresentados dados da “Disciplina”, baseado no cadastro da Disciplina da Grade do Aluno (SDISCGRADEALUNO e SPERIODOALUNO).

Os novos dados serão apresentados da seguinte maneira em destaque:

**Disciplina** / Código da disciplina - Nome da Disciplina - **Número de Créditos - Carga Horária - Período**

**Turma Disciplina** / Código da Turma – Nome do Campus - Nome do Curso – Nome da Habilitação – Nome da Grade – Nome do Turno – Número de Vagas – Tipo – Data de Início – Data de Fim – Nome da Filial

**Horário da Turma/Disciplina** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Subturma** / Código da subturma

**Horário da Subturma** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
