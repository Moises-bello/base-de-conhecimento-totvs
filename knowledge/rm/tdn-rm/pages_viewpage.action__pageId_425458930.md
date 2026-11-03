---
content_hash: 6a3fafe2aded0468eceba8e785972d9dee1dcf95f7e6fd615aa756d32e5f45de
fetched_at: '2026-06-29T00:09:33.168841+00:00'
page_id: '425458930'
product: rm
source: tdn-rm
title: 'Parâmetro: Período Letivo Encerrado'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458930
version: 2
---

Ao marcar um período letivo como encerrado, o sistema irá filtrar os períodos letivos que não estejam encerrados (Período letivo encerrado(ENCERRADO) <> "S") em algumas rotinas do sistema, pois em algumas rotinas não faz sentido tratar período letivo que esteja encerrado (ENCERRADO = S).

Rotinas onde são filtrados os períodos letivos ativos (campo ENCERRADO <> "S"):

Portal Educacional (Alunos):

* Tipo de aluno (entrar como)
* Aluno
* Pai, mãe e responsável acadêmico
* Habilitações do aluno disponíveis;
* Contexto da matrícula online;
* Turmas/disciplinas;
* Horários dos alunos em turma/disciplinas;

Portal Educacional (Professor):

* Contexto do professor;
* Disciplinas de responsabilidade do professor, permitindo a visualização das disciplinas em períodos letivos encerrados dependendo do parâmetro 'Exibir Período letivo encerrado';
* Disponibilidade de horário do professor;
* Horário do professor;
* Horário do professor na turma;
* Seleção de turmas/disciplinas do professor;
* Turma/disciplina para associação de material;

Módulo TOTVS Educacional (RM.exe):

* Processo: Matrícula no período letivo -> Não Permite matrícula, caso o período letivo esteja encerrado;
* Processo: Matricular alunos em disciplinas incluídas na matriz curricular;
* Processo: Gerar bolsa para irmão, caso o processo não permita gerar bolsa para período letivo encerrado;
* Processo: Importação de respostas do candidato;
* Processo: Geração de contabilização de contratos;
* Processo: Exportação/Importação de turma/disciplinas na integração do Scientia;
* Turmas/disciplinas do contrato de estágio do aluno;
* Pagamento de professores: Ao selecionar professores de turmas/disciplinas que estejam com período letivo ativo serão considerados;
* Pagamento de professores (Integração com Protheus): Ao selecionar professores de turmas/disciplinas que estejam com período letivo ativo serão considerados;
* Horários dos alunos em turma/disciplinas;
* Matrícula de alunos em períodos letivos disponíveis para vagas de estágio;
* Consulta rápida de aluno/secretaria;
* Consulta rápida de horário do professor;
* Consulta rápida de notas do aluno;
* Consulta rápida de turmas do professor;

Nas telas do sistema onde existe o campo de período letivo para seleção (lookup), o sistema filtra pelos períodos letivos que estejam ativos automaticamente, caso o sistema esteja parametrizado para "bloquear alteração em períodos letivos encerrados" e o perfil do usuário não esteja marcado para "Alterar dados em período letivo encerrado", são elas:

* Enturmação;
* Matrícula;
* Alocação manual de salas;
* Liberação de avaliações no portal;
* Montagem de quadro de horário da turma;
* Disponibilidade de horário do professor;
* Digitação de notas/faltas;
* Digitação de avaliação;
* Digitação de frequência diária;
* Digitação de avaliação por aluno;
* Digitação de notas/faltas por aluno;
* Relatório fixo de notas/faltas;
* Relatório fixo de avaliações;
* Parâmetro de matrícula do portal (período letivo para matrícula);
* Cadastro de documento do aluno;
* Cadastro de ocorrências do aluno;
* Cadastro de bolsa por período letivo;
* Cadastro de documentos exigidos;
* Cadastro de parametrização por curso;
* Cadastro de modelo de etapa por parametrização por curso;
* Cadastro de período letivo - 'Período letivo anterior';
* Cadastro de turma;
* Cadastro de turma/disciplina;
* Cadastro de turma/disciplina gerenciada;
* Cadastro de turma do MEC;
* Cadastro de complemento de disciplinas;
* Cadastro de complemento de disciplinas da grade;
* Cadastro de linha de pesquisa do professor no período letivo;
* Cadastro de matrícula do aluno no TCC;
* Cadastro de orientações do professor (TCC) no período letivo;
* Cadastro de adicional do aluno;
* Cadastro de ocorrências do professor;
* Cadastro de solenidade;
* Cadastro de gabarito;
* Cadastro de disciplinas do histórico (faculdade);
* Cadastro de contrato do aluno;
* Cadastro de faixa de crédito;
* Cadastro de plano de pagamento;
* Cadastro de responsável do contrato;
* Cadastro de curso do processo seletivo;
* Cadastro de parcela por data;
* Processo de matrícula;
* Processo de matrícula em lote;
* Processo de apuração de resultado;
* Processo de confirmação de matrícula por pagamento;
* Processo de rematrícula do ensino básico;
* Processo de rematrícula do ensino superior;
* Processo de sincronização de créditos financeiros da matrícula com a matriz;
* Processo de transferência interna entre coligadas;
* Processo de transferência entre filiais;
* Processo de cadastro de ocorrência para alunos ;
* Processo de solicitação de atendimento CRM;
* Processo de alocação de salas;
* Processo de cadastro rápido de turmas/disciplinas;
* Processo de atualização de etapas modelo de avaliações;
* Processo de associação de turma/disciplina como gerenciada;
* Processo de cadastro de turma e turma/disciplina;
* Processo de cópia de documentos para outro período letivo;
* Processo de cópia de modelo de etapas para outro período letivo;
* Processo de cópia de provas;
* Processo de cópia de turmas entre períodos letivos;
* Processo de atualização do grupo de complemento de disciplinas;
* Processo de cópia de complementos entre períodos letivos ;
* Processo de matricular alunos em disciplinas incluídas na matriz curricular;
* Processo de inscrição de alunos em vagas de estágio e emprego;
* Processo de cópia de configurações de professores do TCC entre períodos letivos;
* Processo de cópia de linhas de pesquisas (TCC) do professor entre períodos letivos;
* Processo de atualização de campos  do ENADE na matrícula dos alunos;
* Processo de importação do histórico - EB;
* Processo de cópia de plano de pagamento;
* Processo de exclusão ou cancelamento de bolsas de contratos;
* Processo de geração de bolsa para irmãos;
* Processo de geração de parcela do contrato;
* Processo de inclusão/exclusão de bolsa retroativa;
* Processo de repasse de bolsa;
* Processo de aproveitar valores da conta corrente do aluno;
* Processo de aproveitar valores da conta corrente de vários alunos;
* Processo de cadastro rápido de bolsas por período letivo;
* Processo de associação de matrículas a um item de contrato do Nucleus;
* Processo de associação de modelo de etapa ao período letivo;
* Processo de associação de plano de pagamento aos alunos;
* Processo de numeração de turmas;
* Processo de correção de gabaritos;
* Processo de inclusão de atividade ofertada ;
* Processo de matrícula de candidatos do processo seletivo;
* Processo de importação de dados do Scientia Enterprise.
