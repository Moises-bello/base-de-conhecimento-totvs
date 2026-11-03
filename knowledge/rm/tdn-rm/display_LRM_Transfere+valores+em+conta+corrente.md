---
content_hash: d798e8979015a6789ec0777748f7ec121540dfa55d23ea5b51035fb063e7dd38
fetched_at: '2026-06-29T00:11:39.132184+00:00'
page_id: '788599539'
product: rm
source: tdn-rm
title: Transfere valores em conta corrente
type: documentation
url: https://tdn.totvs.com/display/LRM/Transfere+valores+em+conta+corrente
version: 14
---

A partir da versão **12.1.2310** introduzimos o processo *"*Transfere Valores em Conta Corrente", que permite transferir créditos da conta corrente do aluno para outro responsável financeiro vinculado a esse mesmo aluno.

Na visão de conta corrente, o processo permite a seleção exclusiva de registros associados a um único aluno. É importante observar que o processo não pode ser executado simultaneamente para diferentes alunos. Caso tente executar o processo para mais de um aluno, a mensagem 'Selecione registro de um único aluno' será exibida impossibilitando a execução do processo.

No processo de seleção, as seguintes regras são aplicadas para listar os responsáveis financeiros elegíveis para a transferência:

* Responsável financeiro vinculado diretamente ao aluno.
* Responsáveis financeiros vinculados aos contratos ativos do aluno.
* Responsáveis financeiros vinculados às parcelas dos contratos ativos do aluno.

Importante

Não será possível executar o processo para o atual responsável financeiro do item da conta corrente.

Quando a alteração do responsável financeiro da conta corrente for realizada, o registro da mudança será inserido na tabela de log SLOGCONTACORRENTE, abrangendo tanto as informações atuais quanto as anteriores à mudança, por meio dos seguintes campos:

* CODCOLIGADA: Código da coligada
* IDLOGCONTACORRENTE: ID do log da conta corrente
* IDCONTACORRENTE: ID da conta corrente
* CODCFO: Código do cliente fornecedor atual
* CODCFOANT: Código do cliente fornecedor anterior
* CODCOLCFO: Código da coligada do responsável financeiro atual
* CODCOLCFOANT: Código da coligada do responsável financeiro anterior
* CODUSUARIO: Código do usuário atual
* CODUSUARIOANT: Código do usuário anterior
* DTALTERACAO: Data de alteração
