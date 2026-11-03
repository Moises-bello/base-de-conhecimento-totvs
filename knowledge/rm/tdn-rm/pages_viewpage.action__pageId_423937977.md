---
content_hash: 3eae9182c2b2f171bb8531af9833a4e4a071c3b087a18248b9cb28e656baa490
fetched_at: '2026-06-29T00:09:24.649001+00:00'
page_id: '423937977'
product: rm
source: tdn-rm
title: Inventário de Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937977
version: 71
---

### O Inventário permite que seja informado no sistema o resultado da conferência física de mercadorias em estoque. Desta forma o processo de inventário garante os estoques da empresa com as quantidades corretas de seus produtos.

PaginaGeraltrueCadastro de Inventário

Ao incluir um novo inventário no sistema será apresentado ao usuário um assistente, o qual auxilia no processo de inclusão do inventário.

PaginasDoAssistenteInclusaotrueIdentificação

Na etapa de identificação são apresentados os seguintes campos:

**Código do Inventário*:*** este campo deve ser informado manualmente ou será preenchido automaticamente pelo sistema com um código de inventário único respeitando uma máscara previamente parametrizada (mais detalhes em [Parametrização de Inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938132)).

Caso o parâmetro "Utilizar código sequencial" esteja marcado este campo virá preenchido com um código gerado pelo sistema no formato ####.##.##### representando ano, mês e um código sequencial respectivamente (exemplo: 2022.03.00019). Com esta opção o campo código do inventário ficará desabilitado para edição impedindo qualquer alteração por parte do usuário.

Caso a opção seja a não geração do código automático, isto é, o parâmetro "Utilizar código sequencial" esteja desmarcado, então no campo de código do inventário deve ser informado um código do inventário único manualmente de acordo com o parâmetro de [Máscara do Código do Inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938132).

Caso seja informado um código já usado em outro inventário na coligada corrente será apresentado mensagem: "Já existe um inventário com o código *xxxxxx*. Informe um novo código para prosseguir!" e o botão Avançar ficará desabilitado até que seja informado um código válido.

**Saldo a ser Inventariado*:*** deve ser informado qual dos saldos do(s) produto(s) deverá(ão) ser inventariado(s). O default deste campo é o Saldo 2.

**Bloqueia Movimentação*:*** este campo deve ser marcado caso seja necessário efetuar o bloqueio de movimentações dos produtos associados a este inventário.*Observação:* Inventários do tipo Número de Série devem obrigatoriamente ter o campo "Bloqueia Movimentação" marcado.

Atenção!

O campo "Bloqueia Movimentação" modifica o tratamento dos dados que serão gerados pelo Inventário.

* Quando MARCADO, a diferença considerada no Inventário será o Valor Informado na Contagem subtraído do Saldo do Produto por local de estoque (TPRDLOC). O saldo pode ser o Saldo 2 e os Saldos de 5 a 10. Este saldo também está disponível através da Consulta de Saldos e Custos do Produto.
* Quando DESMARCADO, a diferença considerada no Inventário será a soma dos campos SALDOANTERIOR + QTDECOMSINAL (quantidade movimentada) da tabela TRELSLD (Ficha Física Financeira). Será buscada a última movimentação do produto em questão para a filial e local de estoque escolhidos cuja data de movimentação seja igual ou menor que a data base do inventário. O saldo pode ser o Saldo 2 e os Saldos de 5 a 10.

**Data Base do Inventário:** este campo ficará disponível somente quando o campo "Bloqueia Movimentação" estiver desmarcado.

