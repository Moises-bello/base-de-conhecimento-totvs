---
article_id: 26435540396183
category: MDFe - Manifesto de Carga
content_hash: 3505c63323ea522db12cd4989efe40001a97b8dc645a05ce3cc672f6e911d622
fetched_at: '2026-06-28T22:40:08.076411+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Rejeição
  213 CNPJ-Base do Emitente difere do CNPJ-Base do Certificado Digital para MDF-e
type: support-article
updated_at: '2025-06-10T18:59:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26435540396183-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-213-CNPJ-Base-do-Emitente-difere-do-CNPJ-Base-do-Certificado-Digital-para-MDF-e
---

**Dúvida**

Como resolver a Rejeição: 213 CNPJ-Base do Emitente difere do CNPJ-Base do Certificado Digital para MDF-e

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**A validação realizada pela Sefaz indica que o CNPJ do certificado está divergente do CNPJ emissor da nota. É necessário validar o CNPJ do certificado configurado. Essa validação pode ser realizada por meio das interfaces gráficas do TSS, conforme o procedimento descrito na documentação abaixo:

[Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Como visualizar detalhes do certificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26434711165847-TSS-TSSINTERFACE-Como-visualizar-detalhes-do-certificado)

**Observação:** Para clientes que possuem servidor alocado na Totvs, é imprescindível confirmar se o acesso ao smartclient do TSS é viável. Em caso de dúvidas, recomenda-se contatar a equipe de suporte.

Se o CNPJ indicado no XML corresponder ao CNPJ para o qual o certificado foi emitido pela certificadora, é necessário entrar em contato com a Sefaz para identificar a razão da rejeição.

Validação da Sefaz:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26435540380183)
