---
article_id: 1500000308521
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 8d9586e4f683887ae2510a74010b5f6face09c5913e1d5452d2fe456a20fdfd8
fetched_at: '2026-06-28T22:39:56.371719+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - COMO CRIAR
  UMA ESPECIE PARA NFSE
type: support-article
updated_at: '2025-12-23T21:05:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000308521-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-COMO-CRIAR-UMA-ESPECIE-PARA-NFSE
---

**Dúvida**  
Como criar uma espécie para transmissão de NFSE?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**  
Para a transmissão da **Nota Fiscal de Serviços** é preciso configurar a série com a espécie **RPS,** tanto para Modelo Prefeitura quanto Modelo Nacional, com a particularidade de que pra segunda opção, a série deve ser de 1 à 999.  
  
A espécie deve ser configurada no parâmetro **MV\_ESPECIE**.  
No exemplo abaixo a série '**E'** é usada para emissão da NFS-e (Modelo Prefeitura), portanto essa série será configurada com a espécie RPS:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099208354)  
  
Com a espécie configurada corretamente, o campo **F3\_ESPECIE** será gravado conforme o parâmetro:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101438693)
