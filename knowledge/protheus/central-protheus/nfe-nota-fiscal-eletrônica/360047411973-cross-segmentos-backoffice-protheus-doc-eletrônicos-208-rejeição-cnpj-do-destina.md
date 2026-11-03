---
article_id: 360047411973
category: NFe - Nota Fiscal Eletrônica
content_hash: d2ef6c8be0496fbaf230d77482f61ae1a87019bda183dd452e0d398e4e24530b
fetched_at: '2026-06-28T22:40:03.763665+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 208 Rejeição :
  CNPJ do destinatário inválido'
type: support-article
updated_at: '2025-06-18T14:35:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047411973-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-208-Rejei%C3%A7%C3%A3o-CNPJ-do-destinat%C3%A1rio-inv%C3%A1lido
---

**Dúvida**Como solucionar a Rejeição 208 : CNPJ do destinatário inválido   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

 Nesta rejeição será realizada a verificação do **CNPJ do destinatário e a Inscrição Estadual**

A Sefaz não permite  **CNPJ com zeros** ou **dígito de controle inválido**

* Exemplo o XML gerou conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067364974)

* **O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

* **Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

* Para a solução da rejeição realize os seguintes passos:

1- Consulte o **Cadastro de Centralizado de Contribuinte** do link acima.

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13233734314519)

2- Acessar o cadastro de cliente ou fornecedor alterar o CNPJ ou IE do destinatário.

* **CNPJ Cliente e Inscrição estadual**

![cnpj_e_ie_cliente.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10960767221783)

* **CNPJ Fornecedor e Inscrição estadual**

![cnpj_e_ie_forn.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10961301888279)

3- Após isso, exclua a nota e gere novamente.

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067366974)**
