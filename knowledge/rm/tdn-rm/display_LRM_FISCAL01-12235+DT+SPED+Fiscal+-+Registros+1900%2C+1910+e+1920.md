---
content_hash: 8bcbb9e7ee70db7d8c8f070d02d05a59e166b8a40bc7f1705f56f5c4913640e2
fetched_at: '2026-06-29T00:10:37.321997+00:00'
page_id: '539697699'
product: rm
source: tdn-rm
title: FISCAL01-12235 DT SPED Fiscal - Registros 1900, 1910 e 1920
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-12235+DT+SPED+Fiscal+-+Registros+1900%2C+1910+e+1920
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12235 |

## **02. SITUAÇÃO/REQUISITO**

Geração do Registros:

#### **Registro 1900: Indicador de Sub-apuração do ICMS**

Deve ser gerado um Registro para cada Sub-apuração informada nos Períodos de Apuração do ICMS e ICMSST considerando o Período da rotina. Podem existir várias no período. Este registro é “filho” do Registro 0000 (nível 2).

#### **Registro 1910: Período da Sub-apuração do ICMS**

Este registro também deve ser gerado com as informações do Anexo de Sub-Apuração selecionadas para geração do 1900. Também podem conter vários registro no período. Registro “filho” do 1900 (nível 3).

#### **Registro 1920: Sub-apuração do ICMS**

A origem dos dados deste registro são os valores apurados para cada Sub-apuração no momento do encerramento. Este registro deve ser único no período por sub-apuração e deve conter os somatórios dos valores de todas as sub-apurações selecionadas no período. Registro Filho do 1910 (nível 4).

Esses registros só podem ser gerados se a Sub-apuração foi criada com o flag de "Gerar no SPED" marcado.

## **03. SOLUÇÃO**

Registros serão gerados apenas para registros que foram marcados a flag "Gerar no SPED (DSUBAPURACAOPERIODO.GERARSPED)" .

#### **Registro 1900: Indicador de Sub-apuração do ICMS**

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig | Campo RM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "1900" | C | 004 | - | O | Valor fixo |
| 02 | IND\_APUR\_ICMS | Indicador de outra apuração do ICMS: 3 – APURAÇÃO 1; 4 – APURAÇÃO 2; 5 – APURAÇÃO 3; 6 – APURAÇÃO 4; 7 – APURAÇÃO 5; 8 – APURAÇÃO 6. | C | 001\* | - | O | DSUBAPURACAOPERIODO.CODSUBAPURACAO |
| 03 | DESCR\_COMPL\_OUT\_APU R | Descrição complementar de Outra Apuração do ICMS | C | - | - | O | DSUBAPURACAOPERIODO.DESCRICAO |

#### **Registro 1910: Período da Sub-apuração do ICMS**

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig | Campo RM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "1910" | C | 004 | - | O | Valor fixo |
| 02 | DT\_INI | Data inicial da sub-apuração | N | 008\* | - | O | DSUBAPURACAOPERIODO.DTINICIOPER |
| 03 | DT\_FIN | Data final da sub-apuração | N | 008\* | - | O | DSUBAPURACAOPERIODO.DTFIMPER |

#### **Registro 1920: Período da Sub-apuração do ICMS**

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig | Campo RM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "1920" | C | 004 | - | O | Valor fixo |
| 02 | VL\_TOT\_TRANSF\_DEBITOS\_OA | Valor total dos débitos por “Saídas e prestações com débito do imposto” | N | - | 02 | O | DSUBAPURACAOPERIODO.TOTALDEBITOSSAIDA |
| 03 | VL\_TOT\_AJ\_DEBITOS\_OA | Valor total de “Ajustes a débito” | N | - | 02 | O | DSUBAPURACAOPERIODO.TOTALAJUSTESDEBITO |
| 04 | VL\_ESTORNOS\_CRED\_OA | Valor total de Ajustes “Estornos de créditos” | N | - | 02 | O | DSUBAPURACAOPERIODO.TOTALAJUSTESCREDESTORNO |
| 05 | VL\_TOT\_TRANSF\_CREDITOS\_O A | Valor total dos créditos por “Entradas e aquisições com crédito do imposto” | N | - | 02 | O | DSUBAPURACAOPERIODO.TOTALCREDITOSENTRADA |
| 06 | VL\_TOT\_AJ\_CREDITOS\_OA | Valor total de “Ajustes a crédito” | N | - | 02 | O | DSUBAPURACAOPERIODO.TOTALAJUSTESCREDITOS |
| 07 | VL\_ESTORNOS\_DEB\_OA | Valor total de Ajustes “Estornos de Débitos” | N | - | 02 | O | DSUBAPURACAOPERIODO.TOTALAJUSTESDEBESTORNO |
| 08 | VL\_SLD\_CREDOR\_ANT\_OA | Valor total de “Saldo credor do período anterior" | N | - | 02 | O | DSUBAPURACAOPERIODO.SALDOCREDORANTERIOR |
| 09 | VL\_SLD\_APURADO\_OA | Valor do saldo devedor apurado | N | - | 02 | O | Recebe o resultado ABSOLUTO de  DSUBAPURACAOPERIODO.SALDOAPURADO- DSUBAPURACAOPERIODO.TOTALDEDUCOES |
| 10 | VL\_TOT\_DED | Valor total de “Deduções” | N | - | 02 | O | DSUBAPURACAOPERIODO.TOTALDEDUCOES |
| 11 | VL\_ICMS\_RECOLHER\_OA | Valor total de "ICMS a recolher (09-10) | N | - | 02 | O | Valor absoluto do DSUBAPURACAOPERIODO.SALDOAPURADO se ele for **NEGATIVO,** caso **POSITIVO**o campo será gerado como "0". |
| 12 | VL\_SLD\_CREDOR\_TRANSP\_OA | Valor total de “Saldo credor a transportar para o período seguinte” | N | - | 02 | O | DSUBAPURACAOPERIODO.SALDOAPURADO for **POSITIVO** |
| 13 | DEB\_ESP\_OA | Valores recolhidos ou a recolher, extra-apuração. | N | - | 02 | O | DSUBAPURACAOPERIODO.DEBITOSESPECIAIS |
