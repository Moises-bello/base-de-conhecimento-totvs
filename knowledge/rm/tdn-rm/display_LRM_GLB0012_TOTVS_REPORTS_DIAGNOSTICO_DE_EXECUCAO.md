---
content_hash: 15d634ea49c1a5598585dc0514022f3a16eca059d55396c45ac275d67e3f5ac0
fetched_at: '2026-06-29T00:06:20.442690+00:00'
page_id: '223151518'
product: rm
source: tdn-rm
title: GLB0012_TOTVS_REPORTS_DIAGNOSTICO_DE_EXECUCAO
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0012_TOTVS_REPORTS_DIAGNOSTICO_DE_EXECUCAO
version: 121
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo dessa página é detalhar a funcionalidade de “**Diagnóstico de execução"** disponibilizada no Totvs Reports.

Esse recurso possibilita a visualização de todas as informações relacionadas à "memória de execução" dos relatórios durante o processo de geração.

Ele pode ser usado para detectar diversos tipos de falhas ocorridas durante o processo de geração (inconsistência nos dados apresentados, gargalos de performance, estouro de memória, etc).

# Geração do arquivo de diagnóstico:

---

       Ao executar o relatório através do processo "**Assistente de geração de relatórios**", basta selecionar a opção "**Gerar diagnóstico de execução**" conforme figuras abaixo.

Após a geração do relatório, será criado um arquivo no diretório de Logs de processos da máquina "Host".

* Até a release 12.1.33: C:\totvs\CorporeRM\RM.Net\Processos\Logs\Report\Diagnostico
* A partir da release 12.1.34: C:\TOTVS\CorporeRM\RM.Net\**Arquivos**\Processos\Logs\Report\Diagnostico

* Em ambientes 3 camadas, com várias máquinas host, o arquivo será gravado na máquina "host" responsável pela execução do Job em questão.
* Em caso de geração de relatórios proveniente de outras telas do RM (anexo de visão, menus específicos de produtos, etc) o arquivo de diagnóstico sempre será gerado;
* A partir da release 12.1.34 será possível definir um diretório específico para o arquivo de diagnóstico ser gerado utilizando a Tag [FileServerPath](https://tdn.totvs.com/x/swslD). 

  Configurando a tag desta forma, <add key="FILESERVERPATH" value="\\BHD050102134\ARQUIVOS" />, o arquivo de diagnóstico passará a ser gerado no seguinte caminho: \\BHD050102134\ARQUIVOS\Processos\Logs\Report\Diagnostico.

# Análise do atributos:

---

       A análise das informações geradas pelo diagnóstico deve ser feita usando a tela de "**Diagnóstico de execução****"**localizada na visão de relatórios, conforme figuras abaixo:

O usuário deverá selecionar o arquivo gerado pelo processo de execução de relatório disponibilizado no caminho de logs de processos.

Todos os dados utilizados pelo "motor" de geração de relatórios são gerados e gravados dinamicamente nesses arquivos de diagnósticos de execução. Portanto, as informações listadas na tela de análise de diagnóstico dependem das características do relatório em questão. Por exemplo, relatórios que possuem fórmulas apresentarão todas as informações necessárias para a execução das fórmulas. Relatórios que possuem storedProcedures apresentarão informações relacionadas as storedProcedures (nome, parâmetros das storedProcedures, etc).Essas informações poderão sofrer alterações com o tempo devido ao processo natural de evolução da ferramenta.

**Segue abaixo o significado de algumas dessas informações:**

a) - **Contexto de execução**: informações diversas utilizadas pela engine de geração de relatórios.

* + - **Diagnóstico de execução**: informações diversas de contatores de performance e contadores de memória;

      * **Preparação de dados**: tempo gasto na desserialização do layout do relatório e preparação das informações de execução;
      * **Carga de dados**: tempo gasto na recuperação dos dados do relatório do banco de dados (utilizado para medir a eficiência das consultas sql);
      * **Ajuste no relatório**: tempo gasto no ajuste dos objetos da Devex para o correto funcionamento do relatório;
      * **Tamanho (MB) da fonte de dados**: volume dos dados recuperados do banco (em MB);
      * **Tamanho (MB) da serialização do relatório**: volume do relatório gerado (em MB);
      * etc;
    - **Informações do relatório**: informações relacionadas ao cadastro do relatório na base de dados (ex: tipo do relatório, provedor de dados do relatório, etc);
    - **Parâmetros do relatório**: parâmetros de entrada de dados do relatório;
    - **Parâmetros do provider**: parâmetros de entrada de dados dos provedores de dados;
    - **Filtros de relatório**: filtros diversos utilizados nas clausulas "where" das sentenças sql;
    - **Filtros de fórmula**: filtros utilizados pelos controles de fórmulas;
    - **Informações globais**:informações gerais utilizadas pelo relatório;

b) **rptReport1 - [Report principal]:** informações relacionadas aos componentes disponibilizados no relatório (bandas, controles, subDetalhes, etc).

* + - **Membro**: informações diversas de atributos de dados:
      * **Relacionamentos Indiretos**: informações de relacionamento entre os membros;
      * **Lista de campos de DB**: Campos de tabelas que estão ligados na tabela da banda em questão. Esses campos são utilizados na sentença "SELECT" que será disparada no banco de dados;
      * **Lista de campos DB fora do membro**: Campos de tabelas que **não** estão ligados na tabela da banda em questão. Esses campos são utilizados na sentença "SELECT" baseada em cláusulas de "left outerJoin";
      * **Clausula da consulta sql**: informações diversas sobre as cláusulas das sentenças sql geradas dinamicamente;
        + **Campos da consulta sql:** colunas recuperadas pela sentença sql;
        + **Cláusula From:** tabelas localizadas na clausula From;
        + **Cláusula Inner:** informações da InnerJoin;
        + **Cláusula Left Outer Join:** informações da cláusula leftOuterJoin;
        + **Cláusula Select:** sentença completa a ser executada no banco;
        + **Cláusula Where:** informações da cláusula Where;
        + **Order By:** Informações de ordenação (order by);
      * **Bandas**: informações diversas das bandas (detalhe e subDetalhe) e informações diversas de controles. Nessa sessão, as particularidades de cada controle e cada banda poderão ser analisadas.

# Análise do erros e avisos:

---

       Informações diversas de avisos e erros encontrados no relatório.

Para localizar a origem do erro, basta dar um duplo click sobre a mensagem de erro ou aviso listado na janela de mensagens;

divs

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.15

false

**Processo:** Diagnostico de execução

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
