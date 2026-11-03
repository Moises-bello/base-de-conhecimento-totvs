---
article_id: 29929140746519
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 8fa9c0dbe51682a13e80d101a296f4a63e665395bcafc85a36eb61737599a73d
fetched_at: '2026-06-28T22:39:30.499440+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFIS - Help: IE -
  A inscrição estadual informada está inválida para esta unidade federativa'
type: support-article
updated_at: '2025-02-19T16:50:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29929140746519-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIS-Help-IE-A-inscri%C3%A7%C3%A3o-estadual-informada-est%C3%A1-inv%C3%A1lida-para-esta-unidade-federativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29929140736919) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**

Ao informar a inscrição estadual no cadastro de cliente, o sistema está gerando uma mensagem de HELP:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29929113720727)

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus) - todas as versões.

**Causa**

**1 - Divergência de informação**: A mensagem surge quando o sistema tenta verificar a inscrição estadual informada com o estado do cliente, se houver qualquer divergência na informação, o help é acionado. Em muitos casos, no cadastro do **Sintegra**, a inscrição estadual está iniciada por zero, e o usuário está tentando cadastrar no cadastro de cliente sem o zero, e com isso, o sistema gerará o Help, pois a informação não está correta:

**Consulta Sintegra Exemplo:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29929113720983)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29929113723031)**

**Solução:**

Para correção do erro relacionado ao HELP: IE, basta aplicar o pacote a seguir.

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

**Documentação:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=706135215>
