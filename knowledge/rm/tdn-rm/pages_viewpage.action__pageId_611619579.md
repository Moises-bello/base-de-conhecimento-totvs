---
content_hash: ffb92506b29386944634e7f1ff7d69da8e30f9982a8444b70f85e755ebe33a01
fetched_at: '2026-06-29T00:10:59.148867+00:00'
page_id: '611619579'
product: rm
source: tdn-rm
title: Extração de Dados Financeiros- Ernst & Young
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611619579
version: 13
---

Essa documentação tem como intuito orientar o usuário para a correta utilização dos objetos gerenciais referentes à consultoria Ernst & Young.

falsedeckCompletotrueContas a Receber (Trade Receivables)slide

Foi disponibilizado um serviço que será responsável por retornar determinadas informações sobre títulos financeiros a receber, respeitando os parâmetros (filtros) de entrada.

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Layout: layout do Gerador de Saídas a ser usado para geração das informações.

Diretório de Destino: diretório onde os arquivos serão gerados.

Data Inicial: data inicial do intervalo para busca do(s) lançamento(s) financeiro(s) (serão filtrados considerando FLAN.DATAEMISSAO).

Data Final: data final do intervalo para busca do(s) lançamento(s) financeiro(s) (serão filtrados considerando FLAN.DATAEMISSAO).

#### Estáticos (definidos internamente e não variam)

Tipo do(s) Lançamento(s) Financeiro(s): serão listados apenas registros do tipo "A Receber".

Status do(s) Lançamento(s) Financeiro(s): serão listados apenas registros com status "Em Aberto" ou "Parcialmente Baixado".

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório (exibidos somente os campos gerados).

| Campo | Descrição | Arquivo |
| --- | --- | --- |
| Customer account code | Identificação única do cliente (cadastro Clientes/Fornecedores) no seguinte formato:  Coligada do cliente + | + Código do cliente  Ex: 1|C00001 | Customer master |
| Customer account name | Nome Fantasia do cliente | Customer master |
| Customer state | Estado do Endereço Principal do cliente | Customer master |
| Customer country | Descrição do País do Endereço Principal do cliente. | Customer master |
| Customer postal code | Código postal do Endereço Principal do cliente | Customer master |
| Payment terms description | Descrição da Condição de Pagamento default Venda do anexo "Condições de Pagamento Default de Clientes/Fornecedores" | Customer master |
| Transaction code | Identificador único do lançamento financeiro no formato:  Coligada + | + Ref. Lançamento  Ex: 1|123456 | Open transactions |
| Transaction line | Número do documento do lançamento | Open transactions |
| Transaction type code | Código do Tipo de Documento do lançamento | Open transactions |
| Business unit code | Código da Coligada selecionada para geração do relatório | Open transactions |
| Customer account code | Identificação do cliente no lançamento financeiro no formato:  Coligada Cliente/Fornecedor + | + Código Cliente/Fornecedor  Ex: 1|C00001 | Open transactions |
| Document date | Data de Emissão do lançamento financeiro | Open transactions |
| Transaction due date | Data de Vencimento do lançamento financeiro | Open transactions |
| Entry date | Data de Criação do lançamento financeiro | Open transactions |
| Effective date | Data Previsão Baixa do lançamento financeiro | Open transactions |
| Functional amount | Se lançamento financeiro com status "Em aberto" traz o Valor Original, caso "Parcialmente Baixado" valor restante (Valor Original descontado do Valor Original baixado) | Open transactions |
| Functional currency code | Código da moeda configurado para o módulo TOTVS Gestão Financeira. | Open transactions |
| Functional original amount | Valor original do lançamento | Open transactions |
| Document original amount | Valor original do lançamento | Open transactions |
| Document amount | Se lançamento financeiro como origem no módulo TOTVS Gestão de Estoque, Compras e Faturamento buscar valor do movimento relacionado, caso contrário, Valor Original do lançamento. | Open transactions |
| Document amount currency code | Código da Moeda do valor original do lançamento financeiro | Open transactions |

Importante!

Os campos **Functional amount**,****Functional original amo**unt**,**Document original amount**,e **Document amount**(Trade Receivables e Trade Payables) tem sua quantidade de casas decimais pré-definidas de acordo com o esperado pelo Relatório base Ernst & Young (duas casas).

Outro detalhe a se destacar é que esses campos sempre serão arredondados, tomando como base a informação citada acima.

Cada layout irá gerar quatro arquivos TXT contendo dados extraídos dos serviços do financeiro. São eles:

* **FIN - Customer master** (Mestre do cliente)

Dados do cliente: irá trazer os dados de todos os clientes/fornecedores dos lançamentos retornados pelos serviços.

* **FIN - Open transactions** (Transações abertas)

Dados das transações em aberto:

Contas a receber: irá trazer lançamentos financeiros a receber da coligada corrente com status "em aberto" ou "Parcialmente baixado". Os campos necessários e o respectivo mapeamento está no layout do relatório.

Contas a pagar: irá trazer lançamentos financeiros a pagar da coligada corrente com status "em aberto" ou "Parcialmente baixado". Os campos necessários e o respectivo mapeamento está no layout do relatório.

**Importante**: Para lançamentos em aberto o layout usa o Valor Original na apuração dos valores, já para os parcialmente baixados o Valor Original subtraído do Valor Original Baixado.

* **FIN - Transaction type** (Tipo de Documento)

Dados do tipo de documento: irá trazer os dados do tipo das transações movimentadas (tipo de documento). O código será levado no relatório principal (código e descrição) nos lançamentos retornados pelos serviços.

* **FIN - Business Unit** (Unidade de Negócio)

