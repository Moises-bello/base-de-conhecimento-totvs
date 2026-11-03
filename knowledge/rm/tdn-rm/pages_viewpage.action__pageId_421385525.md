---
content_hash: 9c79d6853d25361c94e7d506eef156bf4bffe689bbe7390a63f0bc86fdb2081f
fetched_at: '2026-06-29T00:09:16.378415+00:00'
page_id: '421385525'
product: rm
source: tdn-rm
title: Planilha de Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385525
version: 8
---

Esta planilha possui um detalhamento menor, embora com todos os serviços necessários para execução do projeto, visto que o tempo de orçamento e elementos para análise não permitem maior detalhamento. Esta planilha tem a estrutura solicitada pela contratante da obra.  
   
Para habilitar o uso da planilha de serviços é necessário que o parâmetro Menu Opções| Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Planilha de Serviços a opção Utiliza Planilha de Serviços deve estar marcado.  
   
Para que seja possível alterar os recursos da Planilha de Serviços, o sistema deve ser parametrizado com as opções Menu Opções| Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Planilha de Serviços na opção Onde será Permitido alterar o executar:  
   
Opções:

* Planilha de Atividades
* Planilha de Serviços
* Ambos

A visão de tarefas exibirá somente obras/etapas/serviços do projeto atualmente selecionado, onde:  
  
Obras são compostas por etapas e serviços.  
Etapas podem ou não ser compostas por serviços.  
  
Para que exista uma etapa/serviço, deve-se obrigatoriamente existir uma obra.  
  
As tarefas são compostas por obras, que se dividem em etapas e as etapas podem possuir vários serviços.   
Antes de cadastrar uma etapa, deve-se cadastrar a obra, com o código de acordo com a máscara da tarefa (obras, etapas e tarefas) parametrizada no sistema (Menu Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Exibição).  
  
A obra aparecerá na listagem das tarefas escrita da cor definida no Menu Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | Pasta Exibição | Cores.  
  
Depois de cadastrada a obra, cadastra-se as etapas, com o código da máscara um nível abaixo ao da obra.  
Se não houver nenhum item cadastrado, pressione Insert, Seta para baixo ou clique no ícone ' Incluir '. Dessa forma, o código da obra será gerado, automaticamente, de acordo com a máscara.  
  
Após cadastrar a obra, estando com o cursor posicionado sobre a mesma, ao pressionar Insert ou Seta para Baixo ou no ícone 'Incluir', o código sugerido será o código de uma obra.  
  
Após cadastrar a etapa, estando com o cursor posicionado sobre a obra, ao pressionar Insert ou Seta para Baixo ou no ícone 'Incluir', o código sugerido será o código de uma etapa.  
  
Após cadastrar a etapa, estando com o cursor posicionado sobre a mesma, ao pressionar Insert ou Seta para Baixo ou no ícone 'Inserir nova linha', o código sugerido será uma subetapa ou serviço (dependerá do que você informar para o item).  
  
Para cadastrar um serviço, posicione no serviço que tem código anterior ao que o serviço terá e pressione Insert ou o ícone 'Incluir'. Se o serviço for o último da visão, poderá utilizar Seta para baixo. E assim, por diante.  
  
