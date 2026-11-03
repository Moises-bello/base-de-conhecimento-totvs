---
article_id: 20117614712599
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 9055f45e13d77e6a6816880d3f191273568f131733aa39f5044b35ca9d1148ea
fetched_at: '2026-06-28T22:39:22.091814+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como gerar crédito
  presumido por reflexo?
type: support-article
updated_at: '2023-12-26T14:15:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20117614712599-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-cr%C3%A9dito-presumido-por-reflexo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20117614667543) Tempo aproximado para leitura: 05:00**min** **Dúvida**Como gerar crédito presumido por reflexo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**  
Nesse exemplo vamos calcular o credito presumido pela TES e gerar o reflexo configurado no TES

exemplo:

Parâmetros:

MV\_ESTADO = SC

MV\_P9SPED = .F.

MV\_P9AUTO = F

MV\_USASPED = .T.

Código de lançamento = SC10000003

Credito presumido 9%

Valor da mercadoria = 1000,00

Credito presumido sobre a base de calculo do ICMS

1000,00\*9% = 90,00

Seguem as configurações

TES

Calcula icms = sim

L fiscal icms = tributado

Sit trib icm = 00

CFOP = 5102

**Agreg CrdPre = não**

**Tp  Cred  Pres = B**

**Crd. Pres. = 9%**

Reflexo amarrado no TES o padrão 000070 gerado pelo U\_IMPSPED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20117644810007)

Conteudo do Reflexo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20117644811543)

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20117614672279)

Aba lançamento da apuração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20117614673175)

O credito presumido será gravado nos campos:

FT\_CRDPRES / F3\_CRDPRES

Apuração do ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20117644814999)

Ao gerar o SPED FISCAL será gerado o C197.
