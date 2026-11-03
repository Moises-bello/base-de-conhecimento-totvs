---
content_hash: 7d6b6ae15c00d686ba03a0ee0a1f67dda844a5f9c5edeb388753d145241645be
fetched_at: '2026-06-29T00:08:31.753925+00:00'
page_id: '273308221'
product: rm
source: tdn-rm
title: Processo de Migração de dados entre coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273308221
version: 15
---

A migração e incorporação de dados entre coligadas consiste em fazer cópia de dados cadastrais de uma coligada para outra, utilizando bases RM para RM ou de outros fornecedores de software para o RM.

São três tipos de processos para migração de dados entre coligadas.

**1 - Processo de MIGRAÇÃO TOTAL**

Onde serão migrados os dados cadastrais e parâmetros de uma coligada para outra.

A coligada origem será inativada, pois seus dados serão migrados totalmente para nova coligada.

**2 - Processo de MIGRAÇÃO PARCIAL**

Onde serão migrados os dados cadastrais e parâmetros de forma parcial de uma coligada para outra.

Trata-se da transferência parcial de funcionários da coligada origem para a nova coligada (destino)

**3 - Processo de INCORPORAÇÃO**

Onde serão incorporados dados cadastrais e parâmetros de forma parcial de uma coligada para outra.

Neste cenário não há criação de nova coligada.

A seguir será detalhado os passos para execução destes processos.

**1 - Processo de MIGRAÇÃO TOTAL**

O processo de migração total consiste na criação de uma nova coligada pelo usuário (novo CNPJ) e transferência de todos os dados da coligada origem para esta nova coligada (coligada destino)

Podendo ser de RM para RM ou de um outro fornecedor de software para o RM.

**1.1 - RM para o RM**

Para isto, será necessário seguir os passos abaixo:

1 – Criar uma nova coligada informando o novo CPNJ manualmente.

2 – Fazer a cópia de dados cadastrais de tabelas da coligada origem para a nova coligada (destino) conforme tabelas abaixo:

* Agrupamentos de Contas Gerenciais entre coligadas
* Agrupamentos de Contas Contábeis entre coligadas
* Encargos entre coligadas
* Parâmetros de Lançamentos Financeiros entre coligadas
* Sindicatos entre coligadas
* Eventos entre coligadas
* Funções entre coligadas
* Grupo de Eventos entre coligadas
* Composição de Rateio por Eventos entre coligadas
* Tabelas de Cálculo entre coligadas
* Tarifa entre coligadas
* Linhas de transporte entre coligadas
* Valor fixo entre coligadas
* Tabelas Dinâmicas
* Valores Fixos
* Tabelas de Cálculos
* Clientes Fornecedores
* Rateios de Eventos
* Fórmulas
* Consultas SQL
* Tarifas de Transporte
* Linhas de Transporte

Como exemplo, veja no help como fazer a cópia de eventos entre coligadas:

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosCopiarColigadas.aspx>

3 – Na folha de pagamento, as tabelas onde não há o processo de cópia entre coligadas deverá utilizar o módulo de exportação e importação de dados.

Veja no help como proceder : <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ImportacaoDadosFolhaPagamentos.aspx>

Abaixo as tabelas que poderão ser exportadas e importadas pelo módulo de Importação .Net da folha de pagamento.

* Cargos
* Centro de Custo
* Campos complementares  dependentes
* Verbas de Férias - Adicionais de férias

Para o produto TOTVS Automação de Ponto poderá utilizar o módulo de exportação de importação de dados deste produto das seguintes tabelas disponíveis:

* Parâmetros  do sindicato
  + Parâmetros e abonos
* Dados dos Funcionários  
  + Parâmetros
  + Horários

4 – Para migrar os dados de funcionários, será necessário utilizar o módulo de transferência de funcionário, veja como proceder: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.RescisaoColetiva.aspx>

