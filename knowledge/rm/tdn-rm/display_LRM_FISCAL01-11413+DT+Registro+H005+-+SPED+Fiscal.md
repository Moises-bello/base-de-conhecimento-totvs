---
content_hash: be9d2e96893cde56a6222eadef440b80962c2b0ab86970706f99fd344c685fda
fetched_at: '2026-06-29T00:10:31.206026+00:00'
page_id: '521111465'
product: rm
source: tdn-rm
title: FISCAL01-11413 DT Registro H005 - SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11413+DT+Registro+H005+-+SPED+Fiscal
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | FISCAL01-11413 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11413 |

## **02. SITUAÇÃO/REQUISITO**

Quando a rotina gerar algum dos registros de ressarcimento/complemento (C180, C185, C330, C380, C430, C480, C815 e C870), o sistema deve gerar um Registro H005 com as seguintes informações:

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem da Informação** |
| 01 | REG | Texto fixo contendo "H005” | Fixo “H005” |
| 02 | DT\_INV | Data do inventário | Data final do período da rotina |
| 03 | VL\_INV | Valor total do estoque | (verificar como é gerado nos demais casos e replicar a regra) |
| 04 | MOT\_INV | Informe o motivo do Inventário: | Fixo “06” – Para controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ ressarcimento/ complementação. |

## **03. SOLUÇÃO**

Foi implementado a geração registro H005 quando o Motivo de Inventário, estiver:

* Com a flag de Ressarcimento/Complemento ICMS-ST marcado
* Possuir informações  de inventário no período que o usuário selecionou
