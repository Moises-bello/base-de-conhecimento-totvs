---
content_hash: f277c61a9cc912a78e71b656a47971a69d72a1cd4b6dde6f96ba18f683813376
fetched_at: '2026-06-29T00:08:23.417573+00:00'
page_id: '270085915'
product: rm
source: tdn-rm
title: Configuração do Jobserver na Linha RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270085915
version: 24
---

# Índice

---

.\*ndice:

# Introdução

---

       A execução de processos na linha RM foi modificada estruturalmente para trazer benefícios e possibilidades ao processamento das tarefas e processos. Isso foi possível graças à mudança da arquitetura de Win32 para .Net.

       Conceitualmente, os **Jobs** são os processos na linha RM, e cada um possui informações únicas que vão desde a data da execução do Job, até a estação e o usuário que o executou. O Job é criado no momento da execução de um processo, e é registrado no **Gerenciador de Jobs**, que será detalhado adiante.

       As informações sobre os processos estão mais ricas de informação e detalhamento, além de se tornar mais prático e confiável o gerenciamento das tarefas no sistema.

        Além disso, os Jobs são executados pelo **JobServer**, que é o mecanismo de execução dos processos. O avanço no uso do JobServer vem da possibilidade de utilizar a **Arquitetura 3 Camadas**, onde funcionalidades da linha RM, bancos de dados e estações de trabalho cliente trabalham fisicamente em separado, uma estação diferente para cada camada.

       É possível configurar o RM com seu servidor estando em um local com TimeZone diferente do ambiente Client. O agendamento do JobServer suporta as execuções com servidores globalmente distribuídos, realizando as conversões necessárias para exibir corretamente a data e horário do Job, independente do ambiente em que for consultado. As informações são salvas na base de dados seguindo o TimeZone do próprio ambiente da Base de Dados.

ATENÇÃO

Recomendamos que este recurso seja ativado somente quando você estiver trabalhando na Arquitetura 3 Camadas. Isso porque o serviço realiza constantes consultas ao banco de dados, o que pode trazer perda de desempenho.

        Você pode executar os Jobs de duas formas diferentes: **Execução Assíncrona** e **Agendamento de Processos**. Veja como funcionam:

# 1. Execução Assíncrona de Processos

---

       Os Jobs serão executados de forma assíncrona, ou seja, você poderá realizar outras tarefas enquanto o processo é executado. Todos os Jobs que você definir executar dessa forma, serão processados do servidor de aplicação, o que garante melhor desempenho da execução dos processos.

       Você pode ainda ter a opção de aguardar ou na a execução do processo, bastando clicar no botão “Opções” e desmarcar a opção “Aguardar execução do processo”, durante a execução de um processo (figura 1).

**Figura 1 – Parâmetro “Aguardar execução do processo”**

       Durante a execução do Job, observe que o **Monitor de Jobs**(em destaque na figura 2) é apresentado na parte inferior caso você clique na pasta Progresso da execução dos processos, ao lado das “Mensagens”.

       Você poderá trabalhar em outras tarefas da aplicação RM enquanto ele é executado.

**Figura 2 – Execução Assíncrona do processo pelo Monitor de Jobs**

## 1.1 Agendamento de Processos

---

       Caso você não queira executar o processo imediatamente, ou queira agendar para uma data específica, na linha RM é possível agendar para um mês/dia/horário, e ainda configurar essa execução com uma periodicidade pré-definida.

       Todos os Jobs são passíveis de agendamento, mas esta decisão é tomada durante o desenvolvimento e confecção dos processos. A tela de agendamento é apresentada na penúltima etapa do wizard de processos (figura 3).

## 1.2 Recorrência de Processos

---

       Para realizar execuções recorrentes basta configurar a repetição do Job (figura 3), parametrizando execuções **semanais**, (quais dias da semana serão executados), **mensais** (qual dia do mês) ou mesmo **diariamente** (qual horário do dia).

ATENÇÃOA recorrência e o agendamento de processos estarão disponíveis para uso somente se o *JobServer* estiver configurado para execução em 3 Camadas, no arquivo *RM.Host.Service.exe.config* (confira o tópico “Parametrizações para o uso do JobServer”).

**Figura 3 – Agendamento de Processos**

## 1.3 Monitor de Jobs

---

