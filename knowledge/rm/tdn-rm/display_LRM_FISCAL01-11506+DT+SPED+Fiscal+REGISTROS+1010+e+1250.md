---
content_hash: 7db0549773747ffee92f6eb3d323a63220427e2114e61d3ec1a99d7c2df588b7
fetched_at: '2026-06-29T00:10:45.875040+00:00'
page_id: '553342070'
product: rm
source: tdn-rm
title: FISCAL01-11506 DT SPED Fiscal REGISTROS 1010 e 1250
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11506+DT+SPED+Fiscal+REGISTROS+1010+e+1250
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Varejo Gestão Fiscal  TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração do Arquivo SPED Fiscal |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11506 |

## **02. SITUAÇÃO/REQUISITO**

Incluir no Registro 1010 o campo "**14 - IND\_REST\_RESSARC\_COMPL\_ICMS"**.

Se o Registro 1250 for gerado gerar este campo com “S” (sim), caso contrário “N” (não).

Implementar Registro 1250:

#### **REGISTRO 1250 - INFORMAÇÕES CONSOLIDADAS DE SALDOS DE RESTITUIÇÃO, RESSARCIMENTO E COMPLEMENTAÇÃO DO ICMS**

Este registro deve ser a soma dos valores detalhados no 1255.

|  |  |  |
| --- | --- | --- |
| **Nº** | **Campo** | **Descrição** |
| 01 | REG | Texto fixo contendo "1250” |
| 02 | VL\_CREDITO\_ICMS\_OP | Informar o valor total do ICMS operação própria que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito. |
| 03 | VL\_ICMS\_ST\_REST | Informar o valor total do ICMS/ST que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito. |
| 04 | VL\_FCP\_ST\_REST | Informar o valor total do FCP\_ST agregado ao valor do ICMS/ST informado no campo “VL\_ICMS\_ST\_REST” |
| 05 | VL\_ICMS\_ST\_COMPL | Informar o valor total do débito referente ao complemento do imposto, nos casos previstos na legislação. |
| 06 | VL\_FCP\_ST\_COMPL | Informar o valor total do FCP\_ST agregado ao valor informado no campo “VL\_ICMS\_ST\_COMPL” |

## **03. SOLUÇÃO**

Foi implementado a validação para o campo **14 - IND\_REST\_RESSARC\_COMPL\_ICMS"**. O mesmo apresentará "S" caso exista o registro 1250 for gerado e "N" caso contrario.

Também foi implementado o registro 1250.
