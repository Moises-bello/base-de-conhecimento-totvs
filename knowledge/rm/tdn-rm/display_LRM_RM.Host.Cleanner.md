---
content_hash: d724720f26f6779a16bfbecc61df05b5abff7cfe2c625c0bf43875a3b12df609
fetched_at: '2026-06-29T00:10:51.466883+00:00'
page_id: '567768692'
product: rm
source: tdn-rm
title: RM.Host.Cleanner
type: documentation
url: https://tdn.totvs.com/display/LRM/RM.Host.Cleanner
version: 39
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão do que é e como habilitar o RM.Host.Cleanner.

# Introdução:

---

**O que é o RM.Host.Cleanner?**

        O RM.Host.Cleanner tem a finalidade de limpar arquivos e dados temporários da base de dados, diminuindo a utilização de espaço em disco e melhorando a performance de uma forma geral.

         Ele é completamente parametrizável, incluindo as operações que irá executar e o intervalo de execução das mesmas. O Cleanner é seletivo quanto aos itens a serem removidos e apaga apenas itens que já existam há um determinado tempo, tempo este que é também parametrizável.

# Como instalar:

---

       O RM.Host.Cleanner é um serviço do Windows. Para instalá-lo é necessário criar o arquivo **RM.Host.Cleanner.exe.config** na pasta **RM.net**.

false Como instalarConfiguração:  Arquivo (RM.Host.Cleanner.exe.config) para Oracle:

**Exemplo do arquivo (RM.Host.Cleanner.exe.config) para base Oracle:**

   
  
]]>Observação

A tag  “DBName” está sem valor e a instância foi informada na tag “DBServer”.

A tag "UseDevartDirect=true" habilita a conexão ao banco Oracle para o caso do Servidor não possuir o Client Oracle instalado.

Mais informações:

Arquivo (RM.Host.Cleanner.exe.config )para SQL:

**Exemplo do arquivo (RM.Host.Cleanner.exe.config )para base SQL:**

   

]]>Parâmetros

       Abaixo segue a lista de parâmetros que podem ser adicionados a este arquivo bem como o que realiza cada um: 

false

**(obrigatório): <add key="CleaningInterval" value="30"/>** - Indica o intervalo de tempo em minutos no qual o Cleanner vai executar a limpeza. Esse intervalo indica de quanto em quanto tempo o Cleanner irá verificar se existem itens a serem excluídos e executar a exclusão caso necessário.

**(obrigatório): <add key="PathToClean" value="C:\totvs\CorporeRM"/>** - Indica o caminho das pastas temporárias criadas pelos aplicativos Delphi, e também o caminho dos logs de processo que deverão ser excluídos. Note que o caminho da pasta de processos é por padrão uma pasta raiz – assim todas as subpastas temporárias e de logs serão percorridas pelo aplicativo e poderão ser “limpas”.

Atenção

Toda parte de Deleção de arquivos, sempre respeitará a tag **RemoveFoldersOlderThan.**

Caso a pasta/arquivo tenha sido alterada em um período inferior ao número de dias informados na tag **RemoveFoldersOlderThan** os a**rquivos/pastas** **não serão excluídos.**

**PathToClean** deve ser configurada no Config do RM.Host.Cleaner

**LogPath**deve ser configurada no Config do RM.Host **utilizado** sendo ele **RM.Host.Service.exe** ou **RM.Host.exe**

Path.GetTempPath() - É o caminho das pastas temporárias do Windows do usuário utilizado no Serviço RM.Host utilizado.

O RM.Host.Cleanner não realiza a limpeza da pasta **FileServerPath**.

Os logs do TraceFile gerados no diretório **RM.Net\Processos\Logs\ não serão limpos**.

**<add key="RemoveFoldersOlderThan" value="12"/>** - Indica o tempo em dias que uma das pastas temporárias criadas pelos aplicativos em Delphi ou pelo log de processos deve existir em disco antes que seja removida.

       No caso das pastas, serão deletadas apenas as pastas cuja data também atender ao critério data/hora atual menos o parâmetro "RemoveJobsOlderThan", e APENAS subpastas dos seguintes caminhos:

* ...\Processos\Logs\
* ...\RM.NET\Processos\Logs\

       Apenas subpastas encontradas abaixo desses dois caminhos serão removidas, arquivos permanecerão. Um outro ponto é que se a pasta estiver em uso por qualquer aplicativo do sistema ela não será removida, e isso pode incluir o próprio Windows Explorer ou qualquer outro software residente na memória da máquina como Anti-Virus.

false

**<add key="RemoveJobsOlderThan" value="7"/>** - Indica o tempo em dias que um job (processo) deve existir na base de dados antes que seja excluído.

**<add key="DBServer" value=""/>** - Indica o servidor de banco de dados a que o serviço irá se conectar para limpar os Jobs (processos)

**<add key="DBName" value=""/>** - Indica a base de dados a que o serviço irá se conectar para limpar os Jobs (processos)

**<add key="DBUser" value=""/>** - Indica o usuário para conexão à base de dados onde os Jobs (processos) serão limpos

