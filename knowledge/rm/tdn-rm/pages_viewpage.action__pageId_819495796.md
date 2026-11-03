---
content_hash: 156e3f064ae2fdea9836649d1c523f78b533e78724f94cc6c64b447930055805
fetched_at: '2026-06-29T00:11:45.114411+00:00'
page_id: '819495796'
product: rm
source: tdn-rm
title: Objeto de Manutenção - TCOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819495796
version: 9
---

Por meio do cadastro de Objeto de Manutenção podemos gerenciar todos os equipamentos e seus subconjuntos mapeados. Bem como seu histórico de manutenção, agregação, proprietário, responsável, localização, centro de custo, acessórios e informações complementares específicas de cada tipo de objeto. Para cadastrar o Objeto de Manutenção, acesse menu  Objeto de Manutenção. Na tela de visão é possível incluir, editar, excluir, atualizar, navegar pelos registros, localizar um registro, configurar colunas, exportar dados, imprimir relatórios, acessar Anexos, acessar Processos e aplicar filtros.

**Pasta Identificação**  
Podemos identificar o equipamento de acordo com a tipologia definida para o parque. A partir da escolha de um Tipo de objeto de manutenção, escolhemos o fabricante dentre aqueles que fabricam este tipo. A partir da escolha do fabricante teremos disponível o modelo fabricado pelo mesmo e os submodelos de cada modelo. O campo “Cod. Tipo de Objeto” pode ser configurado para receber sempre um objeto default. Acesse o menu Gerias, Pasta “Nome de Campos e Tabelas” e no comboBox “ Tipo de Objeto de Manutenção Principal” informe o tipo de objeto que deverá fica default no cadastro de Objeto de Manutenção. Caso trabalhe com vários Tipos de Objetos de Manutenção marque o checkbox “Permite Múltiplos Tipos de Objetos de Manutenção”. Assim no cadastro de Objeto de Manutenção será possível informar outros códigos de Tipo de Objeto de Manutenção.

O “Tipo de Objeto de Manutenção Principal” será obrigatório quando o parâmetro “Permite Múltiplos Tipos de Objetos de Manutenção” estiver desmarcado O “Primeiro” e o “segundo Identificador” foram definidos no cadastro de Tipo de Objeto Manutenção. No nosso exemplo do Tipo de Objeto veículo FIESTA, definimos a mascara para o primeiro identificador e o mesmo será usado aqui na tela de cadastro de objeto de manutenção.

**Cod. Tipo de Objeto:** é de preenchimento obrigatório e informa o código do tipo objeto que será cadastrado.  
**Fabricante:** informa o fabricante do objeto de manutenção.  
**Cod. Modelo:** informe o código do modelo do objeto de manutenção.  
**Cod. Submodelo:** informe o código do Submodelo do objeto de manutenção.  
**Data de Venda:** é utilizado normalmente em movimentos de ordem de serviço com garantia.  
**Data de Fabricação:** é a data que o objeto foi fabricado.  
**Ano de Fabricação:** é preenchido automático pelo sistema, a partir do preenchimento do campo “Data de Fabricação”.  
**Ano do Modelo:** digite o ano do projeto do modelo.  
**Valor de Aquisição:** é o preço de compra do objeto de manutenção.

**Estado de Conservação:** é de preenchimento obrigatório e é utilizado para definir o estado atual de conservação do objeto de manutenção. Os estados disponíveis são: novo, usado, reformado, sucateado e danificado e indefinido. O estado de conservação pode ser alterado pelo usuário. Porém, para os estado reformado e sucateado a alteração é realizada pelo sistema.

**Novo:** O Objeto nunca foi usado.  
**Usado:** O Objeto que já está sendo utilizado.  
**Reformado:** Ó Objeto já passou por um processo de reforma.  
**Danificado:** Não pode ser utilizado, não pode ser agregado a outro objeto.  
**Sucateado:** O objeto impróprio para uso.

* Quando é emitido uma Ordem de Serviço do tipo reforma, o sistema altera o “Estado de Conservação” do objeto de manutenção para “Reformado”.
* Quando um objeto de manutenção é “Sucateado” o sistema atualiza o seu “Estado de Conservação” e não é permitido alterar os seus dados.

Objetos sucateados não podem ser alterados, agregados, mandados para o estoque e nem gerar ordem de serviço. Todo o Objeto que for sucateado deverá ter um motivo do sucateamento informado.

“**Status**” é de preenchimento obrigatório e poderá ser utilizado para classificar o Objeto de Manutenção de acordo com a necessidade da gestão de manutenção. Para cadastrar os Status acesse o menu Cadastros / Tabelas Auxiliares / Manutenção / Status do Objeto de Manutenção. Em Gerais na Pasta Identificação, ao marcar o checkbox “Campo Status do Objeto de Manutenção é Obrigatório” torna-se obrigatório o Status no cadastro do Objeto de Manutenção.

O status não deve ser utilizado para expressar situações alteradas freqüentemente, porque é difícil a atualização do cadastro de todos os objetos com freqüência.

Ao alterar o status o sistema não mantém histórico do mesmo.

**Situação do Objeto de Manutenção**: informa a situação do objeto em relação à disponibilidade e localização do mesmo dentro da oficina.

**Normal:** o equipamento ou subconjunto encontra-se disponível.  
**Agregado:** o objeto de manutenção é um objeto agregado a um equipamento ou outro Objeto de Manutenção.  
**Oficina:** o equipamento ou subconjunto encontra-se em manutenção interna. Existe ordem de serviço Em Andamento para o mesmo. Caso exista ordem de serviço aberta com status “Aguardando Análise” ou “Não Iniciada” o status continuará “Normal”.  
**Transferido:** objeto transferido para outra coligada.  
**Em Terceiros:** objeto com ordem de serviço para terceiros em andamento.  
**Estoque:** objeto enviado para estoque. Ao apresentar esta mensagem o sistema também informa o local de estoque.