Dados das coligadas: irá trazer os dados de todas as coligadas dos lançamentos retornados pelos serviços.

Arquivos gerados como exemplo:

Contas a Pagar (Trade Payables)slide

Foi disponibilizado um serviço que será responsável por retornar determinadas informações sobre títulos financeiros a receber, respeitando os parâmetros (filtros) de entrada.

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Layout: layout do Gerador de Saídas a ser usado para geração das informações.

Diretório de Destino: diretório onde os arquivos serão gerados.

Data Inicial: data inicial do intervalo para busca do(s) lançamento(s) financeiro(s) (serão filtrados considerando FLAN.DATAEMISSAO).

Data Final: data final do intervalo para busca do(s) lançamento(s) financeiro(s) (serão filtrados considerando FLAN.DATAEMISSAO).

#### Estáticos (definidos internamente e não variam)

Tipo do(s) Lançamentos Financeiro(s): serão listados apenas registros do tipo "A Pagar".

Status do(s) Lançamentos Financeiro(s): serão listados apenas registros com status "Em Aberto" ou "Parcialmente Baixado".

Campos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório (exibidos somente os campos gerados).

| Campo | Descrição | Arquivo |
| --- | --- | --- |
| Vendor account code | Identificação única do fornecedor (cadastro Clientes/Fornecedores) no seguinte formato:  Coligada do fornecedor+ | + Código do fornecedor  Ex: 1|F00001 | Customer master |
| Vendor account name | Nome Fantasia do fornecedor | Customer master |
| Vendor state | Estado do Endereço Principal do fornecedor | Customer master |
| Vendor country | Descrição do País do Endereço Principal do fornecedor. | Customer master |
| Customer postal code | Código postal do Endereço Principal do fornecedor | Customer master |
| Payment terms description | Descrição da Condição de Pagamento default Venda do anexo "Condições de Pagamento Default de Clientes/Fornecedores" | Customer master |
| Transaction code | Identificador único do lançamento financeiro no formato:  Coligada + | + Ref. Lançamento  Ex: 1|123456 | Open transactions |
| Transaction line | Número do documento do lançamento | Open transactions |
| Vendor invoice reference | Se lançamento originado do módulo TOTVS Gestão de Estoque, Compras e Faturamento carrega o Número do movimento. Se lançamento gerado a partir de uma fatura, busca o Número do Documento da mesma, caso contrário o Número do Documento do lançamento | Open transactions |
| Transaction type code | Código do Tipo de Documento do lançamento financeiro | Open transactions |
| Business unit code | Código da Coligada selecionada para geração do relatório | Open transactions |
| Vendor account code | Identificação do fornecedor no lançamento financeiro no formato:  Coligada Cliente/Fornecedor + | + Código Cliente/Fornecedor  Ex: 1|F00001 | Open transactions |
| Document date | Data de Emissão do lançamento financeiro | Open transactions |
| Transaction due date | Data de Vencimento do lançamento financeiro | Open transactions |
| Entry date | Data de Criação do lançamento financeiro | Open transactions |
| Effective date | Data Previsão Baixa do lançamento financeiro | Open transactions |
| Functional amount | Se lançamento financeiro com status "Em aberto" traz o Valor Original, caso "Parcialmente Baixado" valor restante (Valor Original descontado do Valor Original baixado) | Open transactions |
| Functional currency code | Código da moeda configurado para o módulo TOTVS Gestão Financeira. | Open transactions |
| Document amount | Se lançamento financeiro como origem no módulo TOTVS Gestão de Estoque, Compras e Faturamento buscar valor do movimento relacionado, caso contrário, Valor Original do lançamento. | Open transactions |
| Document amount currency code | Código da Moeda do valor original do lançamento financeiro | Open transactions |
| Original amount | Valor Original do lançamento financeiro | Open transactions |
| Original currency | Código da Moeda do valor original do lançamento financeiro | Open transactions |

Importante!

Os campos **Functional amount**,**Functional original amount**,**Document original amount**,e **Document amount**(Trade Receivables e Trade Payables) tem sua quantidade de casas decimais pré-definidas de acordo com o esperado pelo Relatório base Ernst & Young (duas casas).

Outro detalhe a se destacar é que esses campos sempre serão arredondados, tomando como base a informação citada acima.

Cada layout irá gerar quatro arquivos TXT contendo dados extraídos dos serviços do financeiro. São eles:

* **FIN - Customer master** (Mestre do cliente)

Dados do cliente: irá trazer os dados de todos os clientes/fornecedores dos lançamentos retornados pelos serviços.

* **FIN - Open transactions** (Transações abertas)

Dados das transações em aberto:

Contas a receber: irá trazer lançamentos financeiros a receber da coligada corrente com status "em aberto" ou "Parcialmente baixado". Os campos necessários e o respectivo mapeamento está no layout do relatório.

Contas a pagar: irá trazer lançamentos financeiros a pagar da coligada corrente com status "em aberto" ou "Parcialmente baixado". Os campos necessários e o respectivo mapeamento está no layout do relatório.

**Importante**: Para lançamentos em aberto o layout usa o Valor Original na apuração dos valores, já para os parcialmente baixados o Valor Original subtraído do Valor Original Baixado.

* **FIN - Transaction type** (Tipo de Documento)

Dados do tipo de documento: irá trazer os dados do tipo das transações movimentadas (tipo de documento). O código será levado no relatório principal (código e descrição) nos lançamentos retornados pelos serviços.

* **FIN - Business Unit** (Unidade de Negócio)

Dados das coligadas: irá trazer os dados de todas as coligadas dos lançamentos retornados pelos serviços.

Arquivos gerados como exemplo:
