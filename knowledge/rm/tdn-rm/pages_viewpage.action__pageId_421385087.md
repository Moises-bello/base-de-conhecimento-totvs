---
content_hash: 9993c1af2fc4744ca84c0dc7124ca14f2af3df2be28e9993615dacd1964de58f
fetched_at: '2026-06-29T00:09:13.688559+00:00'
page_id: '421385087'
product: rm
source: tdn-rm
title: Planilha de Atividades 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385087
version: 49
---

---

Conforme processo de Gestão de Projetos de Construção em várias empresas, a organização em Macro processos foi desenvolvida com algumas planilhas que descrevem as atividades que serão executadas no projeto.

A Planilha de Atividades é composta por tarefas com um maior nível de detalhamento. É a estrutura definida no planejamento e utilizada para a execução do projeto.  
 

As tarefas são compostas por obras, que se dividem em etapas e as etapas podem possuir vários serviços.

Antes de cadastrar uma etapa, deve-se cadastrar a obra, com o código de acordo com a máscara da tarefa (obras, etapas e tarefas) parametrizada no sistema (Menu Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Exibição).

A obra aparecerá na listagem das tarefas escrita da cor definida no Menu Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Exibição | Cores.

Depois de cadastrada a obra, cadastra-se as etapas, com o código da máscara um nível abaixo ao da obra.

Podem-se efetuar algumas atividades em grupo, como ativar, desativar, excluir e alterar entre valor cotado e calculado. Para isso selecione as tarefas desejadas e efetue a operação como se fosse para uma única tarefa.

Para limitar o número de registros exibidos na Planilha de Atividades acesse: Cadastro / Segurança  /Administrativa / Servidor de aplicação.

Na tela de Servidor de Aplicação clique em Novo e em Id do server escolher: PrjPlanilhaAtividadesData e informar o número máximo de registros a serem exibidos. Salvar as informações.

Ao acessar a Planilha de Atividades após informar o número máximo de registros deverá ser exibida apenas a quantidade de registros definida. A exibição dos registros está diretamente ligada ao Filtro utilizado para demonstração das atividades;

**Exemplo:**

Na planilha de atividades existem 50 atividades. No Servidor de Aplicação foi definido como número máximo de registros: 10.

Se voltarmos a Planilha de Atividades e estiver definido o filtro: 'Todos' será exibida uma mensagem informando para especificar melhor sua consulta e demonstrado que o filtro retorna 50 valores e o limite máximo é 10. Para serem apresentadas tarefas, o filtro deve ser modificado de forma que o retorno seja igual ou inferior ao número máximo de registros.

Se não existir um número máximo definido, todas as linhas de registro da planilha de atividades serão apresentadas.

As etapas podem possuir vários serviços. A diferença da etapa para o serviço é que o serviço tem os campos quantidade, unidade, composição, valor unitário e BDI preenchidos, as etapas não. Se estes campos forem preenchidos para uma etapa, ela passa a ser um serviço, não podendo ter níveis abaixo.

O valor unitário da tarefa será calculado em duas formas:

* Caso a tarefa seja de valor cotado o valor unitário será exibido conforme o valor da tarefa
* Caso a tarefa esteja com recurso associado o valor unitário da tarefa será o valor do recurso associado

As etapas aparecerão na listagem das tarefas e os serviços aparecerão escritos da cor definida no Menu Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Exibição | Cores.

A inclusão de novas obras, etapas, ou serviços é feito através da inclusão de linhas, tarefas ou sub-tarefas.

Se não houver nenhum item cadastrado, pressione Insert, seta para baixo ou clique no ícone ' Incluir '. Dessa forma, o código da obra será gerado automaticamente, de acordo com a máscara.

Após cadastrar a obra, estando com o cursor posicionado sobre a mesma, ao pressionar Insert ou Seta para Baixo ou no ícone 'Incluir', o código sugerido será o código de uma etapa.

