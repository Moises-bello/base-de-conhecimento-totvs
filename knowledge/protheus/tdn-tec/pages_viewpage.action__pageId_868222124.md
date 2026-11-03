---
content_hash: dbbd4d6d5d100b21eb82d6aa59f1b6dc1a774fbcb7f50dbebc7263c3de025a6c
fetched_at: '2026-07-02T19:24:29.405232+00:00'
page_id: '868222124'
product: protheus
source: tdn-tec
title: Versão 01.04.10
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=868222124
version: 3
---

GreenAppserver 20.3.2.2 trueYellowem desenvolvimento

## Correção

* tlpp.REST: #DTTLPP-2932 Correção na camada tlppCore de acesso ao objeto de classe destinado ao atendimento de um endpoint.

---

## Melhoria

* tlpp.REST: #DTTLPP-2590 Adequação do comportamento do para permitir a mudança da mensagem de retorno HTTP.
* tlpp.REST: #DTTLPP-2943 Ajustes na finalização da Thread para limpeza de memória.
* tlpp.REST: #DTTLPP-2931 Criação da função de callback .
* tlpp.GRPC: #DTTLPP-2935 Implementação do suporte ao protocolo GRPC (behavior sharing).
* WebMonitor: Liberação do  para uso no TDS-VSCode.
* tlpp.PROBAT: #DTTLPP-2707 Criado de teste por Banco de Dados. Ex: @Skip( database="MSSQL" ).
* tlpp.PROBAT: #DTTLPP-2927 Criado de teste por função customizada. Ex: @Skip( custom="minha\_funcao" ).
* tlppCore: Suporte a múltiplos ambientes na chave .
* tlppCore: #DTTLPP-2879 Troca de erroblock por  para os produtos: tlpp.REST e PROBAT.
