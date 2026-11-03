---
article_id: 4410253103127
category: SIGAEST - CUSTOS
content_hash: 1a6f25a75898707d6fef76a4b191ce75476afbca67d9f6252733f471ed1545b3
fetched_at: '2026-06-28T22:39:00.838292+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Contabilização de
  desmontagem - LP 670 e 672
type: support-article
updated_at: '2025-03-12T12:20:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410253103127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Contabiliza%C3%A7%C3%A3o-de-desmontagem-LP-670-e-672
---

**Dúvida**Quais as os Lançamentos Padrões do Estoque/Custos que efetuam a contabilização de movimentos feitos para desmontagem de um produto?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Os lançamentos padrões corretos para contabilizar a desmontagem de produtos são as Lp's 670 e 672.

No exemplo abaixo, vamos desmontar a quantidade de 10 unidades, de uma PA (PA700), para o seu produto que compõe sua produção, no caso a MP700.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410248699671/mceclip0.png)

Serão gerados dois movimentos, RE7 referente a desmontagem da PA, e DE7 referente ao produto que recebe a quantidade que foi desmontada.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410248747159/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410248774807/mceclip2.png)

Após isso, efetue o Recalculo do Custo Médio (MATA330), ou rotina de Contabilização Offline (MATA331), com o pergunte:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410249357079/mceclip6.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410252903063/mceclip3.png)

Veja que o lançamento foi gravado.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410249310359/mceclip4.png)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-MP-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Contabilizar as Movimentações Internas do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-Internas-do-Estoque-)

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
