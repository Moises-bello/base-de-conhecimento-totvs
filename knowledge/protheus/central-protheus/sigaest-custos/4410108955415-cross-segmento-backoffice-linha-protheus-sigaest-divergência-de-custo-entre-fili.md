---
article_id: 4410108955415
category: SIGAEST - CUSTOS
content_hash: cacb49694f991627ec7c2cf316370a4c0717c2558603f25d6d479c33b212e610
fetched_at: '2026-06-28T22:39:00.894536+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Divergência de custo
  entre Filial Origem e Filial Destino ao efetuar Transferência entre Filiais
type: support-article
updated_at: '2021-10-06T12:01:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410108955415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Diverg%C3%AAncia-de-custo-entre-Filial-Origem-e-Filial-Destino-ao-efetuar-Transfer%C3%AAncia-entre-Filiais
---

**Dúvida**Ao efetuar a transferência entre filiais em períodos diferente o custo está ficando divergente. O que fazer para resolver?

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Quando é feita uma transferência entre filiais em um período do estoque e classificada a nota de entrada na filial destino no período diferente ou posterior, é necessário habilitar o parâmetro **MV\_M330TRF:**

***MV\_M330TRF*:** ***Valoriza transferência entre filiais, onde entrada e saída estão em períodos diferentes de fechamento de estoque (.T.-Sim/.F.-Não).***

No exemplo abaixo foi emitida a nota fiscal da filial de origem no dia 28/09/2021 e depois feito o fechamento de estoque:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410108663319/mceclip0.png)

Ao efetuar a classificação da nota fiscal na filial destino em um próximo período e executada a rotina de Custo Médio (MATA330) com o parâmetro MV\_M330TRF **desabilitado**, o custo irá ficar divergente do custo de origem ou com valor zerado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410108730135/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410108749335/mceclip2.png)

Porém, quando executada a rotina de Custo Médio com o parâmetro MV\_M330TRF **habilitado**, o custo será igual da nota fiscal de origem:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410108786711/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410108800151/mceclip4.png)

**Saiba mais:**

*[MP - SIGAEST – Custo nas transferências entre filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024874171-MP-SIGAEST-Custo-nas-transfer%C3%AAncias-entre-filiais)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
