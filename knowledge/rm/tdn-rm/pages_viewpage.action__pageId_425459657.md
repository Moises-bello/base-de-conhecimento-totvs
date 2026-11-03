---
content_hash: 7612f2dc5b50b56aba804aa4c66058af626e2f9ddc1d056d6ad385ecedaf45c8
fetched_at: '2026-06-29T00:09:37.938707+00:00'
page_id: '425459657'
product: rm
source: tdn-rm
title: Apropriação - Solicitação de Armazém Avulsa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459657
version: 2
---

**Apropriação - Solicitação de Armazém Avulsa**

---

Para incluir uma solicitação de armazém avulsa no Protheus, acesse: Protheus | SigaEst | Atualizações | Estoques | Solicitação de Armazém.  Vincule o Projeto e a Tarefa desejados à solicitação que está sendo criada, através do ícone Projetos. Após salvar os dados informados, será gerada uma SA Avulsa.  
     
 **Apropriação através da Baixa de Requisição**  
    
 1. Gerar uma pré-requisição. Acesse: Protheus | SigaEst | Atualizações | Estoques | Gera Pré Requisição  
2. Realizar a baixa da requisição. Acesse: Protheus | SigaEst | Atualizações | Estoques | Baixa Pré Requisição  
    
 *Observações:*

* Necessário preencher os campos Quantidade a requisitar e Qtd Baixa.
* Informe o movimento (obrigatoriamente código 501) e o custo. Como visto no módulo Parâmetros, é obrigatório existir cadastro do tipo saída com código 501.

3. Após informar o tipo de movimento, será informado que existe uma SC para esta pré-requisição. Clique em ajustá-la. A baixa foi realizada.  
    
 4. Neste ponto, já foi gerada a apropriação. Para visualizar no TOP, selecione o pedido e acesse: Anexo | Movimento. O Status que anteriormente estava como pendente, agora esta como parcialmente quitado. O Cronograma da tarefa é alterado, constando o valor apropriado dos materiais.  
    
 ***Observação:***

* O faturamento ou a baixa da Solicitação de Armazém (SA) no Protheus gera uma atualização do status da Solicitação de Compra (SC) original no TOP. Neste momento a SC é atualizada referente a definição e valores de apropriação, além de bloquear a possibilidade de exclusão desta SC no TOP.
* Existe um Anexo no RM chamado Consulta SQL. Através deste recurso é possível incluir um anexo com uma consulta qualquer que inclusive pode consultar uma base de dados externa, como por exemplo, obter as informações de Notas e Baixas feitas no Protheus relacionadas aos Pedidos no TOP.

A consulta SQL pode ser distribuída, via arquivo exportado, ou podemos incluir ela diretamente na base, ou ainda o usuário pode criar ela pela própria interface.Para visualizar no TOP o que ocorre com o pedido no Destino (Protheus) acesse: Anexo | Consulta SQL | Inserir Consulta SQL  
    
    
 **Apropriação através da Nota Fiscal**  
    
 1. Selecionar a SA e gerar uma pré-requisição. A pré-requisição irá gerar uma Solicitação de Compra. Acesse: Protheus | SigaFat | Atualizações | Estoques | Gera Pré Requisição  
2. Cadastrar um pedido de compra associado a solicitação de compra criada. Acesse: Protheus | SigaFat | Atualizações | Estoques | Baixa Pré Requisição  
    
 ***Observações:***

* Selecione a solicitação de compra através do ícone "Solicit".
* Necessário preencher os campos Preço Unitário e Valor Total do produto.
* Será informado que o Armazém não existe, e se deseja criar. Clique em Sim. Como visto no módulo Cadastros, os almoxarifados no Protheus são criados à medida que são referenciados pela primeira vez.

3. Cadastrar um documento de entrada associado ao pedido de compra criado. Acesse: Protheus | SigaFat | Atualizações | Movmtos. Internos | Documento Entrada  
    
 ***Observações:***

* Selecione o pedido de compra através do ícone "Pedido".
* Preencha os campos Tp. Oper e Tipo Entrada de todos os itens.
* Clique no ícone "Projetos" e preencha o campo Estoq./custo com valor "Sim".

No momento que é salvo o Documento de Entrada é atualizado o cronograma no item apropriado