Filial e a Localização do objeto de manutenção são tratadas no processo de transferência.

**Centro de Custo:** ao qual o Objeto de Manutenção esta vinculado. Quando este é um patrimônio o centro de custo é definido no Patrimonio e não fica disponível para edição no Manutenção de Equipamentos. Se o vínculo for desfeito, o Centro de Custo, no Manutenção de Equipamentos, receberá o valor nulo.

**Cliente/Fornecedor:** é associado ao Objeto de Manutenção. Este campo pode ser utilizado em algumas situações específicas:

* Equipamento de terceiros alugado para a empresa: o campo informa o fornecedor do equipamento.
* Equipamento de cliente em manutenção na Empresa: o campo informa o cliente proprietário do equipamento.
* Equipamento Alugado pela empresa: o campo informa o cliente locatário do equipamento.

Quantidade de Reformas: mostra a quantidade de reformas que já foram executadas para o Objeto de Manutenção. Ao emitir uma Ordem de Serviço e marcar o checkbox “Reforma” na Pasta Identificação da OS, o sistema incrementa em uma unidade este campo no momento em que a OS tiver com o seu status alterado para “Terminado” ou “A Faturar”.

Ao cancelar ou reiniciar uma Ordem de Serviço de Reforma do respectivo Objeto de Manutenção que estava com status “Terminado” ou “A Faturar”, este campo será decrementado em uma unidade.

**Data de Criação:** é a data de inclusão do Objeto de Manutenção no Sistema.

Clicando no botão “Verificar Local de Instalação” o sistema emitirá uma mensagem informando onde o Objeto de Manutenção se encontra instalado. A mensagem mostra o código do Cliente/Fornecedor e nome, o local da instalação e endereço completo. Para efetuar a instalação do Objeto de Manutenção, acesse o menu Objeto de Manutenção. Para se fazer uma instalação é necessário acessar o menu Cadastros / Clientes / Fornecedores, selecionar o cliente ou fornecedor onde será feita a instalação do objeto e depois em anexos / Locais de Instalação e cadastrar o local e o endereço onde será feita a instalação do objeto de manutenção.

Os campos “Identificador do Objeto Raiz”, “Identificador do Objeto Pai” e “Código da Posição do Objeto Filho”, serão apresentados quando o objeto filho estiver agregado a outro objeto pai. Por exemplo: o objeto Pneu (filho) agregado ao objeto Veículo (pai). A diferença entre “Identificador do Objeto Raiz” e “Identificador do Objeto Pai” é quando tiver a seguinte situação: o pneu agregado ao veículo e o step agregado ao pneu. Então na edição do objeto step, o veículo seria “Identificador do Objeto Raiz”, o pneu “Identificador do Objeto Pai”.

Clicando no botão “Mudar posição” é possível mudar a posição do objeto, desagregando e agregando novamente na posição desejada.

**Pasta Dados Complementares**  
Permite incluir um funcionário responsável e uma descrição para o objeto de manutenção. Basta digitar as observações no espaço apropriado.

**Pasta Campos Configuráveis**  
Será exibida quando houver configurações de campos no cadastro do Tipo de Objeto de Manutenção, Pasta Campos e Tabelas Opcionais. Os campos serão usados para inserir informações de acordo com a particularidade de cada objeto e/ou a necessidade da empresa.

**Pasta Indicador(es) de Uso**  
Permite visualizar os lançamentos de indicadores de uso dos Objetos de Manutenção. Esta Pasta só ficará visível se houver indicadores de uso habilitados no cadastro de Tipos de Objeto de Manutenção, em Objeto de Manutenção / Tipos de Objeto de Manutenção. Os indicadores de uso poderão estar habilitados ou desabilitados para um Objeto de Manutenção mesmo que tenha sido definido um indicador de uso para mesmo no Tipo de Objeto de Manutenção.

**Medidor e Acumulado:** O valor indicado no medidor do indicador de uso é o valor Medido ou valor do medidor. O valor Acumulado é o total de uso do objeto. Os valores acumulados e medidos são iguais caso o medidor não tenha sido alterado, zerado ou trocado por outro cuja medida seja diferente do valor acumulado. Em Gerais / Parâmetros / Sistemas / Pasta identificação o parâmetro “Campo “Medidor” é obrigatório” estiver marcado, será obrigatório o preenchimento do indicador de uso no cadastro do objeto de manutenção. Caso contrário, não será necessário preenchê-lo.

**Média dia:** média diária dos indicadores de uso, calculada em um intervalo de tempo informado pelo usuário ou em um período parametrizado pelo sistema. Para configurar estes parâmetros acesse Gerais / Parâmetros / Sistema / Pasta Identificação, Tipo do Cálculo da média dos Indicadores de Uso. O cálculo tem dois tipos: manual e automático – número de dias para o cálculo.

**Manual:** o usuário informa manualmente o intervalo para o cálculo. O cálculo manual poderá ser feito pelo botão “Calcular Média/Dia” na Pasta indicadores de uso, ou em Processos “Calcular média diária de  
indicador de uso”.

**Automático:** número de dias para o cálculo: será calculado automaticamente pelo sistema de acordo como número dias parametrizado.

Em Manutenção / Parâmetros / identificação existe a caixa “Consistência de Média de Uso”. A “Consistência de média de uso” está relacionada à média dos valores dos Indicadores de Uso, e possibilita advertir e/ou bloquear a inserção dos indicadores de uso caso estes estiverem acima da média diária de inserção. Para que isso ocorra, é preciso que a Média dos Indicadores de Uso esteja calculada.

Após calculada a média, o sistema irá verificar cada inserção de valor dos Indicadores de Uso, baseado nessa média, o sistema vai enviar uma advertência. Veja abaixo como o sistema poderá advertir:

