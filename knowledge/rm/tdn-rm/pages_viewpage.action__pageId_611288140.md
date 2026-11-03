---
content_hash: 651f89b7a270632d5dab547342e0b90fa471ed406f7e7dfacef93a02207278f4
fetched_at: '2026-06-29T00:10:59.080535+00:00'
page_id: '611288140'
product: rm
source: tdn-rm
title: Extração de dados do Balancete Consolidado - Ernst & Young
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611288140
version: 2
---

Essa documentação tem como intuito orientar o usuário para a correta utilização dos objetos gerenciais referentes à extração de dados nos formatos esperados pela consultoria Ernst & Young.

falsedeckCompletotrueConsolidation trial balance (Consolidação do Balancete)slide

Através desse layout é possível extrair dados consolidados da contabilidade, de duas ou mais empresas, que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

A exportação desse arquivo é realizada através do layout **CTBLAY0024 - Exportacao do Balancete Consolidado - ErnstYoung**. 

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Código do Plano de Contas Consolidado: Plano Consolidado a ser utilizado para extração dos dados.

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do arquivo.

| ID | Formato | Tamanho | Dec | Descrição | Origem dos Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 30 |  | Código da coligada | Código da coligada que deu origem ao saldo da conta. |  |
| 2 | Alfanumérico | 30 |  | Código da conta | Código da conta existente no plano de contas consolidado. |  |
| 3 | Alfanumérico | 30 |  | Segmento da conta | Não aderente ao RM. |  |
| 4 | Alfanumérico | 30 |  | Ano Fiscal | Não aderente ao RM. |  |
| 5 | Alfanumérico | 40 |  | Período Fiscal | Não aderente ao RM. |  |
| 6 | Decimal |  | 2 | Saldo de fechamento na moeda funcional | Saldo consolidado da primeira moeda. | O Saldo devedor deve ser gerado positivo e o Saldo credor negativo. |
| 7 | Alfanumérico | 30 |  | Código da moeda funcional | Moeda corrente existente nos parâmetros do módulo contábil. |  |
| 8 | Decimal |  | 2 | Saldo final na moeda de apresentação | Não aderente ao RM. |  |
| 9 | Alfanumérico | 30 |  | Código da moeda de apresentação | Não aderente ao RM. |  |

Component listing (Lista de Componentes)slide

 Listagem das Coligadas que foram consolidadas no arquivo CTB - Consolidation trial balance.

A exportação desse arquivo é realizada através do layout **CTBLAY0024 - Exportacao do Balancete Consolidado - ErnstYoung**.

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Código do Plano de Contas Consolidado: Plano Consolidado a ser utilizado para extração dos dados.

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do arquivo.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 30 |  | Código do componente | Código da Coligada. | Código da coligada que está sendo consolidada. Esse código será referenciado no arquivo "Consolidation trial balance (Consolidação do Balancete)". |
| 2 | Alfanumérico | 30 |  | Nome do Componente | Nome da Coligada. |  |

Chart of accounts (Plano de Contas)slide

Listagem das contas consolidadas que foram exibidas no arquivo CTB - Consolidation trial balance.

A exportação desse arquivo é realizada através do layout **CTBLAY0024 - Exportacao do Balancete Consolidado - ErnstYoung**. 

falseDadosParâmetros

#### Dinâmicos (podem variar de acordo com o uso)

Código da Coligada: será preenchido de acordo com o Contexto global do Sistema.

Data Inicial: data inicial do intervalo para busca das Partidas.

Data Final: data final do intervalo para busca das Partidas.

Código do Plano de Contas Consolidado: Plano Consolidado a ser utilizado para extração dos dados.

ExemploCampos

#### Abaixo destacam-se os dados retornados pelo serviço, que serão utilizados no preenchimento do relatório.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Numérico |  | 2 | Código da Conta Consolidada | Código da conta do plano de contas paralelo. | Código da conta consolidada que está sendo consolidada. Esse código será referenciado no arquivo "Consolidation trial balance (Consolidação do Balancete)". |
| 2 | Alfanumérico | 30 |  | Segmento da Conta | Não aderente ao RM. |  |
| 3 | Alfanumérico | 30 |  | Nome da Conta | Nome da conta no plano de contas paralelo. |  |
| 4 | Alfanumérico | 30 |  | Tipo da Conta | Natureza da conta para emissão do sped e natureza da conta (credora ou devedora). | Se a Natureza do SPED for "Conta de Ativo", então "Assets".  Se a Natureza do SPED for "Conta de Passivo", então "Liabilities".  Se a Natureza do SPED for "Patrimônio Liquido", então "Equity".  Se a Natureza do SPED for "Conta de Resultado" e a Natureza for Credora, então "Revenue".  Se a Natureza do SPED for "Conta de Resultado" e a Natureza for Devedora, então "Expenses" Caso contrário, será gerado vazio. |
| 5 | Alfanumérico | 30 |  | Subtipo | Não aderente ao RM. |  |
| 6 | Alfanumérico | 30 |  | Classe | Não aderente ao RM. |  |
| 7 | Alfanumérico | 30 |  | SubClasse | Não aderente ao RM. |  |
