---
article_id: 360053413193
category: Escrita Fiscal - Impostos - ICMS
content_hash: 85940b9985c1b1d3d1633fe889a61233e2876fe49df6916f600ca56ea534fca9
fetched_at: '2026-06-28T22:39:24.367638+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Campos que são gravados
  os valores do FECP
type: support-article
updated_at: '2021-07-28T16:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053413193-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Campos-que-s%C3%A3o-gravados-os-valores-do-FECP
---

**Dúvida**Em quais campos serão gravados os valores do FECP?  
   
 **Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80]  
  
**Solução**

Assim como na aba "Impostos", os valores correspondentes ao FECP de cada modalidade serão gravados separadamente.

As tabelas a seguir demonstram os campos gravados em cada situação:

* **FCP Próprio**

Os campos abaixo serão gravados nas operações em que ocorrer o cálculo do FCP Próprio.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Tabelas | | | | | | |
| **SD1** | **SD2** | **SF1** | **SF2** | **SF3** | **SFT** | **CD2** |
| **Base de Cálculo** | D1\_BASFECP | D2\_BASFECP | F1\_BASFECP | F2\_BASFECP | F3\_BASFECP | FT\_BASFECP | CD2\_BFCP |
| **Alíquota** | D1\_ALQFECP | D2\_ALQFECP | - | - | - | FT\_ALQFECP | CD2\_PFCP |
| **Valor** | D1\_VALFECP | D2\_VALFECP | - | - | F3\_VALFECP | FT\_VALFECP | CD2\_VFCP |

* **FCP ST**

Os campos abaixo serão gravados nas operações em que ocorrer o cálculo do FCP-ST.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Tabelas | | | | | | |
| SD1 | SD2 | SF1 | SF2 | SF3 | SFT | CD2 |
| **Base de Cálculo** | D1\_BSFCPST | D2\_BSFCPST | F1\_BSFCPST | F2\_BSFCPST | F3\_BSFCPST | FT\_BSFCPST | CD2\_BFCP |
| **Alíquota** | D1\_ALFCPST | D2\_ALFCPST | - | - | - | FT\_ALFCPST | CD2\_PFCP |
| **Valor** | D1\_VFECPST | D2\_VFECPST | - | - | F3\_VFECPST | FT\_VFECPST | CD2\_VFCP |

* **FCP Complementar**

Os Campos abaixo serão gravados nas operações em que ocorrer o cálculo do FCP Complementar.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Tabelas | | | | | | |
| SD1 | SD2 | SF1 | SF2 | SF3 | SFT | CD2 |
| **Base de Cálculo** | D1\_BSFCCMP | D2\_BSFCCMP | F1\_BSFCCMP | F2\_BSFCCMP | F3\_BSFCCMP | FT\_BSFCCMP | CD2\_BFCP |
| **Alíquota** | D1\_ALFCCMP | D2\_ALFCCMP | - | - | - | FT\_ALFCCMP | CD2\_PFCP |
| **Valor** | D1\_VFCPDIF | D2\_VFCPDIF | - | - | F3\_VFCPDIF | FT\_VFCPDIF | CD2\_VFCP |

(\*) O valor de FCP gravado nos campos *"\_VFCPDIF"* corresponde ao FCP devido ao estado de destino nas operações com não contribuintes (DIFAL - EC87).

(\*\*) Nas aquisições para uso/consumo ou ativo imobilizado com cálculo de diferencial de alíquotas o valor do FCP é gravado no mesmo campo do FCP Próprio (*\_VALFECP*).
