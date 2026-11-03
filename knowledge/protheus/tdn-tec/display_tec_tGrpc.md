---
content_hash: 3d894667ae2a38d00fa9d928cb8029a14cbc6537422ad809211df08bb310d4ca
fetched_at: '2026-07-02T19:24:27.592513+00:00'
page_id: '657201497'
product: protheus
source: tdn-tec
title: tGrpc
type: documentation
url: https://tdn.totvs.com/display/tec/tGrpc
version: 6
---

A classe tGrpc realiza a comunicação GRPC do Application Server e um servidor GRPC através de um conjunto de chamadas de mensagens preestabelecidos.

trueObservações



+ A classe suporta atualmente um conjunto de mensagens preestabelecidas, sendo possivel utilizar para comunicação com outros produtos atraves do protocolo GPRC, desde que utilizem as mesmas mensagens suportadas.

## Exemplos

cppEclipsetruefalse

## Abrangência

20.3.1.0 em diante

|  |  |
| --- | --- |
| **Propriedades** | |
| caractere | **ClientInfoProp**  |  |  | | --- | --- | |  | Setar o conteudo da propriedade client para envio da mensagem | |
| caractere | **MsgId**  |  |  | | --- | --- | |  | Indica um ID para a mensagem | |
| caractere | **MsgType**  |  |  | | --- | --- | |  | Indica o tipo da mensagem | |
| caractere | **MsgContent**  |  |  | | --- | --- | |  | Conteudo da mensagem | |
| caractere | **MsgAud**  |  |  | | --- | --- | |  | Conteudo para auditoria | |
| numérico | **MsgDeliveryTag**  |  |  | | --- | --- | |  | Indica uma flag de entrega da mensagem | |
| numérico | **MsgAckDeliveryTag**  |  |  | | --- | --- | |  | Seta a flag de entrega da mensagem no conhecimento de recebimento (metodo AckMessage) | |
| numérico | **MsgAck**  |  |  | | --- | --- | |  | Seta a flag do metodo AckMessage | |
  

