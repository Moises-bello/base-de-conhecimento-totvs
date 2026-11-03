---
article_id: 360042571593
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 9bff3ecf0227e26253b3d03f6dc86607bc7c64cf044e9c3480dbf5b747aaebfe
fetched_at: '2026-06-28T22:45:21.187692+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Seção duplicada com o nome 'PATCH' na
  linha '[PATCH]'
type: support-article
updated_at: '2024-09-27T19:07:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042571593-RH-Linha-Protheus-TAF-eSocial-Se%C3%A7%C3%A3o-duplicada-com-o-nome-PATCH-na-linha-PATCH
---

**Ocorrência**

Ao atualizar o TAF e TSS, é apresentado um erro: **"Seção duplicada com o nome 'PATCH' na linha '[PATCH]'"**, onde o processo de atualização é abortado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056944053)

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões.

**Causa**

O erro informado no LOG é exibido, devido a sua estrutura do arquivo de configuração **appserver.ini** existir o mesmo caminho duplicado.

**Exemplo:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056073474)

**Solução**

1 – Acesse o arquivo de configuração do TAF na pasta **bin/appserver/appserver.ini** e remova as informações duplicadas neste arquivo e salve-o em seguida:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26678953961495)

2 - Prossiga com a atualização do ambiente TAF/TSS.
