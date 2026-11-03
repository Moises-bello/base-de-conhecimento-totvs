---
content_hash: 4ba2c21ea7b7fd8ea03c4833c836a10722caccc8d285fb87983924c3494df731
fetched_at: '2026-06-29T00:08:04.609381+00:00'
page_id: '235575393'
product: rm
source: tdn-rm
title: DT_Identificar_faltas_aulas_praticas_teoricas_estagio_e_laboratorio
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Identificar_faltas_aulas_praticas_teoricas_estagio_e_laboratorio
version: 118
---

# Identificar faltas em aulas prática, teóricas, estágio e laboratório

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Gestão Educacional |
| **Módulo:** | Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Quadro de Avisos | Quadro de Avisos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Gerar plano de aula | Gerar plano de aula | | Gerenciamento de Aula | Gerenciamento de Aula | | Central de Notificações | Central de Notificações | | Plano de Aula | Visão do plano de aula | | Plano de Aula Sequencial | Processo de Geração de Plano de Aula Sequencial | | Processo de criação de estrutura de oferta | Processo de criação de estrutura de oferta – Integração Scientia | |
| **Cadastros Iniciais:** | Cadastro de plano de aula |
| **Parâmetro(s):** | Exibir aviso de frequência por tipo da aula |
| **Requisito (ISSUE):** | [PCREQ-9363](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9363 "PCREQ-9363") |
| **País(es):** | Todos |
| **Tabelas Utilizadas:** | SPLANOAULA, SDISCIPLINA, SFREQUENCIA, SETAPAS |

## Descrição

O TOTVS Educacional foi alterado visando identificar o tipo da aula: teórica, prática, estágio ou laboratório. O sistema agora permite detalhar a frequência do aluno por este tipo de aula, caso devidamente parametrizado no quadro de avisos.

Foi realizada as alterações detalhadas abaixo no TOTVS Educacional, TOTVS Educa Mobile e Portal Educacional:

**Processo - Gerar plano de aula**

O processo de geração de aula, disponível no cadastro de turma/disciplina, foi alterado para que o usuário do sistema possa indicar um valor padrão inicial para as aulas que serão geradas.

Agora o processo possuí um novo campo, de nome “Tipo da Aula”, com a opção de seleção para os valores de teórica, prática, estágio e laboratório.

**Gerenciamento de aula**

A visão geral do plano de aula será alterada para permitir a seleção do “Tipo da Aula” nos registros referentes ao plano de aula.

Foi criada uma nova coluna, de nome “Tipo da aula”, com as opções de seleção Teórica, Prática, Estágio e Laboratório.

Este campo não é obrigatório e é permitido o valor nulo.

**Cadastro de plano de aula**

Foi adicionado o novo campo “Tipo da aula” no cadastro de plano de aula, com as opções de seleção Teórica, Prática, Estágio e Laboratório.

Este campo não é obrigatório e é permitido o valor nulo.

**Processo de criação de estrutura de oferta – Integração Scientia**

O processo de criação da estrutura de oferta, disponível quando a integração com o Scientia estiver ativa e parametrizada para utilizar o modelo 2, foi alterado para permitir ao usuário do sistema informar um valor para o campo tipo de aula para os registros do plano de aula que serão gerados ao final do processo.

Este campo não é obrigatório e é permitido o valor nulo.

**Processo Gerar plano de aula sequencial**

No processo “Gerar plano de aula sequencial”, disponível em Currículo e Oferta > Turma, foi incluída a opção de seleção de “Tipo de Aula” para indicar um valor padrão para todos os planos de aulas de todas as turmas/disciplinas da turma selecionada.

**Disponibilidade do novo campo ao Professor**

O professor poderá alterar o “Tipo da Aula”, através da funcionalidade de plano de aula do Portal e do Educa Mobile mediante a permissão controlada pelo perfil de acesso do TOTVS Educacional.

Foi criado o item de segurança  “Permitir alteração do Tipo da Aula” no perfil de acesso, disponível na hierarquia abaixo:

*TOTVS Educacional > Outras permissões > RM Portal > Portal > Professor > Diário de Classe > Plano de aula > Permitir alteração do Tipo da Aula.*

**Disponibilidade do novo campo para visualizado do Aluno**

O Portal e Educa Mobile foram alterados para que o aluno possa visualizar qual o “Tipo da Aula” através da funcionalidade de plano de aula existente.

**Função de Fórmula**

Foi criada a função de fórmula “TotalFaltaPorTipoAula” para retornar o total de faltas do aluno pelo tipo da aula. O valor do tipo de aula (teórica, prática, estágio ou laboratório) será passado como parâmetro da função de fórmula seguindo o padrão abaixo:

* T – Teórica
* P – Prática;
* E – Estágio;
* L – Laboratório;

Exemplo: *O usuário do sistema deseja retornar o total de faltas do aluno do tipo estágio durante o processo de apuração de resultados, na fórmula será chamado a função desta maneira **TotalFaltaPorTipoAula(“E”)**.*

**Quadro de Avisos**

Foi criado um novo parâmetro no parametrizador do TOTVS Educacional para exibir ou não o detalhamento da frequência do aluno baseado no novo campo criado “Tipo de Aula” (teórica, prática, de estágio ou laboratório).

O novo parâmetro, de nome “Exibir aviso de frequência por tipo da aula“ encontra-se disponível no parametrizador no caminho abaixo:

*Secretaria > Geral 3/5 > Exibir aviso de frequência por tipo da aula*

Quando parametrizado para exibição de frequência por tipo de aula deve-se também definir o parâmetro "Classificação padrão do tipo da aula quando não preenchido", desta forma os planos que não contiverem esta informação preenchida assume o valor informado no parâmetro como padrão.

O Portal e Educa Mobile também foram alterados para que o quadro de avisos verifique este novo parâmetro e caso esteja marcado, o cálculo da frequência do aluno será a quantidade de aulas a ser considerada do aluno referente ao plano de aula e à classificação da aula.

**Cálculo da Carga Horária**

(Número de faltas 'Frequência Diária do aluno') \* (Carga horária do respectivo tipo de aula - Cadastro de Disciplinas ) / 100.

O quadro de avisos somente será detalhado por tipo de aula, caso o parâmetro (Secretaria > Geral 3-5 > Exibir aviso de frequência por tipo da aula) esteja marcado e possua carga horária do respectivo tipo de aula.

Exemplo: *De um total de 10 aulas temos 7 teóricas e 3 práticas. O cálculo a ser realizado levará em consideração 7 aulas dadas para a classificação “teórica” e 3 aulas dadas para a classificação “prática”.*

**Central de Notificações**

A regra de notificação “Frequência do aluno próximas do limite ou excedido” foi alterada para realizar o envio caso o percentual de faltas de algum tipo de aula atinja o limite de faltas parametrizado (parâmetro Secretaria > Geral 3/5 > Limite de Faltas).

A central de notificações possuí o mesmo comportamento da regra do quadro de avisos citado acima. A frequência por tipo de aula estará disponível somente se o novo parâmetro “Exibir aviso de frequência por tipo da aula“ estiver marcado.

divs