* Avisar se Ultrapassar (%): A porcentagem aqui é baseada na média diária do indicador de uso. Se o valor inserido para o indicador de uso ultrapassar esta porcentagem, o sistema irá advertí-lo.
* Barrar se Ultrapassar (%): A porcentagem aqui também é baseada na média diária do indicador de uso. Se o valor inserido para o indicador de uso ultrapassar esta porcentagem, o sistema irá impedir que o indicador de uso seja inserido.

**Exemplo:**  
O valor de Avisar se Ultrapassar é 10% e já temos um valor de 100 quilômetros para o Indicador de Uso para um Veículo. Insere outro indicador de uso para o Veículo, no valor de 120 quilômetros. O sistema emitirá um aviso de que o valor inserido ultrapassou a média de consistência de uso, porque o valor 120 é maior que os 10%, definidos no “Avisar se Ultrapassar (%)” para a média diária de Indicadores de Uso. A mesma situação acontecerá se definirmos o parâmetro para “Barrar se Ultrapassar”, porém a diferença é que o indicador de uso não poderá ser salvo. Quando o campo “Barrar se Ultrapassar” possuir um valor (diferente de zero), não poderá ser menor que o campo “Avisar se Ultrapassar (%)”.

Em Gerais / Parâmetros / Sistema, Pasta Identificação existe a caixa “Lançamento(s) de Indicador de Uso”.

Atualização: na inserção de indicador de uso por “Atualização” o valor digitado substitui o valor anterior pelo novo valor. Veja o exemplo abaixo do comportamento do parâmetro.

**Exemplo:**  
**Valor Anterior:** 1000 km  
**Novo Valor Digitado:** 1500 km  
**Resultado Final:**1500 km

Incremento: na inserção de indicador de uso por “Incremento” o valor digitado e irá incrementar o valor anterior. Veja o exemplo abaixo do comportamento do parâmetro.

**Exemplo:**  
**Valor Anterior:** 100 km  
**Novo Valor Digitado:** 50 km  
**Resultado Final:**150 km

Não é possível alterar indicadores de uso em objetos filhos, devendo proceder a alteração apenas nos objetos pai.

O valor de indicador de uso do objeto pai será distribuído entre todos os objetos filhos agregado. Sendo que, se este objeto filho já possuir indicador de uso, ao determinar um novo valor para o objeto pai, será efetuado a distribuição por diferença para todos os objetos filhos agregado.

**Exemplo:**  
Agregação do objeto pneu 26 no veiculo Fiesta.  
Considere que ambos não tenham histórico de indicadores de uso.  
Ao agregar o pneu informe a uma Quilometragem de 1500 km, essa Quilometragem ficará visível somente no histórico de indicadores e uso do objeto pai. Depois da agregação ao fazer lançamentos de indicadores de uso no objeto pai 2500 km, no histórico do objeto filho ficará visível o seguinte valor de indicador de uso 1000 km, ou seja, (2500 -1500) isso significa a distribuição por diferença para todos os objetos filhos agregados.

Após Reforma: este campo informa o valor acumulado do Indicador de Uso medido para o Objeto de Manutenção desde a sua última reforma. Ele apresentará o valor do “Acumulado” caso ainda não exista reforma para o Objeto de Manutenção. Quando houver reforma, o campo “Após a Reforma” será zerado e passará a contar o valor acumulado após a última reforma. Para calcular o campo “Após Reforma” basta clicar no botão “Após Reforma”.

**Pasta Integração**  
Permite associar um Objeto de Manutenção a um Bem Patrimonial. Esta Pasta ficará disponível se a flag em Gerais / Parâmetros / Sistema, Pasta Identificação “Integração com RM Bonum” estiver marcado. Por questão de segurança, o será permitido ao usuário associar apenas um Bem Patrimonial a um Objeto de Manutenção, cujo perfil possua permissão de acesso definido em Cadastros / Segurança / Perfil de Usuário / Acesso a Menus.

Nesta mesma aba permite -se vincular um objeto de manutenção a integração com a , exibindo uma caixa de seleção que trás as unidades (equipamentos) que estão disponíveis para o cliente.

Lembrando que não será permitido associar ao objeto de manutenção uma unidade que ja esteja associada a outro.

**Pasta Agregados**  
Permite selecionar os objetos-filhos para que os mesmos sejam agregados ao objeto de manutenção pai selecionado. È possível localizar os objetos filhos e fazer filtros para os mesmos. Selecione o (s) objeto(s)- filho(s) que será(ão) vinculado(s) ao objeto-pai e clique no botão “<<”. É necessário que o objeto-filho tenha sido cadastrado previamente e obrigatoriamente o objeto pai tem que trabalhar com pelo menos um indicador de uso do objeto filho. Para remover um agregado, selecione-o e clique no botão “>>”. Ao agregar um objeto é necessário informar a posição de agregado, as posições foram cadastras no Tipo de Objeto de Manutenção / Anexos – Posições do Tipo de Objeto. Os motivos de agregação são cadastros em Cadastros / Tabelas Auxiliares / Objeto de Manutenção / Motivos de Agregação. Ao desagregar um objeto é preciso informar o motivo de retirada que são cadastrados em Cadastros /Objeto de Manutenção / Motivos / Motivos de Retirada.

Em Manutenção / Parâmetros /  identificação se o parâmetro “Habilitar/Desabilitar Indicadores de Uso do Objeto Pai no Objeto Filho no momento da agregação” estiver marcado. Ao agregar um objeto filho e o mesmo estiver com um indicador de uso desabilitado na Pasta indicador de uso e esse indicador de uso for igual ao do pai, após a agregação o indicador de uso será habilitado no objeto filho.

**Exemplo:**

No cadastro do Tipo de Objeto de Manutenção filho foi habilitado km e horas e no cadastro do objeto de manutenção filho está habilitado somente horas. Ao efetuar a agregação no cadastro do objeto filho será habilitado o indicador de uso km.

