---
article_id: 21248237337623
category: Escrita Fiscal - Configurador de Tributos
content_hash: a797458c5c6c9d7721b164639cfb9335ae6a4a7e29f9ff243ea7a553e056b5d6
fetched_at: '2026-06-28T22:39:17.398475+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como configurar
  o cálculo do ICMS-ST com base reduzida e frete agregado?
type: support-article
updated_at: '2024-11-19T13:28:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21248237337623-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-c%C3%A1lculo-do-ICMS-ST-com-base-reduzida-e-frete-agregado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252447511) Tempo aproximado para leitura: **00:20:00 min**

**Dúvida**Como configurar o cálculo do ICMS-ST com base reduzida e frete agregado?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas versões.  
  
**Solução**

Primeiro informamos que valide a memória de cálculo a seguir, pois através da mesma poderá adequar ao seu cenário.

Esse cálculo foi realizado para um cliente revendedor.

UF de origem SP e UF de destino BA.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237168791)

A composição da base do ICMS-ST tem a seguinte sequência:

R$4.547,60 + R$200,00 (Frete) = R$4.747,60 \* 46,32% (Redução) = R$2.199,09

R$2.199,09 + R$154,30 (IPI) = R$2.353,39 + 66,48% (MVA)  = R$3.917,92

R$3.917,92 \* 19% = R$744,40 - 244,03 (ICMS) = R$500,37

**Tributo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252450327)

**Regra de NCM**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252451991)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252452887)

**Perfil de Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252453655)

No perfil do produto poderá informar um ou mais produtos.

Também poderá incluir todos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252454679)

**Perfil de Operação**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252456087)

Valide se possui o mesmo CFOP no TES e no Perfil de operação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252456727)

**Perfil de Participante**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252458007)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252458647)

**Perfil de Origem/Destino**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237186199)

**Regra de Cálculo Documento Fiscal**

**Base de cálculo IPI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237187223)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252460823)

**Regra de Alíquota IPI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252461847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252464279)

**Regra de Escrituração IPI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237192983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237195415)

**Regra de cálculo - Documentos Fiscais - IPI**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237198103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252471447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237205399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252475671)

**Base de Cálculo ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237207319)

obs: o percentual de redução informado deve ser 26,57% (não tributado).

A diferença entre 100% - 73,43% = 26,57%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237208727)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237210007)**

**Regra de Alíquota ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237212183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252484247)

**Regra de Escrituração ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252485655)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237218967)

**Regra de cálculo - Documentos Fiscais - ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252489111)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237221911)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252492823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237227799)

**Base de cálculo ICMS-ST**

* Deverá duas bases de cálculo do ICMS-ST, uma fictícia e outra que efetivamente será apresentada no pedido de venda.

**Base ICMS-ST fictícia**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252494999)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252496535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252501783)

![Base Ficticia.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252504343)

**Base de cálculo ICMS-ST**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252506263)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252508055)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252514711)

![Base icmsst.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252516503)

**Regra de Alíquota ICMS-ST**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252517655)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252518551)

**Regra de Escrituração ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237254807)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252520471)

**Regra de cálculo - Documentos Fiscais - ICMS-ST**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252524439)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252525207)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252526743)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248237268759)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252530327)

![Valor icmsst.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252533527)

**TES**

O CFOP deve ser igual ao Perfil de Operação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252534423)

**Pedido de venda**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21248252536855)

Mais informações sobre o cálculo do ICMS-ST pelo Configurador de Tributos no link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=754953443>
