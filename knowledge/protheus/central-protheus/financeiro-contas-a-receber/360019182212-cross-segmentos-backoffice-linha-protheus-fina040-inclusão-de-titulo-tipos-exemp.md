---
article_id: 360019182212
category: Financeiro - Contas a Receber
content_hash: a268cb6e34d1caa8cc553cd1744cc7a21d2fb0939c12e3e5beb7ab18cff4d84d
fetched_at: '2026-06-28T22:38:12.588264+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA040 - Inclusão de titulo
  tipos exemplos (NF, BOL, AB-)
type: support-article
updated_at: '2026-01-07T20:19:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019182212-Cross-Segmentos-Backoffice-Linha-Protheus-FINA040-Inclus%C3%A3o-de-titulo-tipos-exemplos-NF-BOL-AB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26596145629079)** **Tempo aproximado para leitura:****00:03:00 min**  
  
  
**Duvida**

Como efetuar um execauto de títulos no Contas a Receber - Inclusão?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – Todas as versões

**Solução**

Segue um **exemplo** do processo

#INCLUDE "PROTHEUS.CH"

#INCLUDE "TBICONN.CH"

User Function FIN040INC()

LOCAL aArray := {}

PRIVATE lMsErroAuto := .F.

PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01" MODULO "FIN" TABLES "SE1","SE5","SA1","SA2"

Conout("----Inicio da Rotina Automatica!------")

aArray := { { "E1\_PREFIXO"  , "MAN"             , NIL },;

{ "E1\_NUM"      , "00002024 "       , NIL },;

{ "E1\_TIPO"     , "NF "             , NIL },;

{ "E1\_NATUREZ"  , "004       "          , NIL },;

{ "E1\_CLIENTE"  , "000001"          , NIL },;

{ "E1\_LOJA"     , "01"              , NIL },;

{ "E1\_EMISSAO"  , CtoD("01/01/2024"), NIL },;

{ "E1\_VENCTO"   , CtoD("01/01/2024"), NIL },;

{ "E1\_VENCREA"  , CtoD("01/01/2024"), NIL },;

{ "E1\_VALOR"    , 500               , NIL }}

MsExecAuto( { |x,y| FINA040(x,y)} , aArray, 3)  // 3 - Inclusao, 4 - Alteração, 5 - Exclusão

If lMsErroAuto

MostraErro()

Else

Conout("Título incluído com sucesso!")

Endif

RESET ENVIRONMENT

Return

**Importante**  
O teste deve ser efetuado conforme o exemplo publicado pelo Desenv. no TDN variáveis restritas em fontes customizados não estão previstas pelo suporte padrão, dado ao fato de que as mesmas não estão documentadas, assim sendo, podem ser descontinuadas ou sofrer alterações de comportamento sem aviso

**Saiba mais**  
[Contas a Receber - FINA040 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Contas+a+Receber+-+FINA040+-+Financeiro+-+P12)
