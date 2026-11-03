---
content_hash: 7814c3bde71971bd5014bf0456988449cfea787f20e372b58d872f3de2eb246f
fetched_at: '2026-06-29T00:10:38.091331+00:00'
page_id: '543089072'
product: rm
source: tdn-rm
title: FISCAL01-12236 - SPED Fiscal - Registro 1921 - Ressarcimento/Complemento ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543089072
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | FISCAL01-12236 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12236 |

## **02. SITUAÇÃO/REQUISITO**

#### **Registro 1921: Ajuste/Benefício/Incentivo da Sub-apuração do ICMS**

Este registro traz os detalhes dos lançamentos de ajustes que afetaram a sub-apuração e possui duas origens de dados:

* Lançamentos de Outros Débitos/Créditos que tenham uma sub-apuração associada
* Lançamentos de Ajustes informados nos Itens dos Lançamentos Fiscais. Neste caso, soma-se o valor de todos os itens que serão detalhados no Registro 1923.

Podem existir vários no período. Esse registro é filho do 1920 (nível 5).

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem do dado** |
| 01 | REG | Indicador do registro | Valor fixo “1921” |
| 02 | COD\_AJ\_APUR | Código do ajuste da SUB-APURAÇÃO e dedução, conforme a Tabela indicada no item 5.1.1. | DLDC.CODAJUSTESPED DCODIGOAJUSTE.CODAJUSTE |
| 03 | DESCR\_COMPL\_AJ | Descrição complementar do ajuste da apuração. | DLDC.OBSERVACAO DLAFAJUSTESPED.DESCRICAOCOMPLEMENTAR |
| 04 | VL\_AJ\_APUR | Valor do ajuste da apuração | DLDC.VALORLDC DLAFAJUSTESPED.VALORICMSI |

## **03. SOLUÇÃO**

Foi incluído a geração do Registro 1921 ao SPED. Após análise foi acordado, que a geração do Registro só ocorre para lançamentos de Outros Débitos/Créditos, não tendo origem de lançamentos fiscais.
