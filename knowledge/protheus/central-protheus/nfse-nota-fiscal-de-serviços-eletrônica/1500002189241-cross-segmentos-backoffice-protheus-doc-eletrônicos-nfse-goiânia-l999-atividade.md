---
article_id: 1500002189241
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: eaab6507be4e13642fa6d7833e6ff8f100e0b8ec0cf38c520e93860b6f917782
fetched_at: '2026-06-28T22:39:57.475377+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Goiânia:
  L999 - ATIVIDADE ECONOMICA NAO NUMERICA'
type: support-article
updated_at: '2025-07-08T19:37:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002189241-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Goi%C3%A2nia-L999-ATIVIDADE-ECONOMICA-NAO-NUMERICA
---

**Ocorrência**Ao realizar a transmissão de um RPS para a prefeitura de Goiânia-GO ocorre a rejeição: ***L999 - ATIVIDADE ECONOMICA NAO NUMERICA.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002075262/mceclip1.png)***  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**A rejeição ocorre por conta da atividade econômica (código de tributação do município) possuir pontuação, exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002133581/mceclip0.png)  
  
**Solução**Para correção deverá informar o conteúdo totalmente numérico, sem pontos e traços no Cadastro do Produto (**B1\_TRIBMUN**) ou caso utilize Indicador de Produtos (**BZ\_TRIBMUN**).  
  
Exemplo em relação ao print acima: 1705
