---
article_id: 4495813817495
category: SIGAEST - CUSTOS
content_hash: fe73f15223e9fe172cbce6f2bb987908155b1644b2f524af2416036ea6b9a977
fetched_at: '2026-06-28T22:39:02.147556+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - De onde
  o Protheus puxa a data na mensagem "Data inicial do processamento"?
type: support-article
updated_at: '2022-02-25T11:51:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4495813817495-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-De-onde-o-Protheus-puxa-a-data-na-mensagem-Data-inicial-do-processamento
---

**Dúvida**De qual parâmetro/de onde o Protheus puxa a data que aparece na tela inicial do Recálculo do Custo Médio (data inicial do processamento)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Pelo padrão do Custo Médio ser calculado a partir do dia do último Fechamento de Estoque + 1 dia, ele validará do parâmetro MV\_ULMES acrescentando um dia.

No exemplo abaixo onde a data início do processamento é 01/01/2022, é por conta da última Virada de Saldos ter sido de 31/12/2021 deixando o parâmetro MV\_ULMES com essa mesma data. Veja abaixo imagens:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4495769709463/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4495802444183/mceclip1.png)

Isso é um padrão do Recálculo do Custo Médio, uma vez que ele começa a recalcular a partir do 1° dia após o último fechamento até a data delegada na pergunta "Data limite Final".

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
