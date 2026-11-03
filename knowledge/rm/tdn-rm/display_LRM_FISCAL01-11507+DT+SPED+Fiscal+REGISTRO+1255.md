---
content_hash: 4451ee2e19bcb61872ce4126c3d28511ceb98cb2095e871551548e4b3a5bed37
fetched_at: '2026-06-29T00:10:45.915697+00:00'
page_id: '553877883'
product: rm
source: tdn-rm
title: FISCAL01-11507 DT SPED Fiscal REGISTRO 1255
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11507+DT+SPED+Fiscal+REGISTRO+1255
version: 1
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11507 |

## **02. SITUAÇÃO/REQUISITO**

Implementar Registro 1255

#### **REGISTRO 1255 - INFORMAÇÕES CONSOLIDADAS DE SALDOS DE RESTITUIÇÃO, RESSARCIMENTO E COMPLEMENTAÇÃO DO ICMS POR MOTIVO**

Este Registro detalha por motivo de ressarcimento/complemento os saldos do ICMS próprio, ICMS ST e FCPST.  As informações são baseadas nos Registros C185; C330; C380; C430; C480; C880.

|  |  |  |
| --- | --- | --- |
| **Nº** | **Campo** | **Descrição** |
| 01 | REG | Texto fixo contendo "1255” |
| 02 | COD\_MOT\_REST\_COMPL | Código do motivo da restituição ou complementação conforme Tabela 5.7 |
| 03 | VL\_CREDITO\_ICMS\_OP\_MOT | Informar o valor total do ICMS operação própria que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito, para o mesmo “COD\_MOT\_REST\_COMPL” |
| 04 | VL\_ICMS\_ST\_REST\_MOT | Informar o valor total do ICMS/ST que o informante tem direito ao crédito, na forma prevista na legislação, referente às hipóteses de restituição em que há previsão deste crédito, para o mesmo “COD\_MOT\_REST\_COMPL” |
| 05 | VL\_FCP\_ST\_REST\_MOT | Informar o valor total do FCP\_ST agregado ao valor do ICMS/ST informado no campo “VL\_ICMS\_ST\_REST\_MOT” |
| 06 | VL\_ICMS\_ST\_COMPL\_MOT | Informar o valor total do débito referente ao complemento do imposto, nos casos previstos na legislação, para o mesmo “COD\_MOT\_REST\_COMPL” |
| 07 | VL\_FCP\_ST\_COMPL\_MOT | Informar o valor total do FCP\_ST agregado ao valor informado no campo “VL\_ICMS\_ST\_COMPL\_MOT” |

## **03. SOLUÇÃO**

Registro 1255 foi implementado na geração do SPED Fiscal
