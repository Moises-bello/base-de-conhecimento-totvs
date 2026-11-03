---
content_hash: 76742ca93f3ecc8b6925713665ea59b789bd82c59c70615e8d77291d2c97b8d9
fetched_at: '2026-06-29T00:11:45.015672+00:00'
page_id: '819042199'
product: rm
source: tdn-rm
title: Tipo de Objeto de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819042199
version: 6
---

**Tipos de Objetos de Manutenção**

O parque alvo da manutenção é composto por objetos que podem ser equipamentos, veículos, máquinas, estruturas, e componentes de instalações. Definir uma Tipologia do parque é segmentá-lo por  
similaridade técnica e demanda de manutenção. A partir de tal segmentação é possível avaliar, planejar e executar ações de manutenções que devem ser aplicadas aos Objetos de Manutenção. Ao definir os tipos  
de objetos de manutenção estabelecemos o que será mapeado, equipamentos e os seus subconjuntos, que também são tratados como objetos de manutenção. Para cada Tipo é necessário definir o padrão e  
nome do primeiro e segundo(opcional) identificador, bem como os dados importantes que deverão ser levantados e cadastrados no processo de Mapeamento.

**Para definir a tipologia dos objetos de manutenção do parque, o usuário deverá acessar:**  “Objeto de Manutenção  / Tipos de Objetos de Manutenção”.  Na tela de visão é possível incluir, editar, excluir, atualizar, navegar pelos registros, localizar um registro, configurar colunas, exportar dados, imprimir relatórios, acessar Anexos, acessar Processos e aplicar filtros.

**Identificação**

Os identificadores podem ser um número de série, uma placa de veículo e etc. Para os identificadores poderá ainda ser definida uma máscara como no exemplo da figura 1 veremos mais tarde no cadastro de Objeto de Manutenção a aplicação da máscara no campo primeiro identificador.

A máscara segue o padrão do sistema que considera a seguinte lógica:

Alguns Objetos de Manutenção fazem apropriação de produtos sem a necessidade de abertura de uma ordem de serviço. Por exemplo: veículos requerem graxa, lubrificantes, combustíveis e outros produtos que podem ser apropriáveis diretamente. Nesse caso marque a opção “Apropriação direta de produto(s)?”. Crie um movimento de apropriação direta de produto no Gestão de Estoque e Faturamento e em seguida no Gestão de Manutenção acesse “Gerais”, Pasta “Movimentos” e marque a flag “Controla Apropriação Direta de Produto(s)” e informe tipo de movimento de apropriação direta cadastrado no Gestão de Estoque e Faturamento.

Múltiplos Indicadores de Uso permite marcar o checkbox do indicador de uso que o tipo objeto de manutenção utilizará. No cadastro de Objeto de Manutenção será possível desabilitar um ou todos os indicadores de uso herdados do tipo de objeto. O cadastro dos indicadores de uso default é feito em “Gerais”.

**Campos e Tabelas Opcionais**  
Permite incluir campos opcionais (numéricos e alfanuméricos) de acordo com a particularidade de cada objeto e/ou a necessidade da empresa. Esses campos ficarão visíveis no cadastro de objeto de manutenção .

* **Anexos – Posições do Tipo de Objeto**  
  Permite cadastrar as posições que um Objeto de Manutenção filho poderá ocupar ou agregar no objeto pai. Por exemplo: o Objeto de Manutenção Pneu (objeto-filho) pode ocupar o eixo traseiro esquerdo do Objeto de Manutenção veículo (objeto-pai). Marcando a opção “Não atualiza indicador de uso”, se você alterar o indicador de uso do objeto-pai, não será alterado o indicador de uso do objeto-filho, ou seja, do agregado.
* **Anexos – Mão-de-Obra por Tipo de Objeto**  
  Permite associar uma mão-de-obra habilitada para execução dos serviços para cada Tipo de Objeto de Manutenção, Modelo ou Submodelo. Quando o parâmetro “Disponibilizar todas as Mãos-de-Obra de obra quando não segmentado” estiver marcado e não haver segmentação de Mão-de-Obra. Todas as Mãos-de-Obra ficarão visíveis na abertura de Ordem de Serviço, caso a situação da Mão-deObra no RM Labore seja diferente de (férias, afastado, demitido e etc). Nas Ordens de Serviços a Mão-de-obra será alocada de acordo com sua disponibilidade. Para Mão-de-Obra terceirizada será necessário a integração do Gestão de Manutenção com RM Vitae. Caso não possua o RM Vitae, toda Mão-de-Obra alocada será proveniente do castrado de funcionários, realizado no Gestão de Manutenção com integração com o aplicativo RM Labore.
