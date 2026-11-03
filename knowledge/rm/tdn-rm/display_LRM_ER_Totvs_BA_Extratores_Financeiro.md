---
content_hash: 21c6f9ce189d8e72bedf7261031f1a03b3f7793f7a549a485b2dca028f370f58
fetched_at: '2026-06-29T00:06:24.781453+00:00'
page_id: '224120769'
product: rm
source: tdn-rm
title: ER_Totvs_BA_Extratores_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Totvs_BA_Extratores_Financeiro
version: 130
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Linha RM | **Módulo** | Totvs Gestão Financeira |
| **Segmento Executor** | Educacional | | |
| **Projeto** | CTB - Projeto de Desenvolvimento - 12.1.9 | **IRM** | PCREQ-8810 |
| **Requisito** | PCREQ-8813 | **Subtarefa** | PDR\_EDU\_CTB005-33 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

Definir a regra dos extratores do Financeiro que alimentam os dados para o TOTVS Smart Analytics.

## Definição da Regra de Negócio

Dimensões

| Dimensão | Tabela Stage |
| --- | --- |
| CLIENTE | HJ7 |
| EMPRESA | HJ4 |
| ESPECIE DOCUMENTO | HJG |
| ESTABELECIMENTO | HKK |
| FORNECEDOR | HKJ |
| MODALIDADE | HJF |
| MOEDA | HJ6 |
| PORTADOR | HG4 |
| REGIAO | HJB |
| REPRESENTANTE | HJC |

Fatos

| Nome da Fato | **Tabela StageArea** |
| --- | --- |
| CONTAS A PAGAR CARTEIRA | HKL |
| CONTAS A PAGAR PAGAMENTO | HLI |
| CONTAS A PAGAR VENCIMENTO | HLD |
| CONTAS A RECEBER CARTEIRA | HLL |
| CONTAS A RECEBER RECEBIMENTO | HLI |
| CONTAS A RECEBER VENCIMENTO | HLE |

Os conceitos utilizados para a extração dos dados são disponibilizados no caminho {PATH\_RM}\ObjetosGerenciais\Conceito\TOTVSBA.

Ex.: C:\totvs\CorporeRM\ObjetosGerenciais\Conceito\TOTVSBA

As fórmulas visuais para execução dos conceitos serão disponibilizadas no caminho {PATH\_RM}\ObjetosGerenciais\Fórmulas Visuais\TOTVSBA.

 Ex.: C:\totvs\CorporeRM\ObjetosGerenciais\Fórmulas Visuais\TOTVSBA

Os extratores RM utilizam a versão nova do conceito RM para extrair os dados da base. Para utilização dos extratores é necessário dicionar a tag abaixo para aumentar o timeout de execução dos DataServers

<add key="DBSCommandTimeout" value="100000" />

 

**Configuração do BA**

 O Configurador do extrator do TOTVS Smart Analytics se encontra no módulo Integração aba Ferramentas do RM.exe. Na primeira tela informamos o usuário e senha da base do Corpore e na tela seguinte selecionamos o projeto de integração TOTVS Business Analytics. Na tela seguinte deve-se informar os dados para conexão na base stage (Fluig Smart Data) e o caminho onde se encontram os conceitos dos extratores. Os conceitos serão importados já configurados para a base RM como origem e para a base stage (Fluig Smart Data) como destino. Todas as tabelas e views do BA serão recriadas e o configurador irá criar/atualizar as tabelas da base stage área (Fluig Smart Data), criar os parâmetros utilizados nos extratores e realizar a carga inicial nas tabelas.

 O configurador não faz a importação das fórmulas visuais. Elas devem ser importadas manualmente após rodar o configurador pelo processo *Importação de Fórmula Visual* na visão da mesma. Para cada fórmula ser importada é necessário marcar “Todas Coligadas” na Seleção da Coligada, informar uma categoria na aba Parâmetros e selecionar a consulta da fórmula e selecionar “Fixo” no “Código da Consulta SQL”.

 

**Parametrizador BA**

