---
content_hash: 40b9c2d18ba4f3c2770a2f3cc1e94c0fb7379863c280a5c73421a26bb118486c
fetched_at: '2026-06-29T00:09:37.138696+00:00'
page_id: '425459566'
product: rm
source: tdn-rm
title: Apropriação - Pedido de Material
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459566
version: 2
---

**Apropriação - Pedido de Material**

---

Ao gerar um pedido no TOP, como mostrado no processo Geração de Pedidos em Suprimentos, é gerado no Protheus uma Solicitação de Armazém. A partir deste ponto é possível realizar a apropriação pela nota fiscal ou pela baixa, como demonstrado no fluxo a seguir.  
    
   
    
 *Observações do fluxo:*

* No **Pedido de Compra**, é possível gerar N Pedidos de Compra para atender a mesma Solicitação de Compra (Parcial). • No Documento de Entrada, podem ser geradas N Notas para atender a um mesmo pedido. E uma nota pode atender a um pedido parcialmente.
* Na **Baixa Pré-Requisição**, podem ser geradas N Baixas de uma mesma Pré-Requisição (Solicitação de Compra) e a baixa pode ser parcial. Também é possível estornar parcialmente.
* Em **Novos Movimentos Apropriados**, os novos movimentos gerados podem ser visualizados: Relatórios Periódicos, Cronograma Apropriado ou pela rastreabilidade de pedidos.
* **Estoq/custo** é um parâmetro que define se a apropriação dos custos da Obra/Tarefas será realizada na entrada da Nota Fiscal de Compra (através do preço da NF) ou na baixa de estoque (através do custo na modalidade do Protheus).

Ao digitar uma nota fiscal de entrada no sistema, clique no botão "Projeto" . Será exibida a tela "Assistente de Apontamentos - Gerenciamento de Projetos". Quando informado o valor "Não" no campo, não ocorrerá apropriação. Ao informar o valor "Sim", ocorrerá apropriação no TOP. O Protheus enviará o movimento (NF ou Baixa) para o TOP com o parâmetro Apropriado marcado ou não, conforme o caso. O processo de apropriação no TOP não se altera.  
    
 **Apropriação através da Baixa de Requisição:**  
    
 1. Gerar uma pré-requisição. Acesse: Protheus | SigaEst | Atualizações | Estoques | Gera Pré Requisição  
    
 *Observação:* Apenas se o pedido gerado no TOP for do tipo Requisição de Compra, não é necessário realizar o passo 1, pois a pré-requisição (Solicitação de Compra) já terá sido gerada.   
    
 2. Realizar a baixa da requisição. Acesse: Protheus | SigaEst | Atualizações | Estoques | Baixa Pré Requisição  
    
 *Observações:*

* Necessário preencher os campos Quantidade a requisitar e Qtd Baixa.
* Informe o movimento (obrigatoriamente código 501) e o custo. Como visto no módulo Parâmetros, é obrigatório existir cadastro do tipo saída com código 501.

3. Após informar o tipo de movimento, será informado que existe uma SC para esta pré-requisição. Clique em ajustá-la. A baixa foi realizada.  
    
 4. Neste ponto, já foi gerada a apropriação. Para visualizar no TOP, selecione o pedido e acesse: Anexo | Movimento. O Status que anteriormente estava como pendente, agora esta como parcialmente quitado. O Cronograma da tarefa é alterado, constando o valor apropriado dos materiais.  
    
 *Observação:*

* O faturamento ou a baixa da Solicitação de Armazém (SA) no Protheus gera uma atualização do status da Solicitação de Compra (SC) original no TOP. Neste momento a SC é atualizada referente a definição e valores de apropriação, além de bloquear a possibilidade de exclusão desta SC no TOP.
* Existe um Anexo no RM chamado Consulta SQL. Através deste recurso é possível incluir um anexo com uma consulta qualquer que inclusive pode consultar uma base de dados externa, como por exemplo, obter as informações de Notas e Baixas feitas no Protheus relacionadas aos Pedidos no TOP.

A consulta SQL pode ser distribuída, via arquivo exportado, ou podemos incluir ela diretamente na base, ou ainda o usuário pode criar ela pela própria interface.Para visualizar no TOP o que ocorre com o pedido no Destino (Protheus) acesse: Anexo | Consulta SQL | Inserir Consulta SQL  
    
 **Apropriação através da Nota Fiscal:**  
    
 1.Selecionar a SA e gerar uma pré-requisição. A pré-requisição irá gerar uma Solicitação de Compra. Acesse: Protheus | SigaFat | Atualizações | Estoques | Gera Pré Requisição  
    
 *Observação:* Apenas se o pedido gerado no TOP for do tipo Requisição de Compra, não é necessário realizar o passo 1, pois a pré-requisição (Solicitação de Compra) já terá sido gerada.  
    
 2. Cadastrar um pedido de compra associado a solicitação de compra criada. Acesse: Protheus | SigaFat | Atualizações | Estoques | Baixa Pré Requisição  
    
 *Observações:*

* Selecione a solicitação de compra através do ícone "Solicit".
* Necessário preencher os campos Preço Unitário e Valor Total do produto.
* Será informado que o Armazém não existe, e se deseja criar. Clique em Sim. Como visto no módulo Cadastros, os almoxarifados no Protheus são criados à medida que são referenciados pela primeira vez.

3. Cadastrar um documento de entrada associado ao pedido de compra criado. Acesse: Protheus | SigaFat | Atualizações | Movmtos. Internos | Documento Entrada  
    
 *Observações:*

* Selecione o pedido de compra através do ícone "Pedido".
* Preencha os campos Tp. Oper e Tipo Entrada de todos os itens.
* Clique no ícone "Projetos" e preencha o campo Estoq./custo com valor "Sim".

No momento que é salvo o Documento de Entrada é atualizado o cronograma no item apropriado
