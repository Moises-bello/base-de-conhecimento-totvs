---
article_id: 1500002432121
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7bcbb08c6c941369c424c73b9b898a54fff96efd702cd5000f013d8b8dc63723
fetched_at: '2026-06-28T22:39:57.350686+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E180 - Base
  de Cálculo informada incorretamente
type: support-article
updated_at: '2025-07-08T19:56:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002432121-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E180-Base-de-C%C3%A1lculo-informada-incorretamente
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre a rejeição: " E180 - Base de Cálculo informada incorretamente".  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre por conta do cálculo na tag <BaseCalculo> não bater com o calculo esperado pela prefeitura:  
  
"BaseCalculo= *Valor de Serviços - Valor Deduções - Desc. Incondicionados".*  
  
Normalmente pelo fato da ausência de tags como Valor de Deduções ou Descontos Incondicionados, não justificando a diferença de valores:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101250114/mceclip2.png)  
  
Exemplo Autorizado:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002404861/mceclip3.png)  
  
Exemplo Rejeitado:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103413093/mceclip4.png)  
 **Solução**Quando o valor da base de cálculo sofrer qualquer tipo de dedução/desconto, **é necessário evidenciar essa diferença** através de tags específicas:  
  
Caso seja <**ValorDeducoes**>, habilitar o parâmetro: [MP - NFSE - Parâmetro MV\_NFSEDED (Valor de Dedução de Base de Cálculo no XML)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017924151-MP-NFSE-Par%C3%A2metro-MV-NFSEDED-Valor-de-Dedu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-no-XML-?source=search)  
  
Caso seja <**DescontoIncondicionado**>, habilitar o parâmetro: [MP - NFSE - MV\_NFSEDIN (Desconto Incondicionado)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047531273-MP-NFSE-MV-NFSEDIN-Desconto-Incondicionado-?source=search)  
  
*Obs.: Os valores nessas tags são montadas com bases em valores fiscais já prontos nas tabelas, exemplos: D2\_DESCON, F3\_ISSSUB e/ou F3\_ISSMAT.*
