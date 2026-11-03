---
content_hash: 06534f31cdefd2e31f3bebd9467e6b6bfdcff7b42c658574055714241dba1c95
fetched_at: '2026-06-29T00:08:51.007514+00:00'
page_id: '336398098'
product: rm
source: tdn-rm
title: Gerenciamento de Alias
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerenciamento+de+Alias
version: 6
---

### **CONTEÚDO**

1. #### **Visão Geral**
2. #### **Exemplo de utilização**

#### **01. VISÃO GERAL**

#### O Alias armazena informações sobre a base de dados utilizada na aplicação. Algumas informações de processamento de jobs também são configuradas na tela de Gerenciamento de Alias.

#### **02. EXEMPLO DE UTILIZAÇÃO**

#### É possível acessar a tela de Gerenciamento de Alias:

* #### Ao abrir o RM.exe, clicando nas configurações do Alias;
* #### Pelo menu: Serviços Globais > Segurança > Gerenciamento de Alias;
* #### Pelo aplicativo RM.AliasManager.exe;
* #### Editando diretamente o arquivo Alias.dat, localizado em: C:\CorporeRM\RM.Net.

#### 

## **CONFIGURAÇÕES DE PROCESSAMENTO DE JOBS NO ALIAS**

#### Para que a execução de processos na nova arquitetura funcione corretamente, é necessário que a base de dados utilizada esteja configurada no arquivo alias.dat. O arquivo encontra-se em C:\CorporeRM\RM.Net. Essa configuração também pode ser feita pelo aplicativo RM.AliasManager.exe.

#### Selecionando o Alias que deseja editar, acesse a aba Serviços:

#### 

#### 

As configurações referentes a execução de processos, está no agrupamento Processamento de Jobs. Veja o detalhamento das tags:

**HABILITAR PROCESSAMENTO DE JOB:** Ativa ou desativa a execução de Jobs (true para ativar e false para desativar).

**Exemplo com a tag:** <JobServerEnabled> true </JobServerEnabled>

**EXECUÇÕES SIMULTÂNEAS:** Quantidade de jobs processados em paralelo no servidor.

**Exemplo com a tag:** <JobServerMaxThreads>5</JobServerMaxThreads>

**Importante**: O número definido aqui é o equilíbrio entre o processamento de Jobs do Servidor e a quantidade de requisições de processos solicitados.

**EXECUTAR APENAS JOBS LOCAIS:** Quando habilitado (= true), faz com que que o servidor execute somente requisições internas, locais. Quando desabilitado (= false) executa qualquer requisição independente do remetente.

**Exemplo com a tag:**  <JobServerLocalOnly> false  </JobServerLocalOnly>

**INTERVALO ENTRE VERIFICAÇÕES (POOLING):** Intervalo em segundos que o servidor busca na base de dados quais são os jobs a serem executados e em seguida são distribuídos para o JobRunner.

**Exemplo com a tag**: <JobServerPollingInterval>10</JobServerPollingInterval>

**Importante**: É necessário definir um número adequado ao tempo de requisições ao servidor, para não encher a fila de Jobs a executar.

**HABILITAR POOL DE PROCESSOS:** O objetivo do Pool de Processos é minimizar o tempo de processamento do job.

**Exemplo com a tag:** <JobServerProcessPoolEnabled>true</JobServerProcessPoolEnabled>

         Quando essa tag está habilitada, após iniciar o host serão criadas automaticamente Threads do JobRunner que ficarão prontas para processar jobs. A quantidade máxima de threads criadas é definido na tag <JobServerMaxThreads>.

         Dessa forma, quando o primeiro job precisar ser executado, ele será processado por um jobrunner que está no pool. Em paralelo, o servidor criará uma nova thread para completar o pool, visto que 1 jobrunner está ocupado. Ao finalizar o job, seu jobrunner será finalizado e o pool continuará com a quantidade configurada na tag JobServerMaxThreads.

**Exemplo com a tag:** <JobServerProcessPoolEnabled>false</JobServerProcessPoolEnabled>

         Para desabilitar o Pool, basta alterar o valor da tag para "false". Dessa forma, a thread do JobRunner será criada apenas quando o sistema solicitar o processamento de algum job. Após finalizar o processamento, a thread também será encerrada. Isso acontecerá para todos os jobs.

**OBS**.: 1. Caso o host esteja configurado para executar 3 camadas, <add key="JobServer3Camadas" value="true" /> (rm.host.exe.config), se a tag <JobServerEnabled> estiver como false, mesmo que o Pool de JobServer esteja habilitado, o Pool não será criado. É preciso que o JobServer esteja habilitado também.

1. Se o ambiente for local, <add key="JobServer3Camadas" value="false" /> (rm.host.exe.config), mesmo se a tag <JobServerEnabled> estiver como false, quando o Pool de JobServer habilitado, o Pool será criado.

ATENÇÃO

#### Caso não exista o arquivo “*alias.dat*”, ou não exista um alias para o banco de dados em questão, essa configuração será criada automaticamente assim que qualquer tela de processo for aberta, tornando essa questão transparente para o usuário.

#### Ainda assim, foi criada uma tela para manutenção do arquivo alias.dat, que pode ser acessada através do menu “Cadastros | Segurança | Administrativa | Gerenciamento de Alias”, ou pela nova MDI, “Segurança | Gerenciamento de Alias”.

#### Veja nos arquivos  e , como os servidores irão trabalhar, conforme configuração dos arquivos.

#### **4. DICIONÁRIO DE TERMINOLOGIAS**

#### **Agendamento de Processos:**Execução agendada dos Jobs. É possível agendar para um mês/dia/horário, e ainda configurar essa execução com uma periodicidade pré-definida.

#### **Alias.dat:**Arquivo de comunicação entre o banco de dados. Neste arquivo você também configura informações sobre a execução do JobServer.

#### **Execução Assíncrona de Processos:**Os Jobs serão executados de forma assíncrona, ou seja, você poderá realizar outras tarefas enquanto o processo é executado.

#### **Job:** são os processos da Linha RM.

#### **JobServer:** é um mecanismo de execução de jobs.

#### **MDI:** *Multiple Document Interface*, ou a Interface de documentos múltiplos. É o ambiente onde as janelas, abas e processos da Linha RM são abertas.

#### **RM.Host.Service.exe.config:**Arquivo de comunicação com o servidor que possui os recursos da Linha RM. Este é um dos arquivos onde você configura a execução do JobServer.

false

**Versão:** 11.80.XX, 12.01.XX
