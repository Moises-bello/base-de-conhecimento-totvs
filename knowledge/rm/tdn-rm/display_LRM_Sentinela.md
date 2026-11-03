---
content_hash: ddef8418926643305fc5f1926907d25cfec6c4ac4ac3d111c25cb3eab728b8f2
fetched_at: '2026-06-29T00:11:48.751616+00:00'
page_id: '827314993'
product: rm
source: tdn-rm
title: Sentinela
type: documentation
url: https://tdn.totvs.com/display/LRM/Sentinela
version: 23
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **[Checagem Rápida de Ambiente](https://tdn.totvs.com/display/LRM/Sentinela#PaginaGeral--1467690101)**
3. **[Tarefas de Execução Agendada](https://tdn.totvs.com/display/LRM/Sentinela#PaginaGeral--1655563624)**
4. **[Ferramentas de Análise](https://tdn.totvs.com/display/LRM/Sentinela#PaginaGeral--1243500065)**

## **01. VISÃO GERAL**

O Sentinela é uma ferramenta de Monitoramento de Ambientes criada para que o usuário possa identificar possíveis ofensores de performance.

Para acessar a ferramenta, basta pesquisá-la no menu **Executar** ou acessar **Serviços Globais | Administração | Sentinela**:

PaginaGeraltrueChecagem Rápida

Aqui o usuário pode executar um checklist de itens relacionados a configurações do ambiente CorporeRM e também relacionados ao SGBD com a finalidade de apresentar pontos de melhoria em suas configurações:

Estas recomendações são apenas um direcionamento para uma boa operação do servidor de banco de dados e não deve ser considerado como único padrão de avaliação, monitoração, e configuração do banco de dados que deve ser realizado por o DBA responsável.IMPORTANTE!

SQL

Este módulo possui funcionalidades de checagem de ambiente, seja o Banco de Dados ou configurações do ambiente, no que tange a performance da aplicação. Muitas destas informações serão úteis para uma análise, permitindo avaliar possíveis problemas de performance ligados ao ambiente.

As opções de checagem poderão ser marcadas individualmente, possibilitando assim, filtrar os itens desejados para análise.

***Verificar .Config Server:***Verificar as configurações do arquivo .config  do Host e já ajusta o que se pode ajustar.

Para garantirmos o correto funcionamento do sistema em um ambiente N camadas, os arquivos de configurações devem ser configurados respeitando as orientações a seguir.

*Localizationlanguage:* A tag LOCALIZATIONLANGUAGE determina em qual linguagem o sistema irá funcionar, habilitar essa tag evita que o RM valide qual a linguagem o sistema operacional está configurado.

Exemplo: <add key=“LOCALIZATIONLANGUAGE” value “pt-BR” />

Visando melhorar a performance de acesso em bancos Oracle, existe um cache para armazenagem de dados do schema da base de dados. Este cache se faz necessário pois o "*GetSchema*" no Oracle tem um custo bastante caro. Para a correta utilização do mesmo, deve-se parametrizar o Config do Host da seguinte forma:

*UseDbSchemaCache:* Indica se o sistema guardará em cache os esquemas obtidos pelas consultas.

Exemplo: <add key="UseDbSchemaCache" value="true" />

*DbSchemaCacheMaxSize:* Define a quantidade de schemas que serão guardados em cache.

Exemplo: <add key="DBSchemaCacheMaxSize" value=“5000"/>

***Registros por Versão:***Retorna todas as visões que contém mais de 1000 registros, que é o número máximo de registros padrão.

Quando maior a quantidade determinada para cada cadastro, maior será o tempo de resposta do sistema para a pesquisa realizada. Recomendamos que mantenha a configuração padrão: 1000 registros.

Para maiores detalhes de como realizar está parametrização acesse: <http://tdn.totvs.com/pages/releaseview.action?pageId=102924324>

***Parâmetros do Banco de Dados:***Retorna um conjunto de parâmetros do banco de dados para auxiliar na análise.

Ao fim da execução o sistema exibirá de forma detalhada as informações pertinentes ao Version e Resources:Principais itens do Version:

* SQLServer\_Star\_time
* CPU\_COUNT
* PHYSICAL\_MEMORY
* PRODUCTVERSION
* COLLATION/CHARACTER SET

Principais itens do Resources:

* LOGIN\_TIME
* HOST\_NAME
* PROGRAM\_NAME
* CPU\_TIME
* MEMORY\_USAGE
* READS/WRITES
* LOCK\_TIMEOUT

***Parâmetros Globais de Performance:*** Verifica se os parâmetros globais de performance estão configurados adequadamente. Lista alguns parâmetros que podem ser desabilitados para melhorar a performance. Segue abaixo itens correspondentes:

* *Temas da MDI*
* *Customização da MDI*
* *Central de Recursos*
* *Verificação da agenda*
* *Verificação de RSS*
* *Painel de Pesquisa no Fluig*
* *Painel da Central de Recursos*
* *Painel de Tarefas*
* *Painel de Pesquisa no GED*
* *Log de execução de actions*

***Desabilitar estatísticas automáticas:*** Verifica se as estatísticas automáticas estão habilitadas para o banco de dados RM.

A opção recomendada é que elas fiquem desabilitadas e que seja rodada de forma recorrente em períodos que os usuários não estão logados nas aplicações.

Configurada como True, as estatísticas de índice são automaticamente criadas, sempre que você criar um índice, o SQL Server cria um conjunto de estatísticas sobre os dados contidos dentro do índice. O otimizador de consulta utiliza essas estatísticas para determinar se ele deve ou não utilizar o índice para ajudar a processar a consulta. Esta opção deve estar desmarcada para não gerar estatísticas em todas as tabelas, nosso banco já tem os índices devidamente criados, por isso, agende uma rotina para executar a procedure RMATUALIZAESTATISTICAS que só atualiza das tabelas do RM. Ex: Quando o sistema executa um comando e que tenha uma cláusula WHERE e o Create Statistics está habilitado, o otimizador de consultas cria estatísticas até mesmo para colunas que não têm índices, mas que aparecem na cláusula WHERE.

***Top 50 CPU:***Lista as querys com maior consumo de CPU ao serem executadas. Através dos resultados apresentados é orientado que o DBA ou responsável pelo Banco de Dados, avalie as consultas SQL em questão.

***Tabelas Grandes:***Lista as maiores tabelas por data (tamanho da tabela), índices (volume de dados dos índices), registros (volume de registros).

Possibilita verificar as tabelas com maior consumo em KB de Dados e Indices, exibindo a quantidade de registros correspondentes.

***Observação:***Atente-se as tabelas correspondentes ao Log de Auditoria e gestão de processos, estas tabelas devem ser limpadas periodicamente.

Instruções para limpeza nos seguintes links:

<http://tdn.totvs.com/pages/viewpage.action?pageId=42043666> (Item 5)

***Checa Collation (DB):***Valida a Collation do Banco. A utilização de um Collation incorreto possibilitará o acesso ao sistema, porém não é possível prever se o sistema apresentará uma não-conformidade durante a sua utilização. A alteração do Collation do Data Base pode ser realizada pela DBA ou responsável pelo Banco de Dados na empresa, caso deseje, podemos realizar tal alteração pelo processo de consultoria (processo tarifado).

Collation determinado pela TOTVS Linha RM pode ser verificado pela portabilidade: <http://tdn.totvs.com/pages/releaseview.action?pageId=60522502>

***Checa Linguagem (DB):***Verifica se a linguagem dos seguintes logins CorporeRM, está parametrizada com o Language ENGLISH:

RM;

SYSDBA.

Caso contrário, o Sentinela irá ajustar automaticamente durante a execução da validação.

***Checa modo de transação****:* Valida se o módulo de transação é o recomendado, que no caso é o ReadCommited.

As transações realizadas no banco de dados possuem um nível de isolamento, que determina o grau em que a transação será isolada das demais transações. Os níveis de isolamento controlam, por exemplo, se serão feitos bloqueios quando os dados são lidos, que tipo de bloqueio é necessário, e por quanto tempo estes bloqueios serão mantidos.

Para melhor aproveitamento do sistema RM, recomendamos a utilização do nível de isolamento READ COMMITTED (default), usando controle de versões de linha, ou seja, com o parâmetro da base de dados READ\_COMMITTED\_SNAPSHOT ativado.

Recomendações pertinentes ao nível de isolamente, disponibilizadas no seguinte link:  <http://tdn.totvs.com/pages/releaseview.action?pageId=61933554>

***Lista todas as triggers da base de dados:***Lista todas as Triggers Habilitadas e Desabilitadas da Base de Dados, informando a data de criação e data de modificação correspondentes.

***Observações:***

* Através das Tarefas de Execução Agendada é possível habilitar e desabilitar as Triggers atuais.
* Caso necessário acesse o seguinte link para mais informações sobre o processo de **desabilitar todas as triggers:** **<http://www.tdn.totvs.com/display/public/rm/Triggers+Habilitadas>**

***Page Life Expectancy:***O indicador Page Life Expectancy (PLE) ajuda a determinar problemas com pressão de memória no SQL Server. O contador mostra quanto tempo médio, em segundos, as páginas de dados estão sendo mantidas no buffer cache. Qualquer valor abaixo de 300 segundos pode indicar que os dados estão sendo removidos do cache com muita frequência e consequentemente provocando a necessidade de leitura em disco, o que por sua vez aumenta o I/O.

***Top 50 índices Fragmentados:***Tabelas mais fragmentadas da base de dados, demonstrando a média de Fragmentação da tabela (Logical Scan Fragmentation) e a quantidade de páginas.

Para correção é recomendada a execução das rotinas de manutenção da Base de Dados: <http://tdn.totvs.com/pages/releaseview.action?pageId=61935061>

***Verificar antivírus:***Verifica se existe algum antivírus instalado pois este pode estar sendo o ofensor de performance da máquina.

Por segurança a maioria dos antivírus realizam as verificações em tempo real nos diretórios TOTVS e banco de dados, prejudicando qualquer execuções e/ou gravação a serem realizadas nos diretórios.

Deste modo é aconselhável tratar os diretórios abaixo como exceção, em todos ambientes que possuem a estrutura instalada:

*Linha RM*

*... :\TOTVS*

*... :\WINDOWS\Microsoft.Net*

*... :\Windows\Assembly*

*Banco de dados*

*ORACLE:*

*..:\ORACLE\app ou ..:\App*

*SQL Server:*

*\* 32bits*

*..:\Program Files (x86)\Microsoft SQL Server*

*..:\Program Files (x86)\Microsoft SQL Server Compact Edition*

*\* 64 bits*

*..:\Program Files\Microsoft SQL Server*

*..:\Program Files\Microsoft SQL Server Compact Edition*

***Validar .Config:***Verifica se as configurações do arquivo .config  na MDI ou Aplicativo estão de acordo com o recomendado e já ajusta o que se pode ajustar.

***Verificar IPV6:***Lista as interfaces de rede que estão configuradas com o IPV6 e recomenda desabilitar. Costuma dar erro ao acessar o fileserverpatch quando usando N Camadas.

Instruções para parametrização deste item, disponíveis no seguinte link: <http://tdn.totvs.com/pages/releaseview.action?pageId=145365112>

***Desabilitar D.E.P.:***Verifica se o Windows Data Execution Prevention está desabilitado no S.O. Ele habilitado ocasiona problema de performance, com overhead no S.O e maior acesso a disco.

Instruções para parametrização deste item, disponíveis no seguinte link: <http://tdn.totvs.com/pages/releaseview.action?pageId=145365112>

***Informações do Sistema:***Retorna um conjunto de informações básicas da máquina.

Os resultados da geração destas funcionalidades podem ser gerados através do Botão Direito, **Salvar Relatório em Arquivo**. Estas informações poderão ser enviadas para a TOTVS para auxiliar na análise do ambiente.

Oracle

***Databse:***

***Verificar .config Server:***Verifica o arquivo .config do serviço de Host.

***Registros por visão:*** Retorna todas as visões que contém número máximo de registros diferente do padrão (1000).

***Parâmetros do banco de dados:*** Retorna um conjunto de parâmetros do banco(Oracle e SQL Server).

***Parâmetros Globais de Performance:*** Verifica se os parâmetros globais de performance estão com a configuração adequada.

***Histórico de Locks nas ultimas 2 horas(2):*** Traz o histórico de Locks ocorridos nas últimas duas horas.

***Jobs Ativos:*** Retorna todos os jobs ativos e sua data de execução.

***Maiores Tabelas:*** Retorna as maiores tabelas do Oracle.

***FK Constraints Sem Índices:*** Retorna todas as contraints do tipo Foreign Key que não possuem índices associados.

***Sessões Inativas:*** Identifica as sessões inativas, retorna o tempo em minutos e o consumo de memória – O filtro é feito com base no tempo de espera em segundos(2400 segundos = 40 minutos).

***Tamanho dos Índices:*** Consulta TAMANHO dos índices conforme estatística do BD (ver data da última análise na coluna 'Last Analyzed') se desejar ver todas as tabelas de todos os schemas não informar valor para o parâmetro OWNER.

***Memória PGA:***Verifica data da última checagem de índices e quantidade de linhas para o mesmo.

***Objetos não compilados:*** Retorna todos os objetos não compilados do oracle.

***Locks nas últimas 2 horas:*** Traz o histórico de locks ocorridos nas ultimas 2 horas.

**Locks nas ultimas semanas:** Traz o histórico de Locks ocorridos nas últimas semanas.

**Todos os cursores abertos:** Retorna todos os cursores abertos.

**Cursores abertos x qtd máxima:** Realiza o comparativo entre os cursores abertos e a qtde máxima permitida.

**Parâmetros do Servidor:** Retorna os parâmetros da instância.

**Pârmetros da sessão:** Retorna os parâmetros da sessão.

**Última checagem de indices:** Consulta estatisticas de consumo de memoria PGA por sessao.

**Memória SGA:** Exibe total de memória, total de memória usada e percentual de memória livre de cada área de memória da SGA, inclusive o total da SGA.

**Tabelas sem PK:** Tabelas sem Primary Key.

**Top 100 Consultas + pesadas:** Retorna as 100 queries que consomem mais CPU.

**Top CPU por sessão:** Retorna queries se maior consumo de CPU por sessão.

**Top CPU por sessão:** Retorna queries se maior consumo de memória por sessão.

**Windows:**

**Informações do sistema:** Retorna um conjunto de informações do computador.

**Verificar Antivírus:** Verifica se Existe algum antivírus instalado.

**Validar .config:** Verifica as configurações do arquivo .config na MDI e/ou Aplicativo.

**Verifique IPV6:** Verifica se existe alguma interface com o protocolo IPV6 habilitado Verifica se o Windows Data Execution Prevention está ativo no sistema operacional.

**Desabilitar D.E.P.:** Verifica se o Windows Data Execution Prevention está ativo no sistema operacional.

trueTarefas de Execução Agendada

Neste grupo de ferramentas o usuário pode executar alguns processos agendados de manutenção do banco de dados, análise de suas consultas sql, habilitar ou desabilitar fórmulas visuais, habilitar ou desabilitar triggers, testes de fórmulas .Net e geração do arquivo NGEN.

Tarefas de execução agendada

***Atualização de Estatísticas (BD):***Executa a atualização de estatísticas do Banco. Recomendando fazer 1 vez por dia e pode-se criar um agendamento para isto.

Efetua a manutenção da base de dados, realizando a atualização de estatísticas. Recomendado que também verifique a consistência física e lógica da base de dados. Estes procedimentos são de responsabilidade do DBA da empresa, caso não possua DBA a equipe de consultoria da TOTVS poderá ser acionada para esta avaliação.

Informações pertinentes a manutenção da Base de Dados estão disponíveis no seguinte link:

<http://tdn.totvs.com/pages/releaseview.action?pageId=61935061>

<http://tdn.totvs.com/pages/releaseview.action?pageId=81790043>

***Recriar Views Materializadas de Schema:***Exclusivo do Banco Oracle, recria as views materializadas de schema com o intuito de melhorar a performance do banco no acesso as mesmas.

A criação de VIEWS Materializadas para os catálogos do Oracle é realizada em alguns clientes como alternativa de melhoria de desempenho para as consultas realizadas pelo provider da aplicação.

Para verificar se possui views materializadas na base realize a seguinte consulta:

SELECT mview\_name FROM all\_mviews WHERE OWNER = 'RM';

A existência destes objetos não consistem em um problema e tem o objetivo de melhorar o desempenho, porém as mesmas precisam estar sempre atualizadas semanalmente.

***Limpeza das tabelas de Job:***Apaga todas as tabelas de Log de Execução de Job que já rodaram, menos as pendentes e agendadas (GRelBatch, GJobLog, GJobXLog, GJobXExecucao, GJobX), objetivo da rotina é o ganho de performance **não serão excluídos jobs com recorrência.**.

Deverá ser realizada a limpeza periódica das tabelas GRelBatch, GJobLog, GJobXLog, GJobXExecucao, GJobX, GJobXExecucaoHst, PScheduleMessagesLogPush para melhorar a performance dos processos do sistema.

Essa operação ira excluir TODOS os dados das tabelas de JOB (Os jobs agendados serão excluídos também!). Essa operação não pode ser desfeita e JAMAIS deve ser executada em horário de produção. Existe risco de parada TOTAL do sistema caso essas observações não sejam seguidas.

A partir da versão 12.1.2506 esta tarefa agendada passa a consumir e executar a action Limpar Log de Execução de Processos - GlbActionProcClearJobs.

Instruções para limpeza através da aplicação disponibilizadas no seguinte link:

<http://tdn.totvs.com/pages/viewpage.action?pageId=42043666> (Item 5)

***Desabilitar Fórmulas Visuais e Habilitar Fórmulas Visuais:***Desabilita e habilita as fórmulas visuais, usado para verificar se a Fórmula Visual é ofensora de performance ou causadora do erro. Para habilitar, usar o log gerado na desabilitação para restaurar as mesmas, utilizando o padrão 'CodColigada|IdFormulaVisual|NomeFormulaVisual'.

***Teste de Consultas SQLs:***Valida a execução das Consultas SQLs, verificando se existe consultas com erro de sintaxe. Também pode ser utilizado para demonstrar o tempo de execução de cada Sentença SQL.

Ao clicar duas vezes sobre o código da consulta SQL, o sistema realizará a abertura do editor, possibilitando assim, a edição.

***Recriação de Índices (BD):***Recria os índices do Banco de Dados e resolve os problemas de fragmentação das tabelas. Demorado e deve ser feito fora do horário de expediente.

Efetua a manutenção da base de dados, realizando a reindexação e ou reconstrução de índices. Recomendado que também verifique a consistência física e lógica da base de dados. Estes procedimentos são de responsabilidade do DBA da empresa, caso não possua DBA a equipe de consultoria da TOTVS poderá ser acionada para esta avaliação.

Informações pertinentes a manutenção da Base de Dados estão disponíveis no seguinte link:

<http://tdn.totvs.com/pages/releaseview.action?pageId=61935061>

<http://tdn.totvs.com/pages/releaseview.action?pageId=81790043>

***Desabilitar e Habilitar Triggers (BD):***Habilita e desabilita as triggers, usado para realizar teste se pode ser as triggers ofensoras de performance ou causadora do erro.

Caso necessário acesse o seguinte link para mais informações sobre o processo de **desabilitar todas as triggers:** **<http://www.tdn.totvs.com/display/public/rm/Triggers+Habilitadas>**

***Execução do NGEN:***Usada para gerar as imagens nativas, o que pode ocasionar em ganho de performance.

O Gerador de Imagem Nativa (NGEN) é uma ferramenta que melhora o desempenho de aplicativos gerenciados. O NGEN cria imagens nativas, que são arquivos que contém o código de máquina específico do processamento compilado e as instala no cache de imagem nativa do computador local. O tempo de execução pode usar imagens nativas do cache em vez de usar o compilador JIT (Just-In-Time) para compilar o assembly original.

***Rebuild de Fórmulas Visuais:***Recompila todas as fórmulas visuais cadastradas, atualizando o assembly armazenado em banco de dados.

***Teste de Fórmulas:***Valida a execução das Fórmulas, verificando se existe fórmulas com erro de sintaxe. Também pode ser utilizado para demonstrar o tempo de execução de cada fórmula. Estes processos podem ser feitos de forma agendada uma vez que é um Job que é gerado na base.

Ao clicar duas vezes sobre o código da fórmula, o sistema realizará a abertura do editor, possibilitando assim, a edição.

Ferramentas de Análise

Através desta opção estão disponíveis um conjunto de ferramentas auxiliares para análise de performance da aplicação RM

## 

***Monitor de Banco de Dados:***Executa o Monitor de Banco de Dados, que dispõe de uma série de funcionalidades para monitoramento online da aplicação, com o por exemplo, locks de tabelas, fila de Jobs e fórmulas visuais. No caso de Locks de tabela, informa as SQLs que estão bloqueando e bloqueadas permitindo o “cancelamento” da mesma.

***Snapshot de Bibliotecas:***Realiza o comparativo entre todos os assemblies da biblioteca identificando possíveis diferenças entre o ambiente cliente, servidor de Jobs e servidor de aplicação. Esta comparação pode ser executada nos seguintes modos: Criar Arquivos de Snapshot e Comparativo Automático.

* **Criar Arquivos de Snapshot:**Cria um arquivo com extensão XML do Cliente, AppServer ou JobServer, que poderá ser utilizado posteriormente no Comparador de Snapshot.
* **Comparativo Automático:**Realize a comparação automática entre o Cliente/AppServer, o AppServer/JobServer e Client/JobServer.

***Comparador de Snapshot:***Compara os assemblies da Biblioteca de forma manual, através dos arquivos XML criados no item Snapshot de Bibliotecas. Ao fim da comparação irá indicar os itens divergentes entre os Ambientes A e B.

***Criar XML de Schema (Banco de Dados):*** Gera o schema do banco de dados em um Gabarito XML para poder ser comparado posteriormente.

***Comparador de Schema (Banco de Dados):***Compara o Schema do Banco de Dados - do alias conectado - a um gabarito XML, identificando diferenças estruturais entre ambos. Deve ser utilizado para comparar Base Dados distintas, sendo assim, o gabarito XML é criado através do item Criar XML de Schema (Banco de Dados) das Ferramentas de Análise.  
  
Ao final da comparação irá apresentar os objetos divergentes entre a Base de Dados conectada e a Base de Dados do gabarito XML.  
  
O relatório da comparação mostra diferenças estruturais como **í****ndices**, **c****onstraints**,  **tabelas**, **colunas** e **checkconstraints** entre o Banco e o Arquivo XML.  
  
A comparação utiliza a cor **laranja** para mostrar que um conteúdo está presente no Banco e não está presente no Arquivo XML, a cor **vermelha**quando o conteúdo está presente no Arquivo XML e não está presente no Banco e a cor **branca**quando o conteúdo está presente tanto no Banco quanto no Arquivo XML e destaca as colunas com a cor **vermelha** para marcar as diferenças entre os valores.

***Visualizar SENTINELA Report:***Permite visualizar um relatório com as informações geradas na opção de Checagem Rápida de Ambiente. Poderá ser utilizado pelo time do Suporte para análise do ambiente.

*Obs.: Arquivo com extensão GOOBER*

***Monitor de AppServer:*** Monitora os tempos de respostas do banco e AppServer com base em uma consulta SQL definida pelo usuário.

***PING Monitor:*** Monitora a rede entre 2 hosts através dos protocolos ICMP/IGMP.

***Conversor de Sentenças SQLServer para******Oracle******:*** Este recurso é destinado ao cliente que migra seu banco de dados à partir do SGBD Sql Server para o Oracle. O processo ajusta o cálculo do controle(CRC) da tabela que armazena as consultas sql do produto, este CRC garante a manipulação das informações contidas na linha, sendo geridas pela própria aplicação. Na maioria das migrações do Sql Server para o Oracle tais controles podem ficar errados, se faz necessário executar este processo para ajustar o controle e devolver a funcionalidade do cadastro de consultas.

Além de garantir o valor do controle correto em relação ao banco de dados Oracle, este processo também aplica alguns ajustes nas consultas contidas no cadastro, retirando o hint 'NOLOCK' bem como ajustando o uso de apelidos nas tabelas das consultas.

Esta ferramenta não faz uma migração completa das consultas T-Sql para PL-Sql, sua intenção principal é apresentar ao usuário um diagnóstico dos itens a serem tratados.

Abaixo a tela do processo sendo executado. Após finalizar é gerada a lista das consultas com os erros da interpretação das sentenças pelo SGBD. Como foi dito anteriormente fica a cargo do usuário analisar e aplicar tais ajustes após sua migração entre bancos:

***Enviar Dados de Diagnóstico para Análise Proativa******:*** Este recurso envia a estrutura do Banco de Dados para TOTVS com a finalidade de gerar diagnósticos estruturais com relação ao modelo da base da respectiva versão. Para mais informações acesse <https://tdn.totvs.com/x/GQyhMQ>
