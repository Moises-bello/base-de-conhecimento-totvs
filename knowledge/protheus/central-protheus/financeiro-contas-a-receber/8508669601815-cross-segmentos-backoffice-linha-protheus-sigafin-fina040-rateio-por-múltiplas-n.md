---
article_id: 8508669601815
category: Financeiro - Contas a Receber
content_hash: 247261179ee5e9f892fe668bf5092e6fc0e38abda2e02e971b78924d1f600335
fetched_at: '2026-06-28T22:38:12.636753+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Rateio por
  múltiplas naturezas e centro de custo
type: support-article
updated_at: '2025-10-08T12:36:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8508669601815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Rateio-por-m%C3%BAltiplas-naturezas-e-centro-de-custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487194901911) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao incluir um título que possui rateio de múltiplas naturezas e centro de custo, o sistema não está gravando a porcentagem corretamente, havendo diferença de centavos no momento da baixa.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA040 - Todas as versões  
  
**Solução**Para correção desse cenário é necessário alterar o tamanho dos campos **EV\_PERC EZ\_PERC.   
  
Exemplo:**   
Para um tamanho total de campo 13, inserir da casa decimal para 9.

1. Acessar **configurador** > **Base de dados** > **Dicionário**> **Base de dados**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8521902798871)

2. Aumentar o tamanho das casas decimais dos campos **EV\_PERC e EZ\_PERC**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8522036288663)

**Saiba mais**

[Rateio por múltiplas naturezas e centro de custo](https://tdn.totvs.com/pages/releaseview.action?pageId=271391703)