|  |  |
| --- | --- |
| **Resumo dos Métodos** | |
| lógico | **[isRunning](#isrunning())**()  |  |  | | --- | --- | |  | Retorna verdadeiro (TRUE) se o gRPC Server esta rodando corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc() | |
| lógico | **[clientSetup](#clientsetup())**()  |  |  | | --- | --- | |  | Retorna verdadeiro (TRUE) se a configuração funcionou no gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc() | |
| lógico | **[tenantSetup](#tenantsetup())**()  |  |  | | --- | --- | |  | Retorna verdadeiro (TRUE) se a configuração funcionou no gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc() | |
| lógico | **[tenantUndo](#tenantundo())**()  |  |  | | --- | --- | |  | Retorna verdadeiro (TRUE) se a configuração funcionou no gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc() | |
| lógico | **[sendMessages](#sendmessages())**()  |  |  | | --- | --- | |  | Retorna verdadeiro (TRUE) se a mensagem foi enviada com sucesso ao gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc() | |
| caractere | **[waitForMessages](#waitformessages())**()  |  |  | | --- | --- | |  | Retorna o conteudo da mensagem (tambem setada em :MsgContent) se a mensagem foi recebida com sucesso ao gRPC Server corretamente. Em caso de erro não altera o conteudo da :MsgContent, e pode ser consultado ErrorCode() e ErrorDesc() | |
| lógico | **[ackMessage](#ackmessage())**()  |  |  | | --- | --- | |  | Retorna o conteudo da mensagem (tambem setada em :MsgContent) se a mensagem foi recebida com sucesso ao gRPC Server corretamente. Em caso de erro não altera o conteudo da :MsgContent, e pode ser consultado ErrorCode() e ErrorDesc() | |
| numérico | **[ErrorCode](#errorcode())**()  |  |  | | --- | --- | |  | Codigo de erro (obs: erros 100 são internos) | |
| caractere | **[ErrorDesc](#errordesc())**()  |  |  | | --- | --- | |  | Descricao do erro | |

  

|  |
| --- |
| **Detalhes dos Métodos** |

**New**

Objeto - **New**()
:   Cria um objeto tGrpc com um servidor pelo protocolo gRPC no modelo do arquivo .proto informado. Atualmente, aceita o modelo Smartlink, predeterminado pela TOTVS.

    **Retorno:**
    :   objeto lRet - retorna o objeto da classe

    **Exemplos:**
    Local oClient := tGrpc():New("smartlink.proto","localhost",5001)

---



**isRunning**

lógico - **isRunning**()
:   Checa se o gRPC Server esta rodando corretamente.

    **Retorno:**
    :   lógico lRet - Retorna verdadeiro (TRUE) se o gRPC Server esta rodando corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc()

    **Exemplos:**
    if ogRPC:isRunning()  
    conout("Server is online")  
    else  
    conout(ogRPC:ErrorDesc())  
    endif

---



**clientSetup**

lógico - **clientSetup**()
:   Configura um client no servidor

    **Retorno:**
    :   lógico lRet - Retorna verdadeiro (TRUE) se a configuração funcionou no gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc()

    **Exemplos:**
    :   [code]  
        ogRPC:ClientInfoProp = '{"dummy.json":{"clientproperties":[{"prop01": false}]}}'  
        if ogRPC:clientSetup()  
        conout(ogRPC:ErrorDesc())  
        endif  
          
        ogRPC:ClientInfoProp = '{"dummy.json":{"clientproperties":[{"prop01": true}]}}'  
        if ogRPC:clientSetup()  
        conout("configuração realizada com sucesso")  
        endif  
        [code]

---



**tenantSetup**

lógico - **tenantSetup**()
:   Configura um um grupo ou entidade de recursos no servidor gRPC

    **Retorno:**
    :   lógico lRet - Retorna verdadeiro (TRUE) se a configuração funcionou no gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc()

    **Exemplos:**
    :   [code]  
        ogRPC:ClientInfoProp := "e4vddea4-baba-4c9a-b772-gh77a5fce789"  
        if ogRPC:tenantSetup()  
        conout(ogRPC:ErrorDesc())  
        endif  
        [code]

---



**tenantUndo**

lógico - **tenantUndo**()
:   Desfaz a configuração um um grupo ou entidade de recursos no servidor gRPC

    **Retorno:**
    :   lógico lRet - Retorna verdadeiro (TRUE) se a configuração funcionou no gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc()

    **Exemplos:**
    :   [code]  
        ogRPC:ClientInfoProp := "e4vddea4-baba-4c9a-b772-gh77a5fce789"  
        if ogRPC:tenantUndo()  
        conout(ogRPC:ErrorDesc())  
        endif  
        [code]

---



**sendMessages**

lógico - **sendMessages**()
:   Envia uma mensagem do client para o servidor

    **Retorno:**
    :   lógico lRet - Retorna verdadeiro (TRUE) se a mensagem foi enviada com sucesso ao gRPC Server corretamente. Em caso de erro retorna FALSE, consultar ErrorCode() e ErrorDesc()

    **Exemplos:**
    :   [code]  
        oGRPC:MsgId := "idval"  
        oGRPC:MsgType := "C"  
        oGRPC:MsgContent := "mensagem enviada do client para o server"  
        oGRPC:MsgAud := "audience"  
        oGRPC:MsgDeliveryTag := 0  
          
          
        if ogRPC:sendMessage()  
        conout("Mensagem enviada com sucesso)  
        else  
        conout(ogRPC:ErrorDesc())  
        endif  
        [code]

---



**waitForMessages**

caractere - **waitForMessages**()
:   Aguarda e recebe uma mensagem do servidor

    **Retorno:**
    :   caractere lRet - Retorna o conteudo da mensagem (tambem setada em :MsgContent) se a mensagem foi recebida com sucesso ao gRPC Server corretamente. Em caso de erro não altera o conteudo da :MsgContent, e pode ser consultado ErrorCode() e ErrorDesc()

    **Exemplos:**
    :   [code]  
        ogRPC:MsgContent := ""  
        conout(ogRPC:waitForMessages())  
        if(ogRPC:MsgContent = "")  
        conout("erro, nao veio informacao do servidor")  
        conout(ogRPC:ErrorDesc())  
        else  
        conout("Mensagem recebida com sucesso)  
        endif  
          
        [code]

---



**ackMessage**

lógico - **ackMessage**()
:   Envia reconhecimento de uma mensagem no cliente

    **Retorno:**
    :   lógico lRet - Retorna o conteudo da mensagem (tambem setada em :MsgContent) se a mensagem foi recebida com sucesso ao gRPC Server corretamente. Em caso de erro não altera o conteudo da :MsgContent, e pode ser consultado ErrorCode() e ErrorDesc()

    **Exemplos:**
    :   [code]  
        ogRPC:MsgContent := ""  
        conout(ogRPC:waitForMessages())  
        if(ogRPC:MsgContent = "")  
        conout("erro, nao veio informacao do servidor")  
        conout(ogRPC:ErrorDesc())  
        else  
        oGRPC:MsgAckDeliveryTag := 1  
        ogRPC:MsgAck := .T.  
        if ogRPC:ackMessage()  
        else  
        conout("setar reconhecimento falhou")  
        conout(ogRPC:ErrorDesc())  
        endif  
        conout("Mensagem recebida com sucesso)  
        endif  
          
        [code]

---



**ErrorCode**

numérico - **ErrorCode**()
:   Retorna o codigo de erro do ultimo comando realizado

    **Retorno:**
    :   numérico lRet - Codigo de erro (obs: erros 100 são internos)

    **Exemplos:**
    :   [code]  
        ogRPC:MsgContent := ""  
        conout(ogRPC:waitForMessages())  
        if(ogRPC:MsgContent = "")  
        conout("erro, nao veio informacao do servidor")  
        conout(ogRPC:ErrorCode())  
        else  
        conout("Mensagem recebida com sucesso)  
        endif  
          
        [code]

---



**ErrorDesc**

caractere - **ErrorDesc**()
:   Retorna a descrição do erro do ultimo comando realizado

    **Retorno:**
    :   caractere lRet - Descricao do erro

    **Exemplos:**
    :   [code]  
        ogRPC:MsgContent := ""  
        conout(ogRPC:waitForMessages())  
        if(ogRPC:MsgContent = "")  
        conout("erro, nao veio informacao do servidor")  
        conout(ogRPC:ErrorDesc())  
        else  
        conout("Mensagem recebida com sucesso)  
        endif  
          
        [code]

  
]]>
