---
content_hash: 3dac82ba5a0b8f0269b189a5989e5b71e65fb45b67795e6d15b4ad7955787c61
fetched_at: '2026-06-29T00:05:53.293530+00:00'
page_id: '1068950619'
product: rm
source: tdn-rm
title: '[Não Publicar] - Registro de movimentações financeiras das disciplinas'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068950619
version: 11
---

Essa documentação visa orientar sobre os registros das movimentações financeiras das disciplinas, no **TOTVS Educacional,** para permitir que tenhamos informações para atender às novas exigências da **Reforma Tributária.** 

## Carga inicial de movimentações financeiras das disciplinas

A carga inicial de movimentações financeiras das disciplinas será necessária para alimentar, com informações iniciais, a estrutura de tabelas que serão utilizadas para possibilitar a identificação da origem das alterações realizadas nas disciplina, pertinentes ao financeiro.

Esse processo será executado ao entrar no módulo Educacional e percorrerá várias tabelas buscando informações das disciplinas e alimentando as novas tabelas de movimentações de disciplinas.

### Obrigatoriedade de execução do processo de carga inicial

A finalização do processo de carga inicial será obrigatória para a execução da geração de lançamentos.

Os processos de geração de lançamentos em lote, por contrato, por parcela e de prévia estarão bloqueados até a finalização do processo de carga inicial.

Nos módulos do Processo Seletivo e Gestão Bibliotecária serão exibidas mensagens informando a necessidade de execução do processo de carga inicial.

Importante:

Os processos de matrículas não serão impactados e não serão bloqueados, mesmo se estiverem configurados para realizar a geração de lançamentos.

Contudo, sem a conclusão da carga inicial, eles não alimentarão a tabela de movimentação de matrícula e não teremos como reliazar o mapeamento das movimentações para a identificação da origem de suas informações.

### Execução do processo

O processo será disponibilizado apenas para os usuários que possuem permissão para a execução do processo de geração de lançamentos.

O processo será de execução única e de apenas um usuário. Caso haja uma tentiva de se executar o processo por um segundo usuário, durante a execução do primeiro, será apresentada uma mensagem informando que já existe um processo em execução.

Até a finalização do processo, todas as mensagens de aviso permanecerão sendo exibidas, assim como a solicitação de execução do processo.

Após finalizado, o processo não será mais solicitado, assim como as mensagens de aviso do Processo Seletivo e da Biblioteca não serão mais exibidas.

Todos os processos de geração de lançamentos são liberados para execução.

### Registro de execução

Na tabela *SPARAMGERAL* é registrada a situação de execução do processo para identificação da finalização ou de um possível erro.

Dessa forma, apenas uma solicitação de execução será processada.

Após a finalização do processo ficarão dois registros identificando o seu sucesso: na *SPARAMGERAL* e na *SPARAM*.

Teremos um registro na *SPARAMGERAL* indicando o status e da data de execução do processo, assim como a da data e horário da finalização do processo. Na *SPARAM* será registrado o contexto e o horário em que o processo foi executado e finalizado.

Caso tenhamos algum erro no processo de carga inicial, teremos apenas um registro na SPARAMGERAL informando o status e a mensagem ocorridada.  

Caso tenhamos o parâmetro com o valor de texto igual a "1", isso representa que o processo está em execução. **Nesse caso, deverá existir um novo parâmetro *LOCKCARGAINICIALDISCMOVFIN* representando que o processo está bloqueado para novas execuções.**

### Parâmetro de contingência

O parâmetro de contigência pode ser utilizado, em caso de erro na execução da carga inicial, como uma forma de liberarmos a obrigatoriedade de execução do processo para uma análise mais detalhada do problema, a fim de não mantermos o sistema bloqueado para a execução dos processos de geração de lançamentos.

Um script com a inclusão do parâmetro *CONTCARGAINICIALDISCMOVFIN*na tabela *SPARAMGERAL* pode liberar o uso do sistema, sem a obrigatoriedade de execução da carga inicial.

Esse parâmetro irá com a informação do número de dias que ele se manterá ativo. Caso o problema não seja corrigido até o final do período, o sistema entenderá que o parâmetro de contingência perdeu sua validade.

Com o parâmetro inválido. os processos de geração de lançamentos serão bloqueados novamente e, juntamente, irão solicitar a execução da carga inicial.

Para que o parâmetro de contigência seja válido, é necessário que existam os dois registros:

* + - *CARGAINICIALDISCMOVFIN* - Registro com o parâmetro com o código "5", indicando que houve um erro, a data de execução e a descrição do erro no campo *VALORMEMO*. Esse registro não pode ser incluso manualmente, pois possui um valor no campo *VALORINTEIRO* que representa um validador calculado.
    - *CONTCARGAINICIALDISCMOVFIN* - Registro indicando a inclusão da contingência para o erro ocorrido. Teremos aqui o campo *VALORINTEIRO* com o número de dias em que o parâmetro será válido a partir da data de execução registrada no campo *VALORDATAHORA*.

Após a correção do problema apresentando, deverá ser executado um script para a remoção do parâmetro *CONTCARGAINICIALDISCMOVFIN* para que o processo seja disponibilizado para execução novamente.

### Tabelas alimentadas

O processo de carga inicial irá alimentar a tabela *SMOVIMENTACOESFINDISCIPLINA* com as informações de todas as possíveis origens de créditos e valores de cobranças de disciplinas utilizados para a realização da geração de lançamentos.