Para a função de Exclusão pode-se utilizar as teclas de atalho Ctrl + Del.  
Para a função de Inclusão pode-se utilizar a tecla Ctrl + Ins.  
O cadastro de uma nova obra ou a alteração de uma obra já cadastrada pode ser feito também através da janela de edição de obras.  
Quando uma tarefa tiver um recurso associado, a unidade não poderá ser alterada, pois ela é a mesma unidade do recurso (composição ou insumo).  
Quando uma tarefa tiver um valor cotado e for associar um recurso (composição / recurso), o valor cotado será desativado e o recurso será ativado.  
Insumos percentuais não podem ser associados à tarefas.  
Com a visão de composições ou de insumos aberta, pode-se arrastar um recurso e soltá-lo na visão de Tarefas. Uma tela de diálogo é aberta e você pode associar um recurso à tarefa ou incluir uma nova atividade com o recurso.  
Se estiver associando uma composição à tarefa e já existir uma composição associada, a mesma será substituída. Caso já exista um insumo associado à tarefa, o mesmo será excluído da tarefa. Se estiver associando um insumo à tarefa e já existir uma composição associada à tarefa, a mesma será excluída da tarefa. Se a tarefa for uma etapa ou uma obra não serão permitidas as associações de composições ou insumos. Se estiver criando uma nova tarefa, a mesma é criada com o Nome, a Descrição e a Unidade do recurso. A Quantidade pode ser informada e o BDI Diferenciado recebe valor um (1). O código é gerado de acordo com a Hierarquia, sendo que é o maior código de seu nível mais 1. Se o recurso for solto sobre um serviço, o serviço será criado no mesmo nível. Se o recurso for solto sobre uma obra/etapa o serviço será criado um nível abaixo.  
A associação será sempre da Planilha de Serviço para a Planilha de Atividade.  
Arrastar Serviço em cima da Etapa da Planilha de Atividades:  
É possível marcar uma ou mais tarefas da Planilha de Serviços e arrastar para uma etapa na Planilha de Atividades.   
Ao soltar o botão do mouse o sistema irá criar tantas atividades quanto forem os serviços que estão sendo arrastados para a Planilha de Atividades.  
A quantidade da atividade será igual ao saldo a alocar do serviço. Caso o usuário deseje, ele pode a qualquer momento alterar a quantidade da atividade, alterando conseqüentemente a quantidade associada.

O campo "Quantidade de Equipe" pode ser informado manualmente na visão da planilha de serviços, e será utilizado no cálculo da função de fórmula [Valor das Horas Produtivas de um Recurso da Tarefa (VLRHORASPRODUTIVASRECURSO)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385490).   
  
**Observação:**  
A somatória das quantidades alocadas de um serviço não pode ser superior a quantidade total prevista na Planilha de Serviço.  
Ao alterar a quantidade de uma atividade deverá recalcular o percentual do PERT.  
A Unidade da atividade será a unidade do serviço.  
O recurso (Composição, Insumo, Verba) será o mesmo do serviço.  
As datas dos serviços associados deverão ser a data da etapa da atividade a qual ele foi associado. O percentual do PERT não será preenchido.  
Irá trabalhar gerenciando a etapa, por isto as datas das atividades folhas deverão obedecer a data da etapa. Ao gerar a nova atividade copiar a data existente.   
Permitir alterar a data da etapa replicando a alteração para as atividades folhas. Pensar em um parâmetro que normatize onde a alteração pode ser feita: etapa ou folha.   
Se houver etapa dentro de etapa e realizar alteração na data da etapa superior, não deverá alterar as datas das etapas internas. Não será possível alterar datas para Obras (somente etapas). As alterações de datas nas atividades folhas estarão condicionadas a restrição de predecessão.  
  
Todos os demais campos da tarefa serão preenchidos com os valores do serviço (Descrição, Nome, Código Auxiliar da tarefa).  
Caso a etapa já possua algumas atividades, as novas serão criadas abaixo da estrutura da última atividade.

Ao definir uma Tarefa como Custo Indireto, os campos Valor Unitário Indireto, Valor Parcial Indireto, Custo Unitário Indireto e Custo Parcial Indireto serão automaticamente preenchidos, após executar o Cálculo do projeto.

Esses campos são utilizados para separar os custos Indiretos dos Diretos.

Caso seja necessário obter o somatório dos Valores Diretos e Indiretos, é possível criar campos calculados no grid.

Ao editar a tarefa é possível informar dados da mesma que esta divida em abas:

Identificação: Nome, codigo da tarefa , descrição, código tarefa aux., bdi da tarefa , quantidade, unidade custo indireto, valor cotado moeda cotada , condição de pagamento do serviço cotado , valor base, moeda de indexação etc.

Avanço Físico: Unidade de referência , formula de peso , peso nível etc.

Pert: Plano programado, Plano Fixado, Plano Real, Plano Base, Plano Cedo e Plano Tarde.

Recursos: Composição local e global,

Campos Livres: Campos criados conforme a necessidade.

Outros: Disciplica , curva de destribuição , tipo de tarefa usada para integração com o BIM etc,

Campos Complementares e Cronograma.