Para efetuar a agregação de um objeto, a mesma dever estar configurada em Manutenção / Tipos de Objetos de Manutenção, edição de um Tipo de Objeto de Manutenção, Anexos / Opções de  
Agregação.

Para agregar um determinado objeto em outro com o qual ele não esteja vinculado (cadastrado), a agregação não será permitida. Caso exista o vínculo (exista o cadastro da agregação), serão disponibilizadas as posições pré-cadastradas entre esse dois Tipos de Objetos.

Ao fazer uma agregação e os objetos de manutenção pai e filho estiverem integrados a um BEM no RM Bonum (Pasta integração) e os BENS integrados ao objeto pai e filho estiverem em filial e/ou local  
diferente, o sistema emitirá uma mensagem informando que será necessário realizar uma transferência física de BENS no RM Bonum entre a filial e/ou local para que o sistema prossiga com a agregação do objeto filho no objeto pai.

Caso seja feito um cancelamento da transferência física entre filial e/ou local do BEM no RM Bonum e esse BEM estiver integrado a um objeto de manutenção pai, o sistema irá permitir o cancelamento de transferência. Mas se o BEM estiver integrado a um objeto filho ao fazer a transferência, o sistema emitirá uma mensagem informativa.

Não é permitido fazer “Lançamentos de Indicadores de uso” e/ou “Alteração de medidor” para objeto filho. Ao tentar fazer uma alteração de medidor para um objeto filho o sistema irá emitir a seguinte mensagem: “A alteração do “Medidor do Indicador de Uso” não é permitida para “Objetos Agregados”!” Ao tentar inserir indicador de uso para um objeto filho o sistema irá emitir a seguinte mensagem: “Não é permitido inserir “Indicador de Uso” para objetos filhos!”.

**Campos Complementares**  
Permite inserir dados nos campos complementares criados para o cadastro de Objeto de Manutenção de acordo com a necessidade de cada empresa. Para cadastrar os campos complementares acesse o menu Cadastros / Campos Complementares / Objeto de Manutenção. Os campos complementares permitem a criação de campos do tipo inteiro, alfanumérico, data, real e texto. Para que a Pasta Campos Complementares fique visível no cadastro de Objeto de Manutenção é necessário a criação dos campos primeiro.

**Anexos – Reforma de Pneu**  
Permite informar os dados relacionados ao processo de reforma do Objeto de Manutenção pneu. A opção de Reforma de Pneu só estará disponível quando o controle de pneus estiver parametrizado em:  Cadastro / Manutenção de Objeto /  Pneus, Campo “Utiliza Controle de Pneus”.

Processo de Reforma: selecione o processo de reforma aplicado ao Objeto de Manutenção pneu, cadastrados e visualizados no menu Pneus / Processo de Reforma.

Modelo do Desenho: selecione o modelo do desenho do objeto pneu, utilizado no processo de reforma, cadastrados e visualizados no menu Pneus / Modelo do Desenho.

Tipo de Borracha: selecione o tipo de borracha do objeto pneu, utilizado no processo de reforma, cadastrados e visualizados no menu Pneus / Tipo de Borracha.

**Anexos – Análises de Índices**  
Data de Medição Inicial e Data de Medição Final: digite a data do período em que se deseja gerar o gráfico com a evolução dos valores do índice de acompanhamento.

**Índice de Acompanhamento**

Selecione o índice cujos valores serão utilizados para gerar o gráfico. É necessário registrar previamente os valores para o índice desejado. Para gerar o gráfico, clique no botão “Atualizar”. Na tela é possível salvar imagem do gráfico, copiar gráfico, imprimir, visualizar impressão, selecionar o tipo de gráfico, selecionar esquema de cores, ativar/desativar 3D, adicionar anotações e acessar a propriedade do gráfico.

**Anexos – Objeto de Manutenção (Visão em Árvore)**

A visão em árvore do cadastro de Objeto de Manutenção permite visualizar e trabalhar com todos os Objetos de Manutenção de forma simplificada. Pois podemos identificar a situação dos objetos agregados, sucateados e transferidos entre coligadas. Observe na imagem do lado esquerdo a árvore mostra ícones agrupando os objetos em situação normal, sucateado e transferido entre coligadas. Do lado direito na imagem na Pasta Dados do Objeto de Manutenção mostra a identificação do objeto, Tipo de Objeto, Modelo, Submodelo, Posição onde objeto está agregado quando ele for um objeto filho e o objeto pai.  
Na tela de visão em árvore é possível incluir, editar excluir, atualizar, localizar um registro, acessar o anexo “Inicialização de Plano de Manutenção” para inicializar um plano e aplicar filtros. Existem ainda os botões “Encolher Tudo” que encolhe toda árvore do Objeto de Manutenção e “Expandir Tudo” que expande toda árvore do Objeto de Manutenção.

**Para agregar um Objeto de Manutenção**  
Selecione do lado direito da tela o Objeto de Manutenção que deseja agregar, arraste-o até o Objeto de Manutenção pai, à esquerda, e solte. Será solicitado a posição de agregação o motivo de agregação e o valor do indicador de uso.

**Para desagregar um Objeto de Manutenção**  
Selecione do lado esquerdo o Objeto de Manutenção pai, do lado direito irá aparecer o objeto filho, clique com o botão direito sobre o objeto filho e clique em “desagregar”. Será solicitado o motivo de retirada. Na Pasta Controle de Plano de Manutenção permite visualizar os planos de manutenção para o Objeto de Manutenção selecionado, os produtos do plano e se possui pendência ou não e seus detalhes.

