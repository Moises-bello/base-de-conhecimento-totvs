---
article_id: 21052370079511
category: Originação de Grãos (OG)
content_hash: 35cc92da42cf222bb5cbe343979ba4fddf9273612d68ac79c7bceee49a5d185c
fetched_at: '2026-06-28T22:45:45.174256+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Tipo de fixação de preço
type: support-article
updated_at: '2025-06-18T12:15:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21052370079511-Agro-Linha-Protheus-AGR-Tipo-de-fixa%C3%A7%C3%A3o-de-pre%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21052370021911) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para registrar **Preço Fixo** ou a **Fixar** nas rotinas de **Contrato OGA280** **e** **OGA290** é apresentada a ocorrência **Tipo de fixação de preço**.  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para encontrar as tabelas referentes ao **agronegócio** no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, analise o **preço fixo** refere-se à **negociação com preço final**, determinado já na negociação da compra ou venda. Este preço pode ser determinado na moeda corrente ou em outra moeda definida no contrato. Os recebimentos e/ou faturamentos irão utilizar este preço definido para a emissão de **notas fiscais**, caso seja em moeda corrente. Se for fixo em outra moeda poderão ser emitidas as **notas fiscais** em um preço padrão **preço pauta**, ou o valor fixo é convertido por uma taxa, e no dia do pagamento,  será emitida uma **nota fiscal** complementar de valor ou uma **Nota de Débito** de acordo com a taxa combinada.  
O **preço a fixar** refere-se à **negociação com preço não determinado**, em que se estabelece em contrato uma data máxima para que seja negociado o preço do produto. Para os recebimentos e/ou faturamentos é utilizado um preço padrão **preço pauta**. Em geral, este valor é menor que o preço padrão de mercado, facilitando gerar o complemento após a fixação do preço. Quando há diferença de preço entre o **fixado** e o **preço recebido faturado** será gerada uma **nota fiscal** de complemento de preço ou uma **nota de crédito** quando o valor fixado for menor que o preço fixado.

![FIX.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/21052310090775)

**Importante**Os ajustes de preços são efetuados por meio da rotina de **Gestor da Entidade - OGA450**.
