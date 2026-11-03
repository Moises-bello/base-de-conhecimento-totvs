---
content_hash: d31dcf09e93783d00418764b7eaa39d14187c0cbaf4142920b0e0161d5342183
fetched_at: '2026-06-29T00:09:27.209190+00:00'
page_id: '423938455'
product: rm
source: tdn-rm
title: Históricos Padrões (Cadastro)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938455
version: 27
---

A implantação de Históricos Padrões tem como finalidade a utilização de expressões iguais para o registro de fatos semelhantes, simplificando a inclusão dos lançamentos contábeis. Estes históricos podem conter em suas descrições apenas um texto ou a combinação de textos mais variáveis.

Para incluir um Histórico Padrão indique um Código e sua Descrição. Feito isto, ao incluir os lançamentos contábeis, no campo Histórico, basta informar o código do histórico desejado que o sistema carrega automaticamente sua descrição.

Para otimizar ainda mais a inclusão das partidas dos lançamentos, na Descrição do histórico poderão ser incluídas as variáveis " \*#\* ", que poderão ser substituídas por quaisquer caracteres e " \*@\* ", que poderão ser substituídas apenas por número, devendo ser incluído um \*@\* para cada número a ser incluído, muito utilizada para datas. E também as variáveis *pré-definidas* que buscam informações na base de dados.

Abaixo os códigos que representam as variáveis pré-definidas que poderão ser utilizadas na contabilização e posteriormente enviadas ao TOTVS Gestão Contábil.

[CTACONCR]: Código conta crédito

[CTAREDCR]: Reduzido conta crédito

[DESCTACR]: Descrição conta crédito

[CTACR]: Código ou reduzido conta crédito

[CTACONDB]:  Código de débito

[CTAREDDB]: Reduzido conta débito

[DESCTADB]: Descrição conta crédito

[CTADB]: Código ou reduzido conta débito

[CTACONCTPRD]: Código conta contra partida

[CTAREDCTPRD]: Reduzido conta contra partida

[DESCTACTPRD]: Descrição conta contra partida

[CTACTPRD]: Código ou reduzido conta contra partida

[DIAATUAL]: Dia da data do lançamento

[MESATUAL]: Mês da data do lançamento

[ANOATUAL]: Ano da data do lançamento

[DIAANTERIOR]: Dia da anterior data do lançamento

[MESANTERIOR]: Mês da anterior data do lançamento

[ANOANTERIOR]: Ano anterior da anterior data do lançamento

[MESANOANTERIOR]: Mês/ano anterior da anterior data do lançamento

[ONTEM]: Data do dia anterior à data do lançamento

[MESEXTENSOATUAL]: Mês da data do lançamento por extenso

[MESEXTENSOANTERIOR]: Mês anterior da data do lançamento por extenso

[MESANOEXTENSOANTERIOR]: Mês/Ano anterior da data do lançamento por extenso

[NRDOC]: Número do documento do lançamento

[BEM]: Código do bem

[PATRIM]: Patrimônio do bem

[DESCBEM]: Descrição do bem

[DATALANORIG]: Data do lançamento original no estorno

[CODIMOVEL]: Código do imóvel

[DESCIMOVEL]: Descrição do imóvel

[CODCONTLOC]: Código do contrato de locação

[NUMCONTLOC]: Número do contrato de locação

[DTCONTRATOLOC]: Data do contrato

[DTLOCACAOINICONTLOC]: Data de início da locação

[DTVIGENCIAINICONTLOC]: Vigência inicial do contrato de locação

[DTVIGENCIAFINCONTLOC]: Vigência final do contrato de locação

[NOMELOCATARIO]: Nome do locatário

[DESCEVENTFIN]: Descrição do evento financeiro

[DTVIGENCIAPRORROGCONTLOC]: Data prorrogação da vigência do contrato de locação

**Atenção**

Nos parâmetros do sistema deve-se definir o *Tipo de código* a ser utilizado no cadastro dos Históricos Padrões, indicando quais caracteres poderão ser utilizados para os códigos. Qualquer caracter, apenas letra ou apenas número.

**Exemplos**

**1 - Código  Descrição**

     0001        Pagamento com Cheque Número ##### de @@/@@/@@ referente a

Na inclusão da partida, ao informarmos o código do histórico 0001, poderemos substituir as variáveis \*#\* e \*@\* por 00137 e 12/03/10 respectivamente e finalizaremos o histórico informando a que despesa se refere. O histórico, então, ficará assim: Pagamento com Cheque Número 00137 de 12/03/00 referente a despesas com transporte.

**2 - Código  Descrição**

     0002        Pgto documento número **[NrDoc]**

Na inclusão da partida, vamos supor que o campo Documento tenha sido preenchido com o número 100573. Ao informarmos o código do histórico 0002, o sistema automaticamente substituirá a variável **[NrDoc]** pelo número do documento informado anteriormente. O histórico, então, ficará assim: Pgto documento número 100573.

**Complemento obrigatório**

Ao cadastrar o histórico, marque este campo, caso seja imprescindível informar dados complementares nas partidas que utilizarem este histórico. Do contrário deixe-o desativado, pois ao marcá-lo você, obrigatoriamente, terá que informar algo como complemento do histórico.

**Complemento não permitido**

Esta opção quando marcada, não permite cadastrar complemento nas partidas que estiverem utilizando este histórico. Apenas os históricos novos ou que não possuam complemento cadastrado nos lançamentos e também não possuam variáveis em sua descrição ( @, #, [CtaDb], [CtaCr], etc ) poderão ser alterados para não permitir complemento.

**Histórico de fechamento**

Ao marcar esta opção ficará definido que o histórico é um "Histórico de Fechamento". Os históricos de fechamento serão utilizados na rotina de "Transferências de Grupos Contábeis". Apenas os históricos novos poderão ser alterados para "Histórico de Fechamento".

**Observações**

Nos parâmetros do sistema existem algumas opções referentes à utilização dos Históricos Padrões. O comportamento do sistema no momento da utilização dos Históricos Padrões irá depender da forma como estas opções estiverem configuradas.   As variáveis pré-definidas só serão preenchidas quando elas existirem no complemento do histórico. Desta forma, caso utilize o histórico padrão com variável no evento contábil deve-se preencher, manualmente, o complemento informando as variáveis.

**Existem variáveis de outros módulos que não estão pré-definidas dentro do cadastro histórico padrão, para mais informações**

Processos

* Copiar Histórico Padrão entre Coligadas