**Arrastar Serviço em cima de Atividade:**  
  
Quando um ou mais serviços forem arrastados para cima de uma atividade, o sistema deverá descobrir a etapa em que esta atividade está inserida e criar uma atividade para cada serviço selecionado dentro desta etapa. A partir daí o comportamento será exatamente o citado no tópico "Arrastar Serviço em cima de Etapa" Serviço em cima de Subprojeto não será permitido.   
  
O campo "Cód. Composição Local" possibilita a digitação do código da composição no cadastro de serviços.  
  
O campo "Cód. Insumo Local" possibilita a digitação do código do insumo no cadastro de serviços.  
  
O campo "Cód. Tarefa Aux." pode ser o mesmo para tarefas diferentes, se o parâmetro "Repetir Código Auxiliar de Planilha" estiver ativo no menu Opções | Parâmetros | TOTVS Obras e Projetos | Parâmetros do Projeto | Cálculo | Outros.  
  
**Anexos:**

**Atividade(s) associada(s)**  
  
No anexo da Planilha de Serviço, existe a opção Atividade(s) associada(s) que mostra para um serviço quais atividades estão relacionadas e a quantidade   
relacionada e saldo em cada atividade.   
  
Ao clicar na etapa na planilha de serviços deverá mostrar todas as atividades que estiverem dentro desta etapa.   
O anexo deverá permitir informar o percentual concluído do pert da atividade relacionada. Este anexo dever funcionar tanto na Planilha como no Pert.

**Exemplo:**

Para a tarefa de código 001.01.02, o campo Código Tarefa Aux. pode ser 001. Para a tarefa de código 002.01.01, o campo Código Tarefa Aux. pode ser 001.

Os campos livres de tarefa são ativados através do Menu Opções | Parâmetros | TOTVS Obras e Projetos | Parâmetros do Projeto | Campos Livres , na pasta Campos Livres, subpasta Tarefas.

**Observações:**

A coluna 'Vlr. Lei Social' retorna o valor da lei social da tarefa. Caso a coluna não aparecer de imediato, é necessário utilizar o ícone 'Configurar Colunas', adicione-a e salve as configurações. Quando for uma tarefa com preço cotado e que não tenha tido uma composição ou insumo associado o valor ficará em branco caso essa tarefa tenha tido um insumo ou composição associada a mesma apresenta o valor da lei social. Esta coluna também leva em consideração a quantidade de obras.

Serviços que possuem insumos associados e estes pertencem a um grupo de custo que tem incidência de lei social, terão seu preço unitário sempre incidindo leis sociais, independente da forma de aplicação (sobre o custo unitário do insumo ou sobre o total do grupo) definida para o projeto.

Em anexos Serviço(s) Associados(s), é possível visualizar os Serviços/Atividades Associados. Este anexo contém a descrição dos serviços relacionados, a quantidade relacionada ou alocada, percentual concluído desta atividade, quantidade a executar e unidade da atividade.

Na planilha de Atividades é possível realizar a associação por este anexo. Ao associar um serviço, é possível editá-lo e visualizar a quantidade disponível. Na planilha de Serviços esta opção é apenas para consulta, com a possibilidade apenas do usuário informar o % Concluído do serviço associado.

Existe uma forma de realizar um filtro em que o usuário pode informar quais tarefas das planilhas devem ser filtradas, existe a opção de Marcação de Filtro em cada atividade ou serviço com a possibilidade de realizar o filtro com apenas as atividades ou serviços que estiverem selecionados. Este filtro será bastante usado para lançar cronograma e Pert da planilha de atividades.

**Atenção:**

Para limitar o número de registro exibidos na Planilha de Serviços acesse: Cadastro->Segurança->Administrativa->Servidor de aplicação. No campo Id do server exibido, escolher: PrjPlanilhaServicoData e informar o número máximo de registros que deseja ser exibido.

Caso não limite os registros apresentados na Planilha de Serviços todas as linhas de registros serão apresentadas. Ou seja, todos os Serviços cadastrados no projeto.

**Valor da Tarefa**

