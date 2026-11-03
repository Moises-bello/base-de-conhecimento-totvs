---
article_id: 360020487912
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: e7a21a733e17d4f854a54a2e6ad43b23bc917e54c033ae47ace4fcbfefbd8780
fetched_at: '2026-06-28T22:45:21.172992+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - O valor 'X' informado na
  tag ideTabRubr não existe na base de dados
type: support-article
updated_at: '2026-06-26T11:50:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020487912-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-O-valor-X-informado-na-tag-ideTabRubr-n%C3%A3o-existe-na-base-de-dados
---

**Dúvida**

Ao integrar os eventos para o TAF ocorre a seguinte falha:

O valor 'x' informado na tag ideTabRubr não existe na base de dados

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF -Todas as versões

**Solução:**

1 - Acesse o TAF em: Atualizações -> Eventos e-Social -> Tabelas -> Identificadores de Rubricas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26731063166615)

2 - Verifique se o código mencionado no erro existe na rotina, caso contrário será necessário incluir:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075204014)

3 - Ao regularizar o status deste registro faça novamente a integração do registro que apresentou erro.
