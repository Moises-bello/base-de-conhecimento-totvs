---
content_hash: 06da06d07f0318ab748bd2bc8a52a8c077f314e4d2e3352162294a2f2d8c7abf
fetched_at: '2026-06-29T00:09:34.649580+00:00'
page_id: '425459211'
product: rm
source: tdn-rm
title: Processo Movimento Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459211
version: 3
---

**Processo Movimento Cotação**

---

No processo Movimento Cotação uma cotação é incluída no MS CRM e sincronizada para a Linha RM como um movimento, conforme o tipo informado na inclusão da cotação.  
    
 *Observações:*

* O tipo de movimento informado deve estar relacionado a Cotação. Por exemplo, informar o tipo de movimento de Solicitação de Compras.
* O tipo de movimento informado deve ter seus parâmetros no RM configurados de acordo com os dados sincronizados deste processo. Por exemplo, não é possível informar um tipo de movimento que contenha campos obrigatórios que não estão entre os dados sincronizados. Caso seja informado este tipo de movimento a sincronização no ocorrerá como esperado.
* Quando o movimento é criado no RM, o identificador deste movimento é retornado para a cotação no MS CRM.
* A sincronização é realizada através do botão "**Lançamento de Movimentos CRM --> Linha RM**", que se encontra na tela de Cotação no MS CRM. Após realizar a inclusão do pedido basta clicar neste botão para que o sincronismo seja realizado.
* O processo ocorre exclusivamente do MS CRM para a Linha RM. Inclusões e/ou alterações realizadas na Linha RM não serão sincronizadas para o MS CRM.
* No caso da cotação, além de outras informações devem constar no pedido o Fornecedor e o Produto. Assim é necessário que estes cadastros já existam no RM e tenham sido sincronizados para o MS CRM, para que este processo funcione corretamente.
* Uma determinada cotação no MS CRM é sincronizado apenas uma vez para a Linha RM. Alterações realizadas na cotação não serão sincronizadas.

Para realizar o processo de Movimento Cotação, acesse: MS CRM (4.0 ou 2011) | Vendas | Cotação   
    
 Para visualizar os movimentos criados no RM, acesse: RM | BackOffice | Gestão de Estoques, Compras e Faturamento  
 Após acesse conforme tipo de movimento informado. Neste exemplo: Compras | Solicitação de Compra  
     
 **Dados Sincronizados**  
    
 Os dados sincronizados da Linha RM para o MS CRM referentes a este cadastro são:

* Código da Coligada
* Código do Fornecedor
* Código do Tipo de Movimento
* Filial do Movimento
* Identificador do Movimento \*\*
* Código da Filial

*\*\* O Identificador do Movimento é retornado pelo RM quando o Movimento é criado no mesmo.*  
    
 Referente ao Item (Produto) da Cotação:

* Identificador do Movimento
* Identificador do Item do Movimento
* Quantidade
* Preço Unitário
* Valor do Desconto  

  ---

---

**Recursos Adicionais**

Acesse o link abaixo para mais detalhes deste cadastro:

- [Como Fazer: Processo Movimento Cotação no MS CRM](http://totvsconnect.blogspot.com.br/2012/09/como-fazer-processo-movimento-cotacao)
