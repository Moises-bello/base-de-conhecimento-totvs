---
article_id: 24474334934295
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: b1036dc128cfe812ce6f69c31d568b8c14b8c8e8f48459d59aa643c79e532f02
fetched_at: '2026-06-28T22:39:58.651551+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE DESTAQUE DE
  FÓRMULA (C5_MENPAD)
type: support-article
updated_at: '2025-05-29T11:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24474334934295-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DESTAQUE-DE-F%C3%93RMULA-C5-MENPAD
---

**Dúvida**Como destacar em **Informações Complementares** o conteúdo do campo C5\_MENPAD criado por fórmula?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A fórmula com o texto deve ser criada conforme exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24474334898839)

Essa fórmula deve ser inserida no campo C5\_MENPAD:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24474321008535)

Os parâmetros devem possuir os conteúdos abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24474334905239)

Dessa forma, a tag Descricao do XML será gerada com a descrição do CODISS conforme tabela 60 (SX5) e a InformacoesComplementares irá destacar a fórmula:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24474334909463)

**Importante:**

Caso o campo Mens.p/nota (C5\_MENNOTA) esteja preenchido, o conteúdo será concatenado em InformacoesComplementares, ficando C5\_MENNOTA + Fórmula.
