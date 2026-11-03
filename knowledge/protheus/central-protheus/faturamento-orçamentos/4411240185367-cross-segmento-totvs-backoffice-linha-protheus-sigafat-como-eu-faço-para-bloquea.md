---
article_id: 4411240185367
category: Faturamento - Orçamentos
content_hash: 82e40480c9eaf9b371bd9b38997e7e404b332e9bdf7b57f1848830b3bb57b7bd
fetched_at: '2026-06-28T22:38:24.926374+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Como eu faço
  para bloquear um cliente por inadimplência até para gerar orçamento
type: support-article
updated_at: '2021-10-25T11:38:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411240185367-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Como-eu-fa%C3%A7o-para-bloquear-um-cliente-por-inadimpl%C3%AAncia-at%C3%A9-para-gerar-or%C3%A7amento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como eu faço para bloquear um cliente por inadimplência até para gerar orçamento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- Todas as versões  
  
**Solução**

A configuração para análise de crédito parte a partir da liberação do pedido via rotina Liberação do pedido (**mata440)**, pois é nesta rotina que as configurações relacionada ao cliente para análise de credito passarão a ser validadas.

No orçamento (**Mata415**), não existe estas validações para tratamento de crédito, pois o orçamento ainda não é formalmente um pedido de venda, podendo mudar a negociação a qualquer momento.

Neste caso, se for necessário alguma validação, será necessário a utilização de ponto de entrada disponível na rotina, não há um ponto específico para esta verificação:

**- M415GRV -** Gravação de orçamento: <https://tdn.totvs.com/x/oYRn>

**- A415TDOK -** Validação da tudook: <https://tdn.totvs.com/x/J4Rn>

Uma opção, se o cliente estiver inadimplente, pode-se deixar seu cadastro bloqueado de uso, deixando o campo **a1\_msblql** (**bloqueio**) como Sim, desta forma, ao tentar inserir seja no orçamento ou pedido, o sistema não permitirá a sua inclusão.

Para mais informações sobre análise de crédito de cliente, acesse:  **[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Configurações para bloqueio de crédito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017748031-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Configura%C3%A7%C3%B5es-para-bloqueio-de-cr%C3%A9dito)**
