---
article_id: 360042517933
category: NFe - Nota Fiscal Eletrônica
content_hash: 53a110d063a9629cda7260b885cfbd7129239040d1aecf9e666fffc6681fdffa
fetched_at: '2026-06-28T22:40:07.134441+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 391 e
  392: Não informados os dados da operação de pagamento por cartão de crédito / débito'
type: support-article
updated_at: '2026-04-04T04:32:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042517933-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-391-e-392-N%C3%A3o-informados-os-dados-da-opera%C3%A7%C3%A3o-de-pagamento-por-cart%C3%A3o-de-cr%C3%A9dito-d%C3%A9bito
---

**Dúvida**Como corrigir a rejeição abaixo:

392 Rejeição : Não informados os dados da operação de pagamento por cartão de crédito / débito

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Foi aberta a issue [DSERTSS1-27892](https://jiraproducao.totvs.com.br/browse/DSERTSS1-27892) para criação das forma de pagamento PIX e Cartão, caso esteja  com a rejeição 391 ou 392, abra um ticket com equipe suporte e solicite que o ticket seja associado a issue.

****Essa validação é  a critério da UF.****

Se o pagamento com cartão for integrado ao sistema de automação da empresa **(tag: tpIntegra=1)** devem ser informados os campos de **CNPJ da Credenciadora e o código de autenticação** da operação **(tag:card/CNPJ e card/cAut)**

* **Exemplo do XML gerado:**

**![](https://totvssuporte.zendesk.com/attachments/token/Qn8Q5x49biiUJZvujVNSZdUhh/?name=inline933504784.png)​**

* **Conforme a nota técnica 2016.​002\_v\_1.61 página 66:**  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/pY6M0xab9K9kvPtz7SjGrP9qt/?name=inline-371901508.png)​  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/FjH0bYFPU4Xxga9hnrOPN9Ixt/?name=inline369920662.png)​  
    
    
  ​  
    
    
  Se a nota foi realizada pelo módulo do loja entrar em contato com equipe Protheus automação comercial e solicitar as configurações.

* **Importante:**

Se gerada pelo faturamento como não há tratamento padrão será necessário revisar a customização da empresa.

A utilização do ponto de entrada **PE01NFESEFAZ.**

Segue link com exemplo:

[PE01NFESEFAZ - Manipulação em dados do Grupo Detalhamento da Forma de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=348298539)

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056902073)**
