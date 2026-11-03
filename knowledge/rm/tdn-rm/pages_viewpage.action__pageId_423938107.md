---
content_hash: f399963ee6b0f8f1f452b8e3e68810101c1cc0cf21277bad2d7831d7a0e92360
fetched_at: '2026-06-29T00:09:25.299561+00:00'
page_id: '423938107'
product: rm
source: tdn-rm
title: Estorno do Item de Movimento (Integração Gestão de Construção e Projetos x
  Gestão de Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938107
version: 10
---

Estorno do Item de Movimento Integrado ao sistema de Gestão de Construção e Projetos   
O estorno de quantidade de um item em uma Solicitação de Compra ou de Armazém, enviada pelo Sistema de Gestão de Construção e Projetos, ocorre sempre que a quantidade do item do movimento for decrementada.   
Ao alterar a quantidade do item, automaticamente será enviado ao Construção e Projetos a quantidade estornada.   
O estorno da quantidade de um item poderá ser visualizado acessando o item na requisição de Materiais.   
Não será permitido ao usuário aumentar a quantidade do item enviado pela requisição de materiais e caso o mesmo seja incrementado, será exibida uma mensagem ao usuário informando que a ação não é permitida.   
Ao enviar uma requisição de materiais para o sistema de Gestão de Estoque, Compras e Faturamento conteúdo do campo INTEGRAAPLICACAO do Movimento de Solicitação de Compra ou cotação, será copiado para o atributo homônimo de seus itens. Essa peculiaridade é visualizada apenas acessando a tabela do banco de dados.  
   
**Pré-Condições**

Ter selecionado o parâmetro responsável por permitir a alteração de itens de movimento integrados ao sistema de Gestão de Construção e Projetos.  
Ter enviado uma requisição de Materiais do TOTVS Gestão de Construção e Projetos para o TOTVS Gestão de Estoque, Compras e Faturamento:

* Passo 1 - Selecione o Movimento e clique em "Editar";
* Passo 2 - Acesse a aba "Itens" e altere a quantidade para um valor inferior ao enviado pela requisição de materiais e salve o registro. O sistema não permite que a quantidade seja incrementada e que seja alterada a quantidade, o projeto, a tarefa, o produto ou a unidade de medida dos itens de movimentos gerados a partir da requisição de materiais;
* Passo 3 - Acesse TOTVS Projetos/ Gestão de Construção e Projetos;
* Passo 4 - Selecione o projeto qual o movimento pertence e acesse: Planejamento/ Geração de Pedidos;
* Passo 5 - Selecione a requisição de materiais que originou o movimento e clique no ícone "Editar";
* Passo 6 - Selecione o item da requisição e clique no ícone "Editar Item do Movimento".O sistema exibira no campo "Quantidade de Estorno" a diferença do valor informado no movimento ao editá-lo e a quantidade solicitada na requisição de materiais.
