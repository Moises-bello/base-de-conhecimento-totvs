---
article_id: 24378831659031
category: RH - Férias
content_hash: cfd74873d6a46affcebe8220f438a4170a6d993a8f7e8e5ce968bffb0864a46a
fetched_at: '2026-06-28T22:43:58.261025+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Execução do Cálculo de Férias por Rotina Automática
  - GPEM030
type: support-article
updated_at: '2025-09-02T17:18:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24378831659031-RH-Linha-Protheus-GPE-Execu%C3%A7%C3%A3o-do-C%C3%A1lculo-de-F%C3%A9rias-por-Rotina-Autom%C3%A1tica-GPEM030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24378847448599) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Execução do Cálculo de Férias por Rotina Automática - GPEM030  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.

**Solução**

Mesmo a rotina GPEM030 utilizando o padrão MVC, a execução da rotina automática deve ser feita com o **MSExecAuto**.

Segue exemplo de implementação:

`#INCLUDE "TOTVS.CH"`

`#INCLUDE "TBICONN.CH"`

`/*/{Protheus.doc} User Function ExeFerAuto`

`Executa o cálculo de férias utilizando o ExecAuto`

`@type User Function`

`@author Cícero Alves`

`@since 07/12/2020`

`@see https://tdn.totvs.com/x/D3JkIg`

`/*/`

`User Function ExeFerAuto()`

`Local cMat          :=``"000208"`

`Local aCab          := {}`

`Local aLogAuto      := {}`

`Private lMsErroAuto := .F.`

`PREPARE ENVIRONMENT EMPRESA``"T1"` `FILIAL``"M SP 02 "` `MODULO``"GPE"`

`// Alterar nome da função para as validações da rotina`

`SetFunName(``"GPEM030"``)`

`// Reinicializa as variáveis Static das rotinas de cálculo`

`// Necessário quando executado mais de um cálculo em sequência`

`RstExecCalc()`

`LogExecRot()`

`RstGpexIni()`

`// Altera o conteúdo dos campos`

`aAdd(aCab, {``"RH_FILIAL"` `,``"M SP 02 "``, NIL })``// Filial do funcionário`

`aAdd(aCab, {``"RH_MAT"`    `, cMat      , NIL })``// Matrícula do funcionário`

`aAdd(aCab, {``"RH_DFERIAS"``, 20        , NIL })``// Dias de férias`

`aAdd(aCab, {``"RH_DABONPE"``, 10        , NIL })``// Dias de abono pecuniário`

`aAdd(aCab, {``"RH_ABOPEC"``,``"2"`        `, NIL })``// Período do abono "1" = Antes; "2" = Depois`

`aAdd(aCab, {``"RH_DATAINI"``, cTOd(``"15/02/2020"``), NIL })``// Data de início das férias`

`aAdd(aCab, {``"RH_MEDATU"` `,``"S"`       `, NIL })``// Se considera o mês atual para as médias S/N`

`// Executa a rotina`

`MSExecAuto( {|x| GPEM030(x)}, aCab)`

`If !lMsErroAuto`

`ConOut(``"Cálculo de férias efetuado."``)`

`Else`

`If IsBlind()``// Sem Interface`

`aLogAuto := MostraErro(``'Null'``)`

`varinfo(``"aLogAuto"``, aLogAuto)`

`Else`

`MostraErro()`

`EndIf`

`EndIf`

`Return`

**Saiba Mais**[RH - Linha Protheus - GPE - Execução do Cálculo de Férias Coletivas/Programadas por Rotina Automática - GPEM060](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24379246345751-RH-Linha-Protheus-GPE-Execu%C3%A7%C3%A3o-do-C%C3%A1lculo-de-F%C3%A9rias-Coletivas-Programadas-por-Rotina-Autom%C3%A1tica-GPEM060)

[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
