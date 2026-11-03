---
content_hash: 8010a951ac0baab35c851622dc57175db055bf32fb5e9583f870342769f2088e
fetched_at: '2026-06-29T00:10:59.067608+00:00'
page_id: '611287311'
product: rm
source: tdn-rm
title: Extração de dados do Razão Contábil - Ernst & Young
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611287311
version: 5
---

Essa documentação tem como intuito orientar o usuário para a correta utilização dos objetos gerenciais referentes à extração de dados nos formatos esperados pela consultoria Ernst & Young.

falsedeckCompletotrueJournal Entries (Lançamentos no Diário)slide

Através desse layout é possível extrair dados dos lançamentos contábeis diários que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **CTBLAY0023 - Exportacao do Razão - ErnstYoung**. 

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Gerar Journal Entries (Lançamentos no Diário): marcar para que o arquivo seja gerado.

#### Estáticos (definidos internamente e não variam)

Serão consideradas as Partidas integradas ao lote 0 (zero).

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do arquivo.

| ID | Formato | Tamanho | Dec | Descrição | Origem dos Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 100 |  | Número do Lançamento Contábil | Identificador do lançamento contábil. | O lançamento contábil pode ser composto por uma ou mais partidas. |
| 2 | Alfanumérico | 100 |  | Número da linha do Lançamento | Identificador da partida contábil. | Concatenar o identificador da partida com 0 se for conta a débito e 1 se for conta a crédito.  Exemplo: Se na partida 123 a conta utilizada for a débito o número da linha no lançamento será 123\_0, porém se a conta for a crédito será 123\_1. |
| 3 | Alfanumérico | 100 |  | Código da Conta Contábil | Código da conta a débito ou a crédito. |  |
| 4 | Alfanumérico | 25 |  | Unidade de Negócios | Código da coligada que deu origem ao lançamento. | Empresa do lançamento. |
| 5 | Decimal |  | 2 | Valor da partida na moeda funcional | Valor informado na partida contábil. |  |
| 6 | Alfanumérico | 25 |  | Código da Moeda Funcional | Moeda corrente existente nos parâmetros do módulo contábil. |  |
| 7 | Decimal |  | 2 | Valor da partida na moeda de apresentação | Segundo valor informado na partida contábil. | Esse campo só será preenchido se o valor da moeda de apresentação for superior a zero. |
| 8 | Alfanumérico | 25 |  | Moeda de Apresentação | Moeda do segundo valor existente nos parâmetros do modulo contábil. | Esse campo só será preenchido se o valor da moeda de apresentação for superior a zero e o sistema estiver parametrizado para trabalhar com segundo valor. |
| 9 | Alfanumérico | 25 |  | Ano Fiscal | Ano da partida contábil. |  |
| 10 | Alfanumérico | 25 |  | Período Fiscal | Mês da partida contábil. |  |
| 11 | Data |  |  | Data efetiva de Lançamento | Data da partida contábil. |  |
| 12 | Data |  |  | Data da última atualização do Lançamento | Data em que ocorreu a inclusão ou a última alteração da partida contábil. |  |
| 13 | Alfanumérico | 25 |  | Usuário da última atualização | Código do usuário que incluiu ou atualizou a partida pela última vez. |  |
| 14 | Alfanumérico | 25 |  | Módulo do Lançamento | Módulo de origem do lançamento. |  |
| 15 | Alfanumérico | 250 |  | Descrição do Lançamento | Descrição do lançamento contábil. |  |
| 16 | Alfanumérico | 250 |  | Descrição da Linha do Lançamento | Descrição da partida contábil. | Campo formado pela concatenação da descrição do histórico padrão  com o complemento existente na partida. |

Chart of accounts (Plano de Contas)slide

Através desse layout é possível extrair dados das contas contábeis que foram referenciadas no arquivo de lançamentos do diário. Essas informações irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **CTBLAY0023 - Exportacao do Razão - ErnstYoung**.

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Gerar Chart of accounts (Plano de Contas): marcar para que o arquivo seja gerado.

#### Estáticos (definidos internamente e não variam)

Serão consideradas as Partidas integradas ao lote 0 (zero).

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do arquivo.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 200 |  | Código da Conta Contábil | Conta contábil existente na partida do lançamento contábil. | Essa informação está presente no arquivo de lançamentos do diário. |
| 2 | Alfanumérico | 200 |  | Descrição da Conta Contábil | Descrição da conta contábil existente na partida do lançamento contábil. |  |
| 3 | Alfanumérico | 200 |  | Código da Empresa | Código da coligada que deu origem ao lançamento contábil. | Essa informação está presente no arquivo de lançamentos do diário. |

