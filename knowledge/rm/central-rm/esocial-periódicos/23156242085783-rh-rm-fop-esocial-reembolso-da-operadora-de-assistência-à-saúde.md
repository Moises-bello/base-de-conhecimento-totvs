---
article_id: 23156242085783
category: esocial - Periódicos
content_hash: 7ed6229c8f53cb0cec14315e38f18c49effb53119203220538f36c4a8701405c
fetched_at: '2026-06-28T22:47:09.457884+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Reembolso da Operadora de Assistência à Saúde
type: support-article
updated_at: '2026-02-20T21:26:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23156242085783-RH-RM-FOP-eSocial-Reembolso-da-Operadora-de-Assist%C3%AAncia-%C3%A0-Sa%C3%BAde
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23156235787287) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como registrar os reembolsos pagos aos funcionários pela Operadora de Saúde no RM para envio ao eSocial através do evento S-1210?  
  
**Ambiente**  
TOTVS RH- TOTVS RM (Linha RM)- Folha de Pagamento- eSocial - Todas as versões  
  
**Solução**  
As Informações relativas a despesas médicas ou odontológicas pagas pelo trabalhador prestador de serviço objeto de reembolso no período de apuração são informadas no evento S-1210 através do grupos abaixo:

* Grupo**infoReembMed**, onde o contribuinte deve indicar no campo **indOrgReemb** a origem do   
  reembolso:  
  1 - Reembolso efetuado pelo empregador no âmbito do plano de saúde (a operadora reembolsa o empregador);  
  2 - Reembolso efetuado pelo empregador como benefício do próprio empregador  
  Esse grupo serve para informação de reembolso de despesa do trabalhador com procedimento forada cobertura do plano de saúde coletivo. O reembolso pelo empregador do valor pago pelotrabalhador a um plano de saúde individual não deve ser informado nesse grupo;
* Grupo **detReembTit**, onde deve ser preenchida a informação de reembolso do titular do plano de saúde coletivo empresarial. A empresa deve informar os dados do prestador e do valor do reembolso, seja no período indicado no período de apuração – **vlrReemb** – ou relativo a anos anteriores **vlrReembAnt**;
* Grupo **infoReembDep**, quando houver reembolso do dependente do plano de saúde coletivo empresarial, informando o campo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25367049214743)

Para realizar o cadastro das informações de reembolso no RM, siga as orientações abaixo:

* [Reembolso da Operadora de Assistência à Saúde](https://tdn.totvs.com/pages/viewpage.action?pageId=452718759)
* [Processo para atualizar o reembolso da Operadora de Assistência à Saúde](https://tdn.totvs.com/pages/viewpage.action?pageId=815566495)