**Observação****:** neste campo pode ser informado algum conteúdo necessário para a identificação do inventário.  
**Tipo do Inventário***:* neste campo pode-se selecionar o tipo do inventário que será realizado. Esta informação será utilizada como filtro na inclusão de produtos, bem como na exibição das informações na etapa de inclusão de Produtos. O valor default do campo será o que está definido nos parâmetros de [Gestão de Estoque, Compras e Faturamento | Inventário | Definições de Inventário | Tipo de Inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938132).  
Em todos os processos do Inventário será considerado o Tipo do Inventário informado no momento da inclusão. Para os inventários que não possuir esta informação, ou seja, estiver nula na base (Inventários criados em versões anteriores), serão consideradas nas consistências o que está definido nos parâmetros de  [Gestão de Estoque, Compras e Faturamento | Inventário | Definições de Inventário | Tipo de Inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938132)..  
Ao salvar o Inventário é verificado se os itens incluídos já fazem parte de algum inventário, considerando o tipo informado. Caso já exista inventário com estes itens em alguma filial/local de estoque será apresentada mensagem informando que o produto já está incluído em algum inventário, conforme o tipo do inventário:

* **Produto**: verifica se o produto já faz parte de algum inventário em aberto.
* **Lote**: verifica se o lote informado para o item de inventário já faz parte de algum inventário em aberto.
* **Número de Série**: verifica se o número de série informado para o item de inventário já faz parte de algum inventário em aberto.
* **Grade Numerada**: verifica se o item de grade antiga já faz parte de algum inventário em aberto.
  + ***Observação***: Quando selecionada a opção Tipo do Inventário Grade Numerada será considerado os produtos de grade antiga. Os produtos de Grade nova são considerados como Tipo do Inventário Produto.

**Tipo Contagem Inventário***:* neste campo pode-se selecionar o tipo de contagem do inventário, recurso existente para versão 12.1.2205 e superiores. A escolha do tipo de contagem influencia na sequência de entrada de dados de contagem e apuração de diferença.

* **Contagem Livre**: A contagem livre permite informar as contagens em qualquer ordem, alterar contagens, apurar diferença zerando itens ou permanecendo aguardando contagem,  o cliente é livre para preencher essas informações na ordem e momento que preferir. Então, ao acessar a tela de contagem, (visão ou edição) nenhuma restrição é aplicada. Esse tipo de contagem é semelhante a forma única de contar existente até a versão 12.1.34.

***Observação***:

* + O campo FIMCONTAGEM é utilizado apenas para contagem "Smart", na contagem "Livre" seu valor é sempre ZERO.
  + A data de apuração é registrado apenas na primeira vez em que ocorre a apuração, então, embora na contagem "Livre" seja possível modificar os valores das contagens e refazer a apuração, a data registrada continua sendo sempre a data da primeira vez em que o processo foi realizado e considerou a contagem em questão.

* **Smart**: A contagem Smart busca otimizar o processo de contagem evitando a recontagem de produtos que atenderam suas regras, na contagem Smart deve-se seguir uma sequência pré-estabelecida, fica disponível apenas a contagem 1, após realizar essa contagem e apurar diferença é liberado a contagem 2 e assim por diante até a apuração de diferenças da contagem 3.

Quando a regra Smart é atendida, nenhuma nova contagem é requerida, sendo assim, na (visão/edição) após apuração o sistema não aceita mais contagens para esses produtos, os campos na edição ficam desabilitados e na visão é exibido um alerta de que não é possível alterar o valor.

Abaixo as regras de contagem que permitem otimizar a realização do inventário:

* + Regra 01: Ao realizar uma contagem de produto com quantidade semelhante ao saldo em estoque, após apuração de diferença desta contagem, sendo a diferença ZERO, a inteligência do Smart entende que o saldo existente e a contagem são compatíveis, a contagem é encerrada por regra Smart para aquele item.
  + Regra 02: Ao realizar duas contagens com valores diferente do saldo em estoque mas iguais entre si, o sistema entende após apuração de diferença que a contagem está correta, apesar de diferente do saldo, uma contagem confirmou a outra, dessa forma evita-se uma terceira contagem, a contagem é encerrada por regra Smart para aquele item.
    - Ao realizar contagem por endereço essa regra só finaliza a contagem se as duas contagens de cada endereço forem iguais, independente de ser igual o somatório de todos os endereços.
  + Regra 03: Ao realizar uma terceira contagem, após a apuração de diferença, independente da diferença apurada, a contagem é encerrada por regra Smart.

