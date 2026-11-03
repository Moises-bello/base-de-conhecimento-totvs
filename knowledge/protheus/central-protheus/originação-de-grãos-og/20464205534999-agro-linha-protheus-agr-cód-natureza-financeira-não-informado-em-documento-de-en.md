---
article_id: 20464205534999
category: Originação de Grãos (OG)
content_hash: 06089c2d0b17f5cc32df71efe001c4414cdc9249c8059aac9dd50c85d1b8b0f2
fetched_at: '2026-06-28T22:45:37.527164+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Cód natureza financeira não informado em Documento
  de entrada
type: support-article
updated_at: '2025-06-24T20:47:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20464205534999-Agro-Linha-Protheus-AGR-C%C3%B3d-natureza-financeira-n%C3%A3o-informado-em-Documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20464205512855) Tempo aproximado para leitura: **00:01:25 min** **Dúvida**Gerar documento de entrada é apresentado alerta de o código da natureza financeira não foi informado?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para solucionar essa ocorrência é necessário inserir no parâmetro **MV\_2DUPNAT** a informação   
**SA2->A2\_NATUREZ**.

![FIG1224.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/20464220574871)

É necessário que a natureza seja informada no cadastro do fornecedor.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20464220577559)

**Importante**A natureza informada no contrato é utilizada para a previsão financeira e não é passada para o título de compra.  
  
**Saiba mais**Para mais informações acerca do parâmetro**MV\_2DUPNAT** acesse a documentação:  
[Integração com o Módulo Financeiro](http://tdn.totvs.com/pages/releaseview.action?pageId=6085174)