Source Listing (Origens)slide

Através desse layout é possível extrair dados dos módulos de origem que foram referenciados no arquivo de lançamentos do diário. Essas informações irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **CTBLAY0023 - Exportacao do Razão - ErnstYoung**.

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Gerar Source Listing (Origens): marcar para que o arquivo seja gerado.

#### Estáticos (definidos internamente e não variam)

Serão consideradas as Partidas integradas ao lote 0 (zero).

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 100 |  | Código da Origem | Identificador do módulo de origem do lançamento contábil. | Essa informação está presente no arquivo de lançamentos do diário. |
| 2 | Alfanumérico | 250 |  | Descrição da Origem | Descrição do módulo de origem do lançamento contábil. |  |

User Listing (Usuários)slide

Através desse layout é possível extrair dados dos usuários que foram referenciadas no arquivo de lançamentos do diário. Essas informações irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **CTBLAY0023 - Exportacao do Razão - ErnstYoung**.

DadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Gerar User Listing (Usuários): marcar para que o arquivo seja gerado.

#### Estáticos (definidos internamente e não variam)

Serão consideradas as Partidas integradas ao lote 0 (zero).

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 100 |  | Identificação do Usuário | Código do usuário que incluiu ou realizou a última alteração da partida existente no lançamento contábil. | Essa informação está presente no arquivo de lançamentos do diário. |
| 2 | Alfanumérico | 250 |  | Nome Completo do Usuário | Nome do usuário que incluiu ou realizou a última alteração da partida existente no lançamento contábil. |  |

Company or Business Unit Listing (Empresa ou Unidade de Negócio)slide

Através desse layout é possível extrair dados das empresas de foram referenciadas no arquivo de lançamentos do diário. Essas informações irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **CTBLAY0023 - Exportacao do Razão - ErnstYoung**.

DadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Gerar Company or Business Unit Listing (Empresa ou Unidade de Negócio): marcar para que o arquivo seja gerado.

#### Estáticos (definidos internamente e não variam)

Serão consideradas as Partidas integradas ao lote 0 (zero).

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 25 |  | Código da Empresa | Código da coligada que deu origem ao lançamento contábil. | Essa informação está presente no arquivo de lançamentos do diário. |
| 2 | Alfanumérico | 100 |  | Descrição da Empresa | Descrição da coligada que deu origem ao lançamento contábil. |  |

Trial balance (Balancete)slide

Através desse layout é possível extrair dados da contabilidade, de uma empresa ou organização, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **CTBLAY0023 - Exportacao do Razão - ErnstYoung**.

DadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Gerar Trial balance (Balancete): marcar para que o arquivo seja gerado.

#### Estáticos (definidos internamente e não variam)

Serão consideradas as Partidas integradas ao lote 0 (zero).

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| ID | Formato | Tamanho | Dec | Descrição | Origem de dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 200 |  | Código da Conta contábil | Conta presente nas partidas existentes nos lançamentos contábeis. |  |
| 2 | Alfanumérico | 25 |  | Empresa | Código da coligada que deu origem ao lançamento contábil. |  |
| 3 | Data |  |  | Data de Início da extração | Data inicial do período em que a auditoria está sendo realizada. |  |
| 4 | Data |  |  | Data Fim da extração | Data final do período em que a auditoria está sendo realizada. |  |
| 5 | Alfanumérico | 25 |  | Ano Fiscal | Não aderente ao RM. |  |
| 6 | Alfanumérico | 25 |  | Período Fiscal | Não aderente ao RM. |  |
| 7 | Decimal |  | 2 | Saldo inicial na moeda funcional | Saldo anterior da primeira moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 8 | Decimal |  | 2 | Saldo final na moeda funcional | Saldo atual da primeira moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 9 | Alfanumérico | 25 |  | Código da Moeda Funcional | Moeda corrente existente nos parâmetros do módulo contábil. |  |
| 10 | Decimal |  | 2 | Saldo inicial na moeda de apresentação | Saldo anterior da segunda moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 11 | Decimal |  | 2 | Saldo final na moeda de apresentação | Saldo atual da segunda moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 12 | Alfanumérico | 25 |  | Código da Moeda de apresentação | Moeda do segundo valor existente nos parâmetros do modulo contábil. |  |
