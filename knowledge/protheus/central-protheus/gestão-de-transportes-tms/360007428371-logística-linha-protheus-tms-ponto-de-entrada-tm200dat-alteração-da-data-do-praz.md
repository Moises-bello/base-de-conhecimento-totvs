---
article_id: 360007428371
category: Gestão de Transportes (TMS)
content_hash: 7b5205f12ac96eb6689d6ca920422197270d9d5236d9fd63738b4ee4b60523d9
fetched_at: '2026-06-28T22:45:31.061029+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM200DAT Alteração da Data
  do Prazo de Entrega
type: support-article
updated_at: '2021-08-23T19:05:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007428371-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM200DAT-Altera%C3%A7%C3%A3o-da-Data-do-Prazo-de-Entrega
---

**Dúvida**Como implementar o ponto de entrada **TM200DAT** Alteração da Data do Prazo de Entrega?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM200DAT** para modificar a data do prazo de entrega.  
  
**Programa Fonte:** TMSA200.PRW  
  
**Sintaxe**: Tm200DAT - Alteração da Data do Prazo de Entrega ( [ dDataEnt ] [ cCdrDes ] [ cHoraBase ] [ aTmpEnt ] [ cTipTra ] [ cCodOri ] [ cCliDev ] [ cLojDev ] [ cCdrCal ] ) --> dDataEnt

**Retorno**:  
dDataEnt  
  
Retorno deverá ser do tipo data para que substitua a data que foi calculada pelo modelo atual.  
  
O modelo atual quando se faz um cálculo no sábado, o Sistema está configurado para aceitar apenas dias úteis e o sábado/domingo configurado como feriados, a contagem é feita como se o cálculo fosse de feito na segunda que é o primeiro dia útil.

**Este ponto de entrada fornece**:

* Data de entrega calculada pelo modelo atual **dDataEnt**;
* Região de destino para o cálculo **cCdrDes**;
* Hora atual do Sistema **cHoraBase**;
* Array com as horas a serem calculadas **aTmpEnt**.
* Tipo de transporte.
* Código de região de origem.
* Se possuir cadastro de consignatário, então é passado o cliente devedor informado no cadastro de consignatários. Senão é passado o cliente devedor do cálculo.
* Se possuir cadastro de consignatário, então é passada a loja devedora informada no cadastro de consignatários. Senão é passada a loja do cliente devedor do cálculo.
* Código da Região de Cálculo

Parâmetros:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| dDataEnt | Data | Data de entrega calculada. |  |  |  |
| cCdrDes | Caracter | Região de destino para o cálculo. |  |  |  |
| cHoraBase | Caracter | Hora atual do Sistema. |  |  |  |
| aTmpEnt | Vetor | Array com as horas a serem calculadas. |  |  |  |
| cTipTra | Caracter | Tipo de Transporte. |  |  |  |
| cCodOri | Caracter | Código de região de origem. |  |  |  |
| cCliDev | Caracter | Se possuir cadastro de consignatário, então é passado o cliente devedor informado no cadastro de consignatários. Senão é passado o cliente devedor do cálculo. |  |  |  |
| cLojDev | Caracter | Se possuir cadastro de consignatário, então é passada a loja devedora informada no cadastro de consignatários. Senão é passada a loja do cliente devedor do cálculo. |  |  |  |
