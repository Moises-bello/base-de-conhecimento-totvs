---
article_id: 36255699700503
category: Financeiro - Carta de Cobrança
content_hash: bdabb007287173eb82c1785a1cc032897a343b0cf7e3fb699f177116b01e3347
fetched_at: '2026-06-28T22:37:28.997279+00:00'
product: protheus
section_id: 35058223754903
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA811 - Configurar
  envio de carta de cobrança via JOB/SCHEDULE
type: support-article
updated_at: '2026-04-02T11:50:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36255699700503-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA811-Configurar-envio-de-carta-de-cobran%C3%A7a-via-JOB-SCHEDULE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36255667589527) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
É possível configurar envio de carta de cobranças via JOB/SCHEDULE?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
A rotina de **envio de carta de cobrança (FINA811)** possui somente chamada via execução automática **(ExecAuto).** Sendo assim não é possível agenda-la via **schedule**.

Para a correta execução automática da rotina **FINA811**, é necessário informar os parâmetros da função conforme abaixo:

**Exemplo de execução automática FINA811:**  
**#INCLUDE "PROTHEUS.CH"**  
**#INCLUDE "TBICONN.CH"**  
  
**User Function ctGetFil() //Utilizado para envio de cartas de cobrança a partir de uma filial centralizadora**  
**Local aFiliais As Array**  
  
**aFiliais := {}**  
  
**If FwIsInCallStack("FINA811")**  
**aFiliais := FWAllFilial(NIL, NIL, cEmpAnt, .F.)**  
**EndIf**  
  
**Return aFiliais**  
  
**User Function EXEC811()**  
  
**Local a811Param As Array**  
**Local cFiltro As Character**  
  
**Private lMsErroAuto := .F.**  
**Private lAutoErrNoFile := .F.**

**RpcSetEnv("01","01","Admin","1","FIN","FINA811",{"SA1"})  // Preparação do ambiente**

**cFiltro := "E1\_TIPO = 'BOL' "**  
  
**a811Param := {}**  
**aSize(a811Param, 17)**  
  
**a811Param[01] := "      " //Código do cliente De (tipo caracter)**  
**a811Param[02] := "  " //Loja do cliente De (tipo caracter)**  
**a811Param[03] := "ZZ" //Código do cliente Até (tipo caracter)**  
**a811Param[04] := "ZZZZZZ" //Loja do cliente Até (tipo caracter)**  
**a811Param[05] := cToD("01/12/2022") //Data de emissão De (tipo data)**  
**a811Param[06] := cToD("01/12/2022") //Data de emissão Até (tipo data)**  
**a811Param[07] := cToD("01/12/2022") //Data de referência (tipo data)**  
**a811Param[08] := 0 //Valor de (tipo numérico)**  
**a811Param[09] := 9999999 //Valor Até (tipo numérico)**  
**a811Param[10] := "1" //(tipo caracter) - IMPORTANTE:  SEMPRE 2 PARA NÃO APRESENTAR TELA DE SELEÇÃO DE FILIAIS**  
**a811Param[11] := "1" //Títulos a vencer (tipo caracter  sendo "1" = Sim ou "2" = Não)**  
**a811Param[12] := "1" //Considera valor (tipo caracter sendo "1" = Total ou  "2" = Saldo)**  
**a811Param[13] := "2" //(tipo caracter) - IMPORTANTE: SEMPRE 2 PARA NÃO APRESENTAR TELA DE SELEÇÃO DE SITUAÇÃO DE COBRANÇA**  
**a811Param[14] := {} //(tipo array) - IMPORTANTE: ENVIAR ARRAY VAZIO**  
**a811Param[15] := "" //(tipo caracter) - IMPORTANTE: SEMPRE VAZIO**  
**a811Param[16] := "CTE001" //Código do layout da carta a ser utilizado (tipo caracter)**  
**a811Param[17] := "1" //Considera clientes bloqueados (A1\_MSBLQL) no filtro. Espera-se conteúdo "1" para considerar clientes bloqueados ou "2" para considerar apenas clientes ativos**  
  
**MSExecAuto({|a,b,c,d| FINA811(a,b,c,d)}, 0, a811Param, NIL, cFiltro)**  
  
**If (lMsErroAuto)**  
**MostraErro()**  
  
**ConOut(Repl("-", 80))**  
**ConOut(PadC("FINA460 automatic routine ended with error", 80))**  
**ConOut(PadC("Ends at: " + Time(), 80))**  
**ConOut(Repl("-", 80))**  
**Else**  
**ConOut(Repl("-", 80))**  
**ConOut(PadC("FINA460 automatic routine successfully ended", 80))**  
**ConOut(PadC("Ends at: " + Time(), 80))**  
**ConOut(Repl("-", 80))**  
**EndIf**

**RpcClearEnv() //****fecha o ambiente que foi preparado pela RpcSetEnv()**  
  
**Return**

**Saiba mais:**

[Carta de Cobrança - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)