O valor da tarefa de serviço é o resultado da multiplicação da quantidade da tarefa pelo valor do recurso(composição ou insumo) associado. O valor da Composição como recurso na tarefa é o somatório do valor parcial de cada recurso(composição ou insumo) associado. O valor parcial do recurso se obtém do valor arredondado do custo unitário multiplicado pelo coeficiente do recurso da composição.

**Alterar quantidade pelo cronograma.**

Na coluna "Alterar Qtde. Cronog." da planilhas de atividades e serviços, existe um checkbox para cada tarefa, que poderá ser marcado/desmarcado.

Se o parâmetro de projeto "Utiliza Planilha de Serviços" estiver desmarcado: Neste caso, a Planilha de Serviços fica indisponível para utilização e o checkbox "Alterar  Qtd. pelo Cronog." ficará disponível para alteração pela .

**Tarefas de Valor Cotado com aplicação de índices:**

Em tarefas de cotado é possível definir seu valor informando manualmente no campo 'Valor Cotado', através do anexo 'Fórmula de Cálculo' ou aplicando índice. Para realizar a indexação sobre o valor são necessárias três premissas:

Cadastrar um índice para cada data da moeda utilizada: no cadastro de Moedas e Índices deve ser informado uma moeda ou índice. • Cadastrar cotações: no mesmo cadastro acima, deve ser informado uma cotação para cada data utilizada posteriormente. A data será o parâmetro em que o TOP se baseará para efetuar o cálculo. • Informar 'Valor Base', 'Data de Indexação' e 'Moeda Indexadora': na tarefa de Valor cotado, é necessário que esses três campos sejam informados para que o cálculo do valor possa ser feito.

O valor indexado da tarefa de valor cotado será calculado utilizando o seguinte cálculo: Valor cotado = Valor Base (tarefa) / (Valor do índice ou moeda na data de indexação da tarefa)) \* (Valor do índice ou moeda na Data base para indexação do Parâmetro de projeto)).

**Exemplo:** Dada a moeda indexadora, Dólar (US$) com as seguintes cotações: Moeda         Data         Cotação  US$       14/10/2014       3,30  US$       15/10/2014       3,54

A tarefa terá como valor base 259,20 e Data de Indexação 14/10/2014. O projeto está parametrizado para utilizar indexação com Data Base para Indexação 15/10/2014. Utilizando a fórmula de cálculo o valor será o seguinte:  
Valor cotado: 259,20 / 3,30 \* 3,54 = 278,05

**Observação:**  Assim como na utilização de indexação para cálculo de preço do insumo, as tarefas de valor cotado somente levarão em consideração a indexação caso o parâmetro Utiliza Indexação estiver habilitado. Assim como o valor de tarefas com recursos associados, o valor indexado em tarefas de valor cotado será calculado a partir do cálculo do projeto. Caso seja informada uma moeda no campo Moeda Cotada, o valor indexado será calculado primeiramente e em seguida será convertido pelo índice da moeda cotada na data da conversão informada nos parâmetros do projeto.

Caso seja informada uma data de indexação que não contenha cotação cadastrada e essa mesma data for maior que a última cadastrada, o valor será calculado utilizando a cotação da última data cadastrada.  Caso seja uma data menor que a primeira informada, o valor não será calculado e uma mensagem será apresentada.

**Observação**:

Esta funcionalidade não deverá estar disponível para projetos globais.

**Unidade e Local de Serviço no Serviço**

Nas [Planilhas de Atividades](http://tdn.totvs.com/pages/viewpage.action?pageId=421385087) e Serviço é possível associar a [Unidade e Local de Serviços](http://tdn.totvs.com/pages/viewpage.action?pageId=451251865) em um determinado Serviço. Na tela de edição do serviço, na aba "Outros" existe dois lookups, o de Unidade de Serviço e de Local de Serviço, onde para definir o Local é necessário o preenchimento da Unidade.

Através do processo de Atualização Múltipla de Registros também é possível alterar a Unidade e Local de Serviço para vários serviços ao mesmo tempo, basta selecionar a opção em "Campo" e definir a Unidade e Local.

Como Fazer

---

[Unidade e Local de Serviço](http://tdn.totvs.com/pages/viewpage.action?pageId=451251865)

Informações Complementares

---

e
