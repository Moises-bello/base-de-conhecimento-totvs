---
content_hash: a5d4074a23d2a085e672363e3c301c61fd754929335231749240b6f49b7d7808
fetched_at: '2026-06-29T00:05:50.975841+00:00'
page_id: '1046428408'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos 2026 - Juros de mora recebidos pelo atraso no pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Informe+de+Rendimentos+2026+-+Juros+de+mora+recebidos+pelo+atraso+no+pagamento
version: 12
---

## **1. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Informe de Rendimentos 2026- Juros de mora recebidos pelo atraso no pagamento |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-17672](https://jiraproducao.totvs.com.br/browse/DRHROTRM-17672) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.294
  + 12.1.2506.263
  + 12.1.2510.183
  + 12.1.2602.107 e superiores

## **03. SITUAÇÃO/REQUISITO**

Devido à substituição da DIRF pelo eSocial e às recentes modificações realizadas na tela Anuais | DIRF/Informe de Rendimentos, identificou-se a necessidade de retornar com a aba "**J****uros de mora recebidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função**" dentro quadro "Campo 4 - Rend. Isentos e não Tribut."

## **04. SOLUÇÃO**

No menu Anuais | DIRF/Informe de Rendimentos, foi retornada a aba "**J****uros de mora recebidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função**" dentro quadro "Campo 4 - Rend. Isentos e não Tribut."

A exibição correta dos eventos nesta aba está condicionada ao cumprimento dos seguintes critérios, devidamente parametrizados nos eventos/verbas, no menu Administração de Pessoal | Eventos | Eventos:

* **`FORCARINCIRRF`** = **FALSO**
* **`ISENTOIRRF`** = **VERDADEIRO**
* **`INCIRRFISENCAO`** = **704**

Ao realizar a consulta para listar os eventos, somente foi listado o evento que atende a regra citada.

**ATENÇÃO:**

Para a consistência dos dados relativos a **juros moratórios** no 'Relatório de Conferência (IRRF) - Informações Complementares', a parametrização e o envio do evento devem seguir as especificações técnicas vigentes. Ressaltamos que a base de cálculo e a respectiva retenção são consolidadas via **evento S-5002**, conforme as orientações disponíveis no  [link](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s-1-3-cons-nt-05-2025/index.html#evtBasesTrab) e nos manuais de orientação do eSocial.

## **05.****ASSUNTOS RELACIONADOS**