**Anexos – Acessório**  
Permite cadastrar os acessórios que acompanhavam o objeto de manutenção quando ele entrou na oficina. Esta janela permite a utilização de campos livres específicos para cada cliente. Basta cadastrá-los em Gerais / Parâmetros / Sistema, Pasta Campos e Tabelas Opcionais / Subpasta Tabela de Acessórios de Objeto.

**Anexos – Produtos do Objeto de Manutenção**  
Permite inserir/editar o produto que poderá ser apropriados ou que irão fazer o controle de vida útil pelo objeto de manutenção.

**Cód.Produto:** número de identificação do produto.

**Cód.Unidade:** código da unidade de medida do produto.

**Quantidade:** quantidade máxima do produto que poderá ser apropriado pelo objeto de manutenção ou quantidade a ser trocada na abertura de ordem de serviço para o controle de vida útil.

**Data de Inicialização:** data que a vida útil ou apropriação do produto começara a ser contada.

**Vida útil na Ordem de Serviço Obrigatório:** exige o emprego de vida útil na Ordem de Serviço.

**%da vida útil:** como já foi falado antes este campo usa como base a vida útil recomendada pelo fabricante e que deve ser informada em Cadastros / Produtos / Serviços / Anexos Produtos – Informações de Manutenção. Como mostra à figura 9 a vida útil da Correia Dentada no cadastro de Produtos / Serviços é de 10000 km. Veja mais detalhes no tópico Aplicações de Produto / Vida útil.

O produto de um determinado Objeto de Manutenção poderá ser controlado através da vida útil ou através da apropriação direta. Marcando o checkbox “Produto Apropriável?” os campos que farão o  
controle da apropriação direta de produto ficarão disponível.

O “Consumo Médio” será a quantidade média consumida do produto.

Índice de Acompanhamento: informe o índice que fará o controle do consumo médio.

Para mais detalhes consulte o cadastro de Índice de Acompanhamento e a Apropriação Direta de Produto.

Os produtos do objeto de manutenção poderão ser informados no Tipo de Objeto de Manutenção no Anexo - Produto(s).  
A diferença é que no Tipo de Objeto os produtos podem segmentados por tipo, modelo e/ou submodelo. Uma vez que os produtos são segmentados no Tipo de Objeto ao executar o processo Atualizar Produtos do Objeto de Manutenção.  
Os produtos referente ao tipo, modelo e/ou submodelo do Objeto de Manutenção ficarão visíveis no Anexo - Produtos do Objeto de Manutenção.

**Anexos – Histórico de Indicador de Uso**  
Permite cadastrar indicadores de uso do Objeto de Manutenção. O Indicador de Uso é composto pelos campos “Medidor” e “Acumulado”. O Acumulado só é alimentado através da inserção de vários  
Medidores.  
É possível inserir dados nos campos complementares criados para o anexo “ Histórico de Indicador de Uso” de acordo com a necessidade de cada empresa. Para cadastrar os campos complementares acesse o menu Cadastros / Campos Complementares / Medição de Indicador de Uso. Os campos complementares permitem a criação de campos do tipo inteiro, alfanumérico, data, real e texto. Para que a Pasta Campos Complementares fique visível no anexo “Histórico de Indicador de Uso” é necessário a criação dos campos primeiro.

**Data da coleta:** Data em que o registro do indicador de uso foi coletado.  
**Medidor:** Valor do medidor.  
**Ultimo Medidor:** Informa o valor último medidor.

**Subprocesso - Alterar indicador de uso**  
Permite alterar os indicadores de uso lançados com valores errados.

**Exemplo:**  
Considere um objeto com os seguintes lançamentos de indicadores de uso:

Se o valor de indicador de uso 10000 for alterado para 12000. O sistema irá fazer o seguinte cálculo:

X = Medidor Novo (12000) – Medidor Antigo (10000)  
X = 2000

Todos os indicadores de uso posterior ao que foi alterado terão seus valores somados a X ou subtraído deX, caso o Medidor Novo seja menor que o medidor antigo.

X = Medidor Novo (8000) – Medidor Antigo (12000)  
X = -4000

Quando um objeto possuir agregados a alteração também irá ocorrer nos objetos filhos da seguinte maneira:

Y= Medidor Antigo do Filho + X  
Y será o indicador de uso do filho alterado.

Se o valor de indicador de uso do pai 20000 for alterado para 25000. O sistema irá fazer o seguinte cálculo para alterar os valores nos filhos:

X= Medidor Novo do Pai (25000) – Medidor Antigo do Pai (20000)  
X= 5000  
Y= Medidor Antigo do Filho (15000) + X  
Y= 20000

* O novo medidor não poderá ser menor ou igual ao medidor anterior.
* Não é permitido alterar indicador de uso para o objeto filho.
* Caso seja feito uma alteração em um indicador de uso cadastrado para o pai antes da agregação, não haverá efeito nos indicadores de uso do objeto filho.
* Não é permitido alterar indicador de uso para o objeto com alteração de medidor.
* Não é permitido alterar indicador de uso para o objeto sucateado.
* Só usuários com permissão poderão alterar indicador de uso.

É possível fazer lançamento simultâneo de Indicadores de uso através do menu Processos / Inserir varias Medições de Indicador de Uso /  Lançamento(s) de Indicador(es) de Uso. Assim não será necessário acessar cada Objeto de Manutenção para inserir a medições. Na tela de visão é possível incluir, salvar, excluir, desfazer, cancelar, navegar pelos registros, localizar um registro e configurar colunas.

Lançamento Simultâneo de Indicadores de Uso

Marcando o checkbox “Fixar Data de Coleta” quando houver a necessidade de se fazer vários lançamentos para Objetos de Manutenção diferentes com data de coleta igual, na próxima linha de inserção do indicador de uso, a “Data da Coleta” ficará fixa.

**Anexos - Histórico de Ordem de Serviço**  
Permite visualizar as ordens de serviço abertas para o Objeto de Manutenção selecionado. Dados como Status da OS, Data de Emissão, entre outros, podem ser visualizados.

