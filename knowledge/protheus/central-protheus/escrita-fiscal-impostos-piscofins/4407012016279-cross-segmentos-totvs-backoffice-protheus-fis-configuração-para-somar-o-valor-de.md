---
article_id: 4407012016279
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 5756aa9e92570b24b4273cb64c9871f601d76c23c33f326901fe7c584e0a0ade
fetched_at: '2026-06-28T22:39:36.804868+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice - Protheus - FIS - Configuração Para Somar
  o Valor de IPI e Deduzir o Valor do ICMS da Base de PIS/COFINS
type: support-article
updated_at: '2021-08-24T19:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407012016279-CROSS-Segmentos-TOTVS-Backoffice-Protheus-FIS-Configura%C3%A7%C3%A3o-Para-Somar-o-Valor-de-IPI-e-Deduzir-o-Valor-do-ICMS-da-Base-de-PIS-COFINS
---

**Dúvida**  
Como Configurar o sistema para somar o valor de IPI e Deduzir o Valor do ICMS da Base do PIS e COFINS?  
  
**Ambiente**  
Cross Segmento - TOTVS - Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
**Solução**  
Para o sistema realizar o cálculo desejado na nota de **saída** é necessário realizar os seguintes passos:  
1. Configurar os **parâmetros** abaixo:

**MV\_DEDBPIS**= S

**MV\_DEDBCOF**= S

2. Configure no TES o campo **Credita IPI (F4\_CREDIPI) = NÃO** - O sistema vai somar o **IPI** na base do **Pis/Cofins;**

OBS: É necessário ter o calculo de **ICMS** e **IPI** no **TES**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407018775063/mceclip0.png)

3. Para o sistema realizar o cálculo para nota de **entrada** é necessário realizar os seguintes passos:

4. Configurar os **parâmetros** abaixo:

**MV\_DEDBPIS**= S

**MV\_DEDBCOF**= S

5. Configure no **TES** o campo **Credita IPI (F4\_CREDIPI) = NÃO -** O sistema vai somar o **IPI** na base do **Pis/Cofins;**

OBS: É necessário ter o calculo de **ICMS** e **IPI** no **TES**;

6. Configurar o cadastro do **fornecedor** campo **Ded. PIS/COF (A2\_DEDBSPC) =** **1 - Legado**: Deduz conforme os parâmetros **MV\_DEDBPIS** e **MV\_DEDBCOF**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407019025815/mceclip1.png)