* **Anexos – Modelos / Submodelos**  
  Permite definir os modelos de cada Tipo de Objeto de Manutenção e o fabricante dos mesmos. É necessário cadastrar os fabricantes antes de definir os modelos. Acesse Cadastros / Fabricantes. No anexo do  cadastro de modelo é possível classificar os Submodelos de acordo com o Modelo de Objeto de Manutenção.

**Exemplo de Segmentação de um Parque:**

**Cod. submodelo:** código gerado automaticamente pelo sistema.  
**Descrição:** descrição do submodelo.  
**Preço:** valor da aquisição do submodelo.  
**Produto:** selecione um produto que poderá ser gerado um objeto de manutenção, para a coligada em questão. Este produto terá o tipo de objeto, modelo e Submodelo da associação correspondente com suas respectivas características.

Um produto será associado somente a um Submodelo, ou seja, se tentarmos associar o mesmo produto a outro Submodelo dará duplicidade na associação. Essa associação será necessária para que seja possível gerar Objeto de Manutenção a partir de produto e para enviar Objeto de Manutenção para o estoque. Veja mais detalhes no Processo enviar objeto de Manutenção para o estoque.

**Anexos – Gerais de Agregação / Posições Passíveis de Agregação no Objeto**  
Permite especificar as agregações entre os Tipos de Objetos de Manutenção. Assim ao tentar agregar um Objeto de Manutenção em outro com o qual ele não esteja vinculado, a agregação não será permitida. Caso exista o vínculo (exista o cadastro da agregação), serão disponibilizadas as posições pré-cadastradas entre esse dois Tipos de Objetos. No anexo do cadastro “Gerais de Agregação” é possível especificar as posições de agregação que foram cadastradas no anexo “Posições do Tipo de Objeto”.

**Anexos – Produto(s)**  
Permite informar o(s) produto(s) que poderá(ão) ser apropriados pelo(s) objeto(s) de manutenção. Um produto poderá ser especifico para um “Tipo de Objeto de Manutenção”, “Modelo” ou “Submodelo”. Informe o código do produto e a quantidade utilizada pelo Objeto de Manutenção. marcando o checkbox “Obriga Vida Útil na OS”, toda vez que o produto for inserido na Ordem de Serviço, o sistema solicitará que seja informado a vida útil do produto.

Percentual (%) de Vida Útil é recomendado pelo fabricante e deve ser informado em Cadastros / Produtos/ Serviços / Anexos / Produtos – Informações de manutenção. Ao preencher o campo, o produto irá vencer quando atingir X% da vida útil recomendada pelo fabricante sobre os valores de indicadores de uso (Dia, Kilometragem, Horas de Uso e/ou Ciclos). seja mais detalhes no tópico Aplicações de Produtos / Vida Útil.

**Produto Apropriável Diretamente?**  
Como foi dito anteriormente, alguns Objetos de Manutenção fazem apropriação de produtos sem a necessidade de abertura de uma ordem de serviço. Marcando o checkbox os campos que farão o controle de Apropriação Direta de Produtos ficarão habilitados.

**Consumo médio**

Digite a quantidade média consumida deste produto. A quantidade destes campos “Consumo médio” a serem exibidos está relacionada à  quantidade de Indicadores de Uso que o Objeto de Manutenção está utilizando. Por exemplo, se o veículo usa Quilometragem e Horas de uso, dois campos “Consumo médio” serão exibidos.

**Índice de Acompanhamento**  
Defina qual o Índice de Acompanhamento utilizar. O Índice selecionado fará o controle do consumo médio do produto. Para cadastrar os Índices de Acompanhamento acesse o menu Cadastros / Índices de Acompanhamento. O cadastro de Índices de Acompanhamento será detalhado mais tarde, quando em “Operações e Manutenção”.

**Processos – Segmentação Múltipla de Produtos**  
Permite associar os produtos a vários Tipos de Objeto de Manutenção, Modelo e Submodelos, evitando assim o trabalho manual de inserir vários produtos de cada vez. Veja mais detalhes no tópico Aplicações de Produtos / Segmentação de Produtos.

