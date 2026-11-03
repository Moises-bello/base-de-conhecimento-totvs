---
article_id: 28603178674071
category: Originação de Grãos (OG)
content_hash: 15e7361c1188d98453cdfca05cd05bc6a389677853beee5af045ff8d577c6a99
fetched_at: '2026-06-28T22:45:41.010347+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Moeda de Faturamento e Moeda de Recebimento
type: support-article
updated_at: '2025-06-25T19:05:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28603178674071-Agro-Linha-Protheus-AGR-Moeda-de-Faturamento-e-Moeda-de-Recebimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28603173136151) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Para que serve a estrutura de **Moeda de Faturamento e Moeda de Recebimento**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para contratos de venda de mercado interno com **moeda estrangeira** são habilitados os campos de **Moeda de Faturamento** e **Moeda de Pagamento**. Abaixo é descrita a regra de funcionamento: Quando o campo Referência estiver como **1 - Faturamento** é utilizado apenas a cotação da **Moeda de Faturamento** para geração da previsão financeira e faturamento.   
Quando o campo Referência estiver como **2 - Pagamento** é habilitado para informar a **moeda de pagamento**, nesse caso a previsão de pagamento será gerada na **moeda** informada nesse campo e o faturamento continuará a ocorrer na **moeda do contrato**. Após realizar o pagamento, deve-se informar a cotação de trava de câmbio na regra fiscal. A partir desse momento então o faturamento utiliza a cotação que foi travada.

![PROTS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28603178649623)