Importante para acompanhamento de processos, o Monitor de Jobs garante o acompanhamento da execução de algum Job em andamento. Você pode acessá-lo pelo menu Sistema | Server | Monitor de Jobs, ou na nova MDI, menu Ferramentas | Monitor de Jobs.

**Figura 4 – Monitor de Jobs**

## 1.4 Gerenciamento de Jobs

---

       Todos os processos são armazenados no servidor, juntamente com a visualização dos logs de processo. Para obter acesso à tela de Gerenciamento de Jobs acesse Sistema | Server | Gerenciamento de Jobs, ou pela nova MDI, Ambiente | Gerenciamento de Jobs.

       A tela de Gerenciamento de Jobs controla todos os Jobs **em execução**, **executados** e os que **estão por executar**. Por ele você poderá interromper ou parar os Jobs em andamento e reiniciá-los posteriormente, garantindo o gerenciamento dos processos de acordo com sua necessidade.

**Figura 5 – Gerenciamento de Jobs**

       Veja mais sobre .

Observação:

O usuário logado no sistema visualizará Jobs da Coligada Global (0) se ele for supervisor do módulo do contexto ou se possuir algum perfil associado que contenha permissão no item "Gerenciamento de Jobs > Consultar Jobs emitidos de todos os Usuários".

# 2. Recursos do Gerenciador de Jobs

---

O Gerenciador de Jobs possui uma série de recursos que controlam a execução dos jobs. Estes recursos vão garantir a gerência e controle de todos os processos que forem executados. Além disso, você tem ainda detalhes do andamento dos processos, tais como data de criação, execução e finalização, servidor onde foram processados, todos os detalhes sobre a recorrência do job, arquivos de logs de execução e dados técnicos do processo.

       Veja mais sobre .

## 2.1 Funcionalidades do Gerenciamento de Jobs

---

**Interromper Job:**Pausa a execução de um ou mais Jobs selecionados. Para usar essa funcionalidade, é preciso que o job esteja em execução.

**Habilitar Job:** Reinicia a execução de um job interrompido do ponto onde parou. O “Habilitar Job” é diferente da função “Reiniciar Job”, pois este último inicia novamente a execução do processo.

**Desabilitar Job:** Desativa a execução de um job que possua recorrência. Ele não mais será executado, a não ser que seja reiniciado ou habilitado novamente.

**Reiniciar Job:** Reinicia a execução de um job do início, sem exigir que o usuário informe novamente os parâmetros para execução, pois serão utilizados os previamente parametrizados.

**Processo para Limpar Log de Execução de Processos:**Executando este processo você poderá excluir as informações dos Jobs (logs de processo), marcando aquelas que desejar remover.

## 2.2 Resultado da execução dos Processos

---

       Essa pasta exibe o resultado da execução do processo, se o Job foi executado com sucesso ou com erros. Exibe os dados como data e horas da solicitação, início do processamento e termino do processo.

      Para acessá-lo, você pode acessar essas informações pelo botão  presente no Monitor de Jobs depois de concluída a execução (figura 6). Pode ainda acessar pela aplicação, no menu Sistema | Server | Gerenciamento de Jobs, editando o registro do Job, ou também pela nova MDI, menu Ferramentas | Gerenciamento de Jobs e editar o Job desejado (Figura 7). Se o Job não for executado corretamente porque precisava da configuração de algum parâmetro, você pode reiniciá-lo, bastando clicar no botão  , também no Monitor de Jobs.

**Figura 6 – Resultado da Execução do Processo**

**Figura 7 – Informações da Execução do Job**

       Veja abaixo os detalhes das Informações dos Jobs:

**Aba Identificação**

Essa aba fornece informações cadastrais do Job, como Identificação e nome, horário da execução, em qual servidor foi executado e qual o usuário que solicitou sua execução.

**Aba Processo**

Essa aba exibe dados técnicos da execução do Job, tais como Classe do Processo e Classe dos Parâmetros.

**Aba Recorrência**

Exibe as informações do Agendamento do Processo, informando qual a recorrência quando houver.

# 3. Parametrizações para o uso do JobServer

---

Este tópico demonstrará como configurar os parâmetros do JobServer.

ATENÇÃOSomente usuários com conhecimento da arquitetura e capacidade técnica devem alterar as configurações. Qualquer alteração indevida afetará o funcionamento não só dos Jobs como o do próprio aplicativo, tendo conseqüências desastrosas e irreversíveis. Veja mais em: .

## 3.1 Configuração do RM.Host.Service.exe.config

