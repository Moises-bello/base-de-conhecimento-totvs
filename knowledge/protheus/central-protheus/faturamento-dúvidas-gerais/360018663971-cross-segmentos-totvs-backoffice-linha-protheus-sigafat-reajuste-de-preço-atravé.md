---
article_id: 360018663971
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e4ff8ff3ed6330a388226037f3d071f400fc78ea4ce614e4d615e3228e1bec76
fetched_at: '2026-06-28T22:38:30.031656+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Reajuste de
  Preço através da rotina MATA511B
type: support-article
updated_at: '2021-12-06T19:01:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018663971-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reajuste-de-Pre%C3%A7o-atrav%C3%A9s-da-rotina-MATA511B
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como utilizar a rotina Reajuste de Preço MATA511B?

**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Todas as Versões  
  
**Solução**Esta rotina faz o reajuste do preço de uma nota gerada, gerando uma nota de complemento de preço.  
  
Para gerar esta nota de complemento, o pedido de venda da nota fiscal gerada, deverá possuir no campo **C5\_REAJUST**, o código da formula que será executada, para calcular o valor da nota de complemento que será gerada.   
Ao rodar a rotina de reajuste, a mesma irá gerar uma nota de complemento, aplicando os valores da fórmula que foi gerada.  
  
Também poderá ser utilizado a regra por tabela de preços, ao invés de formulas, conforme o parâmetro ( Tipo de reajuste ), então neste caso ele avalia a diferença de preço de venda com o preço da tabela de preços para geração da nota de complemento.

**No link abaixo temos vídeos mostrando o passo a passo de como usar a rotina:**  
[Reajuste de preço (MATA511B)](https://tdn.totvs.com/x/dwAmDg)

**Saiba Mais:**

**[Help Online Protheus](https://www.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/sigafat.htm)**

**[Cross-Segmentos-Totvs-BackOffice-Protheus-Fatuamento-SIGAFAT-Reajuste-de-Valores-na-Tabela-de-Preço-Preço-Base-e-Pedidos-em-Aberto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019193491-Cross-Segmentos-Totvs-BackOffice-Protheus-Fatuamento-SIGAFAT-Reajuste-de-Valores-na-Tabela-de-Pre%C3%A7o-Pre%C3%A7o-Base-e-Pedidos-em-Aberto)**

**[Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reajuste-de-Tabela-de-Preço-por-Planilha-de-Formação-de-Preço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333411-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reajuste-de-Tabela-de-Pre%C3%A7o-por-Planilha-de-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o)**
