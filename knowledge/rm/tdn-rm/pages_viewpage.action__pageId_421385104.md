---
content_hash: 7f1ec54e8eb0214e75a14ccf5ed6a42ec11a8070812277998cc9c16a23cd003e
fetched_at: '2026-06-29T00:09:14.054748+00:00'
page_id: '421385104'
product: rm
source: tdn-rm
title: Apropriação de Serviço/Insumo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385104
version: 91
---

A apropriação de insumos consiste na efetuação de registros diários do consumo (compra ou gasto) de insumos na obra, possibilitando um acompanhamento físico e financeiro da mesma através de um comparativo entre o previsto e o apropriado.

A apropriação de insumos de mão-de-obra pode ser feita informando os funcionários que executaram determinada atividade. Para isso é necessário Integrar com RM Labore.

A apropriação de insumos de equipamento e de transporte pode ser feita informando os bens que foram necessários para executar determinada atividade.

Para isso é necessário Integrar-se com RM Bonum(Integrado com Patrimonial).

Nesta janela serão listados os insumos apropriados, de acordo com o filtro utilizado.

É possível cadastrar as apropriações dos insumos aplicados a cada obra do projeto.

Os lançamentos podem ser feitos por serviço, por etapa ou obra.

Pode-se armazenar os valores em uma outra moeda.

É possível realizar o cadastro de uma nova apropriação utilizando a visão, basta utilizar seta para baixo \[ ↓ \] , que serão habilitadas as opções de código tarefa, código insumo, quantidade, moeda, (código funcionário, código funcionário responsável, código pessoa, código pessoa responsável, código bem (cada campo habilitado de acordo com o insumo utilizado.)) e código evento, para inserção das informações, da apropriação.

Para as funções abaixo, pode-se utilizar as respectivas teclas de atalho:

Inclusão Ctrl + Ins

Exclusão Ctrl+ Del

Edição   Ctrl + Enter

**Não será realizada a Apropriação caso o projeto se encontre nos status: Paralisado, Concluído, Revisado ou Cancelado.**

Na visão das Apropriações, o único campo passível de alteração é 'Quantidade':

Caso queira modificar o conteúdo de algum dos demais campos, é preciso acessar o registro através do botão editar ou  Ctrl + Enter:

   
Apropriação de Serviço/Insumo - Item a Item  
**Tarefa**  
Código: Selecione o código da tarefa ao qual o insumo pertence. Esse código pode ser um serviço, etapa ou obra.  
Caso não saiba o código da tarefa, realize a busca através do botão de filtro caracterizado pelas reticencias.  
   
Ao selecionar o código da tarefa, o nome, a descrição e a unidade da mesma serão preenchidas automaticamente. Se o nome for selecionado, o código, a descrição e a unidade serão preenchidas automaticamente.  
   
**Insumo**  
Código: Informe o código do insumo que está sendo apropriado.  
Caso não saiba o código do insumo, realize a busca através do botão de filtro

Ao selecionar o código do insumo, a descrição e a unidade do mesmo será preenchida automaticamente. Se a descrição for selecionada, o código e a unidade serão preenchidos automaticamente.  
Na tela Apropriação de Serviços/Insumos ao realizar uma apropriação de uma tarefa, existe a opção de filtrar apenas os insumos relacionados a tarefa, ou o filtro pode ser de todos os insumos relacionados ao projeto. Após marcar esta opção ao realizar o filtro no campo Insumo, o sistema irá respeitar o filtro selecionado anteriormente.  
O filtro também pode ser aplicado caso o cadastro seja realizado diretamente na grid, Quando a coluna "Insumo Tarefa"estiver selecionada o lookup de insumos trará em seu filtro apenas os insumos vinculados a tarefa, caso este campo não estiver selecionado o filtro do lookup trará como resultado todos os insumos do projeto.  
**Data. Movimento:** Este campo será preenchido automaticamente com a data atual, porém é um campo editável, desta forma a data poderá ser alterada.  
**Data Apropriação:** Este campo será preenchido automaticamente com a data atual, porém é um campo editável, desta forma a data poderá ser alterada.  
   