Temos mapeadas as seguintes origens de dados para a realização de uma matrícula de um aluno e a geração de lançamentos de seus contratos:

* + - Disciplinas da grade
      * *SMOVFINDISCGRADE*
    - Disciplinas do currículo individual
      * *SMOVFINDISCGRADEALUNO*
    - Turmas/disciplinas livres
      * *SMOVFINDISCTURMADISC*
    - Faixas de créditos
      * *SMOVFINDISCFAIXACRED*
    - Tabelas de preço
      * *SMOVFINDISCTABELAPRECO*
    - Itinerários formativos
      * *SMOVFINDISCITINERARIOFORMATIVO*

Todas essas origens irão fornecer informações que nos ajudarão a mapear todas movimentações de alterações nas disciplinas.

## Movimentações financeiras das disciplinas

Todas as movimentações geradas pelas inclusões, alterações e exclusões serão registradas para criação de um histórico e para a realização de um mapeamento das alterações realizadas e da origem da disciplina matriculada.

### Tabela principal

A tabela principal que irá registrar as movimentações será a *SMOVIMENTACOESFINDISCIPLINA*.

Tabelas associadas

Todos os registros de movimentação da tabela principal terão uma associação com uma tabela filha:

* + - Disciplinas da matriz grade:

Todas as alterações realizadas nos campos de número e valor de crédito de cobrança serão registradas como movimentações da disciplina na matriz curricular da grade.

Tabela: *SMOVFINDISCGRADE*

* + - Disciplinas do currículo individual do aluno:

Todas as alterações realizadas nos campos de número e valor de crédito de cobrança serão registradas como movimentações da disciplina do currículo invidual do aluno.

Tabela: *SMOVFINDISCGRADEALUNO*

* + - Turma/Disciplina Livre

Todas as alterações realizadas nos campos de número e valor de crédito de cobrança serão registradas como movimentações da disciplina de turma livre.

Tabela: *SMOVFINDISCTURMADISC*

* + - Faixas de créditos

Todas as faixas de créditos cadastradas, assim como suas alterações, serão registradas como movimentações, apesar de não termos uma disciplina associada. Esse caso será importante para conseguirmos identificar a origem do valor cobrado na disciplina matriculada do aluno.

Tabela: *SMOVFINDISCFAIXACRED*

* + - Tabela de preço

Todos as disciplinas das tabelas de preço terão seus valores registrados como movimentação. As operações de inclusão de valor, alteração, reajuste e cancelamento de reajuste serão registrados como movimentação da disciplina da tabela de preço.

Tabela: *SMOVFINDISCTABELAPRECO*

* + - Itinerário formativo

Todas as disciplinas cadastradas na grade do itinerário formativo serão inserido como uma movimentação associado a ele para manter um mapeamento da origem da disciplina matriculado pelo aluno, mesmo não havendo um registro de número e/ou valor de crédito.

Tabela: *SMOVFINDISCITINERARIOFORMATIVO*

## Movimentações financeiras das matrículas

Todas as matrículas de alunos em disciplinas serão registradas junto a tabela de movimentações financeiras da matrícula. Registraremos todas as matrículas como uma movimentação de inclusão e todas as mudanças no número de crédito e na situação de matrícula serão registradas como uma movimentação de alteração.

Esses registros de movimentações serão importantes para conseguirmos mapear a origem das disciplinas matriculadas e seus valores.

Tabela de movimentação

Todos os registros de movimentações serão guardados na tabela *SMOVIMENTACOESFINMATRICULA*.

## FAQ - Perguntas frequentes

### Ocorreu um erro na execução do processo de carga inicial. Como devo proceder?

Quando o processo é concluído com erro, temos que verificar o log de execução para entendermos o problema.

Ao clicar no botão de informações, teremos mais informações do que aconteceu.

Podemos, também, verificar através do gerenciador de jobs o resultado da execução desse processo. O processo será registrado com o de "Carga inicial das disciplinas" e o nome da classe do processo será: "EduMovFinDisciplinaCargaInicialData".

Poderei identificar que houve um erro, também pela tabela SPARAMGERAL. Nela será registrado o código "5", indicando que houve um erro, e a mensagem no campo VALORMEMO.

### Ocorreu um erro de violação de chave estrangeira com a disciplina, como posso identificar o problema?

Caso tenhamos o erro: ***"The INSERT statement conflicted with the FOREIGN KEY constraint "FKSMOVFINDISCIPLINA\_DISC""***, existe uma grande chance de termos uma inconsistência na base dados.

Nessa situação, teremos que verificar a integridade das chaves que fazem o vínculo com a tabela SDISCIPLINA e, também, identificar quais registram referenciam uma disciplina que não existe.

Como uma sugestão de procedimentos:

* + - Verificar a integridade das chaves estrangeiras que fazem o relacionamento com a disciplina:

      sqlVerificação das chaves estrangeirastrue

      Caso tenhamos alguma chave desabilitada ou com uma marcação como não confiável, isso permitirá que possamos ter uma violação de integridade no banco de dados. Dessa forma, essa situação deverá ser passada para o cliente para que seja analisada junto com a equipe de banco de dados.

* + - Verificar quais regristro fazem referência a disciplinas que não existem:

      sqlBuscar referências inválidastrue

      Caso seja encontrado algum registro nessas consultas, as disciplinas terão que ser cadastradas novamente para que seja mantida a integridade do banco de dados ou o registro que faz a referência deverá ser excluído.
