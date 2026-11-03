---
content_hash: 366ad841ce8c8be0b24be6a7e3143ef2b2205fdb452e5d7fba405cbc920867a5
fetched_at: '2026-06-29T00:09:34.655293+00:00'
page_id: '425459213'
product: rm
source: tdn-rm
title: Processo Movimento Oportunidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Movimento+Oportunidade
version: 5
---

**Processo Movimento Oportunidade**

---

Além de uma Venda, uma Oportunidade também pode gerar um movimento.  
    
 No processo Movimento Oportunidade uma oportunidade é incluída no MS CRM e sincronizada para a Linha RM como um movimento, conforme o tipo informado na inclusão da oportunidade.  
    
 **Observações:**

* Pode ser informado qualquer tipo de movimento, desde que seus parâmetros estejam de acordo com os dados sincronizados deste processo.

Por exemplo, não é possível informar um tipo de movimento que contenha campos obrigatórios que não estão fazem parte do dados sincronizados. Caso seja informado este tipo de movimento a sincronização no ocorrerá como esperado.  
    
 Agora, um tipo de movimento que tenha campos obrigatórios apenas os que são contemplados na integração pode ser informado normalmente na Oportunidade.

* Quando o movimento é criado no RM, o identificador deste movimento é retornado para a oportunidade no MS CRM.
* A sincronização é realizada através do botão "**Lançamento de Movimentos CRM --> Linha RM**", que se encontra na tela de Oportunidade no MS CRM. Após realizar a inclusão do pedido basta clicar neste botão para que o sincronismo seja realizado.
* O processo ocorre exclusivamente do MS CRM para a Linha RM. Inclusões e/ou alterações realizadas na Linha RM não serão sincronizadas para o MS CRM.
* No caso da oportunidade (movimento), além de outras informações, devem constar na oportunidade o Cliente/Fornecedor e o Produto. Assim é necessário que estes cadastros já existam no RM e tenham sido sincronizados para o MS CRM, para que este processo fucione corretamente.
* Uma determinada oportunidade no MS CRM é sincronizado apenas uma vez para a Linha RM. Alterações realizadas no pedido não serão sincronizadas.

Para realizar o processo de Movimento Oportunidade, acesse: MS CRM (4.0 ou 2011) | Vendas | Oportunidade

Para visualizar os movimentos criados no RM, acesse:RM | BackOffice | Gestão de Estoques, Compras e Faturamento

Após acesse conforme o tipo de movimento informado.   
     
 **Dados Sincronizados**  
    
 Os dados sincronizados da Linha RM para o MS CRM referentes a este cadastro são:

* Código da Coligada
* Código do Cliente/Fornecedor
* Código do Tipo de Movimento
* Filial do Movimento
* Identificador do Movimento \*\*
* Código da Filial

*\*\* O Identificador do Movimento é retornado pelo RM quando o Movimento é criado no mesmo.*  
    
 Referente ao Item (Produto) da Oportunidade:

* Identificador do Movimento
* Identificador do Item do Movimento
* Quantidade
* Preço Unitário
* Valor do Desconto

---

**Recursos Adicionais:**

Acesse o link abaixo para mais detalhes deste cadastro:

- [Como Fazer: Processo Movimento Oportunidade no MS CRM](http://totvsconnect.blogspot.com.br/2012/09/como-fazer-processo-movimento)
