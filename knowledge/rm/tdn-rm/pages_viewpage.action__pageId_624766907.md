---
content_hash: 1cca2332a212cec99afc1cf53256d118aa54d68df65fe22a8bdee1a24550ccd9
fetched_at: '2026-06-29T00:11:04.071655+00:00'
page_id: '624766907'
product: rm
source: tdn-rm
title: Movimentações de Produto - App Minha Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624766907
version: 4
---

Movimentação de Produto

A funcionalidade permite **solicitar produtos/serviços** para o sistema de Suprimentos/Faturamento **através do APP Minha Obra**. A solicitação pode ser uma solicitação de compra ou uma requisição de material.

Para acessar a funcionalidade, é necessário que a URL da API tenha sido informada e o perfil do usuário possua permissão de acesso.

As Movimentações de Produto devem ser cadastradas no TOTVS RM para que sejam exibidas no coletor. Para realizar o cadastro o usuário deve acessar o menu em Controle | Mobilidade | Movimentações de Produto | Tipos de Movimentações de Produto.

No cadastro da Movimentação de Produto é obrigatório que sejam informados os campos Descrição, Tipo de Movimento e Saldo Visível.

 

* **Descrição:** Descrição da Movimentação de Produto
* **Tipo de Movimento:** Tipo de Movimento utilizado do TOTVS Gestão de Estoque, Compras e Faturamento
* **Saldo Visível:** Saldo que será exibido no APP Minha Obra ao solicitar um produto
* **Somente Produtos com saldo:**Serão listados no APP Minha Obra apenas produtos que tenham saldo
* **Somente Produtos vinculados à Tarefa:** Filtro para que sejam solicitados apenas produtos vinculados à tarefa escolhida na movimentação
* **Utiliza Contrato:** Opção para que as movimentações de produto impactem os contratos que utilizam as tarefas onde foram realizadas as solicitações
* **Somente Tarefas Vinculadas ao Contrato:** Filtro para que sejam solicitados apenas produtos de tarefas que estejam vinculadas ao contrato selecionado na movimentação de Produto

Após cadastro no TOTVS Obras e Projetos, essas informações serão exibidas nas Movimentações de Produto do APP Minha Obra.

 

Ao selecionar o tipo de requisição desejado, se o mesmo estiver parametrizado para utilizar contrato, a tela de seleção de contratos será exibida para que o contrato associado ao pedido seja selecionado. Apenas contratos de serviços serão exibidos.

Ao informar o Contrato e Avançar, a tela de itens da Requisição é exibida para que o Produto/Serviço e Tarefa sejam selecionados.

Se o tipo de requisição não estiver parametrizado para utilizar contrato, após selecionar o tipo de requisição desejado, será aberto a tela de itens da Requisição.

   

Para que o saldo do produto seja exibido é necessário definir a tarefa e o produto, pois o local de estoque e filial estão definidos na obra representada pela tarefa, e o saldo exibido corresponde ao que foi definido na parametrização da movimentação selecionada para gerar o movimento. Se na parametrização estiver definido que serão exibidos apenas Produtos que tenham saldo, a seleção da tarefa se torna obrigatória antes da seleção do produto. O saldo que será utilizado para validar se o produto tem quantidade disponível, é o mesmo definido para exibição.

Ao adicionar um item na lista da requisição, a tarefa será mantida para o próximo item, sendo um facilitador para a inclusão de um produto que estará relacionado com a mesma tarefa selecionada.

Na tela de itens da Requisição, ao clicar no ícone com as quantidades dos Produtos adicionados ou clicar em Finalizar, é aberto a tela que permite visualizar os itens de movimento, que serão apresentados antes de salvar.

Nessa tela, é permitido remover, alterar a quantidade, cancelar ou confirmar e salvar os produtos.

Também é permitido acessar a tela para inclusão de novos produtos, através da opção "Adicionar mais Produtos".

 

Nas telas de Contrato e Produto/Tarefa é possível visualizar as movimentações realizadas anteriormente, sendo possível visualizar os seu itens e consequentemente excluir o movimento gerado.

Clicando no botão "Filtrar", é possível consultar todas as requisições baseadas em informações do filtro, tais como Data de Criação, Período, Usuário, Identificador do Movimento, Número do Movimento e Tarefa. Ao confirmar o filtro, as opções selecionadas serão exibidas na tela principal, onde existe a possibilidade de excluí-las.

    

---

Veja mais:
