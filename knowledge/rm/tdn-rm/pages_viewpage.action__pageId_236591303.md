---
content_hash: aa8a080e4771e336993404ca81f464dde57fb2723491384b5f3e6e2f1a7588e6
fetched_at: '2026-06-29T00:08:06.502863+00:00'
page_id: '236591303'
product: rm
source: tdn-rm
title: ER_Fechamento_de_Período_Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236591303
version: 70
---

# Fechamento de Período Fiscal

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | Linha RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Fechamento de Período Fiscal | Fechamento de Período Fiscal |        |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Período Fiscal | Cadastro de Período Fiscal | | Fechamento de Período Fiscal | Fechamento de Período Fiscal | | Reabertura de Período Fiscal | Reabertura de Período Fiscal | | EFD Contribuições | EFD Contribuições | | SPED Fiscal | SPED Fiscal | | ECF – Escrituração Contábil\Fiscal | ECF – Escrituração Contábil\Fiscal | | TAF | TAF | | DAPI | DAPI | | SINTEGRA | SINTEGRA | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** | TUVILA |
| **Requisito (ISSUE):** |  |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** | DPERIODOFISCAL, DPERIODOFISCALLOG  DLAFAGRUPHISTORICO, DLAFTRANSPHISTORICO, DLAFEXTERIORHISTORICO, DCTRCHISTORICO, DCOMPONENTECARGAHISTORICO, DCTEEMISSORHISTORICO, DCTEDOCHISTORICO, DCTESEGUROHISTORICO, DCTEMOTORISTAHISTORICO, DLAFCOMPLEMENTOCTRCHISTORICO, DLAFDISPOSITIVOHISTORICO, DLAFAGRUPFLXHISTORICO, DLAFHISTORICO, DITEMHISTORICO, DTRBITEMHISTORICO, DITEMLOTEPRDHISTORICO, DITEMBEMHISTORICO, DITEMCOMPLHISTORICO, DHISTITEMHISTORICO, DLAFMOVPROCESSOJUDHISTORICO, DTRBLAFHISTORICO, DLAFNORMAHISTORICO, DLAFRATCCUHISTORICO, DLAFRATDEPHISTORICO, DNFTERCEIROSHISTORICO, DITEMCUPOMCANCHISTORICO, DLAFCOMPLHISTORICO, DLAFGUIAHISTORICO, DLAFMOVNOTAEMPENHOHISTORICO, DLAFENQUADRAMENTOSHISTORICO, DHISTLAFHISTORICO, DLAFCTBHISTORICO  DCARTA, DLDCNF, DLAFREFERENCIA, DITEMREFERENCIA, DATIVO, DATIVOCOMPONENTE |
| **Sistema(s) Operacional(is):** |  |
| **Versões/Release:** | *12.1.13* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** | *12.1.13* |

O objetivo deste documento é oferecer as regras para **Fechamento e Reabertura de Períodos Fiscais** conforme será explicitado abaixo.

Conterá, também, as especificações técnicas de desenvolvimento.

Entende-se por **Período Fiscal** o espaço de tempo em que os dados referentes às Notas Fiscais estarão disponíveis para manipulação.

Não confundir com Período de Apuração dos Tributos.

**1 - Introdução**

Visando maior desempenho, o módulo TOTVS Gestão Fiscal adotará o conceito de **Períodos Fiscais**. Dessa forma ao “Fechar um Período”,

o sistema tornará os dados relacionados às Notas Fiscais disponíveis apenas para consulta, movendo estes dados para tabelas

denominadas de “tabelas históricas”. Reduzindo assim o volume de dados das tabelas referentes às Notas Fiscais que estão sendo trabalhadas

no período atual, acarretando em ganho de performance na execução das rotinas do sistema.

**1.1 - Escopo**

O escopo da Implementação consiste:

* Criação de tabelas históricas;
* Criação de um Cadastro de Período Fiscal;
  + Criação de Processo para Fechamento de Período Fiscal;
  + Criação de Processo para Reabertura de Período Fiscal;
* Disponibilizar acesso de Leitura para as Notas Fiscais de Período Fiscal Fechado;
* Adaptação de Rotinas Fiscais para que possam ler dados das Notas Fiscais de Períodos Fiscais fechados.

**2 - Implementações**

Para atender ao cenário exposto na Introdução serão necessárias as seguintes implementações.

**2.1 - Criação das Tabelas Históricas**

Será efetuada a criação de novas tabelas (Histórico) para que possam ser armazenados os dados referentes às Notas Fiscais.