## Aplicação de Produtos

Muitos produtos utilizados pelos equipamentos, Objetos de Manutenção, devem ser controlados para que seja possível reduzir os custos de manutenção e evitar falhas que interrompam o funcionamento do mesmo. Tal redução é possível através da instalação de peças compatíveis, do controle da sua vida útil e acompanhamento do consumo dos produtos do tipo “consumíveis” - lubrificantes, combustíveis, suprimentos etc.

Os três processos que fazem parte de deste controle são:

1. Segmentação de Produtos.
2. Vida útil.
3. Apropriação Direta e Medição de Consumo.

Os produtos utilizados pela manutenção são aqueles cadastros no Sistema de Gestão de Estoque e Faturamento pela gestão de materiais. Porém nem todos os produtos e serviços transacionados pela empresa são peças e serviços utilizados pela manutenção. Com o objetivo de disponibilizar para a manutenção somente os seus produtos e serviços, no Sistema de Gestão de Estoque e Faturamento acesse o menu Cadastros / Produtos / Pasta Integração, deve-se habilitar o parâmetro “Disponível para Manutenção”.

## Segmentação de Produtos

Fazer a segmentação é determinar quais os produtos que podem ser utilizados por um determinado Tipo, Modelo e/ou Submodelo de Objeto de Manutenção. Ou seja, determinar as peças e consumíveis que atendem as especificações técnicas do fabricante e da gestão de manutenção para serem utilizados em um determinado grupo de equipamento ou para as unidades deste. A segmentação de produtos é um pré-requisito para os processos de Controle da Vida Útil e Aplicação Direta de Produtos. Os produtos podem ser associados a um Tipo, Modelo ou Submodelo.

A lista de produtos vinculada a um Tipo aplica-se a todos os Modelos e Submodelos de objetos deste tipo.

A lista de produtos vinculada a um Modelo aplica-se a todos os Submodelos de objetos deste modelo.

A lista de produtos vinculada a um Submodelo aplica-se somente aos objetos deste Submodelo.

## Vida Útil

A vida útil é recomendada pelo fabricante e deve ser informada em Cadastros / Produtos / Serviços / Anexos / Produtos – Informações de Manutenção. Ao informar a vida útil nos campos referente ao indicador de uso definido no Tipo de Objeto de Manutenção, o produto irá vencer quando atingir X% da vida útil recomendada pelo fabricante sobre os valores de indicadores de uso (Dia, Quilometragem, Horas de Uso, Ciclos e etc).

Exemplo:  
Considere o produto Correia Dentada, a vida útil será de 10000 km. Então no cadastro do Objeto de Manutenção / Anexo – Produtos do Objeto de Manutenção informe o produto e a data de inicialização para que a vida útil do produto comece a ser contada. O produto do Objeto de Manutenção será controlado através de apropriação direta de produto ou através da vida útil do produto.

É necessário ter um lançamento de indicador de uso para objeto de manutenção com data anterior a data de inicialização.

Após fazer essas parametrizações lance um indicador de uso para o objeto de manutenção com uma data posterior a data de inicialização.

Nesse estágio ao tentar abrir outra Ordem de Serviço para o Objeto de Manutenção que possui a peça correia dentada o sistema irá validar se a peça já atingiu o seu percentual de vida útil. Como a vida útil ainda não foi atingida, porque ainda faltam 7001 km, ao inserir a peça no item da ordem de serviço e tentar salvar o sistema irá emitir a seguinte mensagem.

“Atenção! A vida útil do (a) “Correia Dentada” ainda não foi atingido (a). Para que o processo continue, é necessária a autorização do supervisor do sistema ou usuário autorizado a liberar o processo.

Deseja continuar? “

Clicando no botão “SIM” , aparecerá a tela de liberação para entrada da senha do supervisor.

Para que haja essa restrição o usuário logado no sistema não poderá ter o perfil de “Supervisor” no cadastro de usuários. E também é necessário acessar o Cadastros / Segurança / Perfis / Acesso a Menus / Operações / Manutenção / Ordem de Serviço. Retire a permissão do usuário na tag de segurança “[03.01.01.26]  
Apropria Produto(s) com vida útil não vencida”.
