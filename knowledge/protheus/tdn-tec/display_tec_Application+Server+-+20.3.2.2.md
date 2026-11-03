---
content_hash: 2a4da923e7d674fe68be66d579699451c0d1a067e473c0c9507343cb4b78b53d
fetched_at: '2026-07-02T19:24:28.534774+00:00'
page_id: '794381792'
product: protheus
source: tdn-tec
title: Application Server - 20.3.2.2
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.2.2
version: 19
---

Application Server - 20.3.2.2

# Correções

Ocorrência de queda no Application Server ao abrir um arquivo SQLITE usando driver CTREE LOCAL.

Incidente: queda de Application Server ao tentar erroneamente abrir um arquivo SQLITE usando o driver CTREE LOCAL.

Solução: implementada uma verificação inicial de formato de arquivo, para cada abertura de arquivo usando o driver c-Tree Local. Essa verificação deve ser habilitada no arquivo **appserver.ini,** acrescentando na **seção GENERAL** a configuração **CHECKFORMAT=1**

Referente ao chamado: DTAPPSRV-7522

Balanceamento de Portal WS com USING\_COOKIES=0

Incidente: cliente não estava conseguindo utilizar Broker HTTP com aplicativo MeuRH e outros portais Totvs.

Solução: foi criada a chave USE\_REDIRECT\_FOR\_COOKIES no Broker HTTP, que permite a utilização do aplicativo MeuRH em conjunto com outras aplicações web.

Referente ao chamado: DTAPPSRV-7412

Ocorrência de queda em função AdvPL HSMFinalize.

Incidente: quando o dispositivo HSM falhava na inicialização e em seguida era utilizada a função HSMFinalize para finalizar o dispositivo, ocorria um Access Violation na aplicação.

Solução: foi adicionado um método que trata quando a inicialização do dispositivo HSM falha.

Referente ao chamado: DTAPPSRV-7502

O AppServer configurado com REST poderia apresenta congelamento, exigindo que o servidor de aplicação fosse reiniciado

Incidente: TOTVS | Application Server poderia apresentar congelamento dos serviços de REST, após período de utilização, forçando o administrador do ambiente a reiniciar os serviços para que a operação voltasse a normalidade.

Solução: realizamos um ajuste na camada de REST do TOTVS | Application Server para evitar que o congelamento ocorra, mantendo o serviço saudável durante toda operação.

Referente ao chamado: DTAPPSRV-7382

4GL - Comando Free de variável preparada esta deletando o cursor 

Incidente:  ao realizar a limpeza de variável, ela também deleta o cursor incorretamente.

Solução: houve uma correção para a deleção correta da variável preparada, porém, não deletando o cursor.

Referente ao chamado: DTAPPSRV-6009

4GL - Leak de memória na instrução PREPARE 4GL gerando estouro de memória.

Incidente:  acumulo de memória causado por uma falha na deleção de cursores.

Solução: correção aplicada na deleção dos cursores para a correta liberação de memória.

Referente ao chamado: DTAPPSRV-7550

# Melhorias

Balanceamento WebSocket Broker HTTP

Solicitação: Broker HTTP não faz balanceamento quando Smartclient HTML utiliza protocolo websockets.

Solução:  implementado tratamento de protocolo websockets no Broker HTTP.  
  
Referente ao chamado: DTAPPSRV-7528

Implementação de tratamento para o código de erro ERROR\_FILE\_SYSTEM\_LIMITATION no Windows.

Solicitação:  
  
Código de erro 665 retornado pelo Sistema Operacional Windows não era tratado, retornando a informação "unexpected".  
  
Mensagem: |\*\*\* hostToFE() cod [665] called from [] unexpected.  
  
Solução:  
  
O código de erro 665 (ERROR\_FILE\_SYSTEM\_LIMITATION), trata-se de uma limitação no formato NTFS para arquivos altamente fragmentados, ou seja, quando é atingido o tamanho de arquivo 90gb, passa a ocorrer este tipo de erro.  
  
ERROR\_FILE\_SYSTEM\_LIMITATION: The requested operation could not be completed due to a file system limitation.  
  
Documentação de apoio:  
[https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes--500-999-](https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes--500-999- "Follow link")  
  
[https://support.microsoft.com/en-au/topic/a-heavily-fragmented-file-in-an-ntfs-volume-may-not-grow-beyond-a-certain-size-da1c0dfd-a5a1-90b4-4bf7-b65b13ef9d35#:~:text=Also%2C%20decompressing%20and%20compressing%20a,for%20a%20very%20fragmented%20file](https://support.microsoft.com/en-au/topic/a-heavily-fragmented-file-in-an-ntfs-volume-may-not-grow-beyond-a-certain-size-da1c0dfd-a5a1-90b4-4bf7-b65b13ef9d35#:~:text=Also%2C%20decompressing%20and%20compressing%20a,for%20a%20very%20fragmented%20file "Follow link")

Referente ao chamado: DTAPPSRV-7577

Rastreabilidade de Jobs do Totvs Application Server

Incidente: mensagens de finalização de jobs, como JOB THREAD Finishing e/ou JOB Thread Finished impressas no log de console, sem configuração adicional de diagnóstico, e sem informação de inicialização.

Solução: as informações de diagnóstico de jobs, incluindo inicialização e finalização, serão mostradas no log de console do Totvs Application Sever. Também serão exibidas informações de rastreabilidade de jobs disparados dinamicamente através da função AdvPL StartJob(), quando a configuração JobsDebug=1 seja definida na seção ONSTART do arquivo de configuração appserver.ini  
  
Referente ao chamado: DTAPPSRV-7546

# Novas Implementações

Implementar recurso na classe SFTP para definir certificados de login via propriedade.

Solicitação: necessidade de um seletor dos caminhos e senha do certificado de login do SFTP via código.

Solução: implementado propriedades, na classe SFTP, para poder selecionar os certificados e senha via código.

Referente ao chamado: DTAPPSRV-7553

Implementar bloqueio de conexões no Monitor Embedded

Solicitação: não estava sendo possível bloquear novas conexões de Smartclient no Totvs Monitor (Monitor Electron) ou Totvs WebMonitor usado com Monitor Embedded no Broker.

Solução: funcionalidade implementada no Monitor Embedded no Broker.

Monitor Embedded: [https://tdn.totvs.com/display/tec/Uso+do+Protheus+Monitor+na+porta+do+Broker](https://tdn.totvs.com/display/tec/Uso+do+Protheus+Monitor+na+porta+do+Broker "Follow link")  
  
WebMonitor: [https://tdn.totvs.com/display/tec/TOTVS+%7C+WebMonitor](https://tdn.totvs.com/display/tec/TOTVS+%7C+WebMonitor "Follow link")

Referente ao chamado: DTAPPSRV-7163

Classe tMetrics

Solicitação: classe de métricas que possibilite a disponibilização de informações do ambiente, tais como consumo de CPU, memória, latências entre os componentes do ambiente e outras.

Solução: implementação da classe tMetrics.

Documentação:

Referente ao chamado: DTAPPSRV-7152 e DTAPPSRV-7153
