---
article_id: 360024963133
category: NFe - Nota Fiscal Eletrônica
content_hash: 876a94466fe62625987f7c5a8a3e4ef24a44bd4ff61080316b59466010c736a5
fetched_at: '2026-06-28T22:40:00.297841+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar a
  mensagem do Suframa referente ao ICMS, PIS, COFINS '
type: support-article
updated_at: '2021-10-11T18:55:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024963133--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-mensagem-do-Suframa-referente-ao-ICMS-PIS-COFINS
---

**Dúvida**Como gerar a mensagem do Suframa referente ao ICMS, PIS, COFINS  ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Parametrô MV\_INFADZF:**

Para sair a mensagem dos três impostos

* **Icms**
* **Pis**
* **Cofins**

O parâmetro deve estar habilitado no configurador **MV\_INFADZF= .T.**

**Exemplo da mensagem:**

Descontos Ref. a Zona Franca de Manaus / ALC. ICMS - R$xx, PIS - R$ xx e COFINS - R$ xx

**Importante:**

Se o parâmetro estiver como **MV\_INFADZF= .F.**

**Será gerada mensagem conforme o exemplo abaixo:**

Descontos Ref. a Zona Franca de Manaus / ALC. ICMS - R$xx,
