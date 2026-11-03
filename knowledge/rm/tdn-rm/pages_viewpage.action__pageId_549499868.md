---
content_hash: c94e9114740104f8cef05bb69727f16f79d7b2e30c85b032f898ef061e59d06b
fetched_at: '2026-06-29T00:10:43.042627+00:00'
page_id: '549499868'
product: rm
source: tdn-rm
title: Orçamento - Inclusão Via DataServers
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549499868
version: 27
---

## **01. VISÃO GERAL**

Dataservers do Orçamento para que os mesmos sejam disponibilizados via WebsService.

## **02. EXEMPLO DE UTILIZAÇÃO**

Admissão - FopOrcamentoStepAdmissaoDataReadView

O ReadView retorna os dados do orçamento cadastrados no RM conforme os parâmetros passados na requisição, conforme exemplo abaixo:

* DataServer: FopOrcamentoStepAdmissaoData
* Filtro: codigo=2
* Contexto: Codcoligada=1

Foram retornados os dados conforme os parâmetros passados:

ReadRecord

O ReadRecord retorna os dados do orçamento cadastrados no RM conforme os parâmetros passados na requisição, conforme exemplo:

**OBS:** Diferentemente do ReadView em que o filtro pode ser passado com apenas o nome de um campo e seu valor, o ReadRecord necessita que sejam passados suas PK's ('CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO').

* DataServer: FopOrcamentoStepAdmissaoData
* PrimaryKey: Os campos 'CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO' de seu Orçamento cadastrado = 1;1;2;1 respectivamente
* Contexto: Codcoligada=1

Foram retornados os dados conforme o solicitado:

SaveRecord

O SaveRecord Insere ou edita os dados de Admissão para realizar um orçamento, para que o SaveRecord funcione os dados do Orçamento devem estar previamente cadastrados na base, já que esse step apenas irá inserir ou editar os dados de Admissão.

Exemplo de utilização:

Exemplo de arquivo XML, com os Campos a serem preenchidos:

<![CDATA[<FopOrcamentoStepAdmissao >  
<PORCAMENTOADMISSAO>  
<CODIGO>1</CODIGO>  
<CODCOLIGADA>1</CODCOLIGADA>  
<CODORCAMENTO>2</CODORCAMENTO>  
<REVISAO>1</REVISAO>  
<DATAADMISSAO>2011-10-01T00:00:00</DATAADMISSAO>  
<CODFUNCAO>00006</CODFUNCAO>  
<CODSECAO>01.03</CODSECAO>  
<CODRECEBIMENTO>M</CODRECEBIMENTO>  
<CODTIPO>N</CODTIPO>  
<CODMOTIVO>01</CODMOTIVO>  
<CODSINDICATO>0001</CODSINDICATO>  
<CODHORARIO>0001</CODHORARIO>  
<INDINICIOHOR>6</INDINICIOHOR>  
<SALARIO>1632,00</SALARIO>  
<JORNADA>13200</JORNADA>  
<QUANTIDADE>3</QUANTIDADE>  
<CODNIVELSAL>04</CODNIVELSAL>  
<GRUPOSALARIAL>E</GRUPOSALARIAL>  
<CHAPABASE>00048</CHAPABASE>  
</PORCAMENTOADMISSAO>  
</FopOrcamentoStepAdmissao>]]>

**OBS: O arquivo XML pode ser ser adquirido através do READRECORD, o arquivo acima é um exemplo de retorno do READRECORD onde foi alterado com os novos dados que desejo inserir, exemplo de utilização do READRECORD está descrito acima.**

Após os dados preenchidos segue o retorno:

Os dados são inseridos no RM:

Os dados de Admissão são armazenados na tabela 'PORCAMENTOADMISSAO'.

Demissão - FopOrcamentoStepDemissaoDataReadView

ReadView retorna os dados referente a demissão cadastrada no orçamento conforme parâmetros passados:

* DataServer: FopOrcamentoStepDemissaoData
* Filtro: codorçamento=1
* Contexto: Codcoligada=1

Retorno dos dados conforme os parâmetros passados.

ReadRecord

O ReadRecord retorna os dados do orçamento cadastrados no RM conforme os parâmetros passados na requisição, conforme exemplo:

**OBS:** Diferentemente do ReadView em que o filtro pode ser passado com apenas o nome de um campo e seu valor, o ReadRecord necessita que sejam passados suas PK's ***('CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO')***.

* DataServer: FopOrcamentoStepDemissaoData
* PrimaryKey: Os campos ***'CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO'*** de seu Orçamento cadastrado = 1;1;3;1 respectivamente
* Contexto: Codcoligada=1

Foram retornados os dados conforme o solicitado:

SaveRecord

O SaveRecord Insere ou edita os dados de Demissão para realizar um orçamento, para que o SaveRecord funcione os dados do Orçamento devem estar previamente cadastrados na base, já que esse step apenas irá inserir ou editar os dados de Demissão.

Exemplo de utilização:

Exemplo de arquivo XML, com os Campos a serem preenchidos:

<![CDATA[<FopOrcamentoStepDemissao >  
<PORCAMENTODEMISSAO>  
<CODIGO>1</CODIGO>  
<CODCOLIGADA>1</CODCOLIGADA>  
<CODORCAMENTO>1</CODORCAMENTO>  
<REVISAO>1</REVISAO>  
<DATADEMISSAO>2020-02-01T00:00:00</DATADEMISSAO>  
<DATAPAGAMENTO>2020-02-01T00:00:00</DATAPAGAMENTO>  
<CODMOTIVO>04</CODMOTIVO>  
<CODTIPO>2</CODTIPO>  
<CONTRATOCOMPRAZO>0</CONTRATOCOMPRAZO>  
<POSSUIAVISOPREVIO>0</POSSUIAVISOPREVIO>  
<DESCONTAAVISOPREVIO>0</DESCONTAAVISOPREVIO>  
<DIASAVISOPREVIO>0</DIASAVISOPREVIO>  
<DATAAVISOPREVIO>2020-01-03T00:00:00</DATAAVISOPREVIO>  
<EXECUTAFORMULAAVISO>0</EXECUTAFORMULAAVISO>  
<NROPERIODO>1</NROPERIODO>  
<QUEBRASECAO>01.03</QUEBRASECAO>  
<SELCHAPA>00001</SELCHAPA>  
<SELSITUACAO>ADEFILMOPRSTUVWX</SELSITUACAO>  
<SELTIPOFUNCIONARIO>ABCDEFIMNOPRSTUXZ</SELTIPOFUNCIONARIO>  
<SELTIPORECEBIMENTO>DHMOPQST</SELTIPORECEBIMENTO>  
<SELFILTRO>0</SELFILTRO>  
<SELFUNCAO>00001</SELFUNCAO>  
<RECCREATEDBY>mestre</RECCREATEDBY>  
<RECCREATEDON>2020-07-14T09:11:32.093</RECCREATEDON>  
<RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
<RECMODIFIEDON>2020-07-14T10:26:06</RECMODIFIEDON>  
<AMBIENTE>4</AMBIENTE>  
</PORCAMENTODEMISSAO>  
</FopOrcamentoStepDemissao>]]>

**OBS: O arquivo XML pode ser ser adquirido através do READRECORD, o arquivo acima é um exemplo de retorno do READRECORD onde foi alterado com os novos dados que desejo inserir, exemplo de utilização do READRECORD está descrito acima, O sistema irá avaliar uma tag SELCHAPA, se tiver sido informada deverá conter um código registrado no cadastro de funcionário. Caso não tenha sido registrado será emitido uma mensagem de erro “Chapa do funcionário não cadastrada. Em Coligada: {0}, Orçamento: {1} Revisão: {2} Demissão: {3}. ”. A informação de seção e função para atualização do quadro de lotação será obtida respectivamente pelo quadro de lotação (PORCAMENTOLOTACAOCAD) .**

Após os dados preenchidos segue o retorno:

Os dados são inseridos no RM:

Os dados de Demissão são armazenados na tabela 'PORCAMENTODEMISSAO'.

DeleteRecord

O DeleteRecord é utilizado para deletar os dados do orçamento cadastrado.

Exemplo:

Deve se informar o dataserver ***"****FopOrcamentoStepDemissaoData" ,***e informar o XML (o mesmo utilizado para realizar o SaveRecord) com as informações que deseja deletar:

***OBS: Após a deleção, o quadro deverá atualizar o quadro, diminuindo o destino e retornando para a função origem.***

Promoção - FopOrcamentoStepPromocaoDataReadView

ReadView retorna os dados referente a Promoção cadastrada no orçamento conforme parâmetros passados:

* DataServer: FopOrcamentoStepPromocaoData
* Filtro: codorçamento=1
* Contexto: Codcoligada=1

Retorno dos dados conforme os parâmetros passados.

ReadRecord

O ReadRecord retorna os dados do orçamento cadastrados no RM conforme os parâmetros passados na requisição, conforme exemplo:

**OBS:** Diferentemente do ReadView em que o filtro pode ser passado com apenas o nome de um campo e seu valor, o ReadRecord necessita que sejam passados suas PK's ('CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO').

* DataServer: FopOrcamentoStepPromocaoData
* PrimaryKey: Os campos 'CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO' de seu Orçamento cadastrado = 1;1;1;1 respectivamente
* Contexto: Codcoligada=1

Foram retornados os dados conforme o solicitado:

SaveRecord

O SaveRecord Insere ou edita os dados de Promoção para realizar um orçamento, para que o SaveRecord funcione os dados do Orçamento devem estar previamente cadastrados na base, já que esse step apenas irá inserir ou editar os dados de Promoção.

Exemplo de utilização:

Exemplo de arquivo XML, com os Campos a serem preenchidos:

<![CDATA[<FopOrcamentoStepPromocao >  
<PORCAMENTOPROMOCAO>  
<CODIGO>2</CODIGO>  
<CODCOLIGADA>1</CODCOLIGADA>  
<CODORCAMENTO>1</CODORCAMENTO>  
<REVISAO>1</REVISAO>  
<DATAPROMOCAO>2011-10-01T00:00:00</DATAPROMOCAO>  
<CODMOTIVO>05</CODMOTIVO>  
<CODFUNCAO>00001</CODFUNCAO>  
<CODRECEBIMENTO>M</CODRECEBIMENTO>  
<TIPOALTERACAOSALARIO>P</TIPOALTERACAOSALARIO>  
<CODAPLICACAO>P</CODAPLICACAO>  
<PERMITEREDUCAOSALARIO>0</PERMITEREDUCAOSALARIO>  
<PERCENTUAL>10,00</PERCENTUAL>  
<SALARIO>0,00</SALARIO>  
<QUEBRASECAO>?????</QUEBRASECAO>  
<SELCHAPA>00002</SELCHAPA>  
<SELSITUACAO>ADEFILMOPRSTUVWX</SELSITUACAO>  
<SELTIPOFUNCIONARIO>ABCDEFIMNOPRSTUXZ</SELTIPOFUNCIONARIO>  
<SELTIPORECEBIMENTO>DHMOPQST</SELTIPORECEBIMENTO>  
<SELFILTRO>0</SELFILTRO>  
<SELFILTROPAR />  
<SELFUNCAO>00002</SELFUNCAO>  
<SELPERFIL />  
<RECCREATEDBY>mestre</RECCREATEDBY>  
<RECCREATEDON>07/08/2020 11:02:25</RECCREATEDON>  
<RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
<RECMODIFIEDON>07/08/2020 11:02:25</RECMODIFIEDON>  
</PORCAMENTOPROMOCAO>  
</FopOrcamentoStepPromocao>]]>

**OBS: O arquivo XML pode ser ser adquirido através do READRECORD, o arquivo acima é um exemplo de retorno do READRECORD onde foi alterado com os novos dados que desejo inserir, exemplo de utilização do READRECORD está descrito acima - Para que a implementação atualize o quadro de lotação VITAE, o campo *<SELCHAPA>****00002****</SELCHAPA>* deverá ser preenchido, o sistema irá avaliar a tag SELCHAPA, a informação de seção e função para atualização do quadro de lotação será obtida pelo quadro de lotação (PORCAMENTOLOTACAOCAD), e para o destino da nova função será validada a tag no arquivo XML <CODFUNCAO>**00001**</CODFUNCAO>.**