**<add key="DBPassword" value=""/>** - Senha para acesso à base de dados onde os Jobs (processos) serão limpos. Para efeitos de segurança, o arquivo pode ser protegido contra leitura por um administrador de rede, por exemplo.

**<add key="RemoveSnowdenLogsOlderThan" value="20"/>** - Indica o tempo em dias que os logs críticos do RM devem ser mantidos na base de dados.  
**<add key="RemoveBehaviorSharingLogsOlderThan" value="45"/>** - Indica o tempo em dias que os logs da tabela GTOTVSLINKLOG devem ser mantidos na base de dados. (0 dias = 1 dia)  
**<add key="RemoveBehaviorSharingMessagesOlderThan" value="45"/>** - Indica o tempo em dias que os logs da tabela GTOTVSLINKMESSAGEEXEC devem ser mantidos na base de dados. (0 dias = 1 dia)

**<add key="RemoveMailSendOlderThan" value="60"/>** - Indica o tempo em dias que os emails armazenados na tabela GMAILSEND e os anexos armazenados na tabela GMAILSENDATTACH devem ser mantidos na base de dados. Caso essa configuração não seja informada, os emails serão armazenados indefinidamente 

       Após criar o arquivo .config, basta acessar o diretório: C:\totvs\CorporeRM\RM.Net e executar **COMO ADMINISTRADOR** o arquivo em lotes "**Instalar RM.Host.Cleanner.bat**". Este arquivo .bat já instala a aplicação como um serviço e, logo após a sua execução, já será possível visualizar o mesmo na janela de “Serviços” do Windows (digite “services.msc” na janela “Executar” do Windows).

Atenção

            O usuário que executa o serviço do Host Cleanner deve ser o mesmo que executa o RM.Host.Service, caso contrário ele limpará diretórios distintos.

       O Cleanner deverá existir em cada máquina onde houver necessidade de fazer essa limpeza, e é útil principalmente em servidores de Terminal (Terminal Services).

       Recomendamos que o RM.Host.Cleanner seja instalado somente nos servidores (APP e TS) uma vez que as estações client, não geram grandes volumes de arquivos temporários.

Observação

Após a instalação, o serviço está instalado mas ainda não iniciou.

Para iniciá-lo é necessário reiniciar o sistema (o serviço inicia automaticamente após isso) ou realizar uma inicialização forçada através do “Serviços” do Windows ou via Prompt de Comando (comando “net start RM.Host.Cleanner”).

       Outra forma de ativar o RM.Host.Cleanner é através da instalação da Biblioteca RM, na qual é possível realizar a parametrização.

**Passo a passo para realizar a parametrização:**

false.1° Passo:2° Passo:3° Passo:

 

Principais tabelas:

---

