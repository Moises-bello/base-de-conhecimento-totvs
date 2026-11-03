---
content_hash: 2d6da7bbeb7344da64f294db09926c86a7f9306074b32c5886c1931122c708cd
fetched_at: '2026-07-02T19:24:19.640594+00:00'
page_id: '243635987'
product: protheus
source: tdn-tec
title: Correção na chamada de funções ADVPL utilizando tipagem e utilizando a cláusula
  DEFAULT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243635987
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Quando um parâmetro não é passado para um função utilizando tipo de dados ocorria erro na atribuição do valor default. |
| Ocorrência | ``` #include "protheus.ch" User Function xTipCall() ```  ``` Local c1 as character Local n1 as numeric Local d1 as date Local l1 as logical Local a1 as array Local b1 as block Local o1 as object ```  ``` ConOut("INI...") ```   **TipParam(, , .T.)**   ``` ConOut("FIM...") Return ```  ```  Static Function TipParam(cChar as character, nNum as numeric, lLog as logical, nVal as numeric) ```  ```  Default cChar := "" Default nNum := 0 Default lLog := .T. Default nVal := 0 ```  ```  ConOut(cChar) ConOut(nNum) ConOut(lLog) ConOut(nVal) ```  ```  Return ``` |
| ``` Correção ``` | Verificação da passagem de parâmetro e atribuição correta do valor default. |
| Informações adicionais | * Disponível em builds superiores a * Revisão: 8673 * SSIM-1120 |
