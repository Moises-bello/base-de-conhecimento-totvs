---
article_id: 29011123207191
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: 86b7a48ebe62e4babc06aa51161c63e1cf9806c157090a45267668780591c5c4
fetched_at: '2026-06-28T22:37:49.960560+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Retorno
  Online - Portas de uso do WebHook do Banco do Brasil
type: support-article
updated_at: '2025-01-07T16:47:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29011123207191-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Retorno-Online-Portas-de-uso-do-WebHook-do-Banco-do-Brasil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29011123187223) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Quais são as portas de uso do WebHook para utilização das baixas?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

É possível simular um servidor de recebimento do evento Webhook em alguns sites da web. Caso tenha dúvidas se o seu servidor está corretamente configurado, utilize esses sites para validar que o evento está sendo disparado pelo banco.

Por padrão a porta da URL utilizada para envio do Webhook é a 443. Caso não seja possível configurar essa porta no seu servidor, existem outras portas que o banco permite que dispare o evento (ex.: 3001, 50900).

Exemplo de URL do REST com a porta: <https://seuendereco:suaporta/api/fin/v1/bb/bol/receivables/>

Abaixo estão relacionadas todas as portas disponíveis para configuração de recebimento do Webhook:

443  
444  
3001  
4431  
8111  
8443  
8483  
9093  
44300  
50900  
59360

**Saiba mais**  
[Testes via Sandbox Webhook](https://apoio.developers.bb.com.br/referency/post/672cf97e4ab0a30013f27a72)  
[Banco do Brasil - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=673798283)
