---
content_hash: 2807ec62d2131902f98f73f7c68671c9b5b9fce27d2ffc2139a3468b3aff287b
fetched_at: '2026-07-02T19:24:19.778392+00:00'
page_id: '244422710'
product: protheus
source: tdn-tec
title: TWebChannel:bJsToADVPL
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel%3AbJsToADVPL
version: 7
---

TWebChannel:bJsToADVPL

Indica o bloco de código que será disparado na chamada (via Javascript) da função **twebchannel.jsToAdvpl**. Essa função Javascript poderá ser chamada através da página/componente carregado no componente [TWebEngine](http://tdn.totvs.com/display/tec/TWebEngine).

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| bloco de código | { |self,codeType,codeContent| } | N |

## Observações

* Este Bloco de código ao ser disparado recebe o **self** (O próprio objeto), o **codeType** (código da mensagem) e **codeContent** (conteudo da mensagem)

## Exemplos

cppEclipsetruefalse
