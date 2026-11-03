---
content_hash: 2d7974abbd69af24d5ddac47e66937fe81e2c6548922f74e0cd5d44bb72d60c0
fetched_at: '2026-06-29T00:10:31.957501+00:00'
page_id: '525013681'
product: rm
source: tdn-rm
title: Movimentações de Produto - App Minha Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525013681
version: 29
---

A funcionalidade Movimentações de Produto permite **solicitar produtos/serviços** para o sistema de Suprimentos/Faturamento **através do APP Minha Obra**. A solicitação pode ser uma solicitação de compra ou uma requisição de material.

Para acessar a funcionalidade, é necessária a respectiva permissão de acesso.

Para configuração, acesse menu Controle > Mobilidade > Minha obra > usuário de Coletores Móveis > Processos > **QRCode para configuração automática do sincronismo do App Minha Obra,** nesta tela que se abre foi incluído o campo para informar a URL da API.

**Exemplo de URL de API:**

[http://nomedocomputador:porta/api/construction-projects/v1/product-movement-parameter?companyId=1&projectId=156&page=1&pageSize=10&order=+Description](http://bhn050102771.bh01.local:8052/api/construction-projects/v1/product-movement-parameter?companyId=1&projectId=156&page=1&pageSize=10&order=+Description)

Ao realizar a leitura do QR Code gerado na tela acima, os campos de Url serão automaticamente preenchidos.

### Cadastro das movimentações

As Movimentações de Produto devem ser cadastradas no TOTVS RM para que sejam exibidas no coletor. Para realizar o cadastro o usuário deve acessar o menu em Controle | Mobilidade | Movimentações de Produto TCOP | Tipos de Movimentações de Produto TCOP.

No cadastro da Movimentações de Produto é obrigatório que sejam informados os campos Descrição, Tipo de Movimento e Saldo Visível.

* **Descrição:**Descrição da Movimentação de Produto
* **Tipo de Movimento:**Tipo de Movimento utilizado do TOTVS Gestão de Estoque, Compras e Faturamento
* **Saldo Visível:**Saldo que será exibido no APP Minha Obra ao solicitar um produto
* **Somente Produtos com saldo:**Serão listados no APP Minha Obra apenas produtos que tenham saldo
* **Somente Produtos vinculados à Tarefa:**Filtro para que sejam solicitados apenas produtos vinculados à tarefa escolhida na movimentação
* **Utiliza Contrato:**Opção para que as movimentações de produto impactem os contratos que utilizam as tarefas onde foram realizadas as solicitações  

  **Observação:**  
  Quando esta opção estiver habilitada, o usuário poderá pesquisar e selecionar o contrato que será utilizado na movimentação de produtos. O sistema exibirá **somente Contratos de Serviço**, filtrando automaticamente os contratos que não estão aptos para esse processo. (Não serão apresentados contratos que estejam nos status **Em Medição**, **Em Aprovação** ou **Em Liberação**.)
* **Somente Tarefas Vinculadas ao Contrato:**Filtro para que sejam solicitados apenas produtos de tarefas que estejam vinculadas ao contrato selecionado na movimentação de Produto

### Integração Protheus

Quando essa integração está ativa, somente é possível selecionar tipos de movimento que estiverem previamente configurados para integrar com solicitação de armazém do Protheus.

Na integração com Protheus, não haverá nada relacionado a saldo do estoque e o contrato do nesse caso, é somente para o filtro de tarefas, por isso a tela de Movimentações de Produto tem as alterações que pode ser observados abaixo:

**Obs:** A data de entrega é somente configurada para o item, uma vez que com o Protheus, os tipos de movimento são pré-configurados.

Ao definir o tipo de movimento que será utilizado é importante verificar nos parâmetros do Totvs Construção e Projetos se nos parâmetros gerais de integração com o backoffice esta definido que utiliza ratio de centro de custo , se estiver marcado nos [Parâmetros - TOP](https://tdn.totvs.com/pages/editpage.action?pageId=421385497)que utiliza, na parametrização do backoffice a infomação preenchida deve ser valor.       

O TCOP passa também a enviar o centro de custo no movimento nas movimentações.

Para seguir utilizando a funcionalidade no app Minha Obra acesse :