* **CAGLOTE**: Agendamento de integração de lotes
* **GJOBX**: Armazena os Jobs
* **GJOBLOG**: Processos executados
* **GJOBXCHANGELOG:** Log de alterações do processo. (Versão 12.1.24 ou superior)
* **GJOBXLOG**: Armazena o log de execução dos jobs
* **GJOBXEXECUCAO**: Execução de Jobs
* **GJOBXEXECUCAOHST:** Histórico de execução dos jobs(A partir da versão 12.1.31 - Veja em: [Melhorias no funcionamento do Job](https://tdn.totvs.com/display/LRM/Melhorias+no+funcionamento+do+Job))
* **QCUBODATA**: Armazena os dados dos cubos e histórico de execução
* **GRELBATCH**: Armazena os relatórios que foram gerados via job
* **GJOBQUEUE**: Processos na fila para serem executados
* **GCRITICALLOG:** Tabela responsável por armazenar os logs críticos
* **GSNOWDENCACHE:** Tabela de cahce das consultas do Snowden
* **GTOTVSLINKLOG**: Tabela de logs de mensagem BehaviorSharing - Veja em: [Integração RM x Smart Link Behavior Sharing](https://tdn.totvs.com/pages/releaseview.action?pageId=654705126)
* **GTOTVSLINKMESSAGEEXEC**: Tabela das mensagen que foram executadas do BehaviorSharing - Veja em: [Integração RM x Smart Link Behavior Sharing](https://tdn.totvs.com/pages/releaseview.action?pageId=654705126)
* **GMAILSEND**: Tabela contendo os emails enviados através do RM
* **GMAILSENDATTACH:**Tabela contendo os anexos dos emails enviados através do RM

false

* Os registros da última atualização de cada cubo ficam armazenados na tabela ***QCUBODATA***. O RM.Host.Cleanner ***deleta os registros anteriores*** a última atualização dos cubos.
* Para que os valores da ***QCUBODATA** **não sejam apagados*** adicione a tag <add key="IgnoreCuboData" value="true"/> no app.config do RM.Host.Cleanner.
* O usuário de Banco de Dados utilizado na ativação do RM.Host.Cleanner deve possuir grants relacionados a INSERT, UPDATE, DELETE nas tabelas citadas acima.

# Regra para limpeza de arquivos e diretórios:

---

       O RM.Host.Cleanner segue a seguinte regra para limpeza de arquivos e diretórios:

* No diretório temporário do usuário (**C:\Users\UserName\AppData\Local\Temp**) serão removidos:
  1. Todos os arquivos com a extensão \*.tmp e \*.ResourceStrings.

* No diretório definido pela tag **<add key="PathToClean">** (caso não esteja configurado, será considerado o diretório onde se encontra o RM.Host.Cleanner) serão removidos:

  1. Todos os sub-diretórios que comecem com \_RM e terminem com .TMP (\_RM\*.TMP), bem como seus respectivos arquivos.
  2. Todos os sub-diretórios dentro de "PathToClean"\RM.Net\Processos\Logs\, bem como seus respectivos arquivos.
  3. Todos os sub-diretórios dentro de "PathToClean"\Processos\Logs\, bem como seus respectivos arquivos.

Importante:

A limpeza é realizada nos sub-diretórios e seus respectivos arquivos.

Os arquivos "**soltos**" do diretório: **"PathToClean"\Processos\Logs\** não serão limpos.

**Exemplo:**

No diretório C:\TOTVS\CorporeRM\RM.Net\Processos\Logs existem pastas e arquivos:

Quando realizada a execução do RM.Host.Cleanner, perceba que as pastas foram apagadas, mas os arquivos soltos permaneceram no diretório.

* No diretório definido pela tag **<add key="LogPath">** do arquivo **RM.Host.Service.exe.config,** serão removidos:

  + Todos os sub-diretórios, bem como seus respectivos arquivos.

Importante:

* O Host.Cleanner não realiza a limpeza da pasta FileServerPath.
* Os logs do TraceFile gerados no diretório RM.Net\Processos\Logs\ não serão limpos.

# Observações:

---

       Segue o critério do serviço para determinar o que deve ou não ser removido da base:

* Jobs que **já foram executados** (DATAFIMEXEC não nula), com sucesso ou não, anteriormente à data calculada de acordo com a parametrização RemoveJobsOlderThan serão apagados. Ou seja, todos os jobs executados com status diferente de 0 ou 1, serão apagados.
* Jobs com status 3 ou 7 serão deletados independente de terem iniciado a execução. Obs: A partir das versões 12.1.33.266, 12.1.34.166, 12.1.2205.108 apenas os jobs que tenham a data de última alteração anterior à data calculada de acordo com a parametrização RemoveJobsOlderThan serão apagados.

* Jobs recorrentes terão somente as suas execuções já finalizadas e de acordo com os critérios acima apagadas. O registro do Job (GJOBX) será mantido para as futuras execuções recorrentes.

       Abaixo segue uma lista com todos os status possíveis dos jobs e seus significados:

* **None = 0 -** O Job ainda não foi executado
* **Running = 1 -** O Job está em execução
* **Finished = 2 -** O Job terminou normalmente a sua execução
* **Canceled = 3 -** A execução do Job foi cancelada
* **Stopped = 4 -** A execução do Job começou e foi interrompida
* **Error = 5 -** Erro na execução do job
* **Warning = 6 -** O Job foi executado com avisos
* **Failed = 7 -** Houve uma falha no servidor durante a execução do Job e a mesma não terminou corretamente.
* **Disabled = 8 -** A execução do job está suspensa até ele ser habilitado novamente. Se ele for habilitado antes da sua hora programada ele roda normalmente, se for depois da sua hora programada e ele tiver recorrência, sua recorrência é recalculada e ele é atualizado para aquela data/hora recalculada; se ele não tiver recorrência, seu status vira Canceled.
* **NoJobServerAvailable = 9 -** No momento da execução do Job, um servidor capaz de processar o Job não estava ativo.

# Recomendação sobre a base da dados:

---

       Por segurança, recomendamos a criação de um usuário de banco específico para o uso do RM.Host.Cleanner.

       Após criar o usuário, será necessário liberar o grant para as tabelas abaixo:

* GJOBX
* GJOBXEXECUCAO
* GJOBXEXECUCAOHST (A partir da versão 12.1.31 - Veja em: )
* GJOBXCHANGELOG
* GJOBXLOG
* GJOBLOG
* GRELBATCH
* GJOBQUEUE
* CAGLOTE
* QCUBODATA
* GUSUARIO
* GSNOWDENCACHE
* GCRITICALLOG
* GTOTVSLINKLOG - Veja em: [Integração RM x Smart Link Behavior Sharing](https://tdn.totvs.com/pages/releaseview.action?pageId=654705126)
* GTOTVSLINKMESSAGEEXEC - Veja em: [Integração RM x Smart Link Behavior Sharing](https://tdn.totvs.com/pages/releaseview.action?pageId=654705126)
* GMAILSEND
* GMAILSENDATTACH

# Como desinstalar:

---

       Para desinstalar o serviço basta rodar o arquivo em lotes **"Desinstalar RM.Host.Cleanner.bat"**, disponível no diretório: **C:\totvs\CorporeRM\RM.Net**

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.1.XX

false

**Processo:** Configuração do RM.Host.Cleanner

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
