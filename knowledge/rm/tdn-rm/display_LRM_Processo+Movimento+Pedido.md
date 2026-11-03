---
content_hash: 55dd8c0a322eeb61f10136d0a8c864ef92c976c5da6e642aae05058bbc016f65
fetched_at: '2026-06-29T00:09:34.680702+00:00'
page_id: '425459219'
product: rm
source: tdn-rm
title: Processo Movimento Pedido
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Movimento+Pedido
version: 4
---

**Processo Movimento Pedido**

---

No processo Movimento Pedido um pedido é incluído no MS CRM e sincronizado para a Linha RM como um movimento, conforme o tipo informado na inclusão do pedido.  
    
 **Observações:**

* O tipo de movimento informado deve estar relacionado a Pedido. Por exemplo, informar o tipo de movimento de Pedido de Venda.
* O tipo de movimento informado deve ter seus parâmetros no RM configurados de acordo com os dados sincronizados deste processo.

Por exemplo, não é possível informar um tipo de movimento que contenha campos obrigatórios que não estão entre os dados sincronizados. Caso seja informado este tipo de movimento a sincronização no ocorrerá como esperado.

* Quando o movimento é criado no RM, o identificador deste movimento é retornado para o pedido no MS CRM.
* A sincronização é realizada através do botão "**Lançamento de Movimentos CRM --> Linha RM**", que se encontra na tela do Pedido no MS CRM. Após realizar a inclusão do pedido basta clicar neste botão para que o sincronismo seja realizado.
* O processo ocorre exclusivamente do MS CRM para a Linha RM. Inclusões e/ou alterações realizadas na Linha RM não serão sincronizadas para o MS CRM.
* No caso do pedido, além de outras informações devem constar no pedido o Cliente e o Produto. Assim é necessário que estes cadastros já existam no RM e tenham sido sincronizados para o MS CRM, para que este processo funcione corretamente.
* Um determinado pedido no MS CRM é sincronizado apenas uma vez para a Linha RM. Alterações realizadas no pedido não serão sincronizadas.

Para realizar o processo de Movimento Pedido, acesse: MS CRM (4.0 ou 2011) | Vendas | Pedidos

Para visualizar os movimentos criados no RM, acesse: RM | BackOffice | Gestão de Estoques, Compras e Faturamento

Após acesse conforme tipo de movimento informado. Neste exemplo: Vendas | Pedido de Venda  
    
 **Dados Sincronizados**  
    
 Os dados sincronizados da Linha RM para o MS CRM referentes a este cadastro são:

* Código da Coligada
* Código do Cliente
* Código do Tipo de Movimento
* Filial do Movimento
* Identificador do Movimento \*\*
* Código da Filial

*\*\* O Identificador do Movimento é retornado pelo RM quando o Movimento é criado no mesmo.*

Referente ao Item (Produto) do Pedido

* Identificador do Movimento
* Identificador do Item do Movimento
* Quantidade
* Preço Unitário
* Valor do Desconto

---

---

**Recursos Adicionais**

Acesse o link abaixo para mais detalhes deste cadastro:

- [Como Fazer: Processo Movimento Pedido no MS CRM](http://totvsconnect.blogspot.com.br/2012/09/como-fazer-processo-movimento-pedido-no)
