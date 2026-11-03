---
content_hash: 5bfe9bc164b8fb487900a3c55f1ac38a171366605114ea4067c2306bd36e125e
fetched_at: '2026-06-29T00:11:25.453153+00:00'
page_id: '708888470'
product: rm
source: tdn-rm
title: Painéis de Cenários SCAE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708888470
version: 26
---

# **1 - Síntese**

No intuito de facilitar o acompanhamento e o envio das informações de produção do SESI. Os painéis de cenários desenvolvidos no SGE apresentarão de forma simplificada e gráfica as informações enviadas pelo extrator SCAE.

As informações apresentadas nos painéis de cenários são exatamente as extraídas pelo extrator SCAE, porém podem ter diferenças com relação a quantidade de matrículas que foram importadas no SCAE, essa diferença está relacionada a críticas que podem apresentar ao subir o arquivo, o que não é tratado nos painéis de cenários.

Cenários Disponíveis:

* Produção da Educação Básica
* Produção da Educação Infantil
* Produção Ensino Fundamental
* Produção Ensino Médio
* Produção Educação de Jovens e Adultos

# **2 - Processo para importação dos Painéis de Cenários**

Ao realizar a importação dos Painéis de Cenários que já existam no SGE, ou seja, ao executar uma atualização, é preciso excluir os Painéis de Cenários, Cubo, Gráficos e Consultas SQL já existentes e nesta ordem, para que o novo painel importado seja atualizado corretamente. **Consultar item 4 - Atualização dos Painéis de Cenários**.

É recomendado criar uma categoria de gráfico e cubo vinculados aos perfis que terão acesso aos painéis de cenários e facilitando a manutenção em caso de atualizações.

A importação deve ser realizada na coligada SESI.

Para que as informações sejam consumidas pelos cenários, foi implementando no extrator SCAE o preenchimento da tabela ZSCAEPRODMES com os campos necessários, a tabela é alimentada com os dados referente ao Mês/Ano de produção durante a execução do extrator.

É pré-requisito que o extrator SCAE esteja atualizado. Para solicitar a última versão é necessário abrir ticket no PRIME.

Serão apresentando os dados de produção a partir de 01/2022. Para popular a tabela utilizada pelos cenários, é necessário que o regional execute o extrator para os meses retroativos, somente após a execução que os dados serão apresentados. A execução do extrator para os meses retroativos não tem impacto na produção já enviada para o SCAE.

## 2.1 - Download dos Painéis de Cenários

## 2.2 - Importação

É necessário que o usuário tenha acesso ao menu “Gestão | Painéis de Cenários” liberado no seu perfil.

Para realizar a importação, acesse o modulo Educacional e acione o menu “Gestão | Painéis de Cenários (clicar no ícone) ” (Figura 1), selecione o ícone ”Importar Cenários” (Figura 2), onde será apresentado um Wizard nativo do SGE.

*Figura 1 – Menu para o cadastro dos Painéis de Cenários*

*Figura 2 - Importar Cenários*

Na tela apresentada, selecione a opção “Adicionar Objetos” e selecione o Cenário a ser importado (Figura 3) e em seguida, selecione a opção “Abrir”.

*Figura 3 - Seleção do arquivo para Importação dos Painéis de Cenários*

Após a seleção dos arquivos, certifique-se que todos os objetos (Cenário, RmPart, Gráfico, Cubo e ConsSQL) estejam selecionados (Figura 4), informe na aba “**Seleção de Usuários**” se os cenários serão importados somente para o usuário Logado ou uma Lista de Usuários, essa opção deve ser informada para cada cenário na tela do importador.

Não é recomentado selecionar a opção Todos na aba “**Seleção de Usuários**”, ao marcar essa opção os cenários serão importados para cada usuário cadastrado no SGE, impactando no crescimento das tabelas GPARTSUSR, GPARTSUSRPART e GPARTSUSRPARTPARAM e no tempo de execução do processo de importação.

*Figura 4 - Seleção dos objetos para Importação dos Painéis de Cenários*

