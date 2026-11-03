---
content_hash: 485a01ff672529f047a0fca1a5c51b92a4fffce7eece00109a989a62ef8c5876
fetched_at: '2026-06-29T00:06:24.118574+00:00'
page_id: '224112190'
product: rm
source: tdn-rm
title: ER_PCREQ_9358_Nao_permitir_matricular_em_lista_espera_quando_existir_corequisito
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ_9358_Nao_permitir_matricular_em_lista_espera_quando_existir_corequisito
version: 125
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações   Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | EDU |
| **Segmento Executor** | Eduacional | | |
| **Projeto1** | [R\_EDU\_EDU018](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_EDU_EDU018) | **IRM1** | [PCREQ-9358](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9358) |
| **Requisito1** | [PCREQ-9359](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9359) | **Subtarefa1** | [PDR\_EDU\_EDU018-17](http://jira.totvs.com.br/browse/PDR_EDU_EDU018-17) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos)

## Objetivo

Apresentar o comportamento da matrícula em disciplinas com correquisitos em turmas com lista de espera de acordo com o novo parâmetro do sistema.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Matrícula em Disciplina | Alteração | Matrícula > Matrícula | - |
| Matrícula em Lista de Espera | Alteração | Matrícula > Mais >Matrícula em Lista de Espera | - |
| Parametrização do Sistema | Alteração | Parametrização > Matrícula | - |
| Matrícula Online | Alteração | Portal > Aluno > Matrícula | - |

**Matrícula em lista de espera**

Surgiu a necessidade de clientes do TOTVS Educacional impedir matriculas quando envolver lista de espera e correquesito.

Será incluído um novo parâmetro de matrícula (parametrizador do sistema > Matrícula > Movimento 3/4), com o nome de “Bloquear matrícula em Lista de Espera em disciplinas com correquisito”. O parâmetro a ser criado estará disponível apenas quando o parâmetro para ativar a lista de espera estiver ativo.

Matriculas pelo sistema ou portal do TOTVS Educacional passarão a verificar o parâmetro supracitado somente se a matrícula em lista de espera estiver ativo, caso uma disciplina possua correquisito e não possuírem vagas nas turmas, o sistema apresentará uma mensagem de turma cheia e não possibilitará as matrículas.

A permissão de perfil de usuário “Matricular em turmas com excesso de alunos” continuará a ser superior as validações das matrículas relacionado a excesso de alunos nas turmas. Por isso, caso o novo parâmetro estiver marcado, a matricula for em turma/disciplina que possua correquisito e a permissão por usuário em questão estiver ativo, o aluno acabará matriculado e não será apresentado a mensagem de turma cheia.

Após a alteração do sistema, o aluno somente conseguirá matricular em lista de espera cujo a turma/disciplina possuir correquisito se o novo parâmetro estiver desmarcado ou o usuário do sistema possuir a permissão de perfil de usuário que possibilite matricular em turma com excesso de alunos.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
