---
article_id: 360062861993
category: NFe - Nota Fiscal Eletrônica
content_hash: 1fe028a47a4ac4605cc302a38cf5fde7e335092d7e16a3dd4a5920a32d7aed67
fetched_at: '2026-06-28T22:40:03.204856+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  437 Rejeição :
  CNPJ da instituição de pagamento inválido '
type: support-article
updated_at: '2021-07-05T19:29:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062861993-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-437-Rejei%C3%A7%C3%A3o-CNPJ-da-institui%C3%A7%C3%A3o-de-pagamento-inv%C3%A1lido
---

**Dúvida**Como solucionar a rejeição abaixo:

437 Rejeição : CNPJ da instituição de pagamento inválido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informado **o CNPJ da instituição de pagamento** Verificar **CNPJ com zeros, nulo ou DV inválido**

1- Se a nota foi realizada pelo **módulo do loja** preencher no cadastro de cliente o campo **CNPJ/CPF  "A1\_CGC" no cadastro de cliente com CNPJ correto.**

![A1_CGC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002383362/A1_CGC.gif)

2- Após isso, **exclua a nota e gere novamente.**

* **Importante:**

Se gerada pelo faturamento como não há tratamento padrão será necessário revisar a customização da empresa.

A utilização do ponto de entrada **PE01NFESEFAZ.**

Segue link com exemplo:

[PE01NFESEFAZ - Manipulação em dados do Grupo Detalhamento da Forma de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=348298539)

* **Validação da Sefaz:**

![437_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360103429733/437_rejeicao.JPG)
