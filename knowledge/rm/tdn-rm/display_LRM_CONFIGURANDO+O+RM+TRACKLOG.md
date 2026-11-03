---
content_hash: 514694b077d4e524cd36f005d02e3dd1ebb7d34cf8923a897030f070717ce50e
fetched_at: '2026-06-29T00:11:23.077682+00:00'
page_id: '706925332'
product: rm
source: tdn-rm
title: CONFIGURANDO O RM TRACKLOG
type: documentation
url: https://tdn.totvs.com/display/LRM/CONFIGURANDO+O+RM+TRACKLOG
version: 46
---

**CONTEÚDO**

# **01. VISÃO GERAL**

---

O **RM TRACKLOG** é o motor de logs do RM responsável por disponibilizar informações sobre o sistema através de arquivos de texto contendo data e hora do evento e mensagens criadas de forma automática.

Portanto, com o **TRACKLOG**, os logs são capazes de mostrar o que, quando e onde aconteceu um evento, além de indicar quem deu início a ele.

## **1.1 O TRACKLOG REGISTRA VÁRIOS NÍVEIS (LEVEL) DE LOG**

| Ordem | Nível (Level) | Identificado no arquivo | Uso |
| --- | --- | --- | --- |
| 0 | `Verbose` | [VRB] | Verbose é o nível mais ruidoso, raramente (ou nunca) habilitado para um aplicativo de produção. |
| 1 | `Debug` | [DBG] | Debug é usado para eventos internos do sistema que não são necessariamente observáveis ​​de fora, mas são úteis para determinar como algo aconteceu. |
| 2 | `Information` | [INF] | Os eventos de informação descrevem coisas que acontecem no sistema que correspondem às suas responsabilidades e funções.  Geralmente estas são as ações observáveis ​​que o sistema pode realizar. |
| 3 | `Warning` | [WRN] | Quando o serviço está degradado, em perigo ou pode estar se comportando fora de seus parâmetros esperados,  os eventos de nível de aviso são usados. |
| 4 | `Error` | [ERR] | Quando a funcionalidade não está disponível ou as expectativas são quebradas, um evento de Erro é usado. |
| 5 | `Fatal` | [FTL] | O nível mais crítico, os eventos fatais exigem atenção imediata. |

## **1.2 INFORMAÇÕES CONTIDAS NO ARQUIVO DE LOG**

O arquivo de log é escrito conforme um template padrão (**outputTemplate**):

[{ProcessId}:{ProcessName}] [{CallerFilePath} - ({CallerLineNumber}) - {CallerMemberName}] [{Module}, {Category}, {Funcionality}] {NewLine}{Exception}"]]>

| Propriedades do templete | Exemplo de dados logado | Descrição |
| --- | --- | --- |
| {SourceContext} | RM.Lib.Monitoring.Tracklog.Test.LogUnitTest | Contexto onde o log se encontra. Geralmente o namespace da classe que está usando o TrackLog. |
| {Timestamp:yyyy-MM-dd HH:mm:ss.fff zzz} | 2022-08-30 17:44:44.870 -03:00 | Data e hora do evento. |
| {Legacy} | [LGC] | Registros do sistema antigo de log são identificado com a tag **[LGC]** |
| [{Level:u3}] | [INF] | Nível (level) do evento. |
| {Tenant} | shared-environment | Identifica o Tenant do evento. Esse item é acoplado à mensagem. |
| {Message:lj} | Information log test | Mensagem do evento. |
| ({EnvironmentName}|{EnvironmentUserName}) | (Production|BH01\carlos.almeida) | Nome do ambiente e do usuário. |
| <{ThreadId}:{ThreadName}> | <13:Host> | ThreadId e ThreadName do evento. |
| [{ProcessId}:{ProcessName}] | [36956:Host.exe] | ProcessId e ProcessName do evento. |
| [{CallerFilePath} - ({CallerLineNumber}) - {CallerMemberName}] | [Lib\RM.Lib.Monitoring.Tracklog.TesteUnitario\LogUnitTest.cs - (114) - Should\_Write\_Info\_Log] | Arquivo de onde foi registrado o evento de log com o número da linha e o método que o chamou. |
| [{Module}, {Category}, {Funcionality}] | [RMLib, SmartClient, Configuracao] | Módulo, categoria e funcionalidade do sistema onde o evento ocorreu. |
| {NewLine}{Exception} | NullReferenceException: Write Error Log Exception ---> System.Exception: Should\_Write\_Error\_Log | `Warning, Error e Fatal é registrado e uma nova linha com a exceção` |

