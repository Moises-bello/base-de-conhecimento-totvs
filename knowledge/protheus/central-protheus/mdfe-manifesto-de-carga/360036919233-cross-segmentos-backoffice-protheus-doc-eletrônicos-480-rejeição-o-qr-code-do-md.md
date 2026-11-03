---
article_id: 360036919233
category: MDFe - Manifesto de Carga
content_hash: b7e52750610c36fbf7b4eacd25cacfe30f53cffb84e4393d19d0cd43e0efca86
fetched_at: '2026-06-28T22:40:08.104075+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 480 Rejeição: O
  QR Code do MDF-e deve ser informado'
type: support-article
updated_at: '2025-06-17T18:46:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036919233-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-480-Rejei%C3%A7%C3%A3o-O-QR-Code-do-MDF-e-deve-ser-informado
---

**Dúvida**Como corrigir a rejeição 480 : O QR Code do MDF-e deve ser informado  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Desde o dia **07/10/2019** é obrigatório gerar o **QR Code.** O sistema gera o **QR Code** de forma automático. 

* Exemplo **DAMDFE:**

![mdfe_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047665494)

* **Protheus:**

Aplicar **Patch do link abaixo**, compilar o RDMAKE do MDFe **(MDFSEFAZ e o DAMDFE) :**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

**Realizar atualização do TSS:**

[TSS Transmissão de Documentos Eletrônicos - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

[TSS - Atualização dos schemas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**Importante:**

Para gerar o **QR Code corretamente** é necessário, após as atualizações **excluir o MDF-e** e **gerar** **novamente** e só, após isso **transmitir.**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048488213)**

* **Conforme o MOC MDF-e versão 3.0:** ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32714118466711)