Após a execução do Configurador é necessário acessar os Parâmetros localizado no módulo Integração.Os parâmetros do BA são divididos entre Parâmetros Globais (divididos em Gerais, Extração, TOTVS Smart Analytics, Educacional e Recursos Humanos) e Parâmetros por Empresa (divididos em Educacional, Recursos Humanos, Controladoria, Materiais, Comercial e Financeiro). Vamos detalhar aqueles que influenciam o Financeiro.

Globais: 

* Gerais: o parâmetro Ativar integração vem por padrão desmarcado, o parâmetro Portador serve para indicar qual tabela opcional do financeiro será utilizada para definir o portador. As tabelas opcionais são definidas nos parâmetros de Contas a Pagar do Financeiro na etapa Tabelas Opcionais do Financeiro.
* Extração: aqui é definido o período de extração dos dados do RM. Ele pode ser fixo ou variável. No modo fixo é definida uma data inicial e uma data final para a extração dos dados.  Esta forma é muito útil para validação das informações e carga inicial da stage área (Fluig Smart Data). No modo Variável pode-se escolher entre intervalos mensais ou intervalos diários. Ao se executar o conceito inicial de extração a data inicial e a data final são calculadas em função da data de execução e dos períodos configurados. Dias/Meses a serem subtraídos da data atual para calcular a data inicial e Dias/Meses a serem adicionados a data atual para calcular a data final. O parâmetro Extração por Fato define os períodos de extração específicos para cada fato. O parâmetro já vem preenchido com todas as fatos disponíveis na linha RM com a configuração sugerida de período de extração. Para que esta configuração sobrescreva a configuração padrão é necessário habilitá-la.
* Educacional: no parâmetro Instituição de Ensino define-se como o nome da instituição de ensino será formado. As opções são Coligada, Filial ou Coligada - FiIial.

Por empresa:

* Educacional: os parâmetros do Educacional são *Situação de Matrícula*, que serve para identificar as situações de matriculas que são consideradas perda de aluno para a instituição de ensino, e *Bolsa de Estudo*, que serve para identificar o campo complementar do Financeiro que é utilizado para armazenar o valor da bolsa oferecida aos alunos.
* Financeiro: os parâmetros Financeiros são *Tipos de Documento a Pagar*, que que indica quais os tipos de documento a pagar que serão enviados para o BA, e *Tipos de Documento a Receber*, que indica quais os tipos de documento a receber que serão enviados para o BA.

**Fórmulas Visuais BA**

As fórmulas visuais do BA são responsáveis em executar os conceitos do BA (extratores), enviar um e-mail com o status da execução e gravar o log da execução no server. No caso do GoodData ela também chama o Smart Analytics Agent para enviar os dados para a nuvem GoodData e envia o log da execução do Agent junto no e-mail da execução do extrator.

 Atividades TOTVS BA

* Executa Conceito BA: Recebe uma consulta SQL e executa os conceitos passados na consulta. Retorna o log e o status da execução.
* Executa Smart Analytics Agent: Recebe o endereço do java.exe, do programa Agent (jar) e do arquivo de configuração do Agent. Retorna o log de execução do Agent.

Layout Fórmula Visual TOTVS BA

Layout Fórmula Visual TOTVS BA (GoodData)

**Métricas do Financeiro**

