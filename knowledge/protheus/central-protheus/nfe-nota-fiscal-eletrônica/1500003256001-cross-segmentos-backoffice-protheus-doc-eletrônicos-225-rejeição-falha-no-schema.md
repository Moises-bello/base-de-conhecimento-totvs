---
article_id: 1500003256001
category: NFe - Nota Fiscal Eletrônica
content_hash: 786c1d33229f4ace58e3b7bbd6cfa090df0f222c7112399e06b40d34e6e83419
fetched_at: '2026-06-28T22:40:03.772786+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 225 Rejeição: Falha
  no Schema XML do lote de NFe'
type: support-article
updated_at: '2025-07-03T12:18:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003256001-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-225-Rejei%C3%A7%C3%A3o-Falha-no-Schema-XML-do-lote-de-NFe
---

**Dúvida**Como solucionar a rejeição 225 Rejeição: Falha no Schema XML do lote de NFe ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Rejeição pode ocorre **pelos motivos abaixo:**

* Espaços **entre as TAGs do XML**
* **Quebras de Linhas**
* Caracteres **especiais**
* Nome de **TAGs errados**
* Versão do XML diferente do esperado pelo **Web Servic**

**1 - Verifique** se há caracteres especiais conforme a documentação abaixo:

[MP - NFE - 029: Falha no schema do XML, com schema válido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049488234--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-no-schema-do-XML-com-schema-v%C3%A1lido)

**2- Além disso, o ambiente deve** estar atualizado com os links abaixo:

* **TSS:**

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

* **Protheus:**

[MP - NFE - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / NFSe / MDFe / MDe](https://suporte.totvs.com/portal/p/10098/download?e=1152113)

* **Validação da Sefaz:**

![225_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360104487873)