**Anexos - Histórico de Filiais**  
Permite visualizar as filias onde o Objeto de Manutenção esteve. O processo de transferência de filiais pode ser realizado na visão do cadastro de Objeto de Manutenção. Clicando em “Processos – Transferência entre Filiais” veja mais detalhe sobre o processo de transferência em “Processos – Transferência entre Filiais”.

**Anexos - Histórico de Agregações**  
Permite visualizar o histórico das agregações do o objeto de manutenção, onde ele foi agregado. O processo de agregação pode ser realizado na visão do cadastro de Objeto de Manutenção Pasta “Agregados” e na visão em árvore do Objeto de Manutenção. Só é possível visualizar Histórico de Agregações para os objetos filhos. Ao acessar o anexo “Histórico de Agregações” será disponibilizado o “Processo – Cancelar Agregação/Desagregação”. Para isso é necessário que o usuário tenha acesso a tag de segurança através do menu Cadastros / Segurança / Perfis.

**Subprocesso – Cancelar Agregação/Desagregação**  
Para uma agregação feita na visão do cadastro de Objeto de Manutenção / Pasta Agregados ou na visão em árvore do Objeto de Manutenção, é possível efetuar o seu cancelamento através da Pasta “Histórico de Agregações” no menu Processos “Cancelar Agregação/Desagregação”. Para o caso de uma desagregação, esta poderá ser cancelada voltando o objeto a ficar agregado. Durante esse processo é possível excluir também os indicadores de uso lançados para a agregação/desagregação, permanecendo somente os lançamentos antes da agregação ou desagregação.

Ao desagregar um objeto através do cadastro de Objeto de Manutenção / Pasta Agregados ou na visão em árvore. No anexo histórico de agregações do objeto filho o status será desagregado, a data de saída e o valor de indicador de uso de saída serão preenchidos. Caso faça o cancelamento da agregação pelo anexo histórico de agregações clicando no processo “Cancelar Agregação/Desagregação” a desagregação será efetuada, mas o histórico de agregação será excluído.

**Anexos – Índices de Acompanhamento**  
Permite cadastrar os valores do índice que será utilizado para aferir a qualidade de um Objeto de Manutenção através de medição periódica. São estabelecidos, no momento da criação do índice, valores mínimo e máximo aceitáveis de qualidade. Baseado neste intervalo, o sistema classifica o objeto da seguinte maneira: valor do índice abaixo do mínimo, valor do índice dentro da faixa, valor do índice acima do máximo.

Os valores mínimos e máximos escolhidos para os índices de acompanhamento podem variar dentro do conjunto dos números racionais (-4,124; -3; 0; 9; 17,865).

É possível inserir dados nos campos complementares criados para o anexo “ Índice de Acompanhamento” de acordo com a necessidade de cada empresa. Para cadastrar os campos complementares acesse o menu “Cadastros / Campos Complementares / Medição do Índice de Acompanhamento”. Os campos complementares permitem a criação de campos do tipo inteiro, alfanumérico, data, real e texto. Para que a Pasta “Campos Complementares” fique visível no anexo “Índice de Acompanhamento” é necessário a criação dos campos primeiro. Veja mais detalhes no tópico Operação e Manutenção / Índice de Acompanhamento.

**Anexos – Alteração de Medidor**  
Permite alterar o medidor de indicador de uso e visualizar as alterações anteriores. Quando o medidor zerar após alcançar seu valor máximo, ou quando for trocado por apresentar defeito, é necessário  
informar a alteração para que o sistema consiga tratar os novos valores sem perder a consistência do valor acumulado. Caso essa alteração não seja informada o sistema irá barrar os lançamentos com valor menor que o valor atual do indicador de uso.

**Data da Alteração:** data em que a alteração foi executada.  
**MA-Quilometragem:** Medidor Antigo.  
**M-Quilometragem:** Novo medidor.  
**Último Medidor:** Apresenta o valor do último medidor do Indicador de Uso.

Exemplo:  
Um velocímetro de ônibus que foi danificado. Tinha vários indicadores de uso, seu último indicador apresentava o valor de 10.000 km. Então, foi necessário instalar um novo velocímetro. O medidor do  
velocímetro novo será 0 km, mas o ônibus que teve o velocímetro danificado já tinha rodado 10.000 km. Para que não seja perdida a medição antiga, incluímos uma alteração de Indicador de Uso, e preenchemos no campo “MA-Quilometragem” Medidor Antigo o valor de 10.000 km, e no “M-Quilometragem” Novo medidor o valor de 0 km, pois se trata de um medidor novo. No Histórico de Indicador de Uso terá dois novos registros, onde o primeiro será o valor da última medição que foi informada, no caso 10.000 km, e o outro indicador terá a nova medição, que é o valor de 0 km.

**Anexos - Inicialização de Plano de Manutenção**  
Permite visualizar todos os Planos de Manutenção pertencentes ao Objeto de Manutenção. A Inicialização de Planos de Manutenção poderá ser inserida, alterada ou excluída desde que não tenha sido gerada nenhuma Ordem de Serviço pelo sistema através do referido Plano de Manutenção. Veja mais detalhes em cadastro de Plano de Manutenção. Quando um plano ainda não está inicializado ele fica com a Inicialização “Pendente” e não é permitido sua edição. Para inicializar um plano selecione o mesmo na Pasta “Anexo - Inicialização de Plano de Manutenção” e clique no subprocesso “Inicialização de Plano de Manutenção” e informe a data de geração e um valor de indicador de uso, o plano será inicializado e ficará com a inicialização “Efetuado”. É possível excluir a inicialização do plano voltando o mesmo a ficar com Inicialização “Pendente”, para isto basta clicar no subprocesso – Excluir Inicialização de Plano. Veja mais detalhes no tópico Operação e Manutenção / Plano de Manutenção.

