---
content_hash: 8ae2012b70033f332c48bc05b27c88bcc3e7ee7c633a32540aa58a2beb299497
fetched_at: '2026-06-29T00:09:14.702935+00:00'
page_id: '421385229'
product: rm
source: tdn-rm
title: Membro(s) de Equipe de Mobilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Membro%28s%29+de+Equipe+de+Mobilidade
version: 5
---

---

Nesta tela será exibido todos os membros incluidos na equipe.

É possivel incluir alterar e excluir membros da equipe.

A informações que serão exibidas dos membros são:

Nome : Nome do membro da equipe

Tipo do Membro da Equipe: Se é funcionário ou terceiro.

Descrição Insumo: Descrição do insumo associado ao membro

Código do Insumo: Código do insumo associado ao membro

Ativo: Se o membro está ativo ou não

Código de Barras: Código de barras do insumo

Peso: Peso do insumo

Percentual: Percentual apontado

Atua em mais de uma equipe: Se o membro atua em mais de uma equipe.

* Membro de equipe são recursos de mão de obra especialistas de acordo com a função para execução de tarefas de um projeto;
* Permitir realizar alocação de tarefas para uma equipe de acordo com a disponibilidade;
* Dependência com o cadastro de pessoas;
* O inclusão de um membro pode ser realizada pela interface de edição ou pelo processo “Inclusão de Membro(s)”;
* Após o cadastro da equipe é necessário a informação dos membros que a compõe. Estes membros podem ser funcionários ou terceiros. Os membros disponíveis para a associação são filtrados de acordo com o parâmetro de projeto “Integração \ Outros \ Considerar funcionário/terceiro de:”;
* Cada membro é associado a um insumo de mão de obra. Tem que ter compatibilidade entre a função do insumo e a função do membro;
* É possível realizar a alteração ou exclusão de um membro da equipe. Na exclusão o sistema irá validar se existe carga no coletor com algum membro da equipe. Caso haja, é verificado se existe algum apontamento de mão de obra pendente para a tarefa em que o membro possui carga. Se existir, o sistema gera uma exceção e informa ao usuário que o membro não poderá ser excluído da equipe e somente poderá ser excluído após a apropriação deste(s) apontamento(s). Caso não exista nenhum apontamento para o membro, o sistema exibe a mensagem informativa “O membro [nome] possui carga em coletor móvel. Deseja continuar a exclusão?”. Se confirmar, o membro da equipe será desassociado da equipe;

**Importante:**

**A partir da data de desligamento, o membro não pode ter nenhum apontamento apropriado;**

**Apontamentos retornados do coletor com data posterior ao desligamento são desconsiderados.**