Após cadastrar a etapa, estando com o cursor posicionado sobre a obra, ao pressionar Insert ou Seta para Baixo ou no ícone 'Incluir', o código sugerido será o código de uma etapa.

Após cadastrar a etapa, estando com o cursor posicionado sobre a mesma, ao pressionar Insert ou Seta para Baixo ou no ícone 'Inserir nova linha', o código sugerido será o código de uma sub-etapa ou serviço (dependerá do que você informar para o item).

Para cadastrar um serviço, posicione no serviço que tem código anterior ao que o serviço terá e pressione Insert ou o ícone 'Incluir'. Se o serviço for o último da visão, poderá utilizar Seta para baixo. E assim, por diante. Para a função de Exclusão pode-se utilizar as teclas de atalho Ctrl + Del.

Para a função de Inclusão pode-se utilizar a tecla Ctrl + Ins.

O cadastro de uma nova obra ou a alteração de uma obra já cadastrada pode ser feito também através da janela de edição de obras.

Quando uma tarefa tiver um recurso associado, a unidade não poderá ser alterada, pois ela é a mesma unidade do recurso (composição ou insumo).

Quando uma tarefa tiver um valor cotado e for associar um recurso (composição / recurso), o valor cotado será desativado e o recurso será ativado.

Insumos percentuais não podem ser associados às tarefas.

Com a visão de composições ou de insumos aberta, pode-se arrastar um recurso e soltá-lo na visão de Tarefas. Uma tela de diálogo é aberta e você pode associar um recurso à tarefa ou incluir uma nova atividade com o recurso.  Se estiver associando uma composição à tarefa e já existir uma composição associada, a mesma será substituída.

Caso já exista um insumo associado à tarefa, o mesmo será excluído da tarefa. Se estiver associando um insumo à tarefa e já existir uma composição associada à tarefa, a mesma será excluída da tarefa.

Caso exista integração orçamentária na tarefa e deseja-se excluir a mesma, a integração será excluída caso não tenha sido consumido valor no Totvs Backoffice.

Se a tarefa for uma etapa ou uma obra não serão permitidas as associações de composições ou insumos.

Se estiver criando uma nova tarefa, a mesma é criada com o Nome, a Descrição e a Unidade do recurso.

A Quantidade pode ser informada e o BDI Diferenciado recebe valor um (1).

O código é gerado de acordo com a Hierarquia, sendo que é o maior código de seu nível mais 1.

Se o recurso for solto sobre um serviço, o serviço será criado no mesmo nível.

Se o recurso for solto sobre uma obra/etapa o serviço será criado um nível abaixo.

O campo "Cód. Composição Local" possibilita a digitação do código da composição no cadastro de atividades.

O campo "Cód. Insumo Local" possibilita a digitação do código do insumo no cadastro de atividades.

O campo "Cód. Tarefa Aux." pode ser o mesmo para tarefas diferentes, se o parâmetro "Repetir Código Auxiliar de Planilha" estiver ativo no menu Opções | Parâmetros | TOTVS Obras e Projetos | Parâmetros do Projeto | Cálculo | Outros.

**Exemplo:**

Para a tarefa de código 001.01.02, o campo Código Tarefa Aux. pode ser 001;

Para a tarefa de código 002.01.01, o campo Código Tarefa Aux. pode ser 001.

O campo "Tarefa associada a Medida do Risco" informa se a tarefa está associada a uma medida de contenção/impulsão ou contingência de risco.

Os campos livres de tarefa são ativados através do Menu Opções | Parâmetros | TOTVS Obras e Projetos | Parâmetros do Projeto | Campos Livres, na pasta Campos Livres, subpasta Tarefas.

A associação será sempre da Planilha de Serviço para a Planilha de Atividade.

O campo "Quantidade de Equipe" pode ser informado manualmente na visão da planilha de atividades, e será utilizado na função de fórmula [Valor das Horas Produtivas de um Recurso da Tarefa (VLRHORASPRODUTIVASRECURSO)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385490).

