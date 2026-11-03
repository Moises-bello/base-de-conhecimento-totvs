---
article_id: 360062302434
category: PMS - Integrações
content_hash: b3963ce7cce8321dc578938897e9ceda2b3746c592566994eb09e6bb911cc612
fetched_at: '2026-06-28T22:37:16.747407+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: MP - PMS - Integração Proposta Comercial X PMS, não preenche o valor do projeto
  (ADZ_PRCVEN)
type: support-article
updated_at: '2021-04-28T15:59:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062302434-MP-PMS-Integra%C3%A7%C3%A3o-Proposta-Comercial-X-PMS-n%C3%A3o-preenche-o-valor-do-projeto-ADZ-PRCVEN
---

**Dúvida**

Quando copio um orçamento de Projeto na Proposta Comercial (CRM), não traz o preço unitário do campo AF3\_CUSTD para o preço unitário da Proposta (ADZ\_PRCVEN), o preço fica em branco.

![proposta.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360102821594/proposta.PNG)  
  
**Ambiente**  
Protheus – Gestão de Projeto / CRM – A partir da versão 12.5  
  
**Solução**

Para que o sistema considere o valor do Orçamento de Projeto na Proposta Comercial, o parâmetro **MV\_ORCSPMS deve estar configurado como .T.**

Com essa configuração o sistema considera o Preço Unitário informado no campo **AF3\_CUSTD** ( Tarefa do Orçamento).

**Saiba mais sobre está integração:**

**<https://tdn.totvs.com/pages/releaseview.action?pageId=540894822>**