| Fato | Indicador | Descrição | Fórmula |
| --- | --- | --- | --- |
| **Contas a Pagar - Carteira** | PMP Carteira | Indica a média em dias correspondente ao período entre a emissão do título até a data de vencimento para a carteira de contas a pagar. | Soma(Prazo Vencimento Carteira \* Vl a Pagar / Total(Vl a Pagar)) |
| **Contas a Pagar - Carteira** | Prazo Vencimento Carteira | Indica a diferença em dias entre a data de vencimento e a data de emissão do título em carteira. | - |
| **Contas a Pagar - Carteira** | Vl Substituição Carteira | Indica o valor do documento que foi substituído. | - |
| **Contas a Pagar - Carteira** | Vl a Pagar | Indica o valor do saldo atual disponível para o título a pagar. | - |
| **Contas a Pagar - Pagamento** | PMP Realizado | Indica a média em dias correspondente ao período entre a emissão do título até a data de pagamento. | Soma(Prazo Pagamento \* Vl Pago / Total(Vl Pago)) |
| **Contas a Pagar - Pagamento** | Prazo Pagamento | Indica a diferença em dias entre a data de pagamento e data de emissão do título. | - |
| **Contas a Pagar - Pagamento** | Vl Desconto Recebido | Indica o valor total de todos os descontos obtidos. | - |
| **Contas a Pagar - Pagamento** | Vl Juros Pagos | Indica o valor total dos juros pagos, inclusive multa. | - |
| **Contas a Pagar - Pagamento** | Vl Juros Pagos no Ano Anterior | Indica o valor total dos juros pagos, inclusive multa para o mesmo período do ano anterior em relação ao definido no relatório ou dashboard. | Soma(Vl Juros Pagos(Ano Anterior)) |
| **Contas a Pagar - Pagamento** | Vl Substituição Pagamento | Indica o valor do documento que foi substituído. | - |
| **Contas a Pagar - Pagamento** | Vl Pago | Indica o total dos valores vencidos. Este valor representa o quanto a empresa ficou inadimplente com seus fornecedores. | - |
| **Contas a Pagar - Vencimento** | PMP Previsto | Indica a média em dias correspondente ao período entre a emissão do título até a data de vencimento. | Soma(Prazo Vencimento \* Vl Vencimento / Total(Vl Vencimento)) |
| **Contas a Pagar - Vencimento** | Prazo Vencimento | Indica a diferença em dias entre a data de vencimento e a data de emissão do título. | - |
| **Contas a Pagar - Vencimento** | Vl Comprado | Indica o valor total comprado, ou seja, o valor do título implantado no contas a pagar. | - |
| **Contas a Pagar - Vencimento** | Vl Comprado no Ano Anterior | Apresenta o valor da métrica Vl Comprado para o mesmo período do ano anterior em relação ao definido no relatório ou dashboad. | Soma (Vl Comprado(Ano Anterior)) |
| **Contas a Pagar - Vencimento** | Vl Substituição Vencimento | Indica o valor do documento que foi substituído. | - |
| **Contas a Pagar - Vencimento** | Vl Vencimento no Ano Anterior | Indica o valor a pagar ou o saldo que a empresa tem a pagar junto aos seus fornecedores para o mesmo período do ano anterior em relação ao definido no relatório ou dashboard. | Soma(Vl Vencimento(Ano Anterior)) |
| **Contas a Pagar - Vencimento** | Vl Vencimento | Indica o valor a pagar ou o saldo que a empresa tem a pagar junto aos seus fornecedores. | - |
| **Contas** **a Receber - Carteira** | PMR Carteira | Indica a média em dias correspondente ao período entre a emissão do título até a data de vencimento para a carteira de contas a receber. | Soma(Prazo Vencimento Carteira \* Vl a Receber / Total(Vl a Receber)) |
| **Contas** **a Receber - Carteira** | Prazo Vencimento Carteira | Indica a diferença em dias entre a data de vencimento e a data de emissão  do título em carteira. | - |
| **Contas** **a Receber - Carteira** | Vl Substituição Carteira | Indica o valor do documento que foi substituído. | - |
| **Contas** **a Receber - Carteira** | Vl a Receber | Indica o valor do saldo atual disponível para o título a receber. | - |
| **Contas** **a Receber - Recebimento** | PMR Realizado | Indica a média em dias correspondente ao período entre a emissão do título até a data de recebimento. | Soma(Prazo Recebimento \* Vl Recebido / Total(Vl Recebido)) |
| **Contas** **a Receber - Recebimento** | Prazo Recebimento | Indica a diferença em dias entre a data de recebimento e a da emissão do título. | - |
| **Contas** **a Receber - Recebimento** | Vl Desconto Concedido | Indica o valor total de desconto concedido. | - |
| **Contas** **a Receber - Recebimento** | Vl Juros Recebidos | Indica o valor total dos juros cobrados. | - |
| **Contas** **a Receber - Recebimento** | Vl Substituição Recebimento | Indica o valor do documento que foi substituído. | - |
| **Contas** **a Receber - Recebimento** | Vl Recebido | Indica o valor recebido pelas cobranças feitas junto aos clientes. | - |
| **Contas** **a Receber - Recebimento** | Vl Recebido no Ano Anterior | Indica o valor recebido pelas cobranças feitas junto aos clientes no Ano Anterior. | Soma(Vl Recebido(Ano Anterior)) |
| **Contas** **a Receber - Vencimento** | PMR Previsto | Indica a média em dias correspondente ao período entre a emissão do título até a data de vencimento. | Soma(Prazo Vencimento \* Vl Vencimento / Total(Vl Vencimento)) |
| **Contas** **a Receber - Vencimento** | Prazo Vencimento | Indica a diferença em dias entre a data de vencimento e a data de emissão do título. | - |
| **Contas** **a Receber - Vencimento** | Saldo Vencido no Ano Anterior | Apresenta o valor da métrica Saldo Vencido para o mesmo período do ano anterior, em relação ao definido no relatório ou dashboard. | Soma(Saldo Vencido(Ano Anterior)) |
| **Contas** **a Receber - Vencimento** | Vl Faturado | Indica o valor total faturado, ou seja, o valor total dos títulos implantados no contas a receber. | - |
| **Contas** **a Receber - Vencimento** | Vl Faturado no Ano Anterior | Indica o valor total faturado, ou seja, o valor total dos títulos implantados no contas a receber no Ano Anterior. | Soma(Vl Faturado(Ano Anterior)) |
| **Contas** **a Receber - Vencimento** | Vl Substituição Vencimento | Indica o valor do documento que foi substituído. | - |
| **Contas** **a Receber - Vencimento** | Vl Vencimento | Indica o valor a receber ou o saldo que a empresa tem a receber junto aos seus clientes. | - |
| **Contas** **a Receber - Vencimento** | Vl Vencimento no Ano Anterior | Indica o valor a receber ou o saldo que a empresa tem a receber junto aos seus clientes para o mesmo período do ano anterior em relação ao definido no relatório ou dashboard. | Vl Vencimento (Ano Anterior) |