**Arrastar Serviço em cima da Etapa da Planilha de Atividades:** É possível marcar uma ou mais tarefas da Planilha de Serviços e arrastar para uma etapa na Planilha de Atividades. Ao soltar o botão do mouse o sistema irá criar tantas atividades quanto forem os serviços que estão sendo arrastados para a Planilha de Atividades. A quantidade da atividade será igual ao saldo a alocar do serviço. Caso o usuário deseje, ele pode a qualquer momento alterar a quantidade da atividade, alterando consequentemente a quantidade associada.

A somatória das quantidades alocadas de um serviço não pode ser superior a quantidade total prevista na Planilha de Serviço.

Ao alterar a quantidade de uma atividade deverá recalcular o percentual do PERT.

A Unidade da atividade será a unidade do serviço.

O recurso (Composição, Insumo, Verba) será o mesmo do serviço.

As datas dos serviços associados deverão ser a data da etapa da atividade a qual ele foi associado.

O percentual do PERT não será preenchido.

Irá trabalhar gerenciando a etapa, por isto as datas das atividades folhas deverão obedecer a data da etapa.

Ao gerar a nova atividade copiar a data existente.

Permitir alterar a data da etapa replicando a alteração para as atividades folhas.

Pensar em um parâmetro que normatize onde a alteração pode ser feita: etapa ou folha.

Se houver etapa dentro de etapa e realizar alteração na data da etapa superior, não deverá alterar as datas das etapas internas.

Não será possível alterar datas para Obras (somente etapas).

As alterações de datas nas atividades folhas estarão condicionadas a restrição de predecessão.

Todos os demais campos da tarefa serão preenchidos com os valores do serviço (Descrição, Nome, Código Auxiliar da tarefa).

Caso a etapa já possua algumas atividades, as novas serão criadas abaixo da estrutura da última atividade.

**Arrastar Serviço em cima de Atividade:**Quando um ou mais serviços forem arrastados para cima de uma atividade, o sistema deverá descobrir a etapa em que esta atividade está inserida e criar uma atividade para cada serviço selecionado dentro desta etapa. A partir daí o comportamento será exatamente o citado no tópico "Arrastar Serviço em cima de Etapa" Serviço em cima de Subprojeto não será permitido.

Ao realizar uma associação de um serviço à planilha de atividades, este serviço não pode ter a sua quantidade inferior à quantidade associada. Neste caso o sistema consiste, para que a quantidade do serviço não seja inferior à quantidade associada.

**Tarefas de Timesheet:**Foi adicionado ao cadastro de tarefas uma nova opção chamada "Tarefa de Timesheet" que classificará a tarefa. Essa classificação permite um acompanhamento do projeto através dos índices de prazo (IDP), custo (IDC) e dedicação (IDD), que poderão ser analisados por tarefa e/ou recurso. Isto é, o projeto pode ou não utilizar Alocação de Recursos.  
Esses números serão alimentados através de um novo controle de apontamentos de tarefas, que será utilizado para registrar o tempo consumido, os recursos utilizados e o percentual de completude das tarefas.  
Os apontamentos poderão ser feitos manualmente ou através da execução de tarefas, que pode ser feito através do processo "Timesheet – Executar/Parar Atividade" ou na barra de ferramentas pelo 'try icon'.  
   
**Alterar quantidade pelo cronograma:**Na coluna "Alterar Qtde. Cronog." das planilhas de atividades e serviços, existe um checkbox para cada tarefa, que poderá ser marcado/desmarcado.   Ao marcar este checkbox em uma etapa ou obra, todos os filhos da respectiva etapa/obra serão marcados. Obras e etapas não terão essa informação gravada.

Se o parâmetro de projeto "Utiliza Planilha de Serviços" estiver marcado:

* O checkbox "Alterar Qtd. Pelo Cronog." ficará disponível para alteração somente através da Planilha de Serviços.
* Este checkbox não poderá ser alterado pela Planilha de Atividades.
* Ao alterar o checkbox de um serviço, todas as atividades vinculadas à ele sofrerão o reflexo da alteração. Ou seja, ao marcar o checkbox do serviço, o sistema irá marcar automaticamente o checkbox de todas as atividades vinculadas a ele. O mesmo ocorrerá ao desmarcá-lo.