Após os dados preenchidos segue o retorno:

Os dados são inseridos no RM:

E são armazenados na tabela "PORCAMENTOPROMOCAO"

DeleteRecord

O DeleteRecord é utilizado para deletar os dados do orçamento cadastrado.

Exemplo:

Deve se informar o dataserver ***"****FopOrcamentoStepPromocaoData" ,***e informar o XML (o mesmo utilizado para realizar o SaveRecord) com as informações que deseja deletar:

***OBS: Após a deleção, o quadro deverá atualizar o quadro, diminuindo o destino e retornando para a função origem.***

Transferência - FopOrcamentoTransferenciaData ReadView

ReadView retorna os dados referente a Transferência cadastrada no orçamento conforme parâmetros passados:

* DataServer: FopOrcamentoStepTransferenciaData
* Filtro: codorçamento=1
* Contexto: Codcoligada=1

Retorno dos dados conforme os parâmetros passados.

ReadRecord

O ReadRecord retorna os dados do orçamento cadastrados no RM conforme os parâmetros passados na requisição, conforme exemplo:

**OBS:** Diferentemente do ReadView em que o filtro pode ser passado com apenas o nome de um campo e seu valor, o ReadRecord necessita que sejam passados suas PK's ('CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO').

* DataServer: FopOrcamentoStepTransferenciaData
* PrimaryKey: Os campos 'CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO' de seu Orçamento cadastrado = 1;1;1;1 respectivamente
* Contexto: Codcoligada=1

Foram retornados os dados conforme o solicitado:

SaveRecord

O SaveRecord Insere ou edita os dados de Transferência para realizar um orçamento, para que o SaveRecord funcione os dados do Orçamento devem estar previamente cadastrados na base, já que esse step apenas irá inserir ou editar os dados de Transferência.

Exemplo de utilização:

Exemplo de arquivo XML, com os Campos a serem preenchidos:

<![CDATA[<FopOrcamentoStepTransferencia >  
<PORCAMENTOTRANSFERENCIA>  
<CODIGO>1</CODIGO>  
<CODCOLIGADA>1</CODCOLIGADA>  
<CODORCAMENTO>4</CODORCAMENTO>  
<REVISAO>1</REVISAO>  
<DATATRANSFERENCIA>2011-10-01T00:00:00</DATATRANSFERENCIA>  
<CODMOTIVO>04</CODMOTIVO>  
<TRANSFERENCIACOLIGADA>0</TRANSFERENCIACOLIGADA>  
<NOVACOLIGADA>0</NOVACOLIGADA>  
<CODTIPO>5</CODTIPO>  
<CODSECAO>01.02</CODSECAO>  
<CODFUNCAO>00001</CODFUNCAO>  
<JORNADA>0</JORNADA>  
<CODSINDICATO>0001</CODSINDICATO>  
<CODHORARIO>0001</CODHORARIO>  
<CODLETRA>6</CODLETRA>  
<NOVACHAPA>99999</NOVACHAPA>  
<QUEBRASECAO>?????</QUEBRASECAO>  
<SELSITUACAO>ADEFILMOPRSTUVWX</SELSITUACAO>  
<SELTIPOFUNCIONARIO>ABCDEFIMNOPRSTUXZ</SELTIPOFUNCIONARIO>  
<SELTIPORECEBIMENTO>DHMOPQST</SELTIPORECEBIMENTO>  
<SELFILTRO>0</SELFILTRO>  
<SELFILTRONOME />  
<SELFILTROPAR />  
<RECCREATEDBY>mestre</RECCREATEDBY>  
<RECCREATEDON>2020-08-10T15:51:09.773</RECCREATEDON>  
<RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
<RECMODIFIEDON>2020-08-10T15:51:09.773</RECMODIFIEDON>  
<SELPERFIL />  
<SELCHAPA>00006</SELCHAPA>  
</PORCAMENTOTRANSFERENCIA>  
</FopOrcamentoStepTransferencia>]]>

