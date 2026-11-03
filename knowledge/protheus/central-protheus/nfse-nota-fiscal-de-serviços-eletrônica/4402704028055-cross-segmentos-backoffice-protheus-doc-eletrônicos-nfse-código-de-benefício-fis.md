---
article_id: 4402704028055
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 443665bef521b12b0b7cfc237e8f4680b0de1d6b37dda8f8706b044b4ba73e73
fetched_at: '2026-06-28T22:39:56.354354+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Código de
  Benefício Fiscal (Rio de Janeiro)
type: support-article
updated_at: '2021-06-15T14:52:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402704028055-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-C%C3%B3digo-de-Benef%C3%ADcio-Fiscal-Rio-de-Janeiro
---

**Dúvida**Como informar o Código de Benefício Fiscal no XML ou TXT para a prefeitura do Rio de Janeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para informar o Código de Benefício Fiscal, deverá criar e configurar o parâmetro **MV\_BENEFRJ:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402704315287/mceclip0.png)**Nele precisará informar um campo que deve ser criado manualmente na SF4, o qual será o responsável por receber essa informação.  
  
Exemplo: Criado o campo F4\_EXEMPLO, logo o conteúdo do parâmetro deverá ser MV\_BENEFRJ = 'F4\_EXEMPLO'.  
  
*Detalhes das propriedades do campo que deverá ser criado na tabela SF4:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402696020503/mceclip1.png)*  
  
Segue a relação completa dos Códigos de Benefício Fiscal disponibilizados pela própria prefeitura do Rio de Janeiro: **[clique aqui.](https://notacarioca.rio.gov.br/files/manuais/beneficios.pdf)**