**Server de extração de dados**

* Contas a pagar - Carteira

ASSUNTO: Gestão de Pagamentos / Contas a Pagar, FATO: Contas a Pagar Carteira, Tabela: HLK

Filtra os títulos a receber em aberto ou parcialmente baixados: FLAN.PAGREC = 2 AND (FLAN.STATUSLAN = 0 OR FLAN.STATUSLAN = 4)

Campo Saldo: VALOR\_PAGAR = VALORORIGINAL - VALORBAIXADO

* Contas a pagar - Pagamento

ASSUNTO: Gestão de Pagamentos / Contas a Pagar, FATO: Contas a Pagar Pagamento, TABELA: HLI

Traz os lançamentos baixados (total ou parcial), ou seja, o que já foi pago dentro de um período (baseado na data da baixa).

Filtro:  FLAN.PAGREC = 2 AND (FLAN.STATUSLAN = 1 OR FLAN.STATUSLAN = 4) AND FLAN.DATABAIXA BETWEEN :DataInicial AND :DataFinal

onde :DataInicial e :DataFinal são os parâmetros para data de extração.

Campo Saldo: VALOR\_PAGO = VALORBAIXADO

* Contas a pagar - Vencimento

ASSUNTO: Gestão de Pagamentos / Contas a Pagar, FATO: Contas a Pagar Vencimento, TABELA: HLD

Traz os lançamentos em aberto (total ou parcial), ou seja os pendentes a pagar vencendo num período.

Filtro: FLAN.PAGREC = 2 AND FLAN.STATUSLAN NOT IN (1, 2, 3) AND FLAN.DATAVENCIMENTO BETWEEN :DataInicial AND :DataFinal

onde :DataInicial e :DataFinal são os parâmetros para data de extração.

Campo Saldo: VALOR\_VENCIMENTO = chama cálculo do valor líquido com data atual

* Contas a receber - Carteira

ASSUNTO: Gestão de Pagamentos / Contas a Receber, FATO: Contas a Receber Carteira, Tabela: HLL

