---
content_hash: 16878cf1138dea4066ce6f50a5589ecbc14ad3b3de81cf76ca1e0170b0f2110d
fetched_at: '2026-07-02T19:24:22.507662+00:00'
page_id: '270102806'
product: protheus
source: tdn-tec
title: Como reforçar a segurança via RPC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270102806
version: 2
---

## Resumo

Este how to tem como objetivo apresentar e explicar a validação de clientes RPC como ferramenta para reforçar a segurança na execução de chamadas via RPC.

## Sumário

20px

## Validação de Clientes RPC

A validação de clientes RPC é uma medida opcional de segurança implementada para permitir que o servidor de uma chamada RPC verifique se o solicitante pode ou não executar chamadas RPC.

Através da execução de uma função AdvPL, definida pelo usuário e indicada no arquivo de configurações do servidor RPC, é possível criar uma política flexível de permissões de execução de funções via RPC.

A medida de segurança é opcional pois depende da configuração ou não da função de validação. No entanto, uma vez configurada, a validação será executada de maneira obrigatória e a cada chamada de método RPC por parte do cliente, até que o servidor seja reiniciado com validação desabilitada.

## Configuração da Função de Validação

A função de validação de clientes RPC é indicada no arquivo de configuração do servidor RPC na seção *'RPC'*, chave *'OnCall'*.  
Caso configurada, habilita a validação de clientes RPC; **caso não configurada, o cliente RPC é considerado válido por padrão**.

## Localização da Função de Validação

A função definida pelo usuário deverá estar no mesmo ambiente (environment) a ser utilizado para execução das tarefas (funções) RPC no servidor, conforme instância da classe  em uso.

## Assinatura da Função de Validação

A função de validação de clientes RPC deverá ter 3 (três) strings de caracteres como argumentos, definindo o IP do cliente RPC, o nome da máquina do cliente RPC e o ambiente (environment) no servidor RPC onde a função está localizada, e deverá retornar um lógico, indicando o resultado da validação conforme definido no corpo da função.

### Sintaxe

false( < \_cClientIP >, < \_cClientHostName >, < \_cServerEnv > )
]]>

### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| \_cClientIP | caractere | IP do cliente RPC. | X |  |
| \_cClientHostName | caractere | Nome da máquina (host name) do cliente RPC. | X |  |
| \_cServerEnv | caractere | Ambiente (environment) no servidor RPC onde a função está localizada. | X |  |

### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lResult | lógico | Retorna o resultado da validação do cliente RPC, conforme definido no corpo da função criada.  Caso o retorno seja **.T.**, indica que o **cliente está habilitado** a executar funções via RPC;  caso o retorno seja **.F.**, indica que o **cliente não está habilitado** a executar funções via RPC. |

### Observações

Nos exemplos de função de validação e seus testes, é assumido que:

* existe no servidor um ambiente propriamente configurado com nome *'EnvTopPorSQL'*;
* não existe no servidor um ambiente propriamente configurado com nome *'OutroEnv'*;
* a função de validação foi compilada no ambiente *'EnvTopPorSQL'* do servidor;
* a função de validação foi configurada no servidor, seção *'RPC'*, chave *'OnCall'*.

### Exemplo da Função de Validação (Lado do Servidor)

cppEclipsetruefalse"
Local cValidHostName := ""
Local cValidServerEnv := ""
If \_cClientIP == cValidIP ;
.And. \_cClientHostName == cValidHostName ;
.And. \_cServerEnv == cValidServerEnv
// cliente pode executar tarefas via RPC neste servidor
cStatus := "VALID"
lResult := .T.
Else
// cliente não pode executar tarefas via RPC neste servidor
cStatus := "NOT VALID"
lResult := .F.
Endif
ConOut( "[INFO] Client is [" + cStatus ;
+ "] for RPC tasks - client IP [" + \_cClientIP ;
+ "] - client host name [" + \_cClientHostName ;
+ "] - server env [" + \_cServerEnv ;
+ "]." )
Return lResult]]>

### Exemplo de Testes da Função de Validação (Lado do Cliente)

cppEclipsetruefalse" // servidor RPC
cPort := 
oRpcSrv := TRpc():New( cEnv )
If ( oRpcSrv:Connect( cServer, cPort ) )
ConOut( 'BEGIN...' )
For nCount := 1 To nNumExc
If nCount > 0
Sleep( 1000 )
Endif
cTime := oRpcSrv:CallProc('Time')
cResult := Str( nCount ) + " - Time(): [" + cTime + "]"
ConOut( cResult )
Next
ConOut( 'END.' )
oRpcSrv:Disconnect()
Else
UserException('RPC connection attempt failed...')
Endif
Return]]>

## Resultado da Função de Validação

Caso bem sucedida, a função de validação retorna o valor lógico resultante da validação do cliente RPC, definido pelo usuário no corpo da função de validação.

Caso mal sucedida, a função de validação retorna falso (.F.), o cliente RPC é considerado como não-válido e a mensagem de erro ***"Invalid RPC Client..."*** é retornada ao cliente e logada.

## Período de Latência de uma Validação

A validação do cliente RPC é executada a cada chamada de método RPC por parte do cliente, até que o servidor seja reiniciado com validação desabilitada.

No entanto, a execução ou não da função de validação de clientes RPC, quando de uma validação, depende do resultado prévio da função de validação e de quando a validação ocorre em relação ao seu período de latência.

Caso bem sucedida, a função de validação somente será executada novamente após o período de ***300 segundos (5 minutos)***, independente do resultado da validação do cliente RPC.

Durante este período, o resultado da validação do cliente RPC retornado será o mesmo.

Após o período de latência, o resultado da validação expira, e a próxima chamada de método RPC por parte do cliente executará a função de validação novamente e o processo se repete.

Caso mal sucedida, a função de validação será executada novamente quando da chamada de método RPC por parte do cliente.

## Resultado da Validação

O resultado da validação de um cliente RPC é um valor lógico que depende do resultado bem sucedido da função de validação de clientes RPC.

Caso válido, o cliente RPC estará habilidato a executar chamadas RPC durante o período de latência de sua validação.

Caso não-valido, o cliente RPC não estará habilitado a executar chamadas RPC e a função de validação RPC será executada novamente na próxima requisição RPC do cliente após o período de latência.