Inicialmente as seguintes tabelas terão um espelho histórico:

|  |  |  |  |
| --- | --- | --- | --- |
| DLAFAGRUP | DLAF | DHISTLAF | DLAFCOMPL |
| DLAFRATDEP | DLAFAGRUPFLX | DITEM | DLAFCOMPLEMENTOCTRC |
| DLAFMOVPROCESSOJUD | DNFTERCEIROS | DHISTITEM | DLAFCTB |
| DCOMPONENTECARGA | DLAFEXTERIOR | DITEMBEM | DLAFDISPOSITIVO |
| DCTEEMISSOR | DLAFTRANSP | DITEMCOMPL | DLAFENQUADRAMENTOS |
| DCTEDOC | DLAFRATCCU | DITEMLOTEPRD |  |
| DCTEMOTORISTA | DLAFMOVNOTAEMPENHO | DLAFNORMA |  |
| DCTESEGURO | DLAFGUIA | DTRBITEM |  |
| DCTRC | DTRBLAF | DITEMCUPOMCANC |  |

Estas tabelas terão como nomenclatura o próprio nome da tabela mais a palavra "HISTORICO" por exemplo "DLAFHISTORICO" e terão a mesma 

estrutura de colunas das tabelas originais.

Tabelas referentes ao Lançamento Fiscal que serão modificadas:

1 - Para as tabelas DCARTA e DLDCNF, também vinculadas ao Lançamento Fiscal será criado um campo IDLAFAGRUPHIST onde este 

será preenchido quando o Lançamento estiver no Historico, campo com vinculação na tabela DLAFAGRUPHISTORICO.

2 - Alterações tabela DLAFREFERENCIA

  Será criado o campo IDLAFREFERENCIA

  Sua PK será alterada e composta pelos campos CODCOLIGADA e IDLAFREFERENCIA

  Serão criados os campos IDLAFHIST e IDLAFREFHIST com vinculação na tabela DLAFHISTORICO

  Será criado um index único com os seguintes campos: CODCOLIGADA, IDLAF, IDLAFREF, IDLAFHIST, IDLAFREFHIST 

3 - Alterações tabela DITEMREFERENCIA 

  Será criado o campo IDITEMREFERENCIA

  Sua PK será alterada e composta pelos campos CODCOLIGADA e IDITEMREFERENCIA

  Serão criados os campos IDLAFHIST, NUMITEMHIST, IDLAFREFHIST e NUMITEMREFHIST com vinculação na tabela DITEMHISTORICO

  Será criado um index único com os seguintes campos: CODCOLIGADA, IDLAF, NUMITEM, IDLAFREF, NUMITEMREF, IDLAFHIST, NUMITEMHIST, IDLAFREFHIST, NUMITEMREFHIST

4 - Serão realizadas algumas alterações nas tabelas DATIVO e DATIVOCOMPONENTE:

Para as duas tabelas.

  Serão criados os campos IDLAFHIST e NUMITEMHIST com vinculação na tabela DITEMHISTORICO

  Será criado o campo IDLAFEHIST com vinculação na tabela DLAFHISTORICO

Estes campos serão utilizados para referenciar os Lançamentos quando os mesmo estiverem no Histórico.

**2.2 - Cadastro de Período Fiscal**

Será criado um novo cadastro no sistema, denominado “Cadastro de Período Fiscal”, responsável por armazenar dos dados dos Períodos Fiscais

que conterá as seguintes funcionalidades:

**Estrutura de Banco do Cadastro:**

Tabela DPERIODOFISCAL - Responsável por armazenar os registros de Períodos Fiscais.

| Coluna | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| CODCOLIGADA | DCODCOLIGADA | Codigo da Coligada | Sim |
| IDPERFISCAL | int | Identificador do Registro | Sim |
| DATAINICIAL | datetime | Data Inicial | Sim |
| DATAFINAL | datetime | Data Final | Sim |
| STATUSPERFISCAL | smallint | Status do Período Fiscal | Sim |
| OBSERVACAO | varchar(200) | Observação | Sim |

obs.: O Campo STATUSPERFISCAL receberá os valores:

0 - Período Fechado

1 - Período Aberto

2 - Período Fechado Parcial

3 - Período Aberto Parcial

**Anexo:**

Tabela DPERIODOFISCALLOG - Responsável por armazenar os registros de Log dos Períodos Fiscais.