Se o parâmetro de projeto "Utiliza Planilha de Serviços" estiver desmarcado, neste caso, a Planilha de Serviços fica indisponível para utilização e o checkbox "Alterar Qtd. Pelo Cronog." ficará disponível para alteração pela Planilha de Atividades.

**Tarefas com checkbox "Alterar Qtd. Pelo Cronog." marcado:**

* Ao alterar o cronograma planejado, a tarefa assumirá a quantidade total digitada no cronograma.
* A alteração da quantidade da tarefa será realizada no momento em que o cronograma for salvo.
* O cronograma planejado destas tarefas só poderá ser alterado manualmente ou pelo processo de Lançamentos Múltiplos no Cronograma.
* Tarefas com Insumos derivados ou fórmula de cálculo para a quantidade não terão suas quantidades calculadas quando já possuírem lançamentos no cronograma.
* Os demais processos do sistema não afetarão o cronograma planejado destas tarefas, por exemplo: Exportação Pert x Cronograma.

Ao alterar atividades, caso exista algum serviço vinculado à atividade, este também será alterado. O serviço adotará o somatório das quantidades de todas as atividades vinculadas a ele.

Ao alterar serviços, o sistema validará se a nova quantidade do serviço é suficiente para atender ao somatório de todas as atividades vinculadas a ele. Caso não seja suficiente, o sistema bloqueará a alteração.

Para as tarefas com checkbox "Alterar Qtd. pelo Cronog." desmarcado, nenhum comportamento será alterado.  
   
**Tarefas de Valor Cotado com aplicação de índices:** Em tarefas de cotado é possível definir seu valor informando manualmente no campo 'Valor Cotado', através do anexo 'Fórmula de Cálculo' ou aplicando índice.  Para realizar a indexação sobre o valor são necessárias três premissas:

* **Cadastrar um índice para cada data da moeda utilizada**: no cadastro de Moedas e Índices deve ser informado uma moeda ou índice.
* **Cadastrar cotações**: no mesmo cadastro acima, deve ser informado uma cotação para cada data utilizada posteriormente. A data será o parâmetro em que o TOP se baseará para efetuar o cálculo.
* **Informar 'Valor Base', 'Data de Indexação' e 'Moeda Indexadora'**: na tarefa de Valor cotado, é necessário que esses três campos sejam informados para que o cálculo do valor possa ser feito.  
  O valor indexado da tarefa de valor cotado será calculado utilizando o seguinte cálculo: *Valor cotado = Valor Base (tarefa) / (Valor do índice ou moeda na data de indexação da tarefa)) \* (Valor do índice ou moeda na Data base para indexação do Parâmetro de projeto)).*

**Exemplo:** 

Dada a moeda indexadora, Dólar (US$) com as seguintes cotações:

**Moeda         Data         Cotação**

US$       14/10/2014       3,30  US$

              15/10/2014       3,54

A tarefa terá como valor base 259,20 e Data de Indexação 14/10/2014.

O projeto está parametrizado para utilizar indexação com Data Base para Indexação 15/10/2014.

Utilizando a fórmula de cálculo o valor será o seguinte:  
Valor cotado: 259,20 / 3,30 \* 3,54 = 278,05

Assim como na utilização de indexação para cálculo de preço do insumo, as tarefas de valor cotado somente levarão em consideração a indexação caso o parâmetro 'Utiliza Indexação' estiver habilitado.

Assim como o valor de tarefas com recursos associados, o valor indexado em tarefas de valor cotado será calculado a partir do cálculo do projeto.

Caso seja informada uma moeda no campo Moeda Cotada, o valor indexado será calculado primeiramente e em seguida será convertido pelo índice da moeda cotada na data da conversão informada nos parâmetros do projeto.

