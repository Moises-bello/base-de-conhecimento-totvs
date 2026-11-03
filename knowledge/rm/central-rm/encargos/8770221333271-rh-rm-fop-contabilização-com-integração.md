---
article_id: 8770221333271
category: Encargos
content_hash: 9302af96082fe2c8b80c6718f74a76dbd15cc5d305330b72b2936056642e943a
fetched_at: '2026-06-28T22:46:52.440595+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Contabilização com integração
type: support-article
updated_at: '2024-06-12T19:18:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8770221333271-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-com-integra%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24139976331031) Tempo aproximado para leitura: **00:01:05 min****Dúvida**Como realizar a contabilização com integração?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Cadastrar códigos de integração contábil na na tabela dinâmica: **CODINTCONT**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768435401879)**

Cadastrar em **Encargos | Cadastros | Cadastros Contábeis | Agrupamento de contas**:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769197545879)  
  
Para cada integração é necessário cadastrar o grupo de contas contábeis. No exemplo utilizei a integração 02-Suporte. Realizar a parametrização nos eventos e marcar a flag Tem integração contábil:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768610314775)

Verifique dentro das seções dos colaboradores se estão preenchidos:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8768717589399)

Gere o Histórico de provisão e encargos, para gerar o lançamento:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769319633431)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769274541207)

**Saiba mais**[RH - RM - FOP - Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019748711-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o)