| Coluna | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| CODCOLIGADA | DCODCOLIGADA | Codigo da Coligada | Sim |
| IDPERFISLOG | int | Identificador do Registro | Sim |
| IDPERFISCAL | int | Identificador do Período Fiscal | Sim |
| DATAMODIFIC | datetime | Data Modificação do Período Fiscal | Sim |
| USUARIOMODIFIC | varchar(50) | Usuário Modificação do Período Fiscal | Sim |
| STATUSPERFISCAL | smallint | Status do Período Fiscal | Sim |
| OBSERVACAO | varchar(200) | Observação | Sim |

**2.2.1 - Cadastro de Período Fiscal**

Cadastro de Período Fiscal, com os dados de Status do Período (Fechado, Aberto, Fechado Parcial, Aberto Parcial), intervalo do Período e Observação.

Neste Cadastro o usuário poderá criar, editar ou excluir registros referentes aos Períodos Fiscais.

**Localização no Sistema:**

  Totvs Gestão Fiscal - Utilitários - Período Fiscal

**ID Help: 811000196**

**O Cadastro conterá os seguintes Anexos:**

  1 - Log de Modificações

    Será gravado um Log a cada inclusão, edição ou exclusão de Registros, também será criado logs a cada Fechamento do Período Fiscal e Abertura do Período Fiscal.

  2 - Lançamentos Fiscais de Saída

  3 - Lançamentos Fiscais de Entrada

**O Cadastro conterá os seguintes Processos:**

  1 - Fechar Período Fiscal

  2 - Abrir Período Fiscal

**Regras:**

  1 - Ao incluir um novo registro o Status será Aberto (Automaticamente).

  2 - A Data Inicial deve ser menor que a Data Final.

  3 - Não podem ser incluídos Períodos Fiscais com o mesmo Intervalo de Datas.

  4 - Não pode ser excluído nem alterado Período Fiscal com Status Fechado.

  5 - O intervalo de datas deve ser Anual.

  6 - Quando for excluído um registro todos os "Logs" referentes a ele serão excluídos.

  7 - O Anexo de "Log" será apenas visível.

**2.2.2 - Processo de Fechamento de Período Fiscal**

O Fechamento do Período Fiscal consiste em Mover os dados das tabelas relacionadas aos Lançamentos Fiscais para as tabelas históricas.

O Processo será executado com base no registro do Período Fiscal, o sistema irá selecionar os Lançamentos Fiscais dentro do ano conforme

informado, e irá mover os dados, estes mesmos dados serão apagados das tabelas do Lançamento Fiscal.

Será criado um "Log" mostrando quem executou o Processo em qual data e com os dados do Período Fiscal em questão.

**Regras:**

  1 - Para Executar o Processo o Período Fiscal deve estar com status Aberto.

  2 - Para Fechar um Período Fiscal o Período anterior deve estar com status Fechado e não pode haver Lançamentos Fiscais anteriores a data Inicial do Período Fiscal.

  3 - Se durante a execução do processo de Fechamento de Período Fiscal ocorrer problema que impeça sua continuidade, sendo que pelo menos um mês foi fechado, o Período terá seu status alterado para "Fechado Parcial". Ao executar novamente o  processo, o sistema iniciará o fechamento do período fiscal a partir do mês onde ocorreu problema.

**2.2.3 - Processo de Abertura de Período Fiscal**

A abertura do Período Fiscal consiste em mover de volta os dados das tabelas históricas para as tabelas “oficiais” do Lançamento Fiscal.

Para a execução do Processo será solicitado ao usuário um motivo para o qual o mesmo está abrindo o Período Fiscal, este motivo será

gravado no "Log" de execução do Processo.

Será criado um "Log" mostrando quem executou o Processo em qual data e com os dados do Período Fiscal em questão.

**Regras:**

  1 - Para Executar o Processo o Período Fiscal deve estar com status Fechado.

  2 - Para Abrir um Período Fiscal o Período posterior deve estar com status Aberto e não pode haver Lançamentos Fiscais (Histórico) posteriores a data Final do Período Fiscal.

  3 - Se durante a execução do processo ocorrer problema que impeça sua continuidade, sendo que pelo menos um mês foi processado, o Período terá seu status alterado para "Aberto Parcial". Ao executar novamente o processo, o sistema iniciará a abertura do período fiscal a partir do mês onde ocorreu problema.

**2.2.4 - Visualização de Lançamentos Fiscais**

Permitir a visualização dos Lançamentos Fiscais de determinado Período Fiscal que esteja "fechado", sem a necessidade de efetuar a abertura do mesmo.

Será disponibilizado dois anexos para visualização dos dados.