Na apropriação pode ser utilizado o parâmetro "Permite apropriar apenas serviço", menu Projeto|Construção e Projetos|Projetos, onde este parâmetro será responsável por realizar filtro no lookup de tarefa,  no momento da apropriação. Quando este parâmetro estiver ativo, as apropriações apenas poderão ser feitas por serviços, não sendo permitido apropriar em agrupadoras (Obras e Etapas). Quando este parâmetro não estiver ativo poderá ser apropriado em tarefa, etapa ou obra. Por padrão este parâmetro estará inativo.  
Não é permitido criar ou alterar apropriações onde a data apropriação é inferior a data limite para apropriação definida nos parâmetros do projeto, através do menu Projeto|Construção e Projetos|Projetos, pasta Apropriação, campo Data Limite para Apropriação.  
   
**Quantidade:** Informe à quantidade que foi apropriada para o insumo Apropriação de Insumo  
   
Se o insumo pertencer ao grupo DNIT Mão-de-obra e Equipamento, através do botão caracterizado pelas reticencias, ao lado do campo quantidade pode-se informar a jornada de trabalho do recurso. As horas trabalhadas serão informadas no campo quantidade.  
Se o insumo pertencer aos demais grupos DNIT informe a quantidade.  
Ao informar que o insumo não poderá ser fracionado em seu cadastro, mas na apropriação se informe uma quantia fracionada o sistema arredondara a quantidade de acordo com o parâmetro do projeto.   
**Preço Unitário:** Ao informar o insumo o sistema busca o preço do insumo. Se no momento do cadastro do insumo não foi informado o preço, na apropriação pode-se informar o preço do insumo.   
   
Se for informado um funcionário para a apropriação, o campo Preço Unitário será preenchido de acordo com a parametrização definida no menu Opções | Parâmetros | Totvs Obras e Projetos | Projetos, pasta Integrações, subpasta Outros, grupo Integrado com o RM Labore, subgrupo Origem do Preço da Apropriação.  
Valor Mão de Obra RM Labore: Marque esta opção caso você queira que o Preço Unitário da apropriação seja lançado de acordo com o valor hora do funcionário do RM Labore apropriado no Totvs Obras e Projetos.  
Ao buscar o valor do RM Labore, será feita outra verificação. Se o parâmetro " Fator de lei social" estiver marcado e na tela do Grupo de custo a lei social correspondente estiver marcada, será multiplicado o fator ao valor da mão-de-obra que foi informada pelo RM Labore.   
Valor Insumo: Marque esta opção caso você queira que o Preço Unitário da apropriação seja lançado de acordo com o valor do Insumo com leis no Totvs Obras e Projetos.  
Se for informado um funcionário para a apropriação, o campo Preço Unitário ficará ativo somente se o parâmetro **"Permite editar preço unitário da apropriação"** estiver ativo. Esse parâmetro é habilitado através do menu Opções | Parâmetros do projeto. O preço sugerido será o salário do funcionário dividido pelo número de horas da jornada de trabalho, se o parâmetro "Aplica leis sociais no preço do RM Labore" estiver inativo. Esse valor é arredondado seguindo a parametrização do TOTVS Obras e Projetos. Se o parâmetro "Aplica leis sociais no preço do RM Labore" estiver ativo será aplicada a taxa de lei social do grupo de custo do insumo que possui a função do funcionário da apropriação. Esse valor é arredondado seguindo a parametrização do TOTVS Obras e Projetos.  
Se o preço do insumo não estiver na moeda do projeto ele pode sofrer uma indexação, conversão ou ambas de acordo com a parametrização do projeto. Caso você queira apropriar em outra moeda, basta alterar a mesma e informar o novo valor.  
**Moeda:** O valor default deste campo será de acordo com os parâmetros do projeto. Parâmetros do projeto - Leis/ Outros - Moeda do projeto. Como se trata de um campo editavél, pode-se alterar a moeda.  
Uma apropriação pode ser efetuada em outra moeda.

