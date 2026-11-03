---
article_id: 28055918599959
category: Comércio Exterior - Easy - Financing
content_hash: dfa12313d6228881f9bbd62cbdb998b77d90a7c20004378b7d7258a5d9bf4b08
fetched_at: '2026-06-28T22:39:53.017496+00:00'
product: protheus
section_id: 1500001538101
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEFF - Ao preencher
  o campo Dt. Ini. Juros (EF1_DT_JUR) é apresentada a mensagem: ''Não há vinculações
  liquidadas neste contrato.'
type: support-article
updated_at: '2024-11-29T18:52:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28055918599959-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEFF-Ao-preencher-o-campo-Dt-Ini-Juros-EF1-DT-JUR-%C3%A9-apresentada-a-mensagem-N%C3%A3o-h%C3%A1-vincula%C3%A7%C3%B5es-liquidadas-neste-contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28055918554519) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Ao preencher o campo **EF1\_DT\_JUR 'Dt. Ini. Juro**, é apresentada a mensagem: 'Não há vinculações liquidadas neste contrato. Como corrigir?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28055918556695)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - A partir da versão12.1.2210  
  
**Solução**A mensagem é apresentada, pois o “Financiamento de Importação” consiste em uma operação na qual o cliente importará um bem ou produto, que possui uma invoice como obrigação de pagar à vista em sua totalidade ou de forma parcial, onde há a expectativa de receber o bem ou produto no futuro. O banco antecipa em moeda estrangeira e efetua o pagamento ao exportador no exterior.

Para que seja possível prosseguir com o preenchimento da data de início de juros no campo Dt. Ini. Juro (**EF1\_DT\_JUR)**  é necessário vincular uma invoice de importação no contrato de financiamento.
