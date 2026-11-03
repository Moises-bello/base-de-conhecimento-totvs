---
article_id: 360061290834
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 0584eaba7ba6b11674d473b88f165e27f996863a3454ca6d7aa2541c3cc677e9
fetched_at: '2026-06-28T22:39:57.652791+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Quebra de
  Linhas na Discriminação de Serviços (Vitória/ES)
type: support-article
updated_at: '2025-06-25T21:05:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061290834-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Quebra-de-Linhas-na-Discrimina%C3%A7%C3%A3o-de-Servi%C3%A7os-Vit%C3%B3ria-ES
---

**Dúvida**Como realizar a quebra de linhas na discriminação de serviço para a prefeitura de Vitória/ES?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**De acordo com o manual de integração Web Service da prefeitura de Vitória ([link](https://nfse.vitoria.es.gov.br/arquivos/docs/NFSE-NACIONAL_Manual_De_Integrao%20verso%202-01.pdf)), a quebra de linhas se dá pelo uso dos seguintes caracteres: **\s\n   
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101529334/mceclip3.png)**Segue um exemplo abaixo onde os caracteres foram inseridos dentro do espaço do campo MEMO no Pedido de Vendas, através da configuração [(citada aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012315132-MP-NFSE-Discrimina%C3%A7%C3%A3o-de-Servi%C3%A7o-com-mais-de-250-caracteres) e o resultado final na visualização da nota impressa em PDF: **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002645722/mceclip2.png)**