---

       O *RM.Host.Service.exe.config*, que fica no diretório “*C:\CorporeRM\RM.Net*” (este diretório pode ser alterado no ambiente de 3 camadas), é o arquivo de configuração do serviço que executa os processos. É neste arquivo que informamos que ativamos e desativamos a execução do modo 3 camadas do JobServer.

       Veja abaixo o código que controla a execução do JobServer:

xml




]]>

       O parâmetro “JobServer3Camadas” precisa estar com seu value igual a true para ativar o modo 3 Camadas do JobServer. Por *default*, o parâmetro está como false, ou seja, **desativado**.

ATENÇÃO

Caso este parâmetro seja alterado em algum momento, é preciso reiniciar o serviço do RM.Host.Service para que as alterações sejam ativadas.

Além disso, para que utilizar o JobServer, é imprescindível a configuração dos parâmetros do arquivo “*Alias.dat*”, que também se encontra em “*C:\CorporeRM\RM.Net*” (pode ser alterado para o ambiente de 3 camadas) . Veja como configurá-lo no tópico abaixo.

## 3.2 Configuração do Alias.dat

---

       Para que a execução de processos na nova arquitetura funcione corretamente, é necessário que o banco de dados utilizado tenha uma entrada correspondente no arquivo alias.dat. O banco precisa ter um alias configurado no arquivo Alias.dat.

       Para realizar a configuração, acesse o documento .

       Como os servidores irão trabalhar, conforme configuração dos arquivos:

DicaDICA: Como os servidores irão trabalhar, conforme configuração dos arquivos:Situação 1

| Arquivo | Tag | Valor |
| --- | --- | --- |
| CONFIG | JOBSERVER3CAMADAS | TRUE |
| ALIAS | JOBSERVERENABLED | TRUE |
| ALIAS | LOCAL ONLY | TRUE |

Resultado: Dados nas  tabelas  GJOBSERVER e GKNOWNJOBSERVER. Executa somente os Jobs que o próprio servidor gerou (servidor e não client) e ninguém processa os seus jobs

Situação 2

| Arquivo | Tag | Valor |
| --- | --- | --- |
| CONFIG | JOBSERVER3CAMADAS | TRUE |
| ALIAS | JOBSERVERENABLED | TRUE |
| ALIAS | LOCAL ONLY | FALSE |

Resultado: Dados nas tabelas GJOBSERVER e  GKNOWNJOBSERVER. Processa qualquer job.

Situação 3

| Arquivo | Tag | Valor |
| --- | --- | --- |
| CONFIG | JOBSERVER3CAMADAS | TRUE |
| ALIAS | JOBSERVERENABLED | FALSE |
| ALIAS | LOCAL ONLY | FALSE |

Resultado: Não irá dado para a tabela GJOBSERVER (Há menos que ligue no Cockpit) e irá para a tabela GKNOWNJOBSERVER

Situação 4

| Arquivo | Tag | Valor |
| --- | --- | --- |
| CONFIG | JOBSERVER3CAMADAS | FALSE |
| ALIAS | JOBSERVERENABLED | INDEPENDENTE |
| ALIAS | LOCAL ONLY | INDEPENDENTE |

Resultado: Não irá dado para a tabela  GJOBSERVER e nem GKNOWNJOBSERVER. Só estará na tabela GKNOWNJOBSERVER se algum dia o servidor já teve uma das configurações acima.

# 4. Dicionário de Terminologias

---

**Agendamento de Processos:**Execução agendada dos Jobs. É possível agendar para um mês/dia/horário, e ainda configurar essa execução com uma periodicidade pré-definida.

**Alias.dat:**Arquivo de comunicação entre o banco de dados. Neste arquivo você também configura informações sobre a execução do JobServer.

**Execução Assíncrona de Processos:**Os Jobs serão executados de forma assíncrona, ou seja, você poderá realizar outras tarefas enquanto o processo é executado.

**Job:** são os processos da Linha RM.

**JobServer:** é um mecanismo de execução de jobs.

**MDI:** *Multiple Document Interface*, ou a Interface de documentos múltiplos. É o ambiente onde as janelas, abas e processos da Linha RM são abertas.

**RM.Host.Service.exe.config:**Arquivo de comunicação com o servidor que possui os recursos da Linha RM. Este é um dos arquivos onde você configura a execução do JobServer.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Configuração do Jobserver na Linha RM

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
