---
article_id: 360018989171
category: NFe - Nota Fiscal Eletrônica
content_hash: 7229b6e0a8dee2f42f84bbccbbe9e1afe92f687a97a1b981eb5d34cbc77283d3
fetched_at: '2026-06-28T22:40:01.937297+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 291 Certificado
  - Assinatura Data de Validade'
type: support-article
updated_at: '2021-10-11T15:35:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018989171--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-291-Certificado-Assinatura-Data-de-Validade
---

**Dúvida**

Como corrigir a rejeição 291 Certificado - Assinatura Data de Validade ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Caso esteja com a rejeição 291 em seu ambiente e já foi configurado com o certificado digital valido no **Wizard Config** da rotina **SPEDNFE**, porem ainda permanece apresentando a rejeição 291 intermitente no seu ambiente, significa que no seu cenário está ocorrendo uma concorrência de serviços do **TSS**.

Lembrando que **não** pode haver **duas** estruturas do **TSS** separadas, apontando pasta mesma base de dados.

**Obs:** Estruturas do **TSS** distintas, significa que ha pastas estruturais diferentes, como: **Certs**, **APO(RPO)** ou **binário(appserver)**.

Caso tenha dificuldades em descobrir onde esta o segundo serviço pode ser identificado no **DBMONITOR** em “IP ORIGEM”, exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014600932/mceclip0.png)

Verifique pelos usuários, para o **TSS** sempre será denominado como “Totvs Service Gateway” e no comentário estará o **JOB** que está rodando e a entidade, no **IP Origem** ira demonstrar o Ip do servidor que está rodando o **TSS** e a porta do serviço.

Assim devera desativar o serviço do **TSS** que estiver rodando com o certificado digital vencido.
