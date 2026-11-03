---
content_hash: 7672acac57e05c9b79ee438c6e0d1247c180dbe68eafe49b669b0f0c54cabb87
fetched_at: '2026-06-29T00:06:27.063522+00:00'
page_id: '230424769'
product: rm
source: tdn-rm
title: ER_PCREQ-9362_Identificar_faltas_em_aulas_práticas_teóricas_estágio_e_laboratório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=230424769
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [R\_EDU\_EDU018](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_EDU_EDU018 "R_EDU_EDU018") | **IRM1** | [PCREQ-9362](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9362 "PCREQ-9362") |
| **Requisito1** | [PCREQ-9363](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9363 "PCREQ-9363") | **Subtarefa1** | [PDR\_EDU\_EDU018-32](http://jira.totvs.com.br/browse/PDR_EDU_EDU018-32) |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

O TOTVS Educacional será alterado visando identificar qual o tipo da aula: teórica, prática, estágio ou laboratório e passará a detalhar a frequência do aluno por este tipo de aula, caso devidamente parametrizado. Esta implementação será disponibilizada apenas para o contexto de Ensino Superior.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Gerar plano de aula | Alteração | Currículo e Oferta -> Turmas/Disciplinas -> Gerar plano de aula | - |
| Gerar plano de aula sequencial | Alteração | Currículo e Oferta -> Turma -> Gerar plano de aula sequencial | - |
| Agendamento/envio de mensagens de notificações temporais | Alteração | Atividades acadêmicas -> Central de notificações -> Agendamento/envio de mensagens de notificações temporais | - |
| Plano de aula | Alteração | Currículo e Oferta -> Turmas/Disciplinas -> Plano de aula | - |
| Gerenciamento de aula | Alteração | Currículo e Oferta -> Mais -> Gerenciamento de aula | - |
| Criar estrutura de oferta a partir das turmas/disciplinas sugeridas | Alteração | Integrações -> Scientia -> Criar estrutura de oferta a partir das turmas/disciplinas sugeridas | - |
| Quadro de Avisos | Alteração | Portal -> Quadro de avisos | - |

Será realizado as alterações detalhadas abaixo no TOTVS Educacional, TOTVS Educa Mobile e Portal Educacional:

**Processo - Gerar plano de aula**

O processo de geração de aula, disponível no cadastro de turma/disciplina, será alterado para que o usuário do sistema possa indicar um valor padrão inicial para as aulas que serão geradas.

Será criado um novo campo, de nome “Tipo da Aula”, com a opção de seleção para os valores de teórica, prática, estágio e laboratório.

**Gerenciamento de aula**

A visão geral do plano de aula será alterada para permitir a seleção do “Tipo da Aula” nos registros referentes ao plano de aula.

Será criado uma nova coluna, de nome “Tipo da aula”, com as opções de seleção Teórica, Prática, Estágio e Laboratório.

**Cadastro de plano de aula**

Será adicionado o novo campo “Tipo da aula” no cadastro de plano de aula, com as opções de seleção Teórica, Prática, Estágio e Laboratório.

**Processo de criação de estrutura de oferta – Integração Scientia**

O processo de criação de estrutura de oferta disponível quando a integração com o Scientia estiver ativa e parametrizado para utilizar o modelo 2 será alterado para permitir ao usuário do sistema informar um valor inicial do tipo de aula dos registros que serão gerados ao final do processo.

**Processo Gerar plano de aula sequencial**

No processo “Gerar plano de aula sequencial”, disponível em Currículo e Oferta > Turma, será incluído a opção de seleção de “Tipo de Aula” que indicará um valor padrão de todos os planos de aulas, para todas as turmas/disciplinas da turma selecionada.

**Disponibilidade do novo campo ao Professor**

O professor poderá alterar o “Tipo da Aula”, através da funcionalidade de plano de aula do Portal e do Educa Mobile mediante a permissão controlada pelo perfil de acesso do TOTVS Educacional.

Será criado o item de segurança do perfil de acesso de nome “Permitir alteração do Tipo da Aula”, disponível na hierarquia abaixo:

*TOTVS Educacional > Outras permissões > RM Portal > Portal > Acadêmico > Professor > Diário de Classe > Plano de Aula > Permitir alteração do Tipo da Aula.*

**Disponibilidade do novo campo ao Aluno**

O Portal e Educa Mobile serão alterados para que o aluno possa visualizar qual o “Tipo da Aula” através da funcionalidade de plano de aula existente.

**Função de Fórmula**

Será criada a função de fórmula “TotalFaltaPorTipoAula” que retornará o total de faltas do aluno pelo tipo da aula. O valor do tipo de aula (teórica, prática, estágio ou laboratório) será passado como parâmetro da função de fórmula seguindo o padrão abaixo:

* T – Teórica
* P – Prática;
* E – Estágio;
* L – Laboratório;

Exemplo: *O usuário do sistema deseja retornar o total de faltas do aluno do tipo estágio durante o processo de apuração de resultados, na fórmula será chamado a função desta maneira **TotalFaltaPorTipoAula(“E”)**.*

**Quadro de Avisos**

Será criado um novo parâmetro no parametrizador do TOTVS Educacional para exibir ou não o detalhamento da frequência do aluno baseado no novo campo criado “Tipo de Aula” (teórica, prática, de estágio ou laboratório).

O novo parâmetro, de nome “Exibir aviso de frequência por tipo da aula“ estará disponível no parametrizador no caminho abaixo:

*Secretaria > Geral 3/5 > Exibir aviso de frequência por tipo da aula*

O Portal e Educa Mobile serão alterados para que o quadro de avisos verifique este novo parâmetro e caso esteja marcado, o cálculo da frequência do aluno será a quantidade de aulas a ser considerada do aluno referente ao plano de aula e à classificação da aula.

Exemplo: *De um total de 10 aulas temos 7 teóricas e 3 práticas. O cálculo a ser realizado levará em consideração 7 aulas dadas para a classificação “teórica” e 3 aulas dadas para a classificação “prática”.*

**Central de Notificações**

A funcionalidade de Central de Notificações, regra de notificação “Frequência do aluno próximas do limite ou excedido” será alterada para realizar o envio caso o percentual de faltas de algum tipo de aula atinja o limite de faltas parametrizado (parâmetro Secretaria > Geral 3/5 > Limite de Faltas).

A central de notificações terá o mesmo comportamento da regra do quadro de avisos citado acima. A frequência por tipo de aula estará disponível somente se o novo parâmetro “Exibir aviso de frequência por tipo da aula“ estiver marcado.

## Dicionário de Dados

Tabela: SPLANOAULA

|  |  |
| --- | --- |
| **Campo** | TIPOAULA |
| **Tipo** | VARCHAR |
| **Tamanho** | 1 |
| **Valor Inicial** |  |
| **Mandatório** | Sim (  ) Não (x ) |
| **Descrição** | Tipo de aula |
| **Título** | Tipo de aula |
| **Picture** |  |
| **Help de Campo** |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