Informe o histórico ou alguma observação referente à apropriação.  
Os campos citados abaixo ficarão habilitados no momento que for informado o insumo integrado com RM Labore ou com RM Bonum.  
**Código do Bem:** Código atribuído ao bem.  
**Descrição do Bem:** Descritivo do bem.  
Os campos Código do bem e descrição do bem ficam visíveis somente se o insumo pertencer ao grupo DNIT A (Equipamentos) ou F (Transporte) e se estiver integrado com o RM Bonum.  
   
**Cod. Funcionário:** Informe a chapa do Funcionário que esta executando a tarefa selecionada. Serão exibidos os funcionários cadastrados de acordo da função que está associada ao Insumo que está sendo apropriado.  
 **Cod. Funcionário Responsável:** Informe a chapa do Funcionário responsável que esta executando a tarefa selecionada.

Será possível informar a pessoa externa (Terceirizado). Esta busca será feita através do cadastro de pessoa externa do RM Labore.  
   
**Cod. Pessoa:** Informe a chapa do externo que esta executando a tarefa selecionada.   
**Cod. Pessoa Responsável:** Informe a chapa do externo responsável que esta executando a tarefa selecionada.

**Código do Evento:** Selecione o código do evento referente à apropriação de horas de funcionários.  
**Descrição do Evento:** Selecione a descrição do evento referente à apropriação de horas de funcionários. Se o código do evento for selecionado, a descrição será preenchida automaticamente e vice-versa.  
   
Os campos mencionados acima ficam habilitados somente se o insumo pertencer ao grupo DNIT Mão-de-obra e se estiver integrado com o RM Labore.

Um funcionário só pode ser apropriado se houver incidência de leis sociais sobre ele, ou seja, se ele pertencer ao grupo de mão-de-obra e se no cadastro do insumo para o qual está sendo apropriado houver uma função informada.  
Quando o funcionário está substituindo outro, ele recebe o valor que for maior. O funcionário substituto receberá o valor do salário do funcionário que está sendo substituído se ele for maior do que o dele. Caso contrário, continuará recebendo o seu próprio salário. Por essa razão, é necessário informar o funcionário substituído.  
Para realizar a associação de um funcionário Demitido/Férias é preciso dar permissão no perfil do usuário.  
Para utilizar a substituição, é necessário informar o funcionário atual para só então informar o funcionário substituído.  
Na apropriação deve-se optar entre informar Funcionário ou Pessoa. Os dois não poderão ser informados em uma mesma apropriação.   
Na apropriação deve-se optar entre informar Funcionário Responsável ou Pessoa Responsável. Os dois não poderão ser informados em uma mesma apropriação.   
Ao se informar Funcionário Responsável ou Pessoa Responsável não será possível informar Evento.

**Campos Complementares de Apropriação**  
São visualizados os campos complementares cadastrados no menu Cadastros | Campos Complementares. Nessa janela os dados devem ser informados. Caso tenha sido definida uma validação do campo complementar com base numa tabela dinâmica, o mesmo será validado nesse momento. Os campos complementares podem ser do tipo Data, Inteiro, Real ou Alfanumérico.

Tudo relacionado à log na apropriação será feito através do log de auditoria que é um aplicativo em uso no Corpore.

Se uma apropriação de Serviços/Insumos possuir uma transferência vinculada, apenas será permitida a alteração da observação e da quantidade, para maior. Os demais campos da tela estarão desabilitados não permitindo qualquer outro tipo de alteração:

A apropriação de Serviços/Insumos que tiver sido originada através de uma transferência de apropriações, não pode ser editada e por isso tem seus campos bloqueados:

Também não poderá ser excluida pela tela de Apopriação de Serviços/Insumos, somente através do processo de , da Visão de Apropriações

Através da coluna Origem da Apropriação, é possível saber onde tal lançamento teve sua origem:

Para saber mais sobre Transferência de Apropriações, .

 

Informações Complementares

---

 

 

 

 

[Mobilidade](http://tdn.totvs.com/display/LRM/Mobilidade)