**OBS: O arquivo XML pode ser ser adquirido através do READRECORD, o arquivo acima é um exemplo de retorno do READRECORD onde foi alterado com os novos dados que desejo inserir, exemplo de utilização do READRECORD está descrito acima, Será obrigatório informar a etiqueta: SELCHAPA. Caso não seja informado o sistema emitirá a msg de erro “Chapa deve ser informada para Coligada: {0}, Orçamento: {1}, Revisão: {2}, Transferência {3}, O sistema irá avaliar uma tag SELCHAPA, a informação de seção e função para atualização do quadro de lotação será obtida pelo quadro de lotação (PORCAMENTOLOTACAOCAD), que irá atualizar como tags: PORCAMENTOTRANSFERENCIA.QUEBRASECAO, PORCAMENTOTRANSFERENCIA.SELFUNCAO respectivamente.**

Após os dados preenchidos segue o retorno:

Os dados são inseridos no RM:

Os dado são armazenados na tabela "PORCAMENTOTRANSFERENCIA"

DeleteRecord

O DeleteRecord é utilizado para deletar os dados do orçamento cadastrado.

Exemplo:

Deve se informar o dataserver ***"FopOrcamentoSteptransferenciaData****" ,***e informar o XML (o mesmo utilizado para realizar o SaveRecord) com as informações que deseja deletar:

***OBS: Após a deleção, o quadro deverá atualizar o quadro, diminuindo o destino e retornando para a função origem.***

Alteração de Seção - FopOrcamentoStepAlteraSecaoDataReadView

ReadView retorna os dados referente a Altera Seção cadastrada no orçamento conforme parâmetros passados:

* DataServer: FopOrcamentoStepAlteraSecaoData
* Filtro: codorçamento=1
* Contexto: Codcoligada=1

Retorno dos dados conforme os parâmetros passados.

ReadRecord

O ReadRecord retorna os dados do orçamento cadastrados no RM conforme os parâmetros passados na requisição, conforme exemplo:

**OBS:** Diferentemente do ReadView em que o filtro pode ser passado com apenas o nome de um campo e seu valor, o ReadRecord necessita que sejam passados suas PK's ('CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO').

* DataServer: FopOrcamentoStepAlteraSecaoData
* PrimaryKey: Os campos 'CÓDIGO','CÓDIGO DA COLIGADA', 'CÓDIGO DO ORÇAMENTO', 'REVISÃO' de seu Orçamento cadastrado = 1;1;1;1 respectivamente
* Contexto: Codcoligada=1

Foram retornados os dados conforme o solicitado:

SaveRecord

O SaveRecord Insere ou edita os dados de Transferência para realizar um orçamento, para que o SaveRecord funcione os dados do Orçamento devem estar previamente cadastrados na base, já que esse step apenas irá inserir ou editar os dados de Alteração de Seção.

Exemplo de utilização:

Exemplo de arquivo XML, com os Campos a serem preenchidos:

<![CDATA[<FopOrcamentoStepAlteraSecao >  
<PORCAMENTOALTERACAOSECAO>  
<CODIGO>1</CODIGO>  
<CODCOLIGADA>1</CODCOLIGADA>  
<CODORCAMENTO>3</CODORCAMENTO>  
<REVISAO>1</REVISAO>  
<DATAALTERACAO>2011-10-01T00:00:00</DATAALTERACAO>  
<CODMOTIVO>04</CODMOTIVO>  
<CODSECAO>01.03</CODSECAO>  
<ALTERACAOPORFORMULA>0</ALTERACAOPORFORMULA>  
<CODAPLICACAO>P</CODAPLICACAO>  
<QUEBRASECAO>01.02</QUEBRASECAO>  
<SELCHAPA>00005</SELCHAPA>  
<SELSITUACAO>ADEFILMOPRSTUVWX</SELSITUACAO>  
<SELTIPOFUNCIONARIO>ABCDEFIMNOPRSTUXZ</SELTIPOFUNCIONARIO>  
<SELTIPORECEBIMENTO>DHMOPQST</SELTIPORECEBIMENTO>  
<SELFILTRO>0</SELFILTRO>  
<SELFILTRONOME />  
<SELFILTROPAR />  
<SELPERFIL />  
<SELFUNCAO>00009</SELFUNCAO>  
<RECCREATEDBY>mestre</RECCREATEDBY>  
<RECCREATEDON>2020-08-07T18:14:41.85</RECCREATEDON>  
<RECMODIFIEDBY>mestre</RECMODIFIEDBY>  
<RECMODIFIEDON>2020-08-07T18:14:41.85</RECMODIFIEDON>  
</PORCAMENTOALTERACAOSECAO>  
</FopOrcamentoStepAlteraSecao>]]>

