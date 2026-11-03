---
article_id: 14704958129303
category: Financeiro - Contas a Pagar
content_hash: 1c572f89797380c454a0f3a8908a7e53e7b949c64696a85b90faf5e7dd4dd5c0
fetched_at: '2026-06-28T22:38:08.566912+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Help PA_EXISTIU
type: support-article
updated_at: '2023-05-23T18:22:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14704958129303-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Help-PA-EXISTIU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**

No módulo Financeiro, ao tentar incluir um PA, o sistema apresenta o Help PA\_EXISTIU.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14792314827799)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Por padrão, o sistema faz a validação e verifica se existe as informações do PA na SE5, confirma as chaves na tabela SE2 - E2\_PREFIXO, E2\_NUM*,* E2\_PARCELA, E2\_TIPO*,* E2\_FORNECE e E2\_LOJA*.*

Caso encontre as informações na SE5, apresenta o help em questão.

**Solução**Incluir o adiantamento com outra numeração e prefixo, para não conflitar com um registro já gravado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14765276678935)