5 – Após a transferência dos funcionários, deverá executar as rotinas de cálculo e fechamento da folha para garantir o funcionamento dos processos de folha nesta nova coligada.

6 – Na coligada origem deverá executar o módulo  Rescisão Coletiva, marcando a opção “Realiza Transferência para outra base de dados".

Este processo irá colocar todos os funcionários na situação “D”, sem rescisão calculada.

Exemplo:

**ANTES DA MIGRAÇÃO TOTAL**

**DEPOIS DA MIGRAÇÃO TOTAL**

**1.2 – Outro Fornecedor de Folha Pagamento para o RM**

No caso de uma migração de dados total de um outro fornecedor de software para o RM, no caso folha de pagamento, deverá exportar os dados no produto origem (outro fornecedor) no layout RM, conforme help layout de tabelas<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.ImportacaoDadosFolhaPagamentos.aspx>, e importar através do módulo de importação .Net do Labore.

Os arquivos textos a serem importados já deverão ter os códigos sincronizados com as coligadas do RM (utilização de de/para), importante para realização de transferência entre empresas onde os códigos cadastrais deverão estar sincronizados.

Obs.: Os de/paras deverão ser realizados de forma manual diretamente no arquivo texto.

As seções, na coligada destino deverão ser criados manualmente ou editadas no arquivo de seção antes da importação.

O cadastro de "chefes e supervisores" na coligada destino, deverão ser criados manualmente.

Para o produto TOTVS Automação de Ponto poderá utilizar o módulo de exportação de importação de dados deste produto das seguintes tabelas disponíveis:

* Parâmetros  do sindicato
  + Parâmetros e abonos
* Dados dos Funcionários  
  + Parâmetros
  + Horários

Para os produtos TOTVS Gestão de Pessoas e TOTVS Segurança e Medicina do Trabalho, a empresa poderá contratar os nossos  serviços de Fábrica para migração dos dados, pois não há importação de dados cadastrais.

**2 - Processo de MIGRAÇÃO PARCIAL**

O processo de migração parcial consiste na transferência de funcionários de uma coligada existente para uma nova coligada.

Podendo ser de RM para RM ou de um outro fornecedor de software para o RM.

Para isto, será necessário seguir os passos abaixo:

1 – Criar uma nova coligada informando o novo CPNJ manualmente.

2 – Fazer a cópia de dados cadastrais de tabelas da coligada origem para a nova coligada (destino) conforme tabelas abaixo:

* Agrupamentos de Contas Gerenciais entre coligadas
* Agrupamentos de Contas Contábeis entre coligadas
* Encargos entre coligadas
* Parâmetros de Lançamentos Financeiros entre coligadas
* Sindicatos entre coligadas
* Eventos entre coligadas
* Funções entre coligadas
* Grupo de Eventos entre coligadas
* Composição de Rateio por Eventos entre coligadas
* Tabelas de Cálculo entre coligadas
* Tarifa entre coligadas
* Linhas de transporte entre coligadas
* Valor fixo entre coligadas
* Tabelas Dinâmicas
* Valores Fixos
* Tabelas de Cálculos
* Clientes Fornecedores
* Rateios de Eventos
* Fórmulas
* Consultas SQL
* Tarifas de Transporte
* Linhas de Transporte

Como exemplo, veja no help como fazer a cópia de eventos entre coligadas:

<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosCopiarColigadas.aspx>

3 – Na folha de pagamento, as tabelas onde não há o processo de cópia entre coligadas, poderá  utilizar o módulo de exportação e importação de dados.

Abaixo as tabelas que deverão ser exportadas e importadas pelo módulo de Importação .Net da folha de pagamento.

* Cargos
* Centro de Custo
* Campos complementares  dependentes
* Verbas de Férias - Adicionais de férias

Para o produto Automação de Ponto deverá utilizar o módulo de exportação de importação de dados deste produto das seguintes tabelas disponíveis:

* + Parâmetros  do sindicato
    - Parâmetros e abonos
  + Dados dos Funcionários  
    - Parâmetros
    - Horários

4 – Deverá criar as novas seções das filiais dos funcionários que serão transferidos manualmente ou via exportação/importação de dados.

5 – No caso de manter os mesmos códigos de seção na coligada destino, não será necessário um arquivo de DEPARA, porém se os códigos de seção da filial na coligada destino são diferentes, poderá contratar a nossa Fábrica para gerar um script de cópia de funcionários com DEPARA de Seção.

6 – Após a carga de dados dos funcionários e de seção, deverá executar as rotinas de cálculo e fechamento da folha para garantir o funcionamento dos processos de folha nesta coligada.

7 – Na coligada origem deverá executar o módulo  Rescisão Coletiva, marcando a opção “Realiza Transferência para outra base de dados".

Este processo irá colocar todos os funcionários na situação “D”, sem rescisão calculada.

**Exemplo:**

**ANTES DA MIGRAÇÃO**

**DEPOIS DA MIGRAÇÃO**

**3 - Processo de Incorporação**

O processo de incorporação consiste em incorporar dados cadastrais de uma coligada já existente para uma outra coligada também existente.

Exemplo: Uma coligada possui três filiais e deseja incorporar essas três filiais na coligada destino, sendo que a coligada destino já possui uma filial.

**Quando os códigos dos cadastros e os parâmetros são iguais nas duas coligadas.**

1 – Deverá criar as novas seções manualmente dos funcionários que serão transferidos para coligada destino.

2 – No caso de manter os mesmos códigos de seção na  coligada destino, não será necessário um arquivo de DEPARA

3 - Caso os códigos de seção sejam diferentes na coligada destino,  a empresa poderá contratar  a Fábrica e  solicitar um script de cópia de funcionários com DEPARA.

4 - Caso os códigos de seção sejam diferentes,  a migração dos dados do funcionário não poderá utilizar o processo de transferência de funcionário,  poderá contratar serviço de Fábrica  para executar script que simule esta transferência , com tratativas de depara.

5 . Eventos com códigos de fórmulas diferentes, conteúdo de evento diferente e código não existente na coligada destino deverá ser avaliados manualmente na base de dados e sincronizados com a coligada origem.

Exemplos :

**Conteúdo de cadastro diferente**

o Evento 0082 na coligada origem é um provento, já na coligada destino é um desconto.

Deverá adequar estes eventos utilizando deparas para que os eventos tenham natureza correta.

**Cadastro de fórmulas**

Deverá adequar as fórmulas que utilizam o mesmo evento e na coligada destino o conteúdo é diferente.  Deverá fazer tratativa com a condição “SE” na fórmula da coligada destino.

Exemplo: SE coligada 1 tratativa CASO CONTRÁRIO coligada 2 tratativa 2

Caso a empresa desejar, poderá contratar serviço da Fábrica ou consultoria do suporte.

**Outros Cadastros**

Deverá incluir cadastros que existem na coligada origem e não existem na coligada destino.

6 – Após a carga de dados dos funcionários e seção, deverá executar as rotinas de cálculo e fechamento da folha para garantir o funcionamento dos processos de folha nesta coligada.

7 – Na coligada origem deverá executar o módulo  Rescisão Coletiva, marcando a opção “Realiza Transferência para outra base de dados".

A coligada origem ficará  inativa.

Exemplo:

**ANTES DA INCORPORAÇÃO**

**DEPOIS INCORPORAÇÃO**

**Quando os códigos dos cadastros e os parâmetros NÃO são iguais nas duas coligadas.**

1 – Deverá utilizar o módulo de exportação/importação com os códigos cadastrais já sincronizados.

Para isto, deverá editar os arquivos de exportação e informar os códigos sincronizados manualmente ou contratar nosso serviço da Fábrica.