# **02. COMO CONFIGURAR**

---

O **TRACKLOG** é configurado através do arquivo JSON **appsettings.log.json,** o qual deve ficar no diretório raiz do sistema RM. Caso o arquivo não seja encontrado, o sistema assume as configurações padrões. 

O conteúdo do arquivo de configuração é divido em algumas sessões, conforme detalhado a seguir. 

## **2.1 SESSÕES DO ARQUIVO DE CONFIGURAÇÃO**

A a sessão principal do arquivo de configuração é a "Serilog", onde é informado como o sistema deve escrever o arquivo de log e os recursos que serão utilizados: 

* ### **Sessão principal Serilog**

| Sessão Principal | Subsesões | Pode ser alterado? | Descrição |
| --- | --- | --- | --- |
| Serilog |  | | |
|  | Using | Não | Recursos usados pelo Serilog |
| Enrich | Não | Informações usadas para enriquecer os dados do log. |
| MinimumLevel | Sim | Nível mínimo que deve ser registrado. 0-Verbose, 1-Debug, 2 - Information (**DEFAULT**), 3-Warning, 4-Error, 5-Fatal |
| [Filter](https://github.com/serilog/serilog-expressions#an-appsettingsjson-json-configuration-example) | Sim | Usa expressão para filtrar eventos que passam pelo pipeline Serilog - Opções de Name: ByExcluding ou ByIncludingOnly |
| WriteTo | Somente os argumentos na subseção **Args** da **MapToFile** | Define como e onde o log deve ser escrito e salvo. |

Atenção

A subsessão **MinimumLevel** utiliza por padrão Information

Ex:  
"**MinimumLevel**": "**Information**"

Onde apenas log´s de **verbosidade** I**nformation,Warning,Error e Fatal** serão gravados, **Ignorando** as verbosidades **Verbose e Debug.**

* ### **Sessão que configura a escrita no arquivo de log**

**"WriteTo": [  
      {  
        "Name": "Async",  
        "Args": {  
          "configure": [  
            {  
              "Name": "MapToFile",  
              "Args": {**

| Propriedade | Descrição |
| --- | --- |
| enable | A propriedade "enable" tem como objetivo desabilitar o recurso de escrita de log em arquivo. Por padrão, o valor dessa propriedade é definido como "false", indicando que o recurso está desativado.   * Padrão: false |
| path | Caminho onde o arquivo de log vai ser salvo   * Padrão: <Diretório Raiz da aplicação>\\Logs Atenção **O usuário do Sistema Operacional que está executando a aplicação precisa ter permissão de gravação no diretório especificado na propriedade "path".**   Formato:  Os diretórios devem ser separados por duas barras invertidas **\\** ou uma barra normal **/** Exemplo:  "path": "C:**\\**TOTVS**\\**RM**\\**Logs**\\**" [✔️](https://coolsymbol.com/copy/Check_Mark_Emoji_Symbol_%E2%9C%94%EF%B8%8F)  "path": "C:**/**TOTVS**/**RM**/**Logs**/**" [✔️](https://coolsymbol.com/copy/Check_Mark_Emoji_Symbol_%E2%9C%94%EF%B8%8F)  "path": "C:**\**TOTVS**\**RM**\**Logs**\**" ❌ |
| restrictedToMinimumLevel | É usado para definir um nível mínimo de log apenas para aquele ***agrupador** específico*.   * Padrão: **Information** |
| formatProvider | Fornece informações de formatação específicas da cultura ou null.  Padrão: Null |
| outputTemplate | Um modelo de mensagem descrevendo o formato usado para gravar no coletor.    * O padrão é "{SourceContext}{Timestamp:yyyy-MM-dd HH:mm:ss.fff zzz} {Legacy} [{Level:u3}] {Message:lj} ({EnvironmentName}|{EnvironmentUserName}) <{ThreadId}:{ThreadName}>[{ProcessId}:{ProcessName}] [{CallerFilePath} - ({CallerLineNumber}) - {CallerMemberName}] [{Module}, {Category}, {Funcionality}] {NewLine}{Exception}". |
| fileSizeLimitBytes | O tamanho máximo aproximado, em bytes, para o qual um arquivo de log poderá crescer. Para crescimento irrestrito, passe null.    * O padrão é 1073741824 (1 GB). Para evitar escrever eventos parciais, o último evento dentro do limite  será escrito na íntegra mesmo que exceda o limite. |
| buffered | Indica se a liberação para o arquivo de saída pode ser armazenada em buffer ou não.    * O padrão é False. |
| shared | Permitir que o arquivo de log seja compartilhado por vários processos.    * O padrão é False. |
| flushToDiskInterval | Se fornecido, uma limpeza completa do disco será executada periodicamente no intervalo especificado. Deve ser maior ou igual a 0. Formato: **d.hh:mm:ss** **d** : numero de dias. **hh**: numero de horas. **mm**: numero de minuto. **ss**: numero de segundos.  Exemplo:  flushToDiskInterval: "2.00:00:00" A limpeza completa do disco será executada a cada dois dias.   * O padrão é Null. |
| rollingInterval | O intervalo no qual o registro será transferido para um novo arquivo.   | RollingInterval |  | | --- | --- | | Infinite | O arquivo de log nunca rolará; nenhuma informação de período de tempo será anexada ao nome do arquivo de log. | | Year | Role todos os anos. Os nomes dos arquivos terão um ano de quatro dígitos anexado no padrão **yyyy**. | | Month | Role a cada mês do calendário. Os nomes dos arquivos terão **yyyyMM** anexado. | | Day | Role todos os dias. Os nomes dos arquivos terão **yyyyMMdd** anexado. | | Hour | Role a cada hora. Os nomes dos arquivos terão **yyyyMMddHH** anexado. | | Minute | Role a cada minuto. Os nomes dos arquivos terão **yyyyMMddHHmm** anexado. |  * O padrão é Null. |
| rollOnFileSizeLimit | Se True, um novo arquivo será criado quando o limite de tamanho do arquivo for atingido.  Nomes de arquivo  terá um número anexado no formato \_NNN, com o primeiro nome de arquivo sem número.   * O padrão é False. |
| retainedFileCountLimit | O número máximo de arquivos de log que serão retidos, incluindo o arquivo de log atual. Para retenção ilimitada, passe null.    * O padrão é 31. |
| encoding | Codificação de caracteres usada para escrever o arquivo de texto. Opções: UTF8, UTF7, UTF32, Unicode, BigEndianUnicode, ASCII, Default   * O padrão é UTF8 |
| retainedFileTimeLimit | O tempo máximo após o término de um intervalo em que um arquivo de log contínuo será retido. Deve ser maior ou igual a 0. Ignorado se rollingInterval for Infinite. Formato: **d.hh:mm:ss** **d** : numero de dias. **hh**: numero de horas. **mm**: numero de minuto. **ss**: numero de segundos.  Exemplo:  retainedFileTimeLimit: "6.14:32:15" O arquivo será retido depois de 6 dias 14 horas e 32 minutos e 15 segundos. Caso o valor informado esteja em um formato invalido esse parâmetro será ignorado pelo sistema.   * O padrão é Null. |

* ### **Sessão que configura a escrita do log no console**

**"WriteTo": [  
      {  
          "Name": "Console",  
          "Args": {**

| Propriedade | Descrição |
| --- | --- |
| theme | Define um tema para ser usado ao escrever o log no console |
| outputTemplate | Um modelo de mensagem descrevendo o formato usado para gravar no console.  Padrão: {Timestamp:yyyy-MM-dd HH:mm:ss.fff zzz} {Legacy} [{Level:u3}] {Message:lj} {EnvironmentUserName} {EnvironmentName}- <{ThreadId}>{NewLine}{ExceptionDetails} |

* ### **Sessão que configura o envio do log para o sistema de monitoramento Seq**

**"WriteTo": [  
      {  
        "Name": "Seq",  
        "Args": {**

| Propriedade | Descrição |
| --- | --- |
| serverUrl | Define a url do servidor Seq. |

\*O  [Seq](https://docs.datalust.co/docs/an-overview-of-seq) é um servidor de pesquisa e análise em tempo real para dados de log de aplicativos estruturados.

## **2.2 ARQUIVO DE CONFIGURAÇÃO PADRÃO**

falseArquivo Padrão

* Download:

jsRDarktrue{NewLine}{ExceptionDetails}"
}
},
{
"Name": "Async",
"Args": {
"configure": [
{
"Name": "MapToFile",
"Args": {
"enable": false, //Se o log está habilitado
"rollingInterval": "Day", //Criar um novo arquivo a cada dia
"fileSizeLimitBytes": "104857600", // Especifica o tamanho de cada arquivo de log 100 MB
"rollOnFileSizeLimit": true, //Habilita um tamanho limite para o arquivo de log
"retainedFileCountLimit": 30, //Limite máximo de arquivos se ultrapassar esse valor o sistema exclui os mais antigos
"retainedFileTimeLimit": "7.00:00:00", //Exclui arquivos com mais de 7 dias
"outputTemplate": "[{Timestamp:dd-MM-yyyy}]-[{Timestamp:HH:mm:ss.fff}]-[MachineName:{MachineName}]-[ProcessName:{ProcessName}]-[PID:{ProcessId}]-[TID:{ThreadId}]-[{Level:u3}]-[M:{Module}]-[C:{Category}]-[F:{Funcionality}]-[{CallerFilePath}]-[{CallerMemberName}]-[{CallerLineNumber}]-[{Message:lj}]{NewLine}{Exception}" //como o Log será gravado
}
}
]
}
}
]
}
}]]>

## **2.3 ARQUIVO DE CONFIGURAÇÃO EXPURGO DE ARQUIVOS**

falseExemplo excluir arquivos com mais de 7 dias

* Download:

jsRDarktrue

## **2.4 EXEMPLOS DE CONFIGURAÇÕES**

### **2.4.1 Registrar log somente no console**

falseRegistrar log somente no console

* Download:

jsRDarktrue{NewLine}{ExceptionDetails}"
}
}
]
}
}]]>

### **2.4.2 Registrar log somente no Seq**

falseRegistrar log somente no Seq

* Download:

jsRDarktrue

### **2.4.3 Registrar log somente no Arquivo, excluindo arquivos antigos a cada 7 após serem criados**

false Registrar log somente no Arquivo, excluindo arquivos antigos a cada 7 dias após serem criados. 

* Download:

jsRDarktrue[{ProcessId}:{ProcessName}] [{CallerFilePath} - ({CallerLineNumber}) - {CallerMemberName}] [{Module}, {Category}, {Funcionality}] {NewLine}{Exception}"
}
}
]
}
}
]
}
}]]>

### **2.4.4 Registrar logs somente de erro ou superior no Arquivo, excluindo arquivos antigos a cada 7 dias após serem criados.**

falseRegistrar logs somente de erro ou superior no Arquivo, excluindo arquivos antigos a cada 7 dias após serem criados.

* Download:

jsRDarktrue[{ProcessId}:{ProcessName}] [{CallerFilePath} - ({CallerLineNumber}) - {CallerMemberName}] [{Module}, {Category}, {Funcionality}] {NewLine}{Exception}"
}
}
]
}
}
]
}
}]]>

### **2.4.5 Definindo o path para especificar onde os arquivos de logs devem ser salvos.**

falseDefinindo o path para especificar onde os arquivos de logs devem ser salvos

* Download:

jsRDarktrueLembre-se

Para usar o arquivo após o download, renomeie-o para **appsettings.log.json** e o coloque dentro do diretório raiz do sistema RM.