Traz os lançamentos pendentes pra receber, filtra os títulos a receber em aberto ou parcialmente baixados.

Filtro: FLAN.PAGREC = 1 AND (FLAN.STATUSLAN = 0 OR FLAN.STATUSLAN = 4)

Campo Saldo: VALOR\_RECEBER = VALORORIGINAL- VALORBAIXADO

* Contas a receber - Recebimento

ASSUNTO: Gestão de Pagamentos / Contas a Receber, FATO: Contas a Receber Pagamento, TABELA: HLJ

Traz os títulos a receber baixados ou parcialmente baixados

Filtro: FLAN.PAGREC = 1 AND (FLAN.STATUSLAN = 1 OR FLAN.STATUSLAN = 4) AND FLAN.DATABAIXA BETWEEN :DataInicial AND :DataFinal

onde :DataInicial e :DataFinal são os parâmetros para data de extração.

Campo Saldo: VALOR\_RECEBIDO = VALORBAIXADO

* Contas a receber - Vencimento

ASSUNTO: Gestão de Pagamentos / Contas a Pagar, FATO: Contas a Pagar Vencimento, TABELA: HLD

Traz os lançamentos em aberto (total ou parcial), ou seja os pendentes a receber vencendo num período.

Filtro: FLAN.PAGREC = 1 AND (FLAN.STATUSLAN = 0 OR FLAN.STATUSLAN = 4) AND FLAN.DATAVENCIMENTO BETWEEN :DataInicial AND :DataFinal

onde :DataInicial e :DataFinal são os parâmetros para data de extração.

Campo Saldo: VALOR\_VENCIMENTO = chama cálculo do valor líquido com data atual

*<Na tabela abaixo informe quais são as rotinas envolvidas, o tipo de operação, a opção de menu e se necessário uma breve descrição das regras de negócio relacionadas a rotina>.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

***Exemplo de Aplicação:***

* *Criar o campo “% Mínimo Espécie” (AAA\_PERESP) onde o usuário informará o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação.*
* *Criar o campo “Referência Mínima para Cálculo” (AAA\_REFCAL) onde o usuário informará um dos 4 valores disponíveis para pagamento das mensalidades  como a referência mínima para calcular o débito total do aluno.*
* *Criar o parâmetro MV\_ACPARNE que definirá se as informações de “% Mínimo Espécie” e “Referência Mínima para Cálculo” serão obrigatórias.*
* *O parâmetro MV\_ACPARNE deve ter as seguintes opções: 1=Obrigatório e 2=Opcional. Deve ser inicializado como opcional>.*

***Tabelas Utilizadas***

* *SE2 – Cadastro de Contas a Pagar*
* *FI9 – Controle de Emissão de DARF>.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Linha RM | **Módulo** | Totvs Gestão Financeira |
| **Segmento Executor** | Educacional | | |
| **Projeto** | CTB - Projeto de Desenvolvimento - 12.1.9 | **IRM** | PCREQ-8810 |
| **Requisito** | PCREQ-8813 | **Subtarefa** | PDR\_EDU\_CTB005-33 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

Definir a regra dos extratores do Financeiro que alimentam os dados para o TOTVS Smart Analytics.

## Definição da Regra de Negócio

Dimensões

| Dimensão | Tabela Stage |
| --- | --- |
| CLIENTE | HJ7 |
| EMPRESA | HJ4 |
| ESPECIE DOCUMENTO | HJG |
| ESTABELECIMENTO | HKK |
| FORNECEDOR | HKJ |
| MODALIDADE | HJF |
| MOEDA | HJ6 |
| PORTADOR | HG4 |
| REGIAO | HJB |
| REPRESENTANTE | HJC |

Fatos

| Nome da Fato | **Tabela StageArea** |
| --- | --- |
| CONTAS A PAGAR CARTEIRA | HKL |
| CONTAS A PAGAR PAGAMENTO | HLI |
| CONTAS A PAGAR VENCIMENTO | HLD |
| CONTAS A RECEBER CARTEIRA | HLL |
| CONTAS A RECEBER RECEBIMENTO | HLI |
| CONTAS A RECEBER VENCIMENTO | HLE |

