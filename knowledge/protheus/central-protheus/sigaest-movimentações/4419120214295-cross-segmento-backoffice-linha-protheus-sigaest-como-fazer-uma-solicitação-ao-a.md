---
article_id: 4419120214295
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 96da9f9244f246b8cff997d9aa824d02d0accc4b110cad6c856bdb3e69f06fa4
fetched_at: '2026-06-28T22:38:54.407990+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como fazer uma Solicitação
  ao Armazém com Autorização de Entrega?
type: support-article
updated_at: '2022-07-18T12:22:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419120214295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-fazer-uma-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-com-Autoriza%C3%A7%C3%A3o-de-Entrega
---

**Dúvida**Existe a possibilidade de ao fazer uma Solicitação ao Armazém, que gere Autorização de Entrega (AE) em vez de Solicitação de Compra (SC)?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Sim, existe a possibilidade e para isso somente basta configurar conforme o passo a passo abaixo:

1. Criar ou editar no Cadastro de Produto (MATA010) e preencher os seguintes campos **B1\_CONTRAT = SIM** e **B1\_PROC** com código do fornecedor padrão, conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419111659287/mceclip0.png)

2. Acessar a rotina de Contrato de Parceria (MATA125) e colocar o código fornecedor que está no campo B1\_PROC e inserir o produto e a quantidade desejada:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419104281239/mceclip1.png)

**Observação**: Caso tenhas dúvidas sobre a rotina de Contrato de Parceria, favor verificar com o time de Suporte Padrão Compras.

3. Efetuar uma Solicitação ao Armazém (MATA105) com quantidade desejada e o armazém correto:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419104347159/mceclip2.png)

4. Ao concluir a criação da Solicitação ao Armazém, acessar a rotina Gerar Pré-Requisição (MATA106),pressione a tecla **F12** com o parâmetro destacado abaixo com conteúdo "**SIM**" e clicar em **OK**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419111757207/mceclip3.png)

5. Selecionar o item em questão e colocar para "Gerar" e clicar em OK.

6. Após isso acessar a rotina Autorização de Entrega (MATA122) e verá foi gerado a Autorização de Entrega da Solicitação ao Armazém:

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419104539671/image.png)

**Saiba mais:**

*[MP - SIGAEST - Solicitação, Pré-Requisição e Baixa da Pré-Requisição - MATA105 - MATA106 - MATA185](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-MP-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185)*

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
