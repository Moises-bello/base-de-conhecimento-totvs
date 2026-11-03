---
content_hash: d7cd54217b26b675087e152bb91536a481ff32756855b71616b888e7f763fcbc
fetched_at: '2026-06-29T00:11:06.182845+00:00'
page_id: '63277402'
product: rm
source: tdn-rm
title: Melhoria de desempenho
type: documentation
url: https://tdn.totvs.com/display/LRM/Melhoria+de+desempenho
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**xx.xx |
| **Processo** | **:** | Desempenho |
| **Subprocesso** | **:** | Melhoria de desempenho |
| **Data da publicação** | **:** | 21/06/2013 |

**Sintoma/Causas**

Após algum tempo de utilização do sistema CorporeRM, as tabelas que armazenam os processos de Jobs acumulam muitos registros gerando um atraso no momento de carregar o Serviço do HOST.

Ou situação que deve se atentar é para a criação dos arquivos de Logs dos processos, que normalmente são armazenados no diretório **c:\totvs\CorporeRM\RM.Net\Processos**.

A quantidade de pastas e arquivos existente do diretório \RM.NET\ (onde se encontram as DLLs do sistema) *podem* interferir diretamente no tempo de carga de nossa aplicação.

Esses dois fatores contribuem para uma queda no desempenho do sistema quanto a execução de novos Jobs ou na inicialização do Serviço do HOST.

**Solução**

#### 1. Alterar Local de Armazenamento dos Logs

a. Abra cada arquivo (RM.Host.Client.exe.config, RM.Host.Service.exe.config e RM.Host.exe.config) em bloco de notas.

Obs.: O procedimento será efetuado uma vez para cada arquivo mencionado.

b. Insira a linha de comando **<add key="LogPath" value="C:\TEMP" />** conforme exemplo abaixo:

<?xml version="1.0" encoding="utf-8" ?>

<configuration>

    <appSettings>

        <add key="Port" value="8050" />

        <add key="ActionsPath" value="C:\CorporeRM\RM.Net;C:\CorporeRM\Corpore.Net\bin" />

**<add key="LogPath" value="C:\TEMP" />**

    </appSettings>

    <system.runtime.remoting>

      <customErrors mode="off"/>

</system.runtime.remoting>

</configuration>

Onde mencionamos C:\temp, será o diretório e local escolhido para gravação dos arquivos de Log, o diretório informado deve ser fora da hierarquia C:\CorporeRM.

c. Crie a pasta com o mesmo nome e endereço indicado nos arquivos, ou seja, no C:\ criar a pasta TEMP**.**

OBS: Importante lembrar, sempre que o sistema for atualizado para uma nova versão da Biblioteca RM, será necessário uma nova configuração desses arquivos.

### 2. Logs de Processos (Jobs Banco de Dados)

Outra opção que pode ser verificada é a Exclusão de dados das tabelas que armazenam os JOBs executados.

GJOBX, GJOBXEXECUCAO e GJOBLOG

Não haverá problemas em efetuar o comando DELETE nas tabelas citadas acima.

Recomendamos que **sempre** antes de efetuar um delete em uma tabela que seja feito um BACKUP da base de dados.

Exemplo:

DELETE GRELBATCH WHERE IDJOBLOG IN (

SELECT IDJOBLOG

FROM GJOBLOG

WHERE DATACRIACAO <'01/01/2010'

)

DELETE GJOBLOG WHERE DATACRIACAO <'01/01/2010'

DELETE GJOBXEXECUCAO WHERE DATAPROGRAMADA < '01/01/2009'

DELETE GJOBX WHERE DATACRIACAO <'01/01/2009'

### 

### 3. Evitar Polling no Banco de Dados

#### 

#### 3.1. Agenda e Compromissos

Para evitar que seja feito verificações constantes no banco de dados com relação a Agendas e compromissos, é necessário definir as TAGS abaixo no arquivo RM.HOST.CLIENT.EXE.CONFIG:

<add key="AppointmentCheckInterval" value="0" />

<add key="AppointmentCheckTimeBefore" value="15" />

<?xml version="1.0" encoding="utf-8" ?>

<configuration>

<appSettings>

<add key="UseExternalHost" value="true" />

<add key="SelfHosted" value="false" />

<add key="Host" value="RM0005131" />

<add key="Port" value="8076" />

<add key="ActionsPath" value="C:\CorporeRM\_1076\RM.Net;C:\CorporeRM\_1076\Corpore.Net\bin" />

<add key="AppointmentCheckInterval" value="0" />

<add key="AppointmentCheckTimeBefore" value="15" />

</appSettings>

<system.runtime.remoting>

<customErrors mode="off"/>

</system.runtime.remoting>

</configuration>

#### 3.2. Serviços (Gráficos, RSS e Jobs)

Eventualmente, o RM.Host.Service.exe ou “Serviço do HOST” realiza verificações na base de dados em busca de processos para serem executados.

Porém esse constante polling na base pode deixar o sistema, em determinadas ocasiões, com o processamento mais lento.

Para desabilitar o processo que o HOST realiza na base de dados, o Supervisor do sistema poderá mudar alguns parâmetros dentro da Visão de Gerenciamento de Alias.

Essas opções são gravadas no arquivo Alias.DAT, presente na pasta rm.net de cada estação de trabalho que tenha a Biblioteca RM instalada.

Figura 1 - Gerenciamento de Alias

Caso não seja utilizado na empresa RSS ou Gráfico, deixar desabilitado as opções conforme imagem acima.

Para maiores informações:

 

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