Informe a “Categoria” do Gráfico e Cubo (Figura 5 e 6). Nesse momento, conforme recomendado anteriormente, pode ser criado uma categoria de Gráfico e Cubo vinculados aos perfis que terão acesso aos painéis de cenários e facilitando a manutenção em caso de atualizações. Esse processo se repete para cada Gráfico e Cubo a ser importado.

*Figura 5 – Informando a categoria do Gráfico*

*Figura 6 – Informando a categoria do Cubo*

Para os regionais onde o código da coligada SESI é diferente de 2 (Template SGE), será necessário também desmarcar a opção “Importar na coligada e sistema originais da consulta” (Figura 7). Essa opção deve ser desmarcada para cada ConsultaSQL importada. Para os regionais onde o código da coligada SESI é **igual** a 2 não é necessária nenhuma ação nessa tela.

*Figura 7 – Desmarcando a opção* “Importar na coligada e sistema originais da consulta”

Após realizar os procedimentos acima em todos Cenários, clique em “Executar” e aguarde o fim da execução do processo.

*Figura 8 – Fim da execução do processo*

Os cenários foram criados na coligada SESI, é necessário realizar o Logout / Login no SGE antes do primeiro acesso para que os parâmetros sejam carregados corretamente (Figura 9).

*Figura 9 – Fechar a janela Cenários*

# **3 - Acessando Painéis de Cenários**

Os cenários estarão disponíveis somente para os usuários informados na importação e que estejam associados aos perfis das categorias informadas nos gráficos e cubos.

É necessário que o usuário tenha acesso ao menu “Gestão | Painéis de Cenários” liberado no seu perfil (Figura 10). É recomendado também uma revisão do perfil do usuário para que tenha acesso somente as opções necessárias.

*Figura 10 – Permissão do Menu Painéis de Cenários do perfil*

## 3.1 - Acesso

Dentro modulo Educacional, é possível acessar os cenários de duas formas;

1. Acione o menu “Gestão | Painéis de Cenários (clicar no ícone) ” (Figura 11), assim o usuário visualiza todos os cenários disponíveis para ele.

*Figura 11 – Acesso a todos os Cenários*

2. Acione o menu “Gestão | Painéis de Cenários (clicar na seta) ” (Figura 12), assim o usuário visualiza somente o cenário solicitado.

*Figura 12 – Acesso a um Cenário especifico*

Selecionando um determinado cenário, é necessário informar os parâmetros desejados. Os parâmetros são comuns entre os gráficos de um cenário, sendo necessário informar uma única vez na área destinada conforme (Figura 13).

*Figura 13 – Informando os parâmetros do Cenário*

Para o cenário “Produção da Educação Básica” é necessário informar também os parâmetros para atualização do Cubo (Figura 14 e 15).

*Figura 14 – Atualizar dados do Cubo*

*Figura 15 – Informar os parâmetros para atualização do Cubo*

*Figura 16 – Cenário Produção da Educação Básica*

## 3.2 - Parâmetros

* **DATA\_INICIO\_D:** Informar a data de início da produção a ser visualizada.

Ex: Visualizar a produção a partir de Janeiro de 2022, deve ser informado 01/01/2022.

* **DATA\_FIM\_D:** Informar a data final da produção a ser visualizada.

Ex: Visualizar a produção até de Dezembro de 2022, deve ser informado 01/12/2022.

* **CODFILIAL\_S:** Informar o código da filial a ser visualizada ou ‘%’ para visualizar todas.
* **SEXO\_D:** Informar ‘M’ para visualizar somente o sexo Masculino ou ‘F’ para visualizar somente o sexo Feminino. Para visualizar todos informar ‘%’.

## 3.3 - RMPart dos Cenários

### **3.3.1 - Produção da Educação Básica**

Gráficos:

* Evolução das matrículas totais - Educação Básica
* Matrículas Educação Básica por etapa de ensino e tipo de financiamento
* Evolução das matrículas por etapa de ensino
* Matrículas Educação Básica por série/ano
* Hora-Aluno Educação Básica por série/ano
* Matrículas Educação Básica por categoria

Cubo:

* Matrículas Educação Básica por escola e etapa de ensino

