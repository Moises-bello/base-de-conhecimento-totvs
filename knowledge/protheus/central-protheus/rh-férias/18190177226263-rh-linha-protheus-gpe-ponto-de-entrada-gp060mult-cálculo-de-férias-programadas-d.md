---
article_id: 18190177226263
category: RH - Férias
content_hash: bfcbe6b90463f5650dde27cb46075318a069bdccf347202fee95850893fd4d39
fetched_at: '2026-06-28T22:43:59.401322+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP060MULT - Cálculo de férias
  programadas de mais de um período aquisitivo automaticamente
type: support-article
updated_at: '2025-09-02T17:15:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18190177226263-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP060MULT-C%C3%A1lculo-de-f%C3%A9rias-programadas-de-mais-de-um-per%C3%ADodo-aquisitivo-automaticamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18190237242647) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Funcionalidade do ponto de Entrada GP060MULT - Cálculo de férias programadas de mais de um período  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.

**Solução**Solicita-se ponto de entrada para possibilitar o **cálculo de mais de um período de férias programadas automaticamente**. Atualmente, existindo um férias **programadas** em **mais de um período aquisitivo**, apenas o **primeiro** é calculado, tendo que executar a rotina **novamente** para calcular o segundo período.  
  
Criação do ponto de entrada **GP060MULT** que deverá retornar um array contendo as seguintes informações:

| Posição | Conteúdo | Tipo |
| --- | --- | --- |
| 1 | Dias de férias | Numérico |
| 2 | Data Inicio das férias | Data |
| 3 | Data Início do período aquisitivo | Data |
| 4 | Data de pagamento do período de cálculo (RCH\_DTPAGO) | Data |
| 5 | Data do Recibo de férias | Data |
| 6 | Data do Aviso de férias | Data |
| 7 | Se possui abono pecuniário | Lógico |
| 8 | Dias de Abono Pecuniário | Numérico |

No momento da execução do array, a tabela SRH (Cabeçalho de férias) estará posicionada no último registro incluído, sendo possível saber qual foi o último período aquisitivo utilizado, ou programação de férias pelos campos SRH→RH\_DATABAS, SRH→RH\_DATAINI e SRH→RH\_DATAFIM, além dos demais campos da tabela.

**Exemplo de criação do ponto de entrada**

Considerando a tabela de Dias de Direito a seguir:

![](https://tdn.totvs.com/download/attachments/538495164/image2020-2-19_11-53-7.png?version=1&modificationDate=1582131374393&api=v2)

E a seguinte parametrização de cálculo:

![](https://tdn.totvs.com/download/thumbnails/538495164/image2020-2-19_11-54-49.png?version=1&modificationDate=1582131374347&api=v2)

Hoje o sistema calcularia apenas as férias com início em 01/03/2019, para que o segundo período seja calculado o ponto de entrada terá que retorna as informações do segundo período aquisitivo, que poderia ser feito da seguinte forma:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 | `#INCLUDE "PROTHEUS``.``CH"`    `User``Function` `GP060MULT()`  `Local aArea         := GetArea()`  `Local aAreaSRF      := SRF->(GetArea())`  `Local aRet          :=``{}`  `Local dDataBas      := SRH->RH_DATABAS``//Data inicio do período aquisitivo calculado`  `Local dDataIni      := SRH->RH_DATAINI``//Data inicio das férias calculadas`  `Local dDataFim      := SRH->RH_DATAFIM``//Data fim das férias calculadas`  `Local dDataPago     := CtoD("")``//Data de pagamento do período`  `Local dDataRec      := CtoD("")``//Data do recibo de férias`  `Local dDataAvi      := CtoD("")``//Data do aviso de férias`  `Local nDiasFer      :=``0`                        `//Dias de Férias programadas`  `Local nDiasAbo      :=``0`                        `//Dias de Abono programados`    `DbSelectArea("SRF")`  `DbSetOrder(``1``)``//RF_FILIAL, RF_MAT, RF_DATABAS, RF_PD, R_E_C_N_O_, D_E_L_E_T_`    `If` `SRF->(DbSeek(SRA->RA_FILIAL + SRA->RA_MAT + DtoS(dDataBas)))``//Posiciona no período aquisitivo calculado`  `SRF->(DbSkip())``//Vai para o próximo peeríodo aquisitivo`  `If` `SRF->RF_FILIAL + SRF->RF_MAT == SRA->RA_FILIAL + SRA->RA_MAT`  `dDataBas  := SRF->RF_DATABAS`  `dDataIni  := SRF->RF_DATAINI`  `nDiasFer  := SRF->RF_DFEPRO1`  `nDiasAbo  := SRF->RF_DABPRO1`  `dDataFim  := dDataIni + nDiasFer + nDiasAbo`  `dDataAvi  := DataValida(dDataIni -``30``,.F.)`  `dDataPago := StoD(AnoMes(dDataIni)+StrZero(F_ULTDIA(dDataIni),``2``))``//Último dia do mês de inicio das férias`  `dDataRec  := DataValida(DataValida(dDataIni-``1``,.F.)-``1``,.F.)``//Define a data do recibo como 2 dias úteis antes da data de inicio das férias`    `aRet :=``{nDiasFer, dDataIni, dDataBas, dDataPago, dDataRec, dDataAvi, nDiasAbo > 0, nDiasAbo}`  `EndIf`  `EndIf`    `RestArea(aAreaSRF)`  `RestArea(aArea)`    `Return aRet` |

**Importante**

1 - O código acima é um exemplo para demonstrar as possibilidades de uso do ponto de entrada. O conteúdo do ponto de entrada, bem como as regras para utilizá-lo, devem ser desenvolvidas de acordo com a necessidade de cada cliente.

2 - O ponto de entrada deve retornar apenas um período no array, após efetuar o novo cálculo, o ponto de entrada é chamado mais um vez para que, caso necessário, um novo período seja informado. Se o array for retornado sem dados, o cálculo prossegue para o próximo funcionário.

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Pontos de Entrada disponíveis na rotina GPEM060 - Férias Coletivas/Programadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034848114-RH-Linha-Protheus-GPE-Pontos-de-Entrada-dispon%C3%ADveis-para-a-rotina-de-Provis%C3%A3o-de-F%C3%A9rias-e-13o-Sal%C3%A1rio-GPEM070)

[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
