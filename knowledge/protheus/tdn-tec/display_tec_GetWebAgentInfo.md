---
content_hash: 4442e70b814afdd58a624a253cee4acdffaa94f6dba412df9b3cc5bbc07e41d6
fetched_at: '2026-07-02T19:24:28.872647+00:00'
page_id: '863910850'
product: protheus
source: tdn-tec
title: GetWebAgentInfo
type: documentation
url: https://tdn.totvs.com/display/tec/GetWebAgentInfo
version: 4
---

GetWebAgentInfo

Retorna um array com as definições do agente local WebAgent que o SmartClient WebApp está se comunicando.

## Sintaxe

false

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | array | Array de strings contendo as definições do WebAgent que está se comunicando com o SmartClient WebApp. |

## Observações

Abaixo, observe a estrutura do array retornado:

falsefalse

* **Função exclusiva para o SmartClient Webapp**. Não está disponível no SmartClient Desktop.
* Se esta função for executada **via Job** ou por um **cliente diferente do SmartClient Webapp**, o retorno será um **array vazio**.
* Caso o agente local **WebAgent esteja desabilitado** nas configurações do SmartClient WebApp, o conteúdo de **cada posição do array** de retorno da função **será uma string vazia**.

## Exemplos

cppEclipsetruefalse 0
cInfoWebAgent:= 'Versão: ' + aInfoWebAgent[1]+chr(13)+chr(10)+;
'Porta: ' + aInfoWebAgent[2]
MsgInfo(cInfoWebAgent, "GetWebAgentInfo")
endif
Return
]]>

## Abrangência

Disponível a partir da build 24.3.0.0 do TOTVS Application Server.
