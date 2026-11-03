---
content_hash: 6f7dfe613759db83881def4f281f2eedbf88796fda44a2239bb47b35a5a70334
fetched_at: '2026-06-29T00:05:54.867730+00:00'
page_id: '110430434'
product: rm
source: tdn-rm
title: Fila de processos parada / não processando?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=110430434
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Iniciar o servidor de JobServer |
| **Subprocesso** | **:** | Configuração correta dos Servidores de JobServer e Verificações do servidor de Jobserver |
| **Data da publicação** | **:** | 17/01/2014 |

   Procedimentos resolver situações, onde o Servidor de Jobserver encontra-se parado ou desabilitado.

Procedimentos:

1.  Executar antes de qualquer coisa, o acerta usuário, disponibilizado junto com o instalador de banco de dados ou já extraído para a pastaC:\totvs\CorporeRM\BaseDados\SQL;

   Exemplo do arquivo: Usuarios SQL 2008.sql

2.  Verifique se a data/hora/minuto das máquinas que estão envolvidas no processo está igual. Sendo as  maquinas Servidor de Banco, Servidor de Terminal Service, Servidor de Processos e Estações clientes.

 3. Feita estas duas avaliações acesse o diretório da máquina que está sendo utilizada como servidora de processos e vá ao diretório “C:\totvs\CorporeRM\RM.Net”. Dentro da pasta informada você deverá encontrar o arquivo “Alias.dat” e apagar o mesmo. Em seguida execute o arquivo “RM.AliasManager.exe”. Preencha os campos conforme a conexão exige.

Na aba “Serviços” deixe marcada a opção “Habilitar Processamento de Job”, atribua um valor para Execuções Simultâneas” e deixe desmarcada a opção “Executar apenas Job’s Locais”. Teste a conexão e caso tenha êxito salve as alterações.

4)  Acesse o sistema novamente;

Via nova mdi (RM.EXE)acessar o menu dos SERVIÇOS GLOBAIS > AMBIENTE> COCKPIT. Na tela clique no botão **“Iniciar**” . O ícone **“Interromper Servidor”**  ficará habilitado. Em seguida tente executar o processo do sistema novamente.

Observação:

Conferir todos os arquivos configs do seu sistema sendo.

A)     Maquina local:

Arquivos de configurações dos aplicativos:

Exemplo:

* Nova MDI: C:\totvs\CorporeRM\RM.Net\ RM.exe.config
* Labore: C:\totvs\CorporeRM\RMLabore\ RMLabore.exe.config
* Etc;

Para ambos as tags deverão ser conferidas:

<appSettings>

  <add key="JobServer3Camadas" **value="true" />**

  <add key="Host" **value="BHD0005438"** />

* Tag Jobserver sempre com o valor true.
* Tag Host: Nome do seu servidor de jobserver.

B)      Maquina Servidora / JOBSERVER

Conferir exclusivamente o arquivo config de host C:\totvs\CorporeRM\RM.Net\**RM.Host.Service.exe.config**

A tag Jobserver, também deverá conter o valor True.

Lembrando que a regra acima, será para todos os arquivos .confg do sistema.

Para maiores informações, acesse o tutorial de instalação para 3 camadas:

<http://tdn.totvs.com/pages/releaseview.action?pageId=65209727>

**DICA: Como os servidores irão trabalhar, conforme configuração dos arquivos sendo:**

1º Situação:

CONFIG - JOBSERVER3CAMADAS = TRUE

ALIAS - JOBSERVERENABLED = TRUE

ALIAS - LOCALONLY = TRUE

Resultado: Dados nas  tabelas  GJOBSERVER e GKNOWNJOBSERVER. Executa somente os Jobs que o próprio servidor gerou (servidor e não client) e ninguém processa os seus jobs.

2º Situação:

CONFIG - JOBSERVER3CAMADAS = TRUE

ALIAS - JOBSERVERENABLED = TRUE

ALIAS - LOCALONLY = FALSE

Resultado: Dados nas tabelas GJOBSERVER e  GKNOWNJOBSERVER. Processa qualquer job.

3º Situação:

CONFIG - JOBSERVER3CAMADAS = TRUE

ALIAS - JOBSERVERENABLED = FALSE

ALIAS - LOCALONLY = FALSE

Não irá dado para a tabela GJOBSERVER (Há menos que ligue no Cockpit) e irá para a tabela GKNOWNJOBSERVER

4º - Situação:

CONFIG - JOBSERVER3CAMADAS = FALSE

ALIAS - JOBSERVERENABLED = Independente

ALIAS - LOCALONLY = Independente

Não irá dado para a tabela  GJOBSERVER e nem GKNOWNJOBSERVER. Só estará na tabela GKNOWNJOBASERVER se algum dia o servidor já teve uma das configurações acima.

Para maiores informações:

 

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