Quando a regra SMART for atendida é registrado na tabela de itens do inventário (TITMINVENTARIO.FIMCONTAGEM = 1) que o item foi encerrado, essa informação pode ser vista na edição/visão e pode ser utilizada para filtros e relatórios.

***Observações:***

* + Utilizando inventário tipo SMART, após realizar a apuração a contagem apurada não pode mais ser alterada.
  + O campo FIMCONTAGEM para contagem "Livre" é sempre ZERO.
  + Para os dois tipos de contagens (Livre ou Smart) o sistema não obriga realizar as três contagens, ficará a critério do responsável pelo inventário realizar ou não. Entendemos que este comportamento gera flexibilidade para o processo, podendo ser adaptável a cada necessidade.

Atenção

O recurso do tipo de contagem esta disponível na release 12.1.2205 ou superior.

Locais de Estoque

Após informar os campos iniciais do inventário é apresentada a etapa para que se possa informar as [Filiais](http://tdn.totvs.com/pages/viewpage.action?pageId=422545738), os [Locais de Estoque](http://tdn.totvs.com/display/LRM/Locais+de+Estoque) e, opcionalmente os [Centros de Custo](http://tdn.totvs.com/display/LRM/Cadastro+Centros+de+Custos) onde serão realizados os processos de inventário.

Endereçamento

Durante o assistente de inclusão do Inventário, será possível incluir o Endereçamento dos Locais de Estoque nos itens de Inventário.

Ao selecionar um Local de Estoque que contenha Endereçamentos cadastrados o assistente irá apresentar uma opção para adicionar os Endereçamentos ao inventário, só serão exibidos os Endereçamentos ativos e que possuam ao menos um produto vinculado a ele.

**N****ão é obrigatório a inclusão de nenhum Endereçamento, mas caso sejam incluídos serão listados somente Produtos que estejam vinculados a esses Endereçamentos.**Se o vínculo de um Endereçamento com Produto estiver marcado como Indisponível, este produto não será exibido.

Recurso existente para versão 12.1.2205 e superiores.

Atenção

O Endereçamento tem como objetivo facilitar as contagens durante o Inventário. O Controle de estoque continua sendo feito por Local de Estoque e portanto NÃO será feito por Endereçamento.

Para mais informações sobre o cadastro de endereçamentos, clique  [AQUI](https://tdn.totvs.com/pages/viewpage.action?pageId=662417226) e para mais informações sobre o vínculo de  Endereçamentos a produtos clique [AQUI](https://tdn.totvs.com/pages/viewpage.action?pageId=664205609).

Produtos

Para finalizar a criação de um novo inventário é preciso selecionar os produtos que serão inventariados.

De acordo com o tipo do inventário, podem ser selecionados para os produtos os Lotes, as Grades e os Números de Série para também serem inventariados.

Após a criação do Inventário é possível inserir novos produtos no mesmo, através da edição do Inventário, desde que o mesmo esteja com status em aberto.

**Inclusão de Produtos**:

            Deverão ser inseridos os produtos a serem inventariados utilizando os filtros do sistema conforme a necessidade.

**Adicionar Sorteando**:

Esta funcionalidade está disponível no Assistente de Inclusão de Inventário e possibilita que sejam selecionados os produtos que não estão incluídos em inventários realizados em um determinado período, ou seja, não inventariados.

São selecionadas informações de produto como Coligada, Identificador do Produto, Código do Produto, Código Reduzido, Nome Fantasia, Unidade de Controle e Código de Grade antiga.

O retorno dos dados realiza o filtro pela coligada, tipo do inventário e produtos que não estão incluídos em inventário por meio da opção de dois filtros:

* + **Filtrar por período:** O usuário escolhe o período onde será realizado o filtro.
  + **Filtrar até a data:**  Equivalente a opção acima, só que tendo como data inferior o começo de uso do RM e a data superior a escolhida pelo usuário.

Após clicar no Botão será exibida uma tela onde é possível escolher o filtro que será utilizado para a seleção dos produtos participantes do sorteio.

Além disso poderá ser definida a quantidade de produtos que serão sorteados, se atendo a quantidade máxima de itens não inventariados dentro do intervalo do filtro selecionado, por padrão este campo virá preenchido com a metade da quantidade máxima permitida. 

É importante salientar que esta funcionalidade também leva em consideração os Endereçamentos, caso eles tenham sido informados, ou seja, se foi selecionado um Local de Estoque que possui Endereçamentos, e na tela de Endereçamentos foram selecionados alguns registros, o sorteio levará em consideração apenas produtos que estão vinculados a estes Endereçamentos.

***Observação***: Após a inclusão do inventário os produtos ficarão bloqueados nos locais de estoque, não deixando incluir movimentações para os mesmos, até que o inventário seja encerrado ou excluído.   
O assistente de inventário não permite que sejam criados dois inventários distintos que possuam um mesmo produto em um mesmo local a ser inventariado.

Recurso existente para versão 12.1.2205 e superiores.

Edição de Inventário

Após a criação do inventário, realizar uma série de operações, como incluir novos produtos, realizar as contagens caso o mesmo ainda esteja aberto e navegar entre os produtos do inventário através do código de barras, auxiliando no processo de contagem.

PaginasEdicaoInventariotrueVisão geral dos itens do inventário

Na visão geral dos itens do inventário são apresentadas as informações principais dos produtos e do processo de inventariação do mesmo.

Se durante o cadastro do inventário ou na inclusão do produto foi utilizado a informação de endereçamento ela será apresentada na visão geral também.

Os produtos que estiverem vinculados a mais de um Endereçamento dentro do mesmo Local de estoque, serão apresentados mais de uma vez, sendo uma para cada Endereçamento, dessa forma, as contagens poderão ser feitas individualmente para cada Endereçamento, mas o processo de **Apurar Diferença do Inventário** levará em consideração o somatório das contagens desse grupo de Endereçamento do Local de Estoque, e a **Geração de Acerto** será feito em um único movimento para o Local de Estoque em questão, sendo este o motivo de só ser possível marcar a o campo de Gera Acerto do primeiro endereçamento.

Caso o usuário tente marcar o campo de Gera Acerto dos outros Endereçamentos será apresentado a ele uma mensagem informativa, falando isso não é permitido.

Caso seja feita a exclusão de um produto  do inventário que contenha a informação de Endereçamento e este produto se encontre em outros Endereçamentos do mesmo local de estoque, estes registros também serão excluídos, mas antes disso será apresentada uma mensagem de confirmação para o usuário. Ao clicar em **sim** ele confirma a ação e a exclusão dos registros será realizada, caso ele não tenha certeza se deseja mesmo excluir os registros, ele deverá clicar em não e a ação de exclusão será cancelada.

Inclusão de produto

Após a criação do Inventário é possível inserir novos produtos no mesmo, através da edição do Inventário, desde que o mesmo esteja com status em aberto.

Observação

Se o tipo de contagem do inventário é Smart e já foi realizada a apuração da diferença em algum momento, a inclusão de novos itens não será permitida, já que para este tipo de contagem é importante que todos os itens se encontrem no mesmo momento de contagem.

Ao incluir um novo item de inventário no sistema são apresentados os seguintes campos:

* **Filial**: deve ser informada a Filial que se encontra o Local de Estoque do produto a ser inventariado.
* **Local de Estoque**: deve ser informado o Local de Estoque em que está o produto a ser inventariado.
* **Endereçamento:** Campo não obrigatório, onde se informa o Endereçamento em que está o produto a ser inventariado
* **Produto**: Neste campo deve ser informado o código do produto que será inventariado.  
  ***Observação:*** Caso seja informado o Endereçamento só serão exibidos produtos relacionados ao Endereçamento.

Contagem (1º Contagem – 2º Contagem – 3º Contagem): deve ser informado o resultado da contagem física do produto.  
***Observação***: Ao informar a 1ª contagem no inventário, as seguintes regras serão validadas:

* A 2ª contagem só poderá ser informada se a 1ª já estiver preenchida.
* A 3ª contagem só poderá ser informada se a 1ª e a 2ª foram informadas.

**Unidade de Controle**: deve ser informada uma unidade de controle vinculada ao produto. Essa unidade de controle do item de inventário pode ser alterada somente na primeira contagem. Data (1º Contagem – 2º Contagem – 3º Contagem): este campo é preenchido automaticamente pelo sistema de acordo com a data/hora que a contagem foi inserida no sistema.

**Diferença Apurada**: neste campo é visualizado a diferença entre a quantidade física encontrada em um local de estoque e a quantidade inventariada para um acerto produto.   
É preenchido após a execução do processo "Apurar Diferença do Inventário".

Caso exista mais de um item de inventário contendo o mesmo produto, mas em Endereços diferentes, somente um desses registros gerará o valor de Diferença. Embora o inventário seja feito a partir do Endereço o Saldo de Estoque não é e portanto não seria possível discriminar quanto do Saldo de Estoque está em cada endereço. Assim, o cálculo da Diferença será feito com o acúmulo das contagens de todos os Endereços daquele Produto/Lote/Numero de Série. Dessa forma, os outros registros desse Endereço ficarão com o campo Diferença vazio.

**Gera Acerto**: este campo deve ser marcado caso deseje gerar movimentos de acerto de estoque para o produto deste item de inventário ao executar o processo "Gerar Acertos e Encerrar o Inventário".

Caso exista mais de um item de inventário contendo o mesmo produto, mas em Endereços diferentes, somente um desses registros poderá estar marcado como Gera Acerto. Embora o inventário seja feito a partir do Endereço, o acerto é feito por Produto. Portanto, não seria correto que se gere um acerto diferente para cada linha de item de Inventário nesse caso.

Caso se tente marcar o campo Gera Acerto para um item que não permita acerto, o sistema irá exibir uma mensagem explicando.

**Movimento de Acerto**: este campo é preenchido com o número do movimento gerado, após a geração do acerto e o encerramento do inventário.

***Observação:*** Caso seja informado o Endereçamento do produto, e o produto se encontre em mais de um Endereçamento no mesmo local de estoque, ao realizar a inclusão, serão incluídos no inventário uma linha para cada um dos Endereçamentos que aquele produto se encontra.

Buscar produto pelo código de barras

A busca de um Produto pelo Código de barras pode ser feita através do Botão de código de barras na barra de itens.

Ao clicar no botão é exibido um campo de texto no qual é possível digitar o código de barras do produto desejado ou ler o código de barras através de um leitor de código de barras.

Após digitar o código desejado e pressionar a tecla “ENTER” no teclado será realizada a busca do produto (Caso utilize um leitor de código de barras basta realizar a leitura do código que a pesquisa será realizada de forma automática).

Após pressionar a tecla “ENTER” os produtos associados ao código de barras serão exibidos na tela.

Caso o código digitado não corresponda a nenhum produto listado nos itens do inventário, uma mensagem será exibida informando que o produto não foi encontrado.

Após encontrar o produto, o usuário poderá preencher a contagem desejada.

Após o preenchimento do campo responsável pela contagem, deve ser confirmado o valor da contagem ao pressionar no teclado a tecla “ENTER”.

Após pressionada a tecla “ENTER” é possível realizar uma nova pesquisa pressionando a tecla “F12” em seu teclado.

Ao pressionar a tecla “F12”, a tela retorna com todos os itens originais, o campo de pesquisa é selecionado novamente e as informações contidas nele são limpas, possibilitando uma nova leitura de código de barras.

Obs.: Recurso existente para versão 12.1.2205 e superiores.

**HOW TO**

648432

648432
