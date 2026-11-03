---
content_hash: 2d0c92977afaa275c4bf57cef8dccb2212852d6ab5aa9dbddbbcfffe25ab5fb2
fetched_at: '2026-06-29T00:12:01.189239+00:00'
page_id: '889102423'
product: rm
source: tdn-rm
title: 5 - Movimentações de Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=889102423
version: 14
---

**Apontamentos de Movimentações de Produto no APP**

A funcionalidade permite **solicitar produtos/serviços** para o sistema de Suprimentos / Faturamento **através do APP Minha Obra.** A solicitação pode ser uma solicitação de compra ou uma requisição de material.

Pré-requisitos para uso

Antes de acessar a funcionalidade, é necessário:

1. Configuração da API: Certifique-se de que a URL da API está configurada. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=525013681).
2. Parametrização dos tipos de movimento no Totvs Construção Obras e Projeto. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=525013681).
3. Permissão de Acesso: O perfil do usuário deve ter permissão para utilizar a funcionalidade.

| Movimentações de Produto | | | |
| --- | --- | --- | --- |
| Após cadastro no TOTVS Construção Obras e Projeto, essas informações serão exibidas no Minha Obra.  Ao selecionar o tipo de requisição desejado, se a mesmo estiver parametrizado para utilizar contrato, a tela de seleção de contratos será exibida para que o contrato associado ao pedido seja selecionado. | Nesta tela, é possível pesquisar e selecionar o contrato que será utilizado para a movimentação de produtos. O filtro considera **apenas Contratos de Serviço**, exibindo somente contratos cujo status seja diferente de **“Em Medição”**, **“Em Aprovação”** e **“Em Liberação”**. | | |
|  |  | | |
| Ao informar o Contrato e Avançar, a tela de itens da Requisição é exibida para que a Tarefa e o Produto/Serviço sejam selecionados. | **Seleção de Tarefas:** Neste campo, você pode escolher a tarefa correspondente de diversas maneiras: inserindo-a manualmente ou realizando uma busca. A seleção seguirá a hierarquia das tarefas, que abrange obras e etapas. No entanto, se houver apenas um item para cada nível, serão exibidas apenas as tarefas. | | **Seleção de Produto/Serviço:** Neste campo, você pode escolher o produto correspondente de diversas maneiras: inserindo-a manualmente ou realizando uma busca.   **Obs:** Se na parametrização estiver definido que serão exibidos apenas Produtos que tenham saldo, a seleção da tarefa se torna obrigatória antes da seleção do produto. |
|  |  | |  |
| **Campo Quantidade:** Neste campo é necessário informar a quantidade do produto selecionado. | **Data de entrega:** Neste campo você deverá informar a data de entrega da requisição, tanto manual sou selecionando a data pelo calendário.  **Obs:** Ao adicionar um item na lista da requisição, a tarefa será mantida para o próximo item, sendo um facilitador para a inclusão de um produto que estará relacionado com a mesma tarefa selecionada. | | |
|  |  | | |
| **Obs:** Há um campo disponível na tela para adicionar observações, se necessário.  Após preencher todos os campos obrigatórios, você terá três opções: '+ Adicionar Produto', 'Finalizar' e 'Ver Todas as Movimentações'. Ao selecionar '+ Adicionar Produto', o item inserido ficará disponível na cestinha, onde você pode visualizar as movimentações já adicionadas.  Se preferir, ao clicar em 'Finalizar' ou 'Ver todas as movimentações', será aberta uma tela para revisar os itens antes de salvar. | Ao clicar em 'Ver Movimentações', é possível visualizar as movimentações realizadas anteriormente, consultar os itens e, se necessário, excluir a movimentação gerada. | | |
|  |  | | |
| Ao clicar na cestinha para verificar as movimentações já inseridas, é possível gerenciar os produtos: remover itens pelo ícone da lixeira, visualizar detalhes, alterar quantidades, adicionar novos produtos, cancelar a movimentação ou confirmar e salvar. | | | Ao clicar em 'Confirmar e Salvar', você será direcionado para a tela de 'Filtrar', onde é possível consultar todas as movimentações com base em critérios como Data de Criação, Período, Usuário, Identificador do Movimento, Número do Movimento e Tarefa. Após aplicar o filtro, as requisições correspondentes serão exibidas na tela principal, permitindo a visualização e exclusão, se necessário. |
|  | | |  |

| Sincronismo |
| --- |
| * Para que o sincronismo possa ser realizado, é necessário que o WebService que receberá e enviará informações esteja ativo; * É necessário dispor de um coletor móvel ou utilizar um emulador; * Com a aplicação no coletor aberta, realizar o sincronismo com o usuário e senha de acesso a base de dados do TOP, ou seja, usuário definido para utilização do coletor; |
|  |
