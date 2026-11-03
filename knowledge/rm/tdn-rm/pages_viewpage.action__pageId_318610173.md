---
content_hash: b6983bb7d267d5550480cacd1975265db1d543b2ca36e9c4d38b25e9aec8e593
fetched_at: '2026-06-29T00:08:47.137414+00:00'
page_id: '318610173'
product: rm
source: tdn-rm
title: DT Digitação de Frequência Diária por Turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=318610173
version: 13
---

# DIGITAÇÃO DE FREQUÊNCIA DIÁRIA POR TURMA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Educacional |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Informe a(s) rotina(s) envolvidas. | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [PORTALMOBILE01-2262](http://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-2262) |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQL Oracle |
| **Tabelas Utilizadas:** | SFREQUENCIA |
| **Sistema(s) Operacional(is):** | Windows |

## 

## Descrição

**Disponível apenas para o Contexto Ensino Básico a partir da versão 12.1.18.127.**

Essa funcionalidade tem como objetivo permitir que o professor  registre a falta para um aluno ou mais alunos, e ela será registrada para todas as turmas/disciplinas daquele professor no dia informado. Levando em consideração o professor do horário da turma/disciplina e a data de inicio e fim do professor também na turma/disciplina.

Ou seja, só serão registradas frequência para o aluno nas aulas que o professor for responsável naquele dia para todas as turmas/disciplinas da turma selecionada

**Parametrização:**

* Conceder a permissão para o professor em: Educacional | Educacional Portal | Professor | Digitação de frequência por turma.

**Descrição do processo:**

Uma Turma possuem cinco disciplinas, sendo:

* + Turma: MD2\_MH
* Disciplinas: 
  + Português
  + Literatura
  + Matemática
  + História
  + Geografia

O professor:Gabriel Fernandes Evangelista, leciona as disciplinas: Português e Literatura.

Ao inciar o processo de digitação de frequência diária por turma, informar a data (de acordo com o Plano de Aula) e em seguida informar a Turma (só serão listadas turmas que o professor der aula na data selecionada); o portal irá listar todas as disciplinas correspondente de acordo com a data.

Ao clicar no botão selecionar, o portal irá listar todos os alunos matriculados nas turmas disciplina.

Para marcar a Ausência para o(s) aluno(s), o professor deverá marcar o checkBox: "Ausente" e caso seja necessário, realizar a justificativa, clicar sobre o ícone: para que sejam listados as justificativas.

A funcionalidade trabalha com ausência no dia como um todo, ou seja, será exibido como ausente o aluno que não tiver comparecido em nenhuma aula do professor no dia. Caso o aluno tenha recebido uma falta em apenas alguma das Turmas/Disicplinas (Menu: Diário de Classe | Frequência) e/ou no menu Frequência Diária no .exe (Educacional | Matrícula e Avaliação | Frequência Diária) o aulo estará destacado em vermelho e com um asterisco \*. Informando que ele possui ausência em algumas aulas do dia porém, não em todas que o professor leciona:

IMPORTANTE

* Quando a Turma/disciplina tiver aula geminada, o portal irá inserir a falta para todos os horários e caso a mesma seja justificada, o portal irá replicar a informação para ambas aulas;

* Assim como nas demais funcionalidades de registro de frequência, a quantidade de ausências só será consolidada na nota da etapa para o aluno caso as aulas dadas estejam informadas. Respeitando ainda essa sincronização o parâmetro "Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina" (Educacional | Parâmetros | Secretaria | Notas/Faltas), ao marcado só será feita a sincronização após o coordenador da turma/disciplina executar o processo de aprovação de frequência;

* A sugestão de aula dadas é baseada nas datas da etapa da turma/disciplina;

* A tela respeita o parâmetro "Utilizar turma/disciplina gerencial na digitação de notas, faltas, avaliação, frequência diária, plano de aula e upload de matérias no portal" (Educacional | Parâmetros | Secretaria | Geral 1), se ele estiver marcado só serão exibidas turma/disciplina gerencial, porém o aluno só visualizará a falta na gerenciada como é realizado atualmente.