Data de Geração: Quando houver Inicialização de Planos de Manutenção, este campo descreverá qual foi à data em que o Objeto de Manutenção já teve um Plano de Manutenção efetuado.

**Anexos - Histórico de Localizações**  
Permite analisar o histórico do Objeto de Manutenção, disponibilizando a visualização de todos os locais  
onde foi transferido.

**Anexos - Histórico de Centros de Custo**  
Mantém o histórico de todos os processos de transferência de centro de custo de um objeto de  
manutenção.

**1º Identificador:** Código do objeto de manutenção.  
**Código do Centro:** Código do centro de custo.  
**Centro de Custo:** Descrição do centro de custo .  
**Data de Entrada:** Data que o objeto de manutenção entrou no centro de custo.  
**Data de Saída:** Data que o objeto de manutenção saiu do centro de custo.  
**Código do Usuário:** Código do usuário que executou a transferência de centro de custo.  
**Nome do Usuário:** Nome do usuário que executou a transferência de centro de custo.

**Processos – Atualizar Produtos do Objeto de Manutenção**  
Permite atualizar a lista de itens do Objeto de Manutenção parametrizados por tipo, modelo e/ou submodelos no cadastro do Tipo de Objeto de Manutenção.

**Processos - Calcular Média Diária de Indicador de Uso**  
Como foi falado anteriormente que o cálculo da Média Diária de Indicador de Uso, poderia ser feito também pelo processo. Lembrando que existe um parâmetro em Gerais / Parâmetros / Sistema / Pasta identificação. Onde é definido se o cálculo da média será manual ou automático. Para calcular a média siga as instruções abaixo:

**Procedimento**

1. Selecione o(s) Objeto(s) de Manutenção que deseja calcular a média dos indicadores de uso.
2. Clique no menu processos Calcula Média Diária de Indicadores de Uso.
3. Selecione ou Digite a Data Inicial do cálculo.
4. Selecione ou Digite a Data Final do cálculo.
5. Configure o agendamento do processo.
6. Clique em executar.

**Agendamento de Processo**

Um agendamento de processo poderá ser feito para um determinado mês/dia/horário. Todos os processos serão armazenados no servidor, mantendo assim os históricos de todos os processos, executados ou não, inclusive tendo acesso a visualização de Log de processo. Para ter acesso a tela de Gerenciamento de Jobs acesse o menu Sistema / Server / Gerenciamento de Jobs.

Calculando a média do dia 26/02/2007 ao 28/02/2007, o valor médio de inserção diária dos indicadores de uso será de 10 km, pois é a média da inserção dos valores do primeiro, segundo e terceiro dia.

**Processos - Conversão entre Indicadores de Uso**  
Converter Indicadores de Uso consiste em modificar os Indicadores de Uso do Objeto de Manutenção selecionado. A conversão é orientada quando se precisa alterar o Indicador de Uso que controla o Objeto de Manutenção, ou quando se deseja inserir mais Indicadores de Uso para melhorar o controle dos Objetos.

Exemplo:  
Acrescentar um novo Indicador de Uso para seus Veículos, que possuem apenas o Indicador “Quilometragem”. O novo indicador será o “Combustível Consumido”, que irá expor o quanto de combustível o Veículo gastou. Em média, considera se que cada veículo faz 10 km /l. Então, no campo Fator de Conversão o valor a ser digitado será “0,1”, pois para cada 1 quilômetro percorrido o Veículo consome 0,1 litro de combustível. Escolha o Indicador de Uso Atual (Quilometragem) e o Novo Indicador de Uso (Combustível Consumido). Ao final do processo, será ativado o Indicador de Uso “Combustível Consumido”, e terá seu valor calculado automaticamente. No histórico dos Indicadores de Uso também estará registrado o valor do Indicador “Combustível Consumido”.

**Processos - Inserir Várias Medições de Indicador de Uso**  
Permite fazer o lançamento de vários indicadores de uso para o Objeto de Manutenção. É preciso preencher os campos Data da Coleta, que é a data do lançamento de indicador de uso e Medidor, que é o valor do medidor a ser lançado no histórico do objeto de manutenção.

**Processos - Enviar Objeto de Manutenção para o estoque**  
Permite enviar um Objeto de Manutenção para estoque e o mesmo ficará disponível no cadastro de produtos do sistema de Gestão de Estoque e Faturamento. Para enviar um objeto para o estoque é necessário fazer a configuração do movimento em Gerais. No campo “Movimentos de Envio e Retirada de Objeto do Estoque” informe o movimento de envio e movimento de retirada.

Como foi falado anteriormente no cadastro de Submodelo no Tipo de Objeto de Manutenção, informe no campo “Produto” o produto cadastrado em Produtos / Serviços.

Exemplo:  
Vamos supor que o objeto veículo Palio EX 1.0, será enviado para o estoque. Então no cadastro de Produto do sistema Gestão de Estoque e Faturamento faça o cadastro do Produto Palio EX 1.0 e no cadastro de submodelo informe no campo Produto o código do produto Palio EX 1.0 .

**Processos - Retirar Objeto de Manutenção do Estoque**  
Permite retirar um Objeto de Manutenção do estoque e o mesmo ficará em situação normal no cadastro de Objeto de Manutenção. Após execução do processo o saldo atual em Saldos e Custos do cadastro de produto será decrescido uma unidade.

**Processos - Transferir Objeto de Manutenção entre Coligadas**  
Permite fazer a transferência de Objetos de Manutenção entre coligadas, considerando que não estejam em estoque, agregados a outros objetos ou com ordem de serviço em andamento. A Filial destino e Localização destino são de preenchimento facultativo. Acessórios, campos complementares e históricos do objeto de manutenção não serão transferidos.

**Coligada Destino:** coligada destino para onde o objeto de manutenção será transferido.

