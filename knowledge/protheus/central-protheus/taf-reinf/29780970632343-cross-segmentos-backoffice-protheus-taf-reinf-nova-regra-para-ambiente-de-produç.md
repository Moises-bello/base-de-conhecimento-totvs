---
article_id: 29780970632343
category: TAF - REINF
content_hash: 098765f5f7d8c5397583e5b1799811404c0d39e8190bafadf23a69327e259798
fetched_at: '2026-06-28T22:41:34.730961+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos - Backoffice Protheus - TAF - REINF - Nova regra para ambiente
  de produção restrita REINF
type: support-article
updated_at: '2025-02-05T19:32:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29780970632343-CROSS-Segmentos-Backoffice-Protheus-TAF-REINF-Nova-regra-para-ambiente-de-produ%C3%A7%C3%A3o-restrita-REINF
---

**Dúvida**

 A Receita Federal altera a regra de envio dos dados da REINF, em ambiente de produção restrita, limitando o armazenamento de, no máximo, 1000 arquivos por tipo de evento para cada contribuinte. Haverá mudanças no TAF?

**Ambiente**  Cross Segmento - TOTVS Backoffice (Linha Protheus) - **SIGATAF** - Todas as versões  
  
**Solução**

**Não haverá alteração no produto em relação as mudanças aplicadas. Caso exceda a quantidade de arquivos enviado será necessário realizar a limpeza de base e novo envio do R-1000.**

1° Para limpeza de base, acesse o painel REINF e clique na opção remover contribuinte, com  essa opção será removido todos movimentos enviados pelo ambiente teste.

![remover contribuinte 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29781002679063)

  Consulte o retorno da remoção.

2° Apure e transmita o R-1000 novamente e em seguida envie os eventos periódicos desejados.

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Cadastro do Complemento de Cadastral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022208052-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Cadastro-do-Complemento-de-Cadastral)
