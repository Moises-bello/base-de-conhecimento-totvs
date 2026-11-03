---
article_id: 360025656852
category: Originação de Grãos (OG)
content_hash: 633a2f001707a88dc09d554a7ef4878d2ce24574efa06590e6dd5fa4775e9fb1
fetched_at: '2026-06-28T22:45:45.177754+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Tipo de fixação de preço
type: support-article
updated_at: '2025-07-10T19:56:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025656852-Agro-Linha-Protheus-AGR-Tipo-de-fixa%C3%A7%C3%A3o-de-pre%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20799842971287)***Tempo aproximado para leitura: **00:01:00 min****Dúvida**O que significa **Preço Fixo** ou **a** **Fixar** nas rotinas de **Contrato de Compra - OGA280** e de **Contrato de Venda - OGA290**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O **preço fixo** refere-se à **negociação com preço final**, determinado já na negociação da compra ou venda. Este preço pode ser determinado na moeda corrente ou em outra moeda definida no contrato. Os recebimentos e/ou faturamentos irão utilizar este preço definido para a emissão de **notas fiscais**, caso seja em moeda corrente. Se for fixo em outra moeda poderão ser emitidas as **notas fiscais** em um preço padrão **preço pauta**, ou o valor fixo é convertido por uma taxa, e no dia do pagamento,  será emitida uma **nota fiscal** complementar de valor ou uma **Nota de Débito** de acordo com a taxa combinada.  
O **preço a fixar** refere-se à **negociação com preço não determinado**, em que se estabelece em contrato uma data máxima para que seja negociado o preço do produto. Para os recebimentos e/ou faturamentos é utilizado um preço padrão **preço pauta**. Em geral, este valor é menor que o preço padrão de mercado, facilitando gerar o complemento após a fixação do preço. Quando há diferença de preço entre o **fixado** e o **preço recebido faturado** será gerada uma **nota fiscal** de complemento de preço ou uma **nota de crédito** quando o valor fixado for menor que o preço fixado.

![FIX.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8021445180311)

**Importante**Os ajustes de preços são efetuados por meio da rotina de **Gestor da Entidade - OGA450**.