**OBS: O arquivo XML pode ser ser adquirido através do READRECORD, o arquivo acima é um exemplo de retorno do READRECORD onde foi alterado com os novos dados que desejo inserir, exemplo de utilização do READRECORD está descrito acima, o campo <SELCHAPA>**00005**</SELCHAPA> é obrigatório, O sistema irá avaliar a tag SELCHAPA, a informação de seção e função para atualização do quadro de lotação será obtida respectivamente pelo quadro de lotação (PORCAMENTOLOTACAOCAD), que irá atualizar as tags:   PORCAMENTOALTERACAOSECAO.QUEBRASECAO,   PORCAMENTOALTERACAOSECAO .SELFUNCAO respectivamente.**

Após os dados preenchidos segue o retorno:

Os dados são inseridos no RM:

E os dados armazenados na tabela "PORCAMENTOALTERACAOSECAO".

DeleteRecord

O DeleteRecord é utilizado para deletar os dados do orçamento cadastrado.

Exemplo:

Deve se informar o dataserver ***"FopOrcamentoStepAlteraSecaoData****" ,***e informar o XML (o mesmo utilizado para realizar o SaveRecord) com as informações que deseja deletar:

***OBS: Após a deleção, o quadro deverá atualizar o quadro, diminuindo o destino e retornando para a função origem.***

## **03. DEMAIS INFORMAÇÕES**

ATENÇÂO

Caso o Parâmetro ***"ATUALIZAR LIMITE DE FUNCIONÁRIOS NO QUADRO DE LOTAÇÃO"***  localizado em **Folha de pagamento| Configurações| Parametrizador| Orçamento| Parâmetros Gerais Orçamento**esteja marcado, e ***"ALTERAÇÃO DO QUADRO DE LOTAÇÃO"*** localizado em **Folha de pagamento| Configurações| Parametrizador| Orçamento|Alteração do quadro de lotação** esteja devidamente preenchido com o **Cod. Step** e **Cod. Motivo**o sistema terá os seguintes funcionamentos para cada Step:

Ao informar os motivos da movimentação nos Steps do Orçamento, seguirá as regras descritas no parâmetro, conforme citado no exemplo abaixo:

**Admissão**

* ***Motivos para atualizar o limite de funcionário no Quadro de Lotação (Aumenta)***

+ ***Aumento de Quadro;***

**Demissão**

* ***Motivos para atualizar o limite de funcionário no Quadro de Lotação (Diminui)***

+ ***Redução de Quadro;***

**Transferência**

* ***Motivos para atualizar o limite de funcionário no QL (Diminui na origem/Aumenta no destino)***

+ ***Substituição;***

**Mudança de Função (Promoção)**

* ***Motivos para atualizar o limite de funcionário no QL (Diminui na origem/Aumenta no destino)***

+ ***Mudança de Função;***

**Mudança de Seção**

* ***Motivos para atualizar o limite de funcionário no QL (Diminui na origem/ Aumenta no destino)***

+ ***Mudança de Seção.***

IMPORTANTE

***Essa funcionalidade estará disponível apenas para Webservice, acima estão os exemplos de como realizar as chamadas via Webservice.***

***1 - Caso seja cadastrado manualmente pelo RM não haverá alteração no quadro de lotação mesmo com parâmetro marcado.***

***2 - Caso insira um registro via WS, e queira edita-lo, você deverá realizar a edição via WS, Apenas a deleção será permitida de forma manual no RM.***

Demais Informações Orçamento

Para mais informações sobre o orçamento e o comportamento do mesmo junto ao quadro de lotação no sistema:

* [Dados do Orçamento](https://tdn.totvs.com/display/public/LRM/Orcamento+Folha+de+Pagamento)
* [Parametrização - Parametrizador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718732)
* [Outros links sobre Orçamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=266981335)
