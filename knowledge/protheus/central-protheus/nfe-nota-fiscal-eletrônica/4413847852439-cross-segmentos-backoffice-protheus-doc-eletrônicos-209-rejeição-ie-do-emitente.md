---
article_id: 4413847852439
category: NFe - Nota Fiscal Eletrônica
content_hash: 49ee10463611629754728b0e86402134821c21e74e8d69696d06dbba8c7aae97
fetched_at: '2026-06-28T22:40:03.163698+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  209 Rejeição :
  IE do emitente inválido'
type: support-article
updated_at: '2025-06-18T14:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413847852439-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-209-Rejei%C3%A7%C3%A3o-IE-do-emitente-inv%C3%A1lido
---

**Dúvida**Como corrigir a rejeição 209 Rejeição : IE do emitente inválido ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Conforme o ***exemplo abaixo, verificar se o IE está correto no grupo do emitente:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413864320919)

2. O retorno da Sefaz pode ocorrer, por exemplo quando o destinatário possui uma ***IE ISENTA, IE diferente do Sintegra*** ou devido à uma inconsistência de Cadastro junto à SEFAZ.

* ***O correto para Sefaz é consultar o CCC:***

Verificação se a IE do emitente ou do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização ***(SEFAZ Autorizadora ou SEFAZ Virtual);***

* **Cadastro Centralizado de Contribuinte (CCC):**

*[Clique Aqui](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)*

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12887360079127)

* ***Saiba mais:***

Essa rejeição é um retorno da ***Sefaz**,* ou seja caso o XML tenha gerado com a ***IE*** do emitente correto, será necessário entrar em contato com a Sefaz.

* ***Validação da Sefaz:***

***![209_rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4413847648791)***