**Anexos:**

  Lançamentos Fiscais de Saída (Histórico)

  Lançamentos Fiscais de Entrada (Histórico)

**Regras:**

1 - Não será possível modificar estes dados. Para que seja realizada alguma modificação será necessário Abrir o Período Fiscal.

2 - Não será possível modificar Lançamentos Fiscais que estejam vinculados, através de Referencias e Referencias dos Itens, a Lançamentos Fiscais que

já estão em Períodos Fiscais Fechados.

3 - Não será possível modificar Laçamentos de Outros Débitos/Créditos que estejam vinculados a Lançamentos Fiscais que já estão em Períodos Fiscais Fechados.

4 - Não será possível modificar registro na Carta de Correção que esteja vinculado a Lançamentos Fiscais que já estão em Períodos Fiscais Fechados.

5 - Não será possível modificar Lançamentos Fiscais onde seus Ativos estejam vinculados a Lançamentos Fiscais que já estão em Períodos Fiscais Fechados.

6 - Não será possível fazer o estorno de Escrituração de Lançamentos Fiscais que já estejam em Períodos Fiscais Fechados.

7 - Não será possível reimportar Lançamentos Fiscais cuja suas Referencias ou Referencias dos Itens a Lançamentos Fiscais que já estão em Períodos Fiscais Fechados.

**2.3 - Rotinas Fiscais**

As obrigações acessórias serão evoluídas para que busquem os dados referentes aos Lançamentos Fiscais das tabelas históricas caso seja solicitada a geração da rotina

para um Período Fiscal que já esteja "Fechado". Se o Período Fiscal estiver com status "Aberto Parcial" ou "Fechado Parcial" as rotinas não serão geradas.

**Rotinas:**

EFD - Contribuições

SPED Fiscal

ECF - Escrituração Contábil Fiscal

DAPI

SINTEGRA

TAF - TOTVS Automação Fiscal

**2.3.1 - EFD - Contribuições**

**Registros afetados com a mudança da origem dos dados:**

Serão afetados direta ou indiretamente os seguintes registros dos seguintes blocos.

Bloco 0 - ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA PESSOA JURÍDICA  
0001,0140,0150,0190,0200,0205,0206,0400 e 0600

Bloco A - DOCUMENTOS FISCAIS - SERVIÇOS (NÃO SUJEITOS AO ICMS)  
A001,A100,A111,A110,A120 e A170

Bloco C - DOCUMENTOS FISCAIS I - MERCADORIAS (ICMS/IPI)  
C001,C100,C380,C395,C400,C500,C600 e C860

Bloco D - DOCUMENTOS FISCAIS II - SERVIÇOS (ICMS)  
D001,D100,D101,D105,D111,D200,D201,D205,D209,D300,  
D309,D500,D501,D505,D509,D600,D601,D605 e D609

Bloco F - DEMAIS DOCUMENTOS E OPERAÇÕES  
F001,F120,F130,F200,F550 e F600

**2.3.2 - SPED - Fiscal**

**Registros afetados com a mudança da origem dos dados:**

Serão afetados direta ou indiretamente os seguintes registros dos seguintes blocos.

Bloco 1, Bloco C e Bloco D - Para estes blocos todos os registros gerados pelo aplicativo RM

**2.3.3 - ECF - Escrituração Contábil Fiscal**

****Registros afetados com a mudança da origem dos dados:****

Serão afetados direta ou indiretamente os seguintes registros dos seguintes blocos.

Bloco Y - Registros: Y550,Y560 e Y570

**2.3.4 - TAF - TOTVS Automação Fiscal**

**Registros afetados com a mudança da origem dos dados:**

Serão afetados direta ou indiretamente os seguintes registros.

T082,T078,T072,T066,T013,T012,T009,T007,T006,  
T005,T003,T001AL,T001AK,T001AJ,T001AD e T001AB

**2.3.5 - DAPI**

**Registros afetados com a mudança da origem dos dados:**

Serão afetados direta ou indiretamente os seguintes registros.

10 - Operações / Prestações

Demostrativo das Operações e Prestações de Entrada (Item IV).

Demostrativo das Operações e Prestações de Saída (Item V).

**2.3.6 - SINTEGRA**

Obs.: Apenas a geração do SINTEGRA - MG será afetada nesta implementação

**Registros afetados com a mudança da origem dos dados:**

Serão afetados direta ou indiretamente os registros com informações originadas de Lançamentos Fiscais contidos nos arquivos REDEX.txt e REGISTRO.txt.
