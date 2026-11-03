---
content_hash: 060f5602fa2429050451beb2a7a77cbe85270eade866453d88736e9f952a8dc2
fetched_at: '2026-06-29T00:08:24.023025+00:00'
page_id: '270102007'
product: rm
source: tdn-rm
title: RMEDU00004_Matrícula On-Line
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270102007
version: 15
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.14 |
| **Processo:** | Matrícula On-line |
| **Passo a passo:** | Manual de configuração para Matrícula On-line |

**TOTVS Educacional | Matricula On-Line**

Permite que alunos, Pais ou Responsáveis acessem o portal para realização da Matricula do aluno.

**Requisitos:**

Alunos, Pais ou responsáveis com usuário de acesso ao portal gerados.

Toda a estrutura para matricula deve ser criada, Parametrização por curso, turmas, turmas disciplinas, planos de pagamento e etc...

O Aluno deve ser previamente Matricula no período Letivo de destino.

Neste processo os alunos, pais ou responsáveis devem acessar ao portal e confirmar a matricula do aluno podendo inserir, excluir disciplinas e planos de pagamento.

Para a realização do é necessário a parametrização do sistema e a realização dos cadastros necessários.

***Configurações |*** ***Parâmetros |******RM Portal |******RM Portal - Matrícula***

* “Matricula disponível para utilização” é necessário a marcação do parâmetro para disponibilização da Matricula On-line.
* O período letivo em que a matricula on-line se encontrará disponível deve ser informado corretamente.
* As situações de matricula após a confirmação da Matricula no período letivo e disciplinas deve ser informado. (Neste caso informamos “Aguardando pagamento” pois o processo de “Confirmação de Matricula por pagamento deve ser executado” para validar a matricula somente após o pagamento da Primeira mensalidade.)

* As informações cadastradas na segunda etapa do wizard de parametrizações da matricula on-line foram criadas para que a instituição facilite a usabilidade do processo. Na imagem abaixo é possível verificar alguns exemplos de cadastros.

* As informações cadastradas na para informar o Título da Matricula, mensagem para matricula indisponível e mensagem para conformação da Matricula

* Parametrização das validações do processo de Matricula. A opção de validar e bloquear o processo dependendo da situação de individual dos alunos.
* Opção de Alerta ou bloqueio para Débitos Financeiros, Documentos pendentes e Ocorrências acadêmicas.
* Para todas as opções citadas é possível a parametrizar as mensagens que serão informadas ao aluno caso a validação seja feita.

* Opção de Alerta ou bloqueio para Débitos financeiros no TOTVS Gestão Bibliotecaria e com empréstimos atrasados.
* Parametrizações opcionais de acordo com a forma de trabalho do cliente. Ex: Exibir a sala no quadro de horários.

* Configuração de disponibilidade do comprovante do matricula.

* Formatação do texto exibido no comprovante de matrícula. Possibilidade de utilização de campos do banco de dados (TAGS) para criação do texto.

* Configuração de disponibilidade do contrato Financeiro.

* Configuração do texto do contrato financeiro. Possibilidade de utilização de campos do banco de dados (TAGS) para criação e formatação do Texto.

* Configuração para geração de lançamentos após termino da matricula, é possível definir a geração por parcelas ou datas.

***Configurações |******Parâmetros |******Matrícula |******Sugestão de disciplinas***

Configuração do SDD (Sugestão de Disciplinas) turmas disciplinas de acordo com as regras de negócio estabelecidas pela instituição.

* Os parâmetros descritos na Sugestão de Disciplinas têm como função limitar a oferta de turmas disciplinas durante a realização da matricula.

Ex: Um aluno se encontra matriculado na seguinte matriz aplicada:

**Curso**: Sistema de Informação; **Habilitação**: Sistema de Informação; **Matriz Curricular**: SI – 2010; **Turno**: TARDE.

Vamos dizer que temos a turma A1 criada para o **Curso**: Sistema de Informação; **Habilitação**: Sistema de Informação; **Matriz Curricular**: SI – 2010; **Turno**: TARDE.

Turma B1 **Curso**: Sistema de Informação; **Habilitação**: Sistema de Informação; **Matriz Curricular**: SI – 2010; **Turno**: NOTURNO.

Se o parâmetro da Sugestão “De outros turnos que não seja do aluno” estiver marcado, o mesmo terá como selecionar a turma A1 ou B1, caso o mesmo esteja desmarcado, o mesmo irá visualizar apenas a turma A1 que pertence a matriz aplicada que o aluno está matriculado.

Obs: seguir a mesma linha de raciocínio para interpretação dos outros parâmetros existentes na sugestão de disciplina.

***Currículo e Oferta | Situação de Matrícula***

Configuração da Situação de matricula

* Identificação do status de matricula

* Realizar a parametrização de Matricula

***Currículo e Oferta |Parametrização por Curso***

Configuração da Parametrização por Curso

* Parametrizar a oferta do curso para o Período Letivo

* O preenchimento da data Inicial, Final, Horário Inicial e Final para que a matricula fique disponível no portal

Incluir o plano de pagamento default é necessário para que o mesmo seja incluído no contrato no final na matricula no EXE.

***Currículo e Oferta | Alunos***

* Localizar o Cadastro do Aluno

Para que o processo de Matricula On-line seja disponível no portal é necessário que o aluno já esteja matriculado no Período Letivo em que a matricula será realizada.

* Para validação da Matricula on-line o campo período deve estar obrigatoriamente preenchido. O sistema irá validar através desse campo a “Configuração de Rematrícula” realizada no status em que o aluno se encontra.

* O Preenchimento do Período conforme mostrado na imagem anterior é importante para a sugestão de matricula nas disciplinas que também valida o parâmetro da Situação de Matricula conforme imagem abaixo, podendo-se definir a prioridade de matricula.

***Currículo e Oferta*** **| *Turma/disciplinas***

* No cadastro das Turmas disciplinas é necessário que o parâmetro “Exibe na Matricula do portal” esteja habilitado para a exibição da turma na matricula on-line.

* No cadastro das Turmas disciplinas é necessário que na aba Período de Matricula as datas estejam compreendidas no Período da Matrícula

***Currículo e Oferta* | *Alunos* | *Geração de Usuários (Alunos)***

***Geração de Usuário para o Aluno, Pais e Responsáveis.***

* É necessário que o aluno, Pais ou Responsáveis tenha usuário de acesso ao portal para navegação e utilização das funcionalidades.

* Validação de permissão do Perfil vinculado aos alunos

* Permissão para execução da Matricula on-line

***Processo de Matricula On-line***

* Apresentação do processo de Matrícula.

* Clicar no menu Educacional

* Clicar na Opção “Matricula online”

* Clicar Iniciar

* Clicar em Continuar Matrícula

* Seleção de Turmas Disciplinas e confirmação de Matricula

* Contrato, Clicar no botão do Termo de Li e Aceito.

* Confirmação da Matricula

* Comprovante de Matricula
