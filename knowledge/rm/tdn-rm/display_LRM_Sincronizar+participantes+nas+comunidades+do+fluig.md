---
content_hash: aa813e0fa9c89ac279af20afbc67c46b9b12203e8d6e3de0234dd173abbd93b9
fetched_at: '2026-06-29T00:09:32.384719+00:00'
page_id: '425458836'
product: rm
source: tdn-rm
title: Sincronizar participantes nas comunidades do fluig
type: documentation
url: https://tdn.totvs.com/display/LRM/Sincronizar+participantes+nas+comunidades+do+fluig
version: 7
---

Este processo verifica nas tabelas do TOTVS educacional os registros que foram alterados com a possibilidade de inclusão ou exclusão de participantes e ou moderadores nas comunidades de acordo com a parametrização do sistema. Para o caso de exclui usuário de alguma entidade, esta ação não sincronizada automaticamente, mas registrada na tabela de log para uma sincronização de exclusão agendada. Assim por exemplo um coordenador ao ser eliminado de uma turma/disciplina, este não será automaticamente eliminado da comunidade vinculada a turma/disciplina.

Para a realização tem alguns parâmetros que podem interferir na execução do processo: Sincronizar alunos, professores, coordenadores ou inscritos como participantes ou moderadores ou não sincronizar? A exclusão de alunos, professores, coordenadores ou inscritos determinam a sua exclusão das comunidades? A data de participação de professores na turma ou de coordenadores na comissão coordenadora foi ultrapassada estes continuam ativos na comunidade. Qualquer erro durante a sincronização de um participante determina a inserção do mesmo na tabela de log da sincronização com o status de erro, acarretando a não atualização da data da última sincronização com sucesso. Desta forma quando o processo de sincronização for novamente executado o sistema deverá reenviar os registros com erro de sincronização ocorridos desde a última sincronização com sucesso. Observação: Para que um professor ou coordenador seja efetivamente eliminado das comunidades eles não podem esta vinculados as comunidades através de outra função.

**Exemplo**: Coordenador que deve ser excluído da comunidade de turma só o será se este não desempenhar a função de professor para essa turma.

**Professor**

• Exclusão:   
Professores demitidos (verificar qual a integração Labore ou Protheus, caso não existe integração basta verificar o status do professor na filial)   
Professores com a data de participação na turma/disciplina já expirada.  (Data de início e fim no cadastro do professor na turma).  
• Inclusão:   
Professores incluídos em turmas/disciplinas devem ser adicionados as comunidades conforme parametrizações.   
Para limitar os registros a serem verificados o sistema realiza os seguintes filtros:   
• Demitidos:   
Os professores que tiverem sido demitidos desde a última execução do processo. No caso de integração com o Protheus ou na ausência de integração verificar a data da alteração do cadastro de professor por filial, já no caso de integração com o Labore verificar esta mesma data no cadastro do funcionário. Participante/Moderador:   
Deve estar parametrizado para adicionar como participante ou moderador das comunidades   
As datas de alteração dos registros relacionados ao professor devem ser posteriores a data em que ocorreu a última sincronização.

**Aluno**  

Alunos devem ser excluídos ou incluídos como participantes quando a situação de matricula assim determinar. Tais ações serão realizadas de acordo com a parametrização do sistema.  

**Ensino Superior**  

Comunidades de curso e habilitação deve-se verificar se a situação de matricula no curso determina que o aluno é um participante ativo da comunidade.  

**Ensino Básico**  

Comunidades de curso e serie deve-se verificar se a situação de matricula no período letivo determina que o aluno é um participante ativo da comunidade.

**Para qualquer contexto**  

Comunidade de turma/disciplina e sub-turma deve-se verificar se a situação de matrícula na disciplina determina que o aluno é um participante ativo da comunidade. Comunidade de turma deve-se verificar se a situação de matrícula no período letivo determina que o aluno é um participante ativo na comunidade. Para limitar os registros que devem ser verificados: Apenas os alunos que tiveram alteração de situação de matricula posterior à data da última sincronização. Verificar os parâmetros do sistema para determinar se apenas as informações dos períodos letivos em aberto deverão ser consideradas. O que evidência que um aluno está matriculado na sub-turma é o preenchimento do campo CODSUBTURMA da matricula do aluno (SMATRICULA).  

**Inscritos**  

Inscritos em uma atividade ofertada são excluídos ou incluídos como participantes de acordo com a parametrização do sistema. Para limitar os registros que devem ser verificados: Apenas os inscritos que tiveram data de alteração posterior à data da última sincronização. 

**OBS.** Sincronização automática para atividades ofertadas permite a definição do tipo de participação para pessoa, professores e alunos.

Este processo deve ser construído de forma que possa ser agendado.

Ao final da execução deste processo, o parâmetro "Data da última sincronização" deve ser atualizado e o parâmetro "Data da última execução com sucesso" só deverá ser atualizado quando não ocorrer erro na sincronização.

Para limitar ainda mais os registros a serem verificados neste processo temos como regra geral a verificação do parâmetro do educacional que estabelece se apenas as informações dos períodos letivos em aberto devem ser consideradas.

Para maiores informações, acesse:

Veja Também

---

[Documento Técnico - Academia Social](http://tdn.totvs.com/x/4w4GD)