Os conceitos utilizados para a extração dos dados são disponibilizados no caminho {PATH\_RM}\ObjetosGerenciais\Conceito\TOTVSBA.

Ex.: C:\totvs\CorporeRM\ObjetosGerenciais\Conceito\TOTVSBA

As fórmulas visuais para execução dos conceitos serão disponibilizadas no caminho {PATH\_RM}\ObjetosGerenciais\Fórmulas Visuais\TOTVSBA.

 Ex.: C:\totvs\CorporeRM\ObjetosGerenciais\Fórmulas Visuais\TOTVSBA

Os extratores RM utilizam a versão nova do conceito RM para extrair os dados da base. Para utilização dos extratores é necessário dicionar a tag abaixo para aumentar o timeout de execução dos DataServers

<add key="DBSCommandTimeout" value="100000" />

**Configuração do BA**

 O Configurador do extrator do TOTVS Smart Analytics se encontra no módulo Integração aba Ferramentas do RM.exe. Na primeira tela informamos o usuário e senha da base do Corpore e na tela seguinte selecionamos o projeto de integração TOTVS Business Analytics. Na tela seguinte deve-se informar os dados para conexão na base stage (Fluig Smart Data) e o caminho onde se encontram os conceitos dos extratores. Os conceitos serão importados já configurados para a base RM como origem e para a base stage (Fluig Smart Data) como destino. Todas as tabelas e views do BA serão recriadas e o configurador irá criar/atualizar as tabelas da base stage área (Fluig Smart Data), criar os parâmetros utilizados nos extratores e realizar a carga inicial nas tabelas.

 

O configurador não faz a importação das fórmulas visuais. Elas devem ser importadas manualmente após rodar o configurador pelo processo *Importação de Fórmula Visual* na visão da mesma. Para cada fórmula ser importada é necessário marcar “Todas Coligadas” na Seleção da Coligada, informar uma categoria na aba Parâmetros e selecionar a consulta da fórmula e selecionar “Fixo” no “Código da Consulta SQL”.

**Parametrizador BA**

Após a execução do Configurador é necessário clicar no botão Parâmetros localizado no módulo Integração aba Ferramentas.

*<Regra de negócio é o que define a forma de fazer o negócio, o processo definido e/ou as regras que devem ser contempladas. Devem ser descritas restrições, validações, condições e exceções do processo. Caso necessário, incluir neste capítulo também regras de integridade que devem ser observadas no momento do desenvolvimento>.*

*<Na tabela abaixo informe quais são as rotinas envolvidas, o tipo de operação, a opção de menu e se necessário uma breve descrição das regras de negócio relacionadas a rotina>.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

***Exemplo de Aplicação:***

* *Criar o campo “% Mínimo Espécie” (AAA\_PERESP) onde o usuário informará o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação.*
* *Criar o campo “Referência Mínima para Cálculo” (AAA\_REFCAL) onde o usuário informará um dos 4 valores disponíveis para pagamento das mensalidades  como a referência mínima para calcular o débito total do aluno.*
* *Criar o parâmetro MV\_ACPARNE que definirá se as informações de “% Mínimo Espécie” e “Referência Mínima para Cálculo” serão obrigatórias.*
* *O parâmetro MV\_ACPARNE deve ter as seguintes opções: 1=Obrigatório e 2=Opcional. Deve ser inicializado como opcional>.*

***Tabelas Utilizadas***

* *SE2 – Cadastro de Contas a Pagar*
* *FI9 – Controle de Emissão de DARF>.*

### Opcional

## Protótipo de Tela

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

### Opcional

## Dicionário de Dados

**Arquivo ou Código do Script:** AAA – Negociação Financeira / \*Versao=CP.2014.12\_03\*/

 

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | <FI9\_FILIAL+FI9\_IDDARF+FI9\_STATUS> |
| **02** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_EMISS+FI9\_IDDARF> |
| **03** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_PREFIX+FI9\_NUM+FI9\_PARCEL+FI9\_TIPO> |

