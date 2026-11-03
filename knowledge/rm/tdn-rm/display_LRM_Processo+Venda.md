---
content_hash: 25bbc9e165aa96e2c136632e334539d1ffe8a0735f14a1039153a736591493c5
fetched_at: '2026-06-29T00:09:34.737357+00:00'
page_id: '425459244'
product: rm
source: tdn-rm
title: Processo Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Venda
version: 2
---

**Processo Venda**

---

No processo Venda é incluída uma oportunidade no MS CRM e sincronizado para a Linha RM gerando uma venda.  
    
 **Observações:**

* Uma Oportunidade no MS CRM pode gerar uma Venda ou um Movimento (Tipo parametrizável) no RM. A diferença entre os dois é que a Venda possui uma **Proposta** relacionada, e o Movimento não. Na aba Empreendimento da Oportunidade, vincule a Proposta desejada**. É esta proposta que caracteriza a oportunidade gerar uma venda no RM.**
* No caso da Venda, além de outras informações, na oportunidade devem constar o Cliente/Fornecedor, o Empreendimento, Unidade (Torre), Sub-unidade (Unidade/Imóvel) e Modalidade. Assim é necessário que estes cadastros já existam no RM e tenham sido sincronizados para o MS CRM, para que o processo de venda funcione corretamente.
* O processo sempre gera uma venda com status Em Preparação.
* Quando a venda é gerada no RM, o identificador desta venda é retornado para a oportunidade no MS CRM.
* A sincronização é realizada através do botão "**Lançamento de Movimentos CRM --> Linha RM**", que se encontra na tela de Orpotunidade no MS CRM. Após realizar a inclusão do pedido basta clicar neste botão para que o sincronismo seja realizado.
* O processo ocorre exclusivamente do MS CRM para a Linha RM. Inclusões e/ou alterações realizadas na Linha RM não serão sincronizadas para o MS CRM.
* Uma determinada oportunidade no MS CRM é sincronizada apenas uma vez para a Linha RM, gerando apenas uma venda. Alterações realizadas na oportunidade não serão sincronizadas.

Para realizar o processo de Venda no MS CRM, acesse MS CRM (4.0 ou 2011) | Vendas | Oportunidade

Para visualizar a venda no RM, acesse: Projetos | Imobiliário | Contratos | Contratos de Vendas e Aluguéis  
    
 **Dados Sincronizados**  
    
 Os dados sincronizados entre a Linha RM e o MS CRM referentes a este processo são:

* Número da Venda/Aluguel
* Código do Empreendimento
* Código do Cliente
* Data Venda
* Valor da Entrada
* Valor Total da Venda
* Código da Modalidade de Venda
* Código da Coligada
* Código Unidade
* Código Sub-Unidade

---

**Recursos Adcionais**

Acesse o link abaixo para mais detalhes deste cadastro:

- [Como Fazer: Processo de Venda no MS CRM](http://totvsconnect.blogspot.com.br/2012/09/como-fazer-processo-de-venda-no-ms-crm)
