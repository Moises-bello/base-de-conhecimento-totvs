---
content_hash: 068f7e55fd15c2f6f9d084fa78ba87d1bc7eaaa4d3f4883d973fc8a726b51645
fetched_at: '2026-07-02T19:24:26.080061+00:00'
page_id: '520661316'
product: protheus
source: tdn-tec
title: TCConfig
type: documentation
url: https://tdn.totvs.com/display/tec/TCConfig
version: 10
---

TCConfig

Permite alterar e consultar definições e configurações diversas do DBAccess em tempo de execução.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cParms | character | Parâmetro ou definição a ser alterada, ou consultada. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cRet | character | Retorna uma string correspondente ao parâmetro informado. |

## Observações

* O parâmetro **cParms** é uma string que identifica a ação ou configuração a ser consultada, ou alterada. Para obter a lista de configurações possíveis – separadas por ";" – chame a função com o parâmetro 'ALL\_CONFIG\_OPTIONS'. Caso seja informada uma configuração desconhecida, a função retorna uma string em branco.
* **ALL\_CONFIG\_OPTIONS** : Lista todas as configurações disponíveis.
* **SETUSEROWSTAMP=ON|OFF** : Permite ligar ou desligar a criação da coluna interna S\_T\_A\_M\_P\_ para novas tabelas. Pode retornar "OK" em caso de sucesso, "NOT\_SUPPORTED" caso o Banco de Dados não tenha suporte para a coluna S\_T\_A\_M\_P\_, ou "INVALID\_OPTION" caso seja informado um parâmetro diferente de "ON" ou "OFF".
* **GETUSEROWSTAMP** : Consulta se a criação da coluna S\_T\_A\_M\_P\_ para novas tabelas está habilitada, retorna "ON" ou "OFF".
* **SETAUTOSTAMP=ON|OFF** : Permite habilitar a criação automática da coluna S\_T\_A\_M\_P\_ na abertura da tabela. Pode retornar "OK" em caso de sucesso, "NOT\_SUPPORTED" caso o Banco de Dados não tenha suporte para a coluna S\_T\_A\_M\_P\_, ou "INVALID\_OPTION" caso seja informado um parâmetro diferente de "ON" ou "OFF".
* **GETAUTOSTAMP** : Consulta se a criação automática da coluna S\_T\_A\_M\_P\_ na abertura da tabela está habilitada, retorna "ON" ou "OFF".
* **SETMEMOINQUERY=ON|OFF** : Define para a conexão atual se o retorno de campos MEMO em Query está habilitado para Queries executadas através do AdvPL usando a função TCGenQry(). Retorna "OK" em caso de sucesso, ou "INVALID\_OPTION" caso seja informado um parâmetro diferente de "ON" ou "OFF".
* **GETMEMOINQUERY** : Consulta se o retorno de campos MEMO em Query está habilitado no momento para a conexão atual, retorna "ON" ou "OFF".

**As opções abaixo estarão disponíveis a partir do DBAccess Build 20200606:**

* **SETUSEROWINSDT=ON|OFF** : Permite ligar ou desligar a criação da coluna interna I\_N\_S\_D\_T\_ para novas tabelas. Pode retornar "OK" em caso de sucesso, "NOT\_SUPPORTED" caso o Banco de Dados não tenha suporte para a coluna I\_N\_S\_D\_T\_, ou "INVALID\_OPTION" caso seja informado um parâmetro diferente de "ON" ou "OFF".
* **GETUSEROWINSDT** : Consulta se a criação da coluna I\_N\_S\_D\_T\_ para novas tabelas está habilitada, retorna "ON" ou "OFF".
* **SETAUTOINSDT=ON|OFF** : Permite habilitar a criação automática da coluna I\_N\_S\_D\_T\_ na abertura da tabela. Pode retornar "OK" em caso de sucesso, "NOT\_SUPPORTED" caso o Banco de Dados não tenha suporte para a coluna I\_N\_S\_D\_T\_, ou "INVALID\_OPTION" caso seja informado um parâmetro diferente de "ON" ou "OFF".
* **GETAUTOINSDT** : Consulta se a criação automática da coluna I\_N\_S\_D\_T\_ na abertura da tabela está habilitada, retorna "ON" ou "OFF".

**As opções abaixo estarão disponíveis a partir do DBAccess Build 20210202:**

* **TCSOFTREFRESH=ON|OFF** : Permite habilitar uma mudança de comportamento na função TCRefresh(), chamado de "Soft Refresh", para que ela não refaça o cache da definição de campos e índices da tabela, mas apenas atualize o registro de último registro inserido no banco de dados.
* **GETTCSOFTREFRESH** : Consulta se o comportamento de "Soft Refresh" está habilitada, retorna "ON" ou "OFF".

**As opções abaixo estarão disponíveis a partir do DBAccess Build 20210911:**

* **GETTEMPNAME=<TABLE>** : retorna o nome físico de uma tabela temporária tradicional ou temporária compartilhada. Somente é possível pegar o nome real após criar a tabela. Para tabelas temporárias compartilhadas, a função retorna o nome da última tabela temporária compartilhada criada. Em caso de erro, a função pode retornar as seguintes mensagens:

| Índice | Mensagem | Descrição |
| --- | --- | --- |
| 1 | ERROR\_UNSUPPORTED | Este banco não suporta tabelas temporárias tradicionais. |
| 2 | ERROR\_INVALID\_NAME | O nome de tabela informado não corresponde a uma tabela temporária tradicional ou compartilhada. |
| 3 | ERROR\_ARGUMENT\_MISSING | Não foi informado um nome de tabela como argumento. |

* **GETAUTORECNO** : consulta se o comportamento de "AUTORECNO" está habilitada, retorna "ON" ou "OFF".
* **SETAUTORECNO=ON|OFF** : permite habilitar o auto RECNO, que faz com que o banco trate o incremento do campo RECNO, retirando esse controle do DBAccess.

**As opções abaixo estarão disponíveis a partir da versão do DBAccess 24.1.0.0:**

* **SETVIEWENABLED=ON|OFF** : Habilita a consulta ao catalogo do banco de dados para procurar por views.
* **GETVIEWENABLED** : Retorna se a opção VIEWENABLED está habilitada.
* **SETTEMPKEEPALIVE=<NNN>** : seta um tempo diferenciado de timeout antes de criar a tabela, deve ser setado antes da criação, ou o Default será usado (Default = 300 segundos ( 5 minutos )). Vale para a conexão a partir do momento que for setado.
* **SETUUIDFIELDS=<XXX,...>** : informa ao DBAccess quais campos devem ser tratados como UUID. Antes de criar a tabela deve ser informado ao DBAccess, usando a função TCConfig("SETUUIDFIELDS=<XXX,...>"), passando como parâmetro os campos que devem ser tratados como UUID, separados por vírgula. Cada banco vai implementar o tipo de campo adequado, conforme abaixo:
* MSSQL usa tipo "uniqueidentifier", alimentando automaticamente pela constraint default do campo usando a função do SGDB NEWID();
* POSTGRES usa tipo "UUID", alimentando automaticamente pela constraint default do campo usando a função do SGDB uuid\_generate\_v1();
* ORACLE usa tipo "RAW" de 16 bytes, alimentando automaticamente pela constraint default do campo usando a função do SGDB SYS\_GUID().
* Na inserção do registro, um campo UUID com constraint cria o UUID para o campo, desde que o valor de UUID não seja informado na inserção. Caso seja informado, será mantido o valor informado.
* Na alteração do registro, uma alteração pode tentar limpar o campo. Se o campo é UUID, com ou sem constraint, qualquer tentativa de limpar o valor será ignorada, sem dar erro.
* Se houver alteração de um UUID, para um valor diferente do atual, a alteração somente será aceita se ele for um campo NC ( No Constraint , ou sem constraint default), usado para registrar amarrações. Se o campo for um UUID "base" ( Com constraint default ), o DBAccess não vai permitir a alteração, e gerar error.log com a ocorrência " TOP Error -29 - Unsupported CHANGE VALUE OF BASE UUID COLUMN XXXXX ( From tISAMFile::Update ), onde XXXXX indica a coluna que houve tentativa de alteração.
* **SETUUIDFIELDSNC=<XXX,...>** : seta tratamento de campos tipo UUID SEM CONSTRAINT por nome, sem criar a constraint default do campo para inserção. Recurso implementado para MSSQL, ORACLE e POSTGRES.
* Na inserção do registro, um campo UUID com constraint cria o UUID para o campo, desde que o valor de UUID não seja informado na inserção. Caso seja informado, será mantido o valor informado.
* Na alteração do registro, uma alteração pode tentar limpar o campo. Se o campo é UUID, com ou sem constraint, qualquer tentativa de limpar o valor será ignorada, sem dar erro.
* Se houver alteração de um UUID, para um valor diferente do atual, a alteração somente será aceita se ele for um campo NC ( No Constraint , ou sem constraint default), usado para registrar amarrações. Se o campo for um UUID "base" ( Com constraint default ), o DBAccess não vai permitir a alteração, e gerar error.log com a ocorrência " TOP Error -29 - Unsupported CHANGE VALUE OF BASE UUID COLUMN XXXXX ( From tISAMFile::Update ), onde XXXXX indica a coluna que houve tentativa de alteração.
* **LISTUUIDFIELDS=<TABLE>** : retorna a lista de campos com tratamento UUID de uma determinada tabela, separados por vírgula. Como somente um campo pode possuir constraint default, este campo será identificado pelo caractere "\*" prefixando o nome do campo. A ordem retornada dos campos corresponde a ordem lógica dos campos na estrutura da tabela.

## Exemplos

cppEclipsetruefalse

## Veja também

* [Implementação - Campo de controle adicional no DBAccess - S\_T\_A\_M\_P\_](https://tdn.totvs.com/x/v6y8Hg)
* [Implementação - Campo de controle adicional no DBAccess - I\_N\_S\_D\_T\_](https://tdn.totvs.com/x/NVY9I)
