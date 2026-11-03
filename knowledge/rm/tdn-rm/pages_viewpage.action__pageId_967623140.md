---
content_hash: ef50ad6eb4e9500decd29cdb50ce6f0eff25909e632a749030d8877d8323d8d3
fetched_at: '2026-06-29T00:12:14.589232+00:00'
page_id: '967623140'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência de IRRF - Adequação para atender ao Leiaute S-1.3
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=967623140
version: 12
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência de IRRF - Adequação para atender ao Leiaute S-1.3 |
| País: | Brasil |
| Issue: | [DRHROTRM-11408](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11408) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410.271
* 12.1.2502.118
* 12.1.2506.174 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Possibilidade de comparar os valores de **Rendimento Não Tributável ou Isento do IRRF** informados no evento **S-5002 - Imposto de Renda Retido na Fonte**, apurados pelo sistema TOTVS Folha de Pagamento, através do **Relatório de Conferência de IRRF**, facilitando a validação e conferência dos dados .

**04. SOLUÇÃO**

Implementado no Relatório de Conferência IRRF o reconhecimento dos valores de **Rendimento não tributável ou isento do IRRF**, conforme especificado no leiaute S-1.3.

No campo {tpInfoIR} do grupo {infoIR}, foram incluídos os códigos **[702, 703, 704]** para o eventoS-5002 – Imposto de Renda Retido na Fonte.

A descrição de cada tipo de IR, na coluna **“Consolidação dos tipos de valores relativos ao IRRF”**, será determinada de acordo com a parametrização do campo **“Isento de IRRF”** existente no cadastro de Eventos/Verbas, conforme exemplificado no print abaixo.

IMPORTANTE:

Quando o campo **“Isento de IRRF”** estiver definido como *“79 - Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores)”*, o sistema apresentará a descrição conforme o conteúdo do campo **“Descrição”** do Evento/Verba. Veja exemplo abaixo:

## **05. DOCUMENTAÇÃO**