**Cliente/Fornecedor:** é possível também definir o cliente/fornecedor do objeto de manutenção.

**Status:** Informe o status que objeto assumirá na coligada de destino.

**Localização de Destino:** Informe à localização que o objeto assumirá na coligada de destino.

Status e Localização de Destino são cadastrados na coligada de destino.

**Processos - Transferir Objeto de Manutenção entre Filiais**  
Permite fazer a transferência de Objetos de Manutenção entre filiais, considerando que não estejam em estoque, agregados a outros objetos ou com ordem de serviço em andamento. A Localização destino é de preenchimento facultativo. Acessórios, campos complementares e históricos do objeto de manutenção não serão transferidos.

**Processos - Transferir Objeto de Manutenção entre Locais**  
Permite fazer a transferência de Objetos de Manutenção entre filiais, considerando que não estejam em estoque, agregados a outros objetos ou com ordem de serviço em andamento. A Localização destino é de preenchimento facultativo. Acessórios, campos complementares e históricos do objeto de manutenção não serão transferidos.

**Processos – Transferência entre Centros de Custo**  
O processo para transferência entre centros de custo consiste em transferir um objeto de manutenção entre centros de custo.

**Data de Transferência:** informe a data de transferência do centro de custo.  
**Centro de Custo de Destino:** informe o novo centro de custo

Ao executar o processo o sistema irá preencher a data de saída do ultimo centro de custo, com a data de entrada do novo centro de custo.

Caso o objeto de manutenção esteja integrado a um Bem, execute o processo de transferência de centro de custo pelo RM.

**Processos - Sucatear Objeto de Manutenção**  
Permite sucatear o objeto de manutenção, selecionando o motivo pelo qual o objeto está sendo sucateado. Quando o objeto sucateado for um objeto raiz, todos os objetos agregados também serão sucateados, e todas as operações com estes objetos (edição, agregação, desagregação, lançamento de indicadores de uso e índice de acompanhamento) ficarão indisponíveis. Para sucatear um determinado objeto de manutenção é necessário cadastrar os motivos em Cadastros / Tabelas Auxiliares / Objeto de Manutenção / Motivo de Sucateamento.

Ao abrir uma ordem de serviço para um objeto sucateado, o sistema irá emitir uma mensagem informando que o objeto foi sucateado. Assim não será permitido abrir ordem de serviço para um objeto sucateado.

* **Processos - Cancelar Sucateamento de Objeto de Manutenção**  
  Permite cancelar o sucateamento do Objeto de Manutenção que esteja neste estado de conservação. Ao ser cancelado, o estado de conservação do objeto passará a ser “Usado”.
* **Processos – Cria OS do Plano de Manutenção**  
  Permite criar ordem de serviço para o objeto de manutenção que possua Plano de Manutenção vencido. Caso o Plano de Manutenção não esteja vencido o sistema irá emitir uma mensagem avisado que o plano não está vencido.
* **Processos – Cria OS para Terceiros do Plano de Manutenção**  
  Permite criar ordem de serviço para terceiros do Objeto de Manutenção que possua Plano de Manutenção vencido. Caso o Plano de Manutenção não esteja vencido o sistema irá emitir uma mensagem avisado que o plano não está vencido.
* **Processos - Imprimir Objeto de Manutenção**  
  Permite a impressão e a visualização de um relatório de Objeto de Manutenção personalizado por meio do Gerador de Relatórios.

**Processos - Gerar Objeto de Manutenção a partir do Patrimônio**

Permite gerar objeto de manutenção selecionando a partir de qual patrimônio o objeto será criado, facilitando o cadastro e categorização do mesmo.

Ao selecionar esse processo, é solicitada a escolha dos patrimônios que darão origem ao objeto de manutenção que será criado, imagem abaixo:

Importante:

Existem duas formas distintas de controle de transferência para um objeto de manutenção.

Quando o objeto de manutenção não possui vínculo com um patrimônio, todo o controle de transferência é realizado diretamente pelo módulo de Manutenção de Equipamentos, incluindo os registros de histórico.

Por outro lado, quando o objeto de manutenção está vinculado a um patrimônio, o controle de transferência passa a ser realizado exclusivamente pelo módulo Patrimonial. Nesse cenário, as movimentações e históricos de transferência não são enviados para o histórico da Manutenção de Equipamentos, pois as informações válidas passam a ser as registradas no cadastro do patrimônio.

Esse comportamento pode ser observado no momento em que um objeto de manutenção é vinculado a um patrimônio. Nessa situação, o sistema remove as informações de transferência existentes no objeto de manutenção, justamente para garantir que o controle seja centralizado no módulo Patrimonial, evitando divergência de informações entre os módulos.

Dessa forma, para consultar o histórico de transferências de objetos vinculados a patrimônios, é necessário acessar diretamente o cadastro do patrimônio correspondente.

Após, é solicitado o preenchimento dos dados do Objeto a ser criado:

Importante:

O tipo de Objeto dita quais indicadores estarão habilitados nesta tela de cadastro de dados do Objeto de Manutenção.

O processo não executa se o valor Acumulado não estiver preenchido no cadastro dos dados.

Após criado o Objeto de Manutenção, automaticamente será criado um Histórico de Indicador de Uso.

Exemplo de um objeto foi criado através do Processo:

Exemplo de Histórico de Indicador de Uso preenchido com um registro após o cadastro através do processo:

### Integração com a News GPS

Na aba **Integração**, existe um campo específico para vincular um equipamento da **News GPS**. Este campo está sempre visível, mas só será habilitado se a integração com a Telemetria estiver ativada nos parâmetros do sistema, na opção **Integração > Telemetria**. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=932123350)

* **Objetivo:** Permitir ao usuário selecionar uma unidade (veículo/equipamento) da base da News GPS para associá-la ao equipamento em manutenção.

Telemetria
