---
content_hash: 0b7f726cc028e362d4d41c28999a60b81cd6b9a490db2c75567a24fc93b476f6
fetched_at: '2026-06-29T00:09:26.048056+00:00'
page_id: '423938230'
product: rm
source: tdn-rm
title: Cadastro de Locais de Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Locais+de+Estoque
version: 9
---

Por esta opção cadastra-se a tabela de Local de Estoque por filial.   
O Local de Estoque trata-se de uma entidade principal para o correto controle de estoque.   
É criado conforme local de armazenagem dos produtos nas filiais e tem a sua importância dentro do Gestão de Estoque, Compras e Faturamento, pois todo o saldo dos produtos estará vinculado à filial/local de estoque da empresa, permitindo assim a obtenção de informações por local de estoque ou consolidados. Temos a possibilidade de inativar um local de estoque e desta forma, o mesmo não será mais exibido para movimentações.   
***Observações***: A descrição "Local de Estoque" para esta tabela é default do sistema, podendo ser alterada através do Menu Opções | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Local de Estoque.   
Segue abaixo a descrição de determinados campos do cadastro de local de estoque:

* **Campos obrigatórios**: Filial, Código, Nível de estoque (caso esteja habilitado)
* **Campos não obrigatórios**: Descrição, Identificador da unidade de negócio, Endereço, Defaults Contábeis
* **Código**: Informe o código do local de estoque, de acordo com a máscara parametrizada em Menu Opções | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Local de Estoque.
* **Faixa do Nível de Estoque**: Informe em qual das 3 faixas este local irá buscar o estoque mínimo, o estoque máximo e o ponto de pedido, cadastrados nos produtos, na pasta controle de estoque. O campo Faixa de Estoque só será visualizado caso o sistema não esteja parametrizado para trabalhar com ressuprimento.
* **Unidade de Negócio**: Para selecionar a unidade de negócio é necessário o seu cadastramento no Gestão Fiscal, através do Menu Cadastro | Tabelas Auxiliares | Unidade de Negócio. A unidade de negócio irá representar, nos lançamentos fiscais, a empresa contratante, utilizado pela empresa contratada, para realização de sua atividade. As Unidades de Negócio somente serão visualizadas no local de estoque quando cadastrado na filial correspondente. A tela de Defaults Contábeis não será implementado na primeira versão da migração, por se tratar de uma tela de outro produto, que é customizada pelo TOTVS Gestão de Estoque, Compras e Faturamento.

***Exemplo***: No Local de estoque 01 foi cadastrada a Filial Belo Horizonte, somente as Unidades de Negócio da filial Belo Horizonte estarão disponíveis para seleção.   
Defaults Contábeis: Campo a ser informado as contas de débito e/ou credito referente a contabilização do movimento.   
Endereço: Segue a inclusão dos dados referente ao endereço do local de estoque, caso este possua.   
No TOTVS Gestão de Estoque, Compras e Faturamento o Cadastro de Locais de Estoque está localizado no seguinte caminho: BackOffice | Gestão de Estoque, Compras e Faturamento | Cadastros | Locais de Estoque

**Migração**

Para o Cadastro de Locais de Estoque do TOTVS Gestão de Estoque, Compras e Faturamento serão desenvolvidas telas Web utilizando o TOTVS HTML Framework.   
Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig e/ou Portal RM para que o usuário possa ter um acesso mais ágil e prático do cadastro.

1
complete
Tabelas Utilizadas **TLOC**.