Consulta SQL:

* TOTVS.CBSESI.001 - Matrículas Educação Básica por escola e etapa de ensino
* TOTVS.GFSESI.001 - Evolução das matrículas totais - Educação Básica
* TOTVS.GFSESI.002 - Matrículas Educação Básica por etapa de ensino e tipo de financiamento
* TOTVS.GFSESI.003 - Evolução das matrículas por etapa de ensino
* TOTVS.GFSESI.004 - Matrículas Educação Básica por série/ano
* TOTVS.GFSESI.005 - Hora-Aluno Educação Básica por série/ano
* TOTVS.GFSESI.006 - Matrículas Educação Básica por categoria

### 3.3.2 - Produção da Educação Infantil

Gráficos:

* Evolução das matrículas Educação Infantil
* Distribuição das matrículas Educação Infantil
* Evolução das matrículas Educação Infantil por tipo de financiamento
* Matrículas Creche e Pré-escola por tipo de financiamento
* Hora-Aluno Educação Infantil
* Matrícula Educação Infantil por categoria

Consulta SQL:

* TOTVS.GFSESI.007 - Evolução das matrículas Educação Infantil
* TOTVS.GFSESI.008 - Distribuição das matrículas Educação Infantil
* TOTVS.GFSESI.009 - Evolução das matrículas Educação Infantil por tipo de financiamento
* TOTVS.GFSESI.010 - Matrículas Creche e Pré-escola por tipo de financiamento
* TOTVS.GFSESI.011 - Hora-Aluno Educação Infantil
* TOTVS.GFSESI.012 - Matrícula Educação Infantil por categoria

### 3.3.3 - Produção Ensino Fundamental

Gráficos:

* Evolução das matrículas Ensino Fundamental
* Distribuição das matrículas Ensino Fundamental
* Evolução das matrículas Ens. Fundamental por tipo de financiamento
* Matrículas Ensino Fundamental por ano e tipo de financiamento
* Hora-Aluno Ensino Fundamental
* Matrículas Ensino Fundamental por categoria

Consulta SQL:

* TOTVS.GFSESI.013 - Evolução das matrículas Ensino Fundamental
* TOTVS.GFSESI.014 - Distribuição das matrículas Ensino Fundamental
* TOTVS.GFSESI.015 - Evolução das matrículas Ens. Fundamental por tipo de financiamento
* TOTVS.GFSESI.016 - Matrículas Ensino Fundamental por ano e tipo de financiamento
* TOTVS.GFSESI.017 - Hora-Aluno Ensino Fundamental
* TOTVS.GFSESI.018 - Matrículas Ensino Fundamental por categoria

### 3.3.4 - Produção Ensino Médio

Gráficos:

* Evolução das matrículas Ensino Médio
* Matrículas Ensino Médio por série
* Distribuição das matrículas Novo Ensino Médio
* Matrículas Ensino Médio por categoria
* Hora-Aluno Ensino Médio
* Evolução das matrículas Ensino Médio por tipo de financiamento

Consulta SQL:

* TOTVS.GFSESI.019 - Evolução das matrículas Ensino Médio
* TOTVS.GFSESI.020 - Matrículas Ensino Médio por série
* TOTVS.GFSESI.021 - Evolução das matrículas Ensino Médio por tipo de financiamento
* TOTVS.GFSESI.022 - Distribuição das matrículas Novo Ensino Médio
* TOTVS.GFSESI.023 - Hora-Aluno Ensino Médio
* TOTVS.GFSESI.024 - Matrículas Ensino Médio por categoria

### 3.3.5 - Produção Educação de Jovens e Adultos

Gráficos:

* Evolução das matrículas EJA
* Matrículas EJA por etapa de ensino e tipo de financiamento
* Evolução das matrículas EJA por modalidade de ensino
* Distribuição das matrículas Nova EJA
* Hora-Aluno EJA
* Matrículas EJA por categoria
* Matrículas Educação de Jovens e Adultos
* Matrículas por modalidade de ensino

Consulta SQL:

* TOTVS.GFSESI.025 - Evolução das matrículas EJA
* TOTVS.GFSESI.026 - Matrículas EJA por etapa de ensino e tipo de financiamento
* TOTVS.GFSESI.027 - Evolução das matrículas EJA por modalidade de ensino
* TOTVS.GFSESI.028 - Distribuição das matrículas Nova EJA
* TOTVS.GFSESI.029 - Hora-Aluno EJA
* TOTVS.GFSESI.030 - Matrículas EJA por categoria
* TOTVS.GFSESI.031 - Matrículas Educação de Jovens e Adultos
* TOTVS.GFSESI.032 - Matrículas por modalidade de ensino

# **4 - Atualização****dos Painéis de Cenários**

Para atualização dos Painéis de Cenários é necessário excluir os Painéis de Cenários, Cubo, Gráficos e Consultas SQL conforme sequencia abaixo.

## 4.1 - Excluir Painéis de Cenários

Acesse o modulo Educacional e acione o menu “Gestão | Painéis de Cenários (clicar no ícone)” (Figura 17), selecione a aba referente aos cenários listados abaixo e clique sobre a opção **Deletar Guia Selecionada** (Figura 18).

* Produção da Educação Básica
* Produção da Educação Infantil
* Produção Ensino Fundamental
* Produção Ensino Médio
* Produção Educação de Jovens e Adultos

A exclusão dos cenários e feita de forma individual, por usuário, mesmo se a importação do cenário for feita escolhendo mais de um usuário. Ou seja, cada usuário deve realizar a exclusão do cenário.

*Figura 17 – Menu dos Painéis de Cenários*

*Figura 18 – Deletar Guia Selecionada*

## 4.2 - Excluir Cubo

Acesse o modulo Inteligência de Negócios e acione o menu “Gestão Estratégica | Cubo” (Figura 19), crie um novo filtro (Título LIKE Matrículas Educação%) conforme (Figura 20) e clique em executar.

*Figura 19 – Acessando Cadastro de Cubos*

*Figura 20 – Criando novo filtro Cadastro de Cubos*

Selecione o Cubo (Matrículas Educação Básica por escola e etapa de ensino) e clique no ícone excluir (Figura 21).

*Figura 21 – Excluir Cubo Selecionado*

## 4.3 - Excluir Gráficos

Acesse o modulo Educacional e acione o menu “Gestão | Gráfico (clicar no ícone)” (Figura 22), crie um novo filtro (Parâmetros exclusivos da fonte de dados LIKE %TOTVS.GFSESI.0%) conforme (Figura 23) e clique em executar.

*Figura 22 – Acessando Cadastro de Gráfico*

*Figura 23 – Criando novo filtro Cadastro de Gráfico*

Confirme se todos os gráficos listados pertencem a categoria utilizada na importação do Painéis de Cenários, selecione todos os gráficos e clique no ícone excluir (Figura 24).

*Figura 24 – Excluir Gráficos Selecionados*

## 4.4 - Excluir Consultas SQL

Acesse o modulo Educacional e acione o menu “Gestão | Visões de Dados (clicar no ícone)” (Figura 25), crie um novo filtro (Código LIKE TOTVS.GFSESI.0% OU Código LIKE TOTVS.CBSESI.0% ) conforme (Figura 26) e clique em executar.

*Figura 25 – Acessando Visões de Dados (Consultas SQL)*

*Figura 26 – Criando novo filtro Visões de Dados (Consultas SQL)*

Selecione todas Consultas SQL listadas e clique no ícone excluir (Figura 27).

*Figura 27 – Excluir Consulta SQL Selecionadas*

*Figura 28 – Verificar se as consultas SQL estão associadas no SGE*

Caso apresente erro na exclusão das consultas SQL, deve ser analisado o log e identificar onde as consultas ainda estão associadas. Somente depois de remover todas as associações será possível excluir todas consultas SQL referentes aos Painéis de Cenários.

Realizado todas etapas de exclusão dos Painéis de Cenários, Cubo, Gráficos e Consultas SQL pode iniciar uma nova importação dos Painéis de Cenários conforme **item 2 - Processo para importação dos Painéis de Cenários.**
