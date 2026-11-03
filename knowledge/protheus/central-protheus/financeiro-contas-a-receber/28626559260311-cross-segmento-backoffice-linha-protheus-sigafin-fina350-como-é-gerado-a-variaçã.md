---
article_id: 28626559260311
category: Financeiro - Contas a Receber
content_hash: 38ab6c58c5e83caf23a192f0819f8cfb366f10897a02c6c8ee3f597b0a8d011e
fetched_at: '2026-06-28T22:38:12.512591+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA350 - Como é gerado
  a variação após executar a FINA350
type: support-article
updated_at: '2024-12-18T18:36:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28626559260311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA350-Como-%C3%A9-gerado-a-varia%C3%A7%C3%A3o-ap%C3%B3s-executar-a-FINA350
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28626559226903) Tempo aproximado para leitura: 00:08 min **Dúvida**Como fica o cálculo da variação cambial na baixa quando executamos a FINA350?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA350 - Todas as versões  
  
**Solução**

Ao executar a rotina **FINA350** e modificar a moeda, o sistema deixará de levar em conta a moeda informada na inclusão do título, passando a levar em conta a moeda no campo **E1\_TXMDCOR**.

**Exemplo**

Incluimos um movimento onde a moeda é R$ 5,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28626573457047)

Ao executar **FINA350** considerando o valor da moeda em R$ 4,90. Observe que o sistema gera uma movimentação na SE5 com a variação cambial, que no nosso caso foi negativa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28626573460375)

Observe que o campo **E1\_TXMDCOR** foi preenchido com a moeda indicada no FINA350

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28626559235223)

Caso execute novamente a **FINA350**, o campo **E1\_TXMDCOR** será modificado novamente. No exemplo, estou indicando a moeda a R$ 6,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28626559237143)

O sistema cria mais uma variação, agora com o valor positivo de R$ 1.100,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28626573464343)

Quando efetuamos uma baixa em que o dólar está a R$ 6,20, o sistema fará o cálculo entre a moeda R$ 6,00 e a baixa para 6,20, e não mais de R$ 5,00, conforme especificamos na origem do título.

Portanto, a diferença seria de R$200, ao invés de R$1.200,00, uma vez que o sistema já fez essa alteração no momento da execução da FINA350

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28626573465623)

A contabilização dessas movimentações seria pela LP 599 contas a pagar ou 598 contas a receber.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28626559242647)

**Saiba mais**

[Contabilização da Variação Monetária - FINA350 - Financeiro - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=562474217)

[Lançamento padrão financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)
