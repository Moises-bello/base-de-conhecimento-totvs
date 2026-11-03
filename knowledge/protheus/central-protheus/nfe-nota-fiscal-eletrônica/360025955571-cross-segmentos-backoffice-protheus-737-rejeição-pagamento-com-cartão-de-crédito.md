---
article_id: 360025955571
category: NFe - Nota Fiscal Eletrônica
content_hash: 58dd83aa2b2a7f49fc76780a47fa5c69da3bd028bae1c6db96bed4217ba56f18
fetched_at: '2026-06-28T22:40:00.160975+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: '   Cross Segmentos - Backoffice Protheus - 737 Rejeição: Pagamento com cartão
  de crédito em sistema de automação não integrado'
type: support-article
updated_at: '2021-10-08T17:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025955571--Cross-Segmentos-Backoffice-Protheus-737-Rejei%C3%A7%C3%A3o-Pagamento-com-cart%C3%A3o-de-cr%C3%A9dito-em-sistema-de-automa%C3%A7%C3%A3o-n%C3%A3o-integrado
---

**Dúvida**Como corrigir a rejeição 737 Rejeição: Pagamento com cartão de crédito em sistema de automação não integrado ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao utilizar opção de pagamento com cartão de crédito a Sefaz espera 1 na TAG **tpIntegra** temos um tratamento no padrão pelo módulo do loja no qual a empresa deve possuir a integração​ com **TEF**.

* **Caso a empresa não utilize o loja deve utilizar o ponto de entrada para gerar o conteúdo:**  
    
  <http://tdn.totvs.com/pages/viewpage.action?pageId=348298539>

![](https://totvssuporte.zendesk.com/attachments/token/R0JNQABbR3ah83LnrRmDeEEca/?name=inline471183953.png)​​  
  
  
aadd(aDetPag,;  
{"03",; // Forma de pagamento  
550.00,; // Valor do Pagamento  
20.00,; //Troco  
"1",; // Tipo de Integração para pagamento //Opcional se levar deverá preencher os itens abaixo com valor ou "".  
"32331472001195",; //CNPJ da Credenciadora de cartão de crédito e/ou débito // Opcional  
"01",; //Bandeira da operadora de cartão de crédito e/ou débito //opcional  
"123456"}) //Número de autorização da operação cartão de crédito e/ou débito //opcional  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/ZStFA7FYtJFlGzlw1PpQTixDZ/?name=inline1302605577.png)​

* **Validação da Sefaz:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024936751/mceclip0.png)