Caso o projeto utilize cotação e tenha sido informada para a tarefa uma fórmula de cálculo, o valor calculado para a indexação prevalecerá.

Caso seja informada uma data de indexação que não contenha cotação cadastrada e essa mesma data for maior que a última cadastrada, o valor será calculado utilizando a cotação da última data cadastrada.

Caso seja uma data menor que a primeira informada, o valor não será calculado e uma mensagem será apresentada.

Esta funcionalidade não deverá estar disponível para projetos globais.

**Unidade e Local de Serviço na Tarefa:**Em [Planilha de Atividades](https://tdn.totvs.com/pages/viewpage.action?pageId=421385087) e [Planilha de Serviços](https://tdn.totvs.com/pages/viewpage.action?pageId=421385525) é possível associar a [Unidade e Local de Serviços](http://tdn.totvs.com/pages/viewpage.action?pageId=451251865) em uma determinada tarefa.

Na tela de edição da tarefa, na aba "Outros" existe dois lookups, o de Unidade de Serviço e de Local de Serviço, onde para definir o Local é necessário o preenchimento da Unidade.

Através do processo de Atualização Múltipla de Registros também é possível alterar a Unidade e Local de Serviço para várias tarefas ao mesmo tempo, basta selecionar a opção em "Campo" e definir a Unidade e Local.

**Anexos**

No anexo da Planilha de Atividades, existe a opção serviço(s) associado(s), que mostra para uma atividade quais serviços estão relacionados, a quantidade e saldo em cada atividade.

Ao clicar na etapa na planilha de atividades deverá mostrar todos os serviços associados as atividades que estiverem dentro desta etapa.

O anexo de serviço deverá permitir informar o percentual concluído do Pert da atividade relacionada. Este anexo dever funcionar tanto na Planilha de Atividades como no Pert.

A coluna 'Vlr. Lei Social' retorna o valor da lei social da tarefa. Caso a coluna não aparecer de imediato, é necessário utilizar o ícone 'Configurar Colunas', adicione-a e salve as configurações.

Quando for uma tarefa com preço cotado e que não tenha tido uma composição ou insumo associado o valor ficará em branco caso essa tarefa tenha tido um insumo ou composição associada a mesma apresenta o valor da lei social. Esta coluna também leva em consideração a quantidade de obras.

Atividades que possuem insumos associados e estes pertencem a um grupo de custo que tem incidência de lei social, terão seu preço unitário sempre incidindo leis sociais, independente da forma de aplicação (sobre o custo unitário do insumo ou sobre o total do grupo) definida para o projeto.

**Serviços Associados:**Em anexos Serviço(s) Associados(s), é possível visualizar os Serviços/Atividades Associados. Este anexo contém a descrição dos serviços relacionados, a quantidade relacionada ou alocada, percentual concluído desta atividade, quantidade a executar e unidade da atividade.

Na planilha de Atividades é possível realizar a associação por este anexo.

Ao associar um serviço, é possível editá-lo e visualizar a quantidade disponível.

Na planilha de Serviços esta opção é apenas para consulta, com a possibilidade apenas do usuário informar o % Concluído do serviço associado.

Uma forma de realizar um filtro em que o usuário pode informar quais tarefas das planilhas devem ser filtradas, existe a opção de Marcação de Filtro em cada atividade ou serviço com a possibilidade de realizar o filtro com apenas as atividades ou serviços que estiverem selecionados. Este filtro será bastante usado para lançar cronograma e Pert da planilha de atividades.

**Valor da Tarefa:**O valor da tarefa de serviço é o resultado da multiplicação da quantidade da tarefa pelo valor do recurso (composição ou insumo) associado.

O valor da Composição como recurso na tarefa é o somatório do valor parcial de cada recurso (composição ou insumo) associado.

O valor parcial do recurso se obtém multiplicando o valor arredondado do valor unitário da tarefa pela quantidade.

O custo parcial segue a mesma lógica, sendo obtido, multiplicando o custo unitário da tarefa pela quantidade.

Importante:

Para esses cálculos de valor e custo parciais mencionados deve-se considerar os parâmetros de arredondamento de valores, sendo eles: ArrendondarPlanilhaTarefa e NumCasasDecimaisPlanTarefa.

O valor unitário que é utilizado no cálculo do valor parcial pode ser impactado pelo BDI.

Os valores de Custo Unitário e Valor Unitário representam o Valor do Recurso da tarefa, mas para casos onde o tipo de recurso configurado for Valor Cotado é considerado o valor cotado da tarefa.

**Projeto vinculado:**Criado o campo "Projeto vinculado" na tela de planilha de atividade. Aba recurso.

O Parâmetro se encontra em Parâmetros do Projeto – Outros - Calcular Projetos Vinculados a Tarefas.

A tarefa que receber o projeto vinculado será uma tarefa de valor cotado.

Ao clicar no lookup para escolher o projeto a ser vinculado será exibido os projetos da coligada em questão.

Projeto revisado, no momento de vincular só apresentará a última revisão.

Com o parâmetro setado "Calcular Projetos Vinculados a Tarefas" o valor atualizado do projeto vinculado será considerado no cálculo do projeto. Caso contrário, não será considerado.

**Exemplo:**

Projeto A contém 2 tarefas no valor de R$2,50 cada. Total do projeto A →5,00;

Projeto B contém 4 tarefas no valor de R$2,50 cada. Total do projeto B -> 10,00;

No projeto A vinculo o projeto B;

Ao calcular o projeto A o resultado será R$15,00;

Edito o projeto B, incluindo mais uma tarefa no valor de R$5,00;

No projeto A realizo o cálculo do projeto, porém o parâmetro "Calcular Projetos Vinculados a Tarefas" não está setado;

O valor do projeto continua R$15,00;

Com o parâmetro setado o valor do projeto será R$20,00.

**Processos**

**Atualização Múltipla de Registros**: Realiza a atualização dos registros selecionados na Planilha de Atividades, de acordo com o campo e o valor.   
   
**Ativar ou Desativar Tarefas**: Permite ativar ou desativar as tarefas selecionadas na Planilha de Atividades. Caso desativado esta não tem o seu valor refletido no cálculo do projeto e cronograma.  
   
**Alterar Valor Cotado para Calculado e Calculado para Cotado**: Permite alterar uma atividade selecionada na planilha de atividade, que possui um recurso associado para uma atividade de valor cotado, ou retorná-la para calculado**.**   
   
**Alterar Serviço Direto para Indireto e Indireto para Direto**: Para definir se o serviço é de custo direto ou indireto. Os serviços de custo indireto não afetam diretamente o valor do projeto. Somente são considerados no cálculo do valor do BDI do projeto. A cor de um serviço (tarefa) que possui custo indireto pode ser definida através do Menu Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Exibição | Cores.

Ao definir uma Tarefa como Custo Indireto, os campos Valor Unitário Indireto, Valor Parcial Indireto, Custo Unitário Indireto e Custo Parcial Indireto serão automaticamente preenchidos, após executar o Cálculo do projeto.

Esses campos são utilizados para separar os custos Indiretos dos Diretos.

Caso seja necessário obter o somatório dos Valores Diretos e Indiretos, é possível criar campos calculados no grid.

   
**Trocar Código da Tarefa**:  Realiza a alteração do código da atividade selecionada na planilha de atividade, para o código desejado, a alteração de código de tarefas pode impactar em outros processos como : pedidos, contratos e dentre outros, por isso ao executar o processo uma mensagem é exibida na tela informando ao usuário que os vínculos permanecerão os mesmo, pois a relação não é feita pelo código e sim pelo identificador.

   
**Reorganizar Código das Tarefas**:  Reorganiza o código das atividades de acordo com o código inicial e código final. 

* É sugerido a tarefa corrente na visão como código inicial e final;
* Na definição da faixa serão ajustados os registros que estiverem dentro da faixa definida;
* Não é necessário selecionar tarefas.

**Exemplo:**

Tarefas: 001.01.05, 001.01.06 e 001.01.08

Se for informado a faixa 001.01.06 - 001.01.07, nada ocorre, pois dentro desta faixa se encontra somente a tarefa 001.01.06.  
Neste caso deveria ser informada a faixa 001.01.06 a 001.01.08 e automaticamente seria ajustado as tarefas 001.01.06 e 001.01.08.

Resultado: 001.01.05, 001.01.06 e 001.01.07

**Associar Tarefa Percentua**l: Processo permitido somente para serviços que utilizam valor cotado para associar uma atividade percentual.   
   
**Copiar Etapas e Tarefas**: Realiza o número desejado de cópias de etapas e atividades da planilha de atividades.   
   
**Alterar Nome e Descrição das Tarefas**: Para este processo é possível realizar a alteração conforme as seguintes opções: Nome da tarefa igual a descrição do recurso associado. Descrição da tarefa igual a descrição do recurso associado. Nome e descrição da tarefa igual a descrição do recurso associado. Nome da tarefa igual a descrição da tarefa**.**   
   
**Memória de cálculo da tarefa durante o projeto**: Exibe o período a quantidade o custo o custo total o valor e o valor total das atividades durante o projeto.   
   
**Alteração de Recursos da Tarefa**: Selecionando o tipo de recurso desejado, o sistema permite que outro recurso seja associado a atividade.   
   
**Alterar Hierarquia da Tarefa**: Este processo altera a hierarquia das tarefas conforme algumas validações que o sistema realiza: Não é possível criar uma tarefa filha sem ter uma tarefa pai existente. Não é possível serviço filho de um serviço. Não se pode criar uma etapa filha de um serviço. Não será possível etapa ou serviço com obra inválida.   
   
**Transformar Recurso Global em Local**: Realiza a transformação de um recurso global associado a uma atividade para um recurso local.   
   
**Lançamentos Múltiplos Cronograma**: Permite realizar vários lançamentos no cronograma de acordo com os períodos selecionados. Conforme a grandeza selecionada e permite aplicar nos cronogramas Previstos, Realizado e Medido. Ainda existe a opção de ratear o percentual informado entre todos os períodos selecionados.   
   
**Lançar cronograma automaticamente**: Faz o lançamento de acordo com as datas selecionadas e o tipo de cronograma Previsto, Realizado ou Medido. Exibindo além de tudo o cálculo de dias através do botão Calcular dias.  
   
**Exportar Planilha para o Excel com fórmulas**: Esta é uma funcionalidade que realiza a exportação da planilha de atividades completa com as fórmulas do Excel nos campos Valor Parcial, % na Obra e % Planilha.   
   
**Exportar Pert para o Cronograma**: Exporta o Pert para o cronograma de acordo com as opções selecionadas na Data de Origem, Cronograma de Destino, Converter Medições e Escopo da Conversão.

**Transformar Serviço em Etapa**: Modifica o tipo da tarefa, transformando-a em Etapa. Se o serviço (tarefa) selecionado tiver orçamento integrado com o TOTVS Backoffice o processo não será executado:

**Desmembrar Tarefas para a Folha de Produtividade:**Foi criado um processo na Planilha de Atividades onde será permitido o desmembramento de uma tarefa em vários locais de serviço.

Através do processo Desmembrar Tarefas da Planilha de Atividades é possível desmembrar uma atividades ligadas a um locais de serviço e uma [Equipe do Projeto](http://tdn.totvs.com/display/LRM/Equipe+de+Mobilidade).

Após a execução do processo a tarefa selecionada irá se transformar uma etapa e será criada uma nova atividade para a tarefa original e novas atividades para cada Local de Serviço com os campos de Unidade de Serviço, Local de Serviço e Equipe preenchidos.

**Exemplo:**

Processo executado

A quantidade desmembrada será dividida igualmente entre as novas tarefas criadas para cada local de serviço selecionado, ficando o restante para a tarefa original.

O valor de Mão Obra da Tarefa se refere aos valores dos insumos de Natureza "Mão de Obra", onde esses valores não tem a incidência de Leis Sociais.

Através das opções disponíveis em “Adicionar descrição da Unidade de Serviço e Local de Serviço” é possível concatenar a descrição da Unidade e Local de Serviço no nome da tarefa que será resultado do desmembramento, na descrição ou em ambos. Essa opção somente estará disponível se o parâmetro de projeto "Igualar Descrição/Nome da tarefa a Descrição do recurso que está sendo associado" não estiver marcado.

Através dos parâmetros de cores (Parâmetros de Projeto/Exibição/Cores) é possível definir uma cor diferenciada para a tarefa que foi utilizada para o desmembramento.

Caso o processo seja executado novamente para a tarefa original, não será criada uma nova etapa. Neste caso apenas será criado uma nova atividade para cada local de serviços.

Através do desmembramento é possível definir informações para o PERT e cronograma para as tarefas que serão criadas, basta definir a Nova Data Início e a Nova Duração, sendo que essas informações são Data Inicio Programada e Duração da tarefa selecionada, os Dias de Folga e a opção de Sequenciar Datas de Início das Tarefas caso deseje. Ao executar o processo, as tarefas criadas terão suas datas de início programada alteradas, assim como a duração, e no caso de sequenciar as datas das mesmas, serão incluídas as predecessoras em relação à cada tarefa criada, considerando a folga (defasagem).

Se a opção "Criar uma Folha Tarefa de Produtividade para cada Tarefa desmembrada" estiver marcada, serão criadas novas Folhas Tarefas com as respectivas novas tarefas associadas com o valor alocado de acordo com o desmembramento.

Para definir o Valor Alocado do item da folha tarefa, existem duas possibilidades, a primeira sem a opção "Recalcular projeto antes de criar as Folhas Tarefas" que calcula a partir do valor unitário da tarefa origem vezes a quantidade da nova tarefa criada, a segunda possibilidade, esta com a opção de recalcular o projeto marcada, busca o valor de mão de obra da tarefa criada, porém é realizado o cálculo do projeto após a criação das tarefas para que o valor possa ser resgatado.

Se a tarefa selecionada para desmembramento tiver orçamento integrado com o TOTVS Backoffice o processo não será executado:

**Melhorias para Mercado Internacional - Cálculo por Rendimento Diário**

Disponível somente para o mercado internacional, para licitações públicas que exigem o detalhamento dos serviços (composições) por rendimento.

Seguir os passos:

* No módulo "Projetos / Construção e Projetos" acesse a visão de projetos;
* Selecione um projeto;
* Acesse "Orçamento -> Planilha -> Planilha de Atividades";
* Selecionar uma tarefa que tenha como recurso uma composição do tipo "por Rendimento";
* Acessar "Funções Principais -> Outros -> Calendário da Atividade";
* Incluir um calendário com horas do turno diferente da jornada da composição;
* Acione "Salvar";
* O sistema irá emitir o seguinte alerta "A jornada definida no calendário desta atividade está diferente da jornada definida no recurso. Para recursos do tipo composição por rendimento e recomendado que as jornadas sejam compatíveis.";
* Acione "Ok";
* O sistema irá gravar o calendário.

  Informações Complementares

---

[Cronograma](http://tdn.totvs.com/display/LRM/Cronograma+Anexos)

[Unidade e Local de Serviço](http://tdn.totvs.com/pages/viewpage.action?pageId=451251865)

  Processos da Planilha de Atividades

---

[Replanejamento de Índices](https://tdn.totvs.com.br/pages/releaseview.action?pageId=421385544)

[Importar Apropriações das Tarefas do Backoffice](https://tdn.totvs.com/pages/releaseview.action?pageId=518472242)

[Associar Recursos às Tarefas](https://tdn.totvs.com/pages/viewpage.action?pageId=528477305)
