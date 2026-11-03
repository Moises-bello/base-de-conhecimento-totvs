---
content_hash: 2aaace6dad7e9604f989c73161acc59acc2d70b8a47546342d2c2bf6083a7524
fetched_at: '2026-06-29T00:08:18.648467+00:00'
page_id: '266963888'
product: rm
source: tdn-rm
title: DT_Alteracao_Modelo1_Integracao_Scientia
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Alteracao_Modelo1_Integracao_Scientia
version: 6
---

# Integração TOTVS Educacional X Scientia - Modelo 1

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Educacional | | |
| **Módulo:** | *TOTVS Educacional* | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Exportação de Dados para o Scientia Enterprise | Exportação de Dados para o Scientia Enterprise | | Importação de Dados do Scientia Enterprise | Importação de Dados do Scientia Enterprise | | Parâmetros do Educacional | Parâmetros do Educacional | | | |
| **Requisito (ISSUE):** | [EDUEDU001-183](http://jiraproducao.totvs.com.br/browse/EDUEDU001-183) | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

A integração do TOTVS Educacional com o Scientia Enterprise foi planejada para que seja possível utilizar as funcionalidades de geração de quadro de horário, alocação de professores e alocação de salas disponíveis no Scientia Timetabler para geração de oferta de Turma/Disciplina no TOTVS Educacional.

Ao utilizar esta integração, o Scientia Timetabler será a ferramenta padrão para planejamento e organização do quadro de horários, alocação de Professores e Salas para as respectivas Turmas/Disciplinas do TOTVS Educacional.

Esta integração é dividida em dois processos principais, Exportação de dados do TOTVS Educacional para o Scientia Enterprise e Importação de dados do Scientia Enterprise para o TOTVS Educacional.

O processo de exportação de dados para o Scientia Enterprise é um recurso que envia os dados essenciais dos cadastros do TOTVS Educacional, permitindo a utilização do Scientia Enterprise para alocar professores, salas e gerar as ofertas de horários das Turmas/Disciplinas. No envio das informações o processo utiliza mascaras pré-definidas para que a relação entre informações dos dois sistemas seja identificada corretamente, possibilitando que a leitura da oferta montada seja realizada.

O processo de importação de dados é o recurso que permite que os agendamentos realizados no Scientia Timetabler sejam importados para o TOTVS Educacional, possibilitando assim que os horários da oferta de Turma/Disciplina e as alocações de Professores e Salas para estas Turmas/Disciplinas sejam atualizadas. Este processo busca informações das Atividades do Scientia que obedeçam as chaves criadas no processo de exportação.

## Definição da Regra de Negócio

# Parametrização de integração com Scientia

Acessar**: Módulo Educacional | Parâmetros| Integração | Scientia**

* Selecione “Utilize integração com Scientia”.
* Escolha qual tipo de banco de dados será utilizado na integração, SQL Server ou Oracle.
* Insira informações de conexão com a base de dados de Exportação e teste a conexão
* Insira informações de conexão com a base de dados de Importação e teste a conexão
* Defina em Modelo de integração: "Modelo 1 - Otimiza horários e recursos de turma/disciplina existente"
* Defina o comportamento do sistema:
  + Permitir atualização dos horários da turma/disciplina que possua professor com folha de pagamento aprovada
  + Permitir alteração de salas via integração após a matrícula de alunos
  + Permitir alteração de professores da turma/disciplina via integração após a matrícula de alunos
  + Permitir alteração de horários via integração após a matrícula de alunos
  + Permitir atualização de turma/disciplina com conteúdo de plano de aula preenchido
  + Quando houver alunos matriculados na turma/disciplina enviar o total de alunos matriculados

**É necessário parametrizar tanto a base de exportação quanto a de importação para que seja possível exportar com sucesso, pois existem informações que são validadas no Scientia durante o processo.**

# Exportação de Dados para o Scientia

Acessar: **Módulo Educacional | Integrações | Scientia | Exportação de Dados para o Scientia Enterprise**

* Ao abrir o processo, a primeira tela exibida é a de boas vindas, basta avançar.
* A seguir temos a tela de seleção de Período Letivo. Nesta tela existem os seguintes parâmetros:
  + **Dados a exportar:**Este parâmetro possibilita a opção de enviar todos os dados novamente, enviar os dados alterados desde a última exportação ou enviar apenas os registros que foram alterados a partir de uma data, que possui como padrão a data da última integração. Na primeira exportação é obrigatório o envio de todos os registros.
  + **Lista de Períodos Letivos:** Devemos selecionar o(s) Período(s) Letivo(s) que ser(á)ão integrado(s) dentro da lista de Períodos Letivos com status aberto.
  + Avance para a próxima tela.
  + A seguir temos a tela de seleção de professores onde pode-se utilizar os seguintes modos de seleção:
    - Seleção padrão do sistema
    - Seleção via SQL
    - Não enviar a informação de professores
  + Avance para a próxima tela.
  + A seguir temos a tela de seleção de Turmas/Disciplinas que serão exportadas para o Scientia Enterprise. Nesta tela temos as seguintes opções
    - **Quantidade de aulas semanais:** Este parâmetro indica quantos Templates de Atividade serão gerados para as Turmas/Disciplinas que não possuem o campo de Quantidade de Aulas preenchido.
    - **Enviar todas as Turmas/Disciplinas dos Períodos Letivos selecionados:** Este parâmetro determina que o processo envie todas as Turmas/Disciplinas existentes nos Períodos Letivos, Filial e/ou Nível de Ensino selecionados.
    - **Filtros de Matriz Aplicada e Carga Horária:** Caso não deseje enviar todas as Turmas/Disciplinas dos Períodos Letivos selecionados, utilize estes filtros para restringir as Turmas/Disciplinas que deseja enviar. O filtro de carga horária busca na Grade ou Turma a carga horária dependendo do Nível de Ensino da Turma/Disciplina.

 Serão enviadas todas as Turmas/Disciplinas listadas, independente de estar selecionada ou não. Utilize a seleção de Turmas/Disciplinas para remover as disciplinas que não deseja enviar.

* Execute o processo, ao final, os dados já estarão disponíveis na base de integração para serem importados no Scientia pelo SPDA – Syllabus Plus Data Adaptor.

**Importante:**

* Se o parâmetro do TOTVS Educacional "**Quando houver alunos matriculados na turma/disciplina enviar o total de alunos matriculados**" estiver marcado as turmas/disciplinas que contenham alunos matriculados enviarão no campo PosPlannedSize do Programme of Study do Scientia o total de alunos matriculados . Para todos os outros cenários o sistema continuará enviando a informação do máximo de alunos da turma ou turma/disciplina de acordo com a configuração do controle de vagas definido na matriz curricular.
* Como a base do Scientia é anual, deve-se ter muita atenção ao escolher os períodos letivos que deseja integrar.
* Caso possua dúvidas de como executar o SPDA consulte a documentação do Scientia ou entre em contato com o Help Desk.

# Importação de Dados do Scientia

Depois de criada a oferta de horário no Scientia Timetabler e executado o aplicativo "Run Scheduled Extract" já é possível executar o processo de importação de dados do Scientia no TOTVS Educacional. ("Run Scheduled Extract" é responsável por atualizar as informações do RDB)

Acessar**: Módulo Educacional | Integrações | Scientia | Importação de Dados do Scientia Enterprise**

* Ao abrir o processo, a primeira tela exibida é a de boas vindas, basta avançar.
* A seguir temos a tela de opções do processo de Importação, nela deve-se escolher quais Turmas/Disciplinas presentes no Scientia Timetabler devem ser importadas.
* Além das Turmas/Disciplinas, temos as seguintes opções de importação:
  + **Atualizar turma/disciplina que contenha plano de aula gerado:** Permite atualizar informações de Turmas/Disciplinas que já possuam planos de aula gerados. Quando marcada está opção os planos de aula serão excluídos das Turmas/Disciplinas
  + **Atualizar turma/disciplina com dados de pagamento de professores aprovado:** Permitem atualizar informações de Turmas/Disciplinas que contenham professores com dados de pagamento aprovados. Está opção só estará disponível se os parâmetros de sistema “Permitir atualização de Turma/Disciplina com dados de pagamento do professor aprovado” e “Utilizar controle de alteração de registro com o item professor da Turma/Disciplina” estiverem marcados.
  + **Sobregravar a estrutura da turma/disciplina mesmo que contenha alunos matriculados:** Esta opção só estará habilitada se o usuário possuir em seu perfil de usuário no cadastro de permissões a opção "Permitir sobregravar a estrutura da oferta através da importação do Scientia mesmo quando houver alunos matriculados" marcada.
    - Se o usuário marcar esta opção no processo de importação as turmas/disciplinas que possuírem alunos matriculados terão a estrutura da oferta totalmente atualizada se as aulas não tiverem iniciado, seguindo a mesma regra das turmas/disciplinas sem alunos matriculados.
    - Consideraremos que as aulas da turma/disciplina iniciaram se:
      * Plano de aula gerado com conteúdo realizado digitado
      * Frequência diária lançadaDesta forma antes do início das aulas a instituição de ensino teria total flexibilidade no momento do planejamento da oferta, mesmo com alunos já matriculados nas turmas/disciplinas.
  + **Permite superalocar professores:** Esta opção só estará habilitada se o usuário possuir em seu perfil de usuário no cadastro de permissões a opção "Permitir superalocação de professores" marcada.
    - Se o usuário marcar esta opção o choque de horário de professores quando encontrado não aborta a importação dos dados, caso contrário o sistema emite um erro e não atualiza as turmas/disciplinas
  + **Permite superalocar salas:** Esta opção só estará habilitada se o usuário possuir em seu perfil de usuário no cadastro de permissões a opção "Permitir superalocação de salas" marcada.
    - Se o usuário marcar esta opção o choque de horário de salas quando encontrado não aborta a importação dos dados, caso contrário o sistema emite um erro e não atualiza as turmas/disciplinas
  + **Permite superalocar alunos:** Esta opção só estará habilitada se o usuário possuir em seu perfil de usuário no cadastro de permissões a opção "Matricular alunos com choque de horário" marcada.
    - Se o usuário marcar esta opção o choque de horário de alunos quando encontrado não aborta a importação dos dados, caso contrário o sistema emite um erro e não atualiza as turmas/disciplinas.
* Avance para a próxima tela.
  + Esta etapa fica visível quando:
    - O sistema estiver parametrizado para permitir alteração de horário ou professores de turmas/disciplinas com alunos matriculados
    - Pelo menos uma das turmas/disciplinas selecionadas na etapa anterior possuir alunos matriculados e a opção "Sobregravar a estrutura da turma/disciplina mesmo que contenha alunos matriculados" estiver desmarcada ou já tiver iniciado as aulas (plano de aula com conteúdo realizado ou frequência diária digitada) o usuário deverá definir um conjunto de datas para criação dos horários modulares.
  + Quando permite alteração de horário os seguintes campos ficam disponíveis
    - Novos horários da turma/disciplina - para horários que estão sendo enviados pelo scientia e não estiverm criados na oferta do TOTVS Educacional
      * Data início
      * Data fim (pode-se buscar a data fim automaticamente basta que a opção "Utilizar como data fim dos novos horários o valor atribuído como data mim na turma/disciplina, turma ou período letivo")
    - Encerramento de horários da turma/disciplina - para horários que não estão sendo enviados pelo scientia e que estão associados a turma/disciplina no TOTVS Educacional
      * Data início (pode-se buscar a data início automaticamente basta que a opção "Utilizar como data início dos horários encerrados o valor atribuido como data início na turma/disciplina, turma ou período letivo")
      * Data fim
  + Quando permite alteração de professores os seguintes campos ficam disponíveis
    - Data início de participação dos novos professores
    - Data término de participação dos professores atuais
  + Caso as datas informadas sejam menores que a data do dia da execução será exibido um aviso para o usuário com o seguinte texto "A data início para novos horários e/ou data início de participação de novos professores é inferior a data atual, antes de prosseguir certifique-se que a frequência dos aluno se o conteúdo realizado dos planos de aula estão atualizados" e solicitada uma confirmação para prosseguimento.

* Execute o processo e o sistema tentará atualizar os dados das turmas/disciplinas selecionadas

# Informações Adicionais

O processo de exclusão de registros que fazem integração com o Scientia no TOTVS Educacional envia comandos de exclusão para a tabela de integração SPDA do Scientia Enterprise, desta forma, se a integração estiver habilitada, é necessário que exista a configuração correta das bases de integração para que estes comandos possam ser enviados.

No quadro abaixo descrevemos as tabelas envolvidas no processo de exportação de dados para o Scientia.

|  |  |
| --- | --- |
| **Tabelas Utilizadas** | TblDepartmentMain – Department |
| **Tabelas Utilizadas** | TblSuitabilityMain – Suitability |
| **Tabelas Utilizadas** | TblStaffMain – Staff |
| **Tabelas Utilizadas** | TblStaffSharedWithDepartments  – StaffSharedWithDepartments |
| **Tabelas Utilizadas** | TblStaffPrimarySuitability – StaffSuitability |
| **Tabelas Utilizadas** | TblPOSMain  –  POS |
| **Tabelas Utilizadas** | TblStudentSetMain – StudentSet |
| **Tabelas Utilizadas** | TblModuleMain – Module |
| **Tabelas Utilizadas** | TblActivityTemplateMain – ActivityTemplate |
| **Tabelas Utilizadas** | TblZoneMain – Zone |
| **Tabelas Utilizadas** | TblLocationMain – Location |
| **Tabelas Utilizadas** | TblLocationSharedWithDepartments - Location Shared With Departments |
| **Tabelas Utilizadas** | TblLocationPrimarySuitability - LocationSuitability |

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Exportação de Dados para o Scientia Enterprise | Alteração | Integrações -> Scientia -> Exportação de Dados para o Scientia Enterprise | - |
| Importação de Dados do Scientia Enterprise | Alteração | Integrações -> Scientia -> Importação de Dados do Scientia Enterprise | - |
| Parâmetros do TOTVS Educacional | Alteração | Configurações -> Parâmetros | - |