|  |  |
| --- | --- |
| **Campo** | <AAA\_PERESP> |
| **Tipo** | <N> |
| **Tamanho** | <6> |
| **Valor Inicial** | <Varia de acordo com o tipo informado. Por exemplo, quando o campo “tipo” for date, neste campo pode ser informado uma data>. |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | <Referência Mínima para Cálculo> |
| **Título** | <Ref.Calc.> |
| **Picture** | <@E999.99> |
| **Help de Campo** | <Informar o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação> |

### (Opcional)

## Grupo de Perguntas

 

*<Informações utilizadas na linha Protheus>.*

 

**Nome: FINSRF2**

|  |  |
| --- | --- |
| **X1\_ORDEM** | 01 |
| **X1\_PERGUNT** | Emissão De |
| **X1\_TIPO** | D |
| **X1\_TAMANHO** | 8 |
| **X1\_GSC** | G |
| **X1\_VAR01** | MV\_PAR01 |
| **X1\_DEF01** | Comum |
| **X1\_CNT01** | '01/01/08' |
| **X1\_HELP** | Data inicial do intervalo de emissões das guias de DARF a serem consideradas na seleção dos dados para o relatório |

### (Opcional)

## Consulta Padrão

*<Informações utilizadas na linha Protheus>*

**Consulta: AMB**

|  |  |
| --- | --- |
| **Descrição** | Configurações de Planejamento |
| **Tipo** | Consulta Padrão |
| **Tabela** | “AMB” |
| **Índice** | “Código” |
| **Campo** | “Código”; ”Descrição” |
| **Retorno** | AMB->AMB\_CODIGO |

### (Opcional)

## Estrutura de Menu

*<Informações utilizadas na linha Datasul>.*

**Procedimentos**

|  |  |  |  |
| --- | --- | --- | --- |
| **Procedimento** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Módulo** |  |  |  |
| **Programa base** |  |  |  |
| **Nome Menu** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Registro padrão** | Sim | Sim | Sim |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Release de Liberação** |  |  |  |

**Programas**

|  |  |  |  |
| --- | --- | --- | --- |
| **Programa** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Nome Externo** |  |  |  |
| **Nome Menu/Programa** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Nome Verbalizado**[1]**** | (Max 254 posições) | (Max 254 posições) | (Max 254 posições) |
| **Procedimento** |  |  |  |
| **Template** | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) |
| **Tipo**[2]**** | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Categoria**[3]**** |  |  |  |
| **Executa via RPC** | Sim/Não | Sim/Não | Sim/Não |
| **Registro padrão** | Sim | Sim | Sim |
| **Outro Produto** | Não | Não | Não |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Query on-line** | Sim/Não | Sim/Não | Sim/Não |
| **Log Exec.** | Sim/Não | Sim/Não | Sim/Não |
| **Rotina (EMS)** |  |  |  |
| **Sub-Rotina (EMS)** |  |  |  |
| **Localização dentro da Sub Rotina (EMS)** |  |  |  |
| **Compact**[4]**** | Sim/Não | Sim/Não | Sim/Não |
| **Home**[5]**** | Sim/Não | Sim/Não | Sim/Não |
| **Posição do Portlet**[6]**** | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right |
| **Informar os papeis com os quais o programa deve ser vinculado** |  |  |  |

**Cadastro de Papéis**

*<O cadastro de papéis é obrigatório para os projetos de desenvolvimento FLEX a partir do Datasul 10>.*

*<Lembrete: o nome dos papeis em inglês descrito neste ponto do documento, devem ser homologados pela equipe de tradução>.*

|  |  |
| --- | --- |
| **Código Papel** | **(máx 3 posições)** |
| **Descrição em Português\*** |  |
| **Descrição em Inglês\*** |  |

---

[1] Nome Verbalizado é obrigatório para desenvolvimentos no Datasul 10 em diante.

[2] Tipo é obrigatório para desenvolvimento no Datasul 10 em diante

[3] Categorias são obrigatórias para os programas FLEX.

[4] Obrigatório quando o projeto for FLEX

[5] Obrigatório quando o projeto for FLEX

[6] Obrigatório quando o projeto for FLEX

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
