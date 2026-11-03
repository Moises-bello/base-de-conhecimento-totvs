---
content_hash: de63a149a8a4f472d6b48fc38e2e9f7a288bcd822e9450047ce17bf79e2dab15
fetched_at: '2026-06-29T00:09:28.641714+00:00'
page_id: '423938734'
product: rm
source: tdn-rm
title: Assistente de Apropriação Direta de Produto(s)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938734
version: 3
---

A apropriação direta de produtos consiste em mensurar, movimentar o estoque e apurar o custo dos materiais/produtos utilizados pelos objetos de manutenção no dia a dia de um setor de manutenção.   
Esses materiais são, por exemplo, combustíveis, lubrificantes ou qualquer consumível utilizado no funcionamento das maquinas em um setor de manutenção.   
O gasto desses produtos é medido através do processo de apropriação direta de produtos.  
Para que um objeto de manutenção faça apropriação direta de produtos é necessário que no cadastro do tipo de objeto de manutenção a tag "Apropriação Direta de Produto(s)?" esteja marcada e existam produtos vinculados aos objetos de manutenção no cadastro de objeto de manutenção nos anexos "Produtos do Objeto de Manutenção" e esteja com o campo "Produto Apropriavel?" marcado.  
Para acessar o processo de apropriação direta de produtos vá ao menu Operações | Apropriação Direta de Produto(s), e acesse o processo "Assistente de Apropriação Direta de Produto(s)" que se encontra na tela de visão das apropriações.  
A apropriação será gerada através de um WIZARD. Na primeira parte existe o campo "Descrição do Processo", onde o usuário deverá informar o nome do processo que será executado, vale lembrar que este campo não é de preenchimento obrigatório portanto, se for da vontade do usuário, esse passo poderá ser avançado sem o preenchimento deste campo.   
No próximo passo o usuário deverá informar os dados para o movimento que será gerado ao finalizar a apropriação.   
Deverá ser informado a data da apropriação, o tipo de movimento que será gerado para a apropriação, a filial, o departamento, o local de estoque para qual será gerado a apropriação, o cliente o centro de custo e por fim deverá selecionar o preço.  
As opções existentes no campo "Buscar preço de:" é previamente parametrizado acessando o parâmetro do tipo de movimento no sistema TOTVS Gestão de Estoque, Compras e Faturamento.   
Ao selecionar algum preço o sistema preencherá o campo preço unitário com o valor do preço referente à opção escolhida.  
Ao preencher os dados do movimento é necessário no próximo passo selecionar os objetos de manutenção que serão feitas as apropriações.   
Basta seleciona-los e clicar e avançar.   
Ao marcar o botão "fixar 1º identificador", no próximo passo, ao pressionar enter para inserir outro objeto o código do primeiro objeto selecionado será automaticamente preenchido, isso evita o retrabalho de selecionar o objeto de manutenção novamente.   
Ao clicar no botão "fixar 1º identificador" só poderá ser selecionado um objeto de manutenção apenas.   
Vale lembrar que só serão listados na grid os objetos de manutenção que possuem produtos que podem ser apropriados, se o objeto não possuir produtos para apropriar o mesmo não será listado na grid.  
Após selecionar o objeto de manutenção para que os produtos apareçam para ser apropriados é necessário, como dito acima, que os mesmos estejam informados no cadastro de objeto de manutenção no anexo "Produtos do objeto de manutenção" e que o campo "Produto apropriável?" esteja marcado.   
Se existirem produtos vinculados ao objeto de manutenção, ao selecionar o objeto e avançar para o próximo passo os produtos associados a ele ficaram disponíveis para serem apropriados.   
Se o usuário não desejar apropriar algum produto, basta não informar valor no campo quantidade (que vem marcado por default com o valor zero).  
Por ultimo existem as tabelas do movimento e do item.  
Essa funcionalidade permite o usuário inserir os dados referentes às Tabelas Opcionais do Financeiro que será visualizado no movimento gerado no TOTVS Gestão de Estoque, Compras e Faturamento ao Gerar uma apropriação direta de Produtos, veja:

**Tabelas do Movimento**: Ao clicar nesse botão o usuário terá a opção de preencher as informações referentes às Tabelas opcionais do movimento. Para configurar os campos que estarão disponíveis para preenchimento o usuário deverá acessar o TOTVS Gestão de Estoque, Compras e Faturamento no menu Assistente | Parâmetros | Gestão de Estoque, Compras e Faturamento, escolher o movimento desejado e acessar o item "Mov - Tab Opcional" .   
Os campos estarão disponíveis de acordo com a parametrização escolhida (Não Edita, Edita e Mostra), podendo ser obrigatório e também ter valores default.

**Tabelas Item Movimento**: Ao clicar nesse botão o usuário terá a opção de preencher as informações referentes às Tabelas opcionais do item. Para configurar os campos que estarão disponíveis para preenchimento o usuário deverá acessar o TOTVS Gestão de Estoque, Compras e Faturamento no menu Assistente | Parâmetros | Gestão de Estoque, Compras e Faturamento, escolher o movimento desejado e acessar o item "Item - Tab Opcional". Os campos estarão disponíveis de acordo com a parametrização escolhida (Não Edita, Edita e Mostra), podendo ser obrigatório e também ter valores default.  
Depois de preencher os campos do movimento e do item nas tabelas opcionais, basta avançar para a última tela e clicar e executar para que a apropriação seja realizada.  
***Observação***: É possível gerar uma apropriação direta para objetos que não utilizam indicadores de uso.
