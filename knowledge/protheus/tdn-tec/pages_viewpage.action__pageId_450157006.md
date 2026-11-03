---
content_hash: c10f7fe7ee2336712c568512edb796ee80caca3f7608c5b1d7ae82dfe3d49cff
fetched_at: '2026-07-02T19:24:23.465493+00:00'
page_id: '450157006'
product: protheus
source: tdn-tec
title: Seção [RPC], chave onCall - Assinatura da função de validação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450157006
version: 2
---

Assinatura da Função de Validação

A função de validação de clientes RPC deverá ter 3 (três) strings de caracteres como argumentos, definindo o IP do cliente RPC, o nome da máquina do cliente RPC e o ambiente (environment) no servidor RPC onde a função está localizada, e deverá retornar um lógico, indicando o resultado da validação conforme definido no corpo da função.

## Sintaxe

(, , ) -> lResult]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| <cClientIP> | Caractere | Endereço IP do cliente RPC. | X |
| <cClientHostName> | Caractere | Nome da máquina (host name) do cliente RPC. | X |
| <cServerEnv> | Caractere | Ambiente (environment) no servidor RPC onde a função está localizada. | X |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lResult | Lógico | Retorna o resultado da validação do cliente RPC, conforme definido no corpo da função criada. |

## Observações

### Resultado da Função de Validação

Caso bem sucedida, a função de validação retorna o valor lógico resultante da validação do cliente RPC, definido pelo usuário no corpo da função de validação.  
Caso mal sucedida, a função de validação retorna falso (.F.), o cliente RPC é considerado como não-válido e a mensagem de erro Invalid RPC Client... é retornada ao cliente e logada.

## Exemplo

Exemplo da função de validação, nesse caso u\_somefunc, que deve estar compilada no repositório do ambiente que vai atender as solicitações RPC.

"
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
return lResult]]>
