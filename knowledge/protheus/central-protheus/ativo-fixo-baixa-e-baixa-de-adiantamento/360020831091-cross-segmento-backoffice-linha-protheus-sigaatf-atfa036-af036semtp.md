---
article_id: 360020831091
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: ed3a892def44271f56ddc171ff9d40187a05bed84a8ace79d6056ee642721489
fetched_at: '2026-06-28T22:41:55.473926+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 - AF036SEMTP
type: support-article
updated_at: '2022-05-10T13:18:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020831091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-AF036SEMTP
---

**Dúvida**Ao efetuar uma baixa do ativo imobilizado pela rotina ATFA036 é apresentado o seguinte HELP:

![](https://totvssuporte.zendesk.com/attachments/token/DujDEynZzzzBOcOn8AHERaR17/?name=inline-314943582.png)

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80

**Solução:**

O HELP "**AF036SEMTP**" pode ser apresentado por dois motivos, são eles:

1- O tipo do ativo não estar marcado no momento da baixa conforme imagem(pode ser tipo 01 - Fiscal, 10 - Gerencial, entre outros):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017276672/mceclip0.png)

2- O campo **N1\_STATUS** na tabela **SN1** estar diferente de 1 - Em uso, para obter mais detalhes desse campo pode-se acessar: [MP - SIGAATF - N1\_STATUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008522071-MP-SIGAATF-N1-STATUS?source=search)
