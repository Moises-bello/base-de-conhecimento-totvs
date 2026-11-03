---
content_hash: c79dfc6e41396606a8057fa095f991a56c72b08b8c55bf6b802279b3d75facc2
fetched_at: '2026-06-29T00:09:29.137715+00:00'
page_id: '423938817'
product: rm
source: tdn-rm
title: Produtos/Serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938817
version: 121
---

Nesta  opção  devem  ser  cadastrados  todos  os  produtos  e  serviços  que  serão  utilizados  nos  diversos processos do sistema.  
Antes de se iniciar o cadastro de um produto é preciso definir suas parametrizações, pois sem elas não será possível  cadastrar o produto. Os parâmetros do produto podem  ser  acessados  através do menu Opções / Parâmetros / Tabelas /  Produtos. Os principais parâmetros a serem definidos são:

* Nome da Tabela;
* Máscara;
* Opções de controle da Máscara;
* Utilização e máscara do código reduzido do produto;
* Tipo de Histórico;  - Utilização de Características Físicas, Fiscais do Produto;
* Utilização de Produto Composto, Grade Numerada, Lote;
* Vínculo de Fornecedores/Clientes ao produto;
* Definições de até 5 preços com suas respectivas moedas ao produto.

******Observações***:***O correto preenchimento de todos os dados do produto é muito importante. Apesar de permitir a qualquer momento a alteração de quase todos os campos, procure informar sempre os dados corretos, pois a alteração de uma informação que é utilizada para alguns dos controles efetuados, pode afetar cálculos já feitos e isto alterarão os dados anteriores que podem inclusive já estar registrados em relatórios. Portanto, depois de realizar movimentações, procure não alterar dados de produtos já cadastrados e principalmente aqueles que já foram utilizados em movimentações.

**Identificação:**Nesta pasta são preenchidos os campos que identificarão os produtos ou serviços.

**Marca***:* neste campo deve ser selecionado um default de Marca para o produto. Ao preencher este campo, a marca selecionada será incluída também no anexo Marcas do Produto.  
***Observações**:*A foto do produto deve ser do tipo JPG ou BMP, num formato de 170 X 160 pixels de tamanho, não podendo ultrapassar os 10240KB (10MB). No cadastro do produto, além de selecionar o código do [fabricante](https://tdn.totvs.com/x/XsdEGQ) existente, poderá cadastrar um novo na própria visão. As funcionalidades do sistema que utilizam o lookup de Produto, passam a ter opção de pesquisar o registro pela marca.

**Detalhes:**Nesta pasta são preenchidos os campos que complementaram a identificação dos produtos ou serviços.

**Descrição***:*Nesta pasta, serão informados os campos referentes à descrição do produto.

Na inclusão de um novo registro o **Nome Fantasia**será copiado para a **Descrição do Produto** quando a descrição do produto não possuir valor. Na alteração de um registro, quando a descrição do produto não possuir informação e o nome fantasia tiver sido alterado, será copiado para a Descrição do Produto o conteúdo do Nome Fantasia.

**Características*:***Nesta pasta, serão informados os campos referentes às características do produto.  
Validade (em dias): Este campo deverá ser preenchido com valores inteiros para que o campo Data de Validade do Lote no Anexo Lotes do Produto possa ser validado. O TOTVS Gestão de Estoque, Compras e Faturamento, será consistido da seguinte forma:  
Data de Validade do Lote (**=**) Data Fabricação do Lote  Validade (em dias).

**Classificação**: Nesta pasta, serão informados os campos referentes às tabelas de classificação do produto e a natureza orçamentária.  
As tabelas de classificação somente serão apresentadas, se estiverem configuradas no sistema, através do menu Ambiente | Parâmetros | TOTVS Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais |Tabelas | Tabelas de Classificação.  
***Observação***: Nesta pasta, serão apresentados os campos observação, histórico do produto, e campos livres para outras observações sobre o produto.

**Outros Dados*:***Nesta pasta, serão informados os campos sobre os outros dados do produto.  
Esta pasta, somente será apresentada se habilitado o campo Dados Fiscais do produto através do menu: "Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Produtos.

* **Nomenclatura Comum do Mercosul (NCM):**

* 1
  complete
  Referência (A-Z): Informe a referência de A a Z do produto, cada letra se relaciona ao número informado no campo posterior, para o produto com IPI. Esta letra poderá ser impressa na nota fiscal e, como os números correspondentes à tabela NCM (Nomenclatura Comum do Mercosul) são muito grandes e o campo correspondente reservado na nota é pequeno, a letra é impressa em lugar do código, também na própria nota, em lugar visível. 

  2
  complete
  Número: Código de Identificação do produto. 

  3
  incomplete
  Código EX: É uma exceção à regra aplicada à NCM da qual foi excepcionada. Isto é, aplica-se ao EX uma alíquota diferente daquela aplicada à NCM de faz parte.

IMPORTANTE

* A partir da versão 12.1.2502, os campos da **Nomenclatura Comum do Mercosul (NCM/ Número e Código EX)** e a **Nomeclatura Brasileira de Serviço (NBS)** serão substituídos por um lookup de **Classificação Fiscal de Bens e Serviços - NCM/NBS**, que utiliza as informações do cadastro da [Classificação Fiscal de Bens e Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=913828140). Assim as informações ficarão centralizadas neste cadastro e será associado seu identificador ao produto ou serviço.
* Produtos com NCM preenchido e serviços com NBS informado serão vinculados automaticamente ao cadastro de Classificação de Bens e Serviços ao atualizar a versão do sistema.
* Com a mudança de comportamento dos campos, a visão dos produtos passa a ter os campos com nome NCM e NBS. Para visualização dos produtos e serviços em cada classificação acesse: Cadastro|Fiscais|Mais|Classificação de Bens e Serviços|Anexo|Produtos.

**Procedência***:*Informe o código de procedência (origem da mercadoria) do produto. A partir deste código e de acordo com a Natureza de Operação do movimento, o código da Situação Tributária é formado e poderá ser impresso nas notas Fiscais, a situação tributária do produto indica origem e tipo de tributação do mesmo.:  
0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;  
1 - Estrangeira - Importação Direta, exceto a indicada no código 6;  
2 - Estrangeira - Adquirida no Mercado Interno, exceto a indicada no código 7;  
3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%;  
4 - Nacional, produção em conformidade com o Decreto-Lei n° 288/67 e as leis n°s 8.248/91, 8.387/91, 10.176/01 e 11.484/01;  
5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% (quarenta por cento);  
6 - Estrangeira - Importação Direta, sem similar nacional, constante em lista de Resolução CAMEX;  
7 - Estrangeira - Adquirida no Mercado Interno, sem similar nacional, constante em lista de Resolução CAMEX;  
8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%.

De acordo com o tipo de tributação informado na Natureza, o sistema comporá o código da Situação Tributária conforme a tabela B - Tributação pelo ICMS que tem os seguintes códigos:  
00 - Tributada Integralmente.   
10 - Tributada e com cobrança do ICMS por Substituição Tributária.   
20 - Tributação com redução de Base de Cálculo.   
30 - Tributação Isenta ou não tributada e com cobrança do ICMS por substituição tributária.   
40, 41 e 50 - Tributação Isenta, Não tributada ou Suspensão.   
51 - Tributação com Diferimento (a exigência do preenchimento das informações do ICMS diferido fica a critério de cada UF).   
60 - Tributação ICMS cobrado anteriormente por substituição tributária.  
70 - Tributação ICMS com redução de base de cálculo e cobrança do ICMS por substituição tributária   
90 - Tributação ICMS: Outros, exemplo:

* Se no campo "Procedência", informou para o produto o código igual a 0, significa que o produto é nacional, se o tipo de ICMS da Natureza for "Normal" o código da Situação Tributária será 000, significando que o produto é nacional com tributação de ICMS integral.
* Se no campo "Procedência", informou o código 0 e se o tipo de ICMS da Natureza for "Normal e ST", o código da Situação Tributária será 010, significando que o produto é nacional com tributação e com cobrança do ICMS por Situação Tributária.
* Descontos na Compra e na Venda - Porcentagem (%).
* Comissões - Porcentagem (%).
* Exigir Fornecedor Qualificado - (Sim / Não): Ao marcar essa opção o produto passará a ser considerado para o controle de [Qualificação de Fornecedores](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121), quando o mesmo estiver parametrizado para "Utiliza por Produto/Fornecedor". ° Produto Visível ClicBusiness - (Sim / Não): Permitir integração do produto com o ClicBusiness.
* Outros: Definição de valores default (padrão) para cada um dos campos que compõem esta subseção.
  + Condição de Pagamento - Tipo de Aplicação - Grupo de Faturamento - Indicador de produção em escala relevante - Margem Bruta de Lucro - Tipo de Conta - Tributação Cupom Fiscal - Código NBS do Serviço.
* GLP:

* + Campos de preenchimento não obrigatório, para apuração fiscal sobre combustíveis (%), onde os valores devem ser preenchidos pelo usuário quando o produto enquadra-se nas categorias: Gás Liquefeito de Petróleo, Gás Natural Importado e Gás Natural Nacional.
  + O Valor de Partida é preenchido de conforme medida por Quilograma sem ICMS.
  + Estes campos aceitam valores decimais de até 04(quatro) casas após a vírgula.

**Percentual de Mistura de Combustível***:* Nesse campo será informado o Percentual de Mistura do Combustível. Campo utilizado para  atender a legislação de Tributação Monofásica destinada a Combustível (NT2023.001 e Convênio ICMS 115/2023)

**Indicador de Origem***:* Nesse campo será informada a Origem do Combustível (Nacional ou Importada). Campo utilizado para  atender a legislação de Tributação Monofásica destinada a Combustível (NT2023.001 e Convênio ICMS 115/2023)

**Preço**: Nesta pasta, serão informados os campos sobre os preços, casas decimais e tolerância do produto.

* Alterar edição do preço e Número de decimais no preço, somente serão visualizados se nos parâmetros do produto, menu "Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas | Produtos | Definições de Produtos | Definições de Produtos 3/3, optou-se por sua utilização.
* A informação da moeda é obrigatória para cada preço.
* O número de casas decimais indicado ao marcar a opção "Alterar edição do preço", será apenas para o produto específico, e somente no momento em que estiver incluindo este como um item do movimento ou como item de contrato (Campo Preço Faturamento), é que será informado um preço com o número de casas decimais indicado neste cadastro e que poderá ser visualizado em relatórios utilizando-se a função (KPUF).
  + A configuração BuscarPreçoEm do item de movimento pode afetar esse comportamento, veja documentação
* Os preços aqui informados devem obedecer ao número de casas decimais indicado nos parâmetros. Portanto, o número de casas decimais aqui informada (s ) somente será (ão ) utilizadas na edição do item do movimento e do item de contrato (Campo Preço Faturamento).
* A utilização do recurso de tolerância é definido por tipo de movimento na pasta identificação/outros dados, exemplo:   
  Um produto entrou no estoque em Kg. O mesmo é controlado em g e a saída também é em g. O valor de entrada foi R$ 1,52. Na conversão para g o sistema tratará o valor financeiro da mesma forma que o valor quantitativo, ou seja, serão usados mais de 2 casas decimais. Com esta opção o sistema fará a multiplicação da quantidade x o preço unitário com todas as casas decimais informadas neste campo.

**Controle de Estoque:**Nesta pasta, serão informados os campos sobre controle de estoque do produto.  
Dias de Validade Mínima: O campo "Dias de Validade Mínima" deverá ser preenchido para que em Movimentos de Compra possa ser feita uma consistência não permitindo que o movimento seja incluído caso a Data do Movimento seja maior que a diferença entre a Data de Validade do Lote e Dias de Validade Mínima. A mensagem de consistência a ser mostrada no Movimento de Compra é a seguinte:  
"Item X: Validade do Lote XXXX fora do prazo mínimo do item".  
***Observação**:*Além de informar os campos unidades de compra, venda e controle, poderá cadastrar novas unidades pela janela de edição do cadastro de produto. Múltiplo de Quantidade Compra e de Venda somente serão consistidos no movimento se o parâmetro do tipo de movimento "Validar Múltiplo na Qtde" (pasta Itens/Outros Dados) estiver marcado.

**Unidades***:*Nesta opção, cadastra-se a tabela de unidades de medida que serão utilizadas pelo sistema. As unidades aqui cadastradas serão informadas nos produtos.

* Unidade de Controle | Unidade de Compra | Unidade de Venda:

* + Podem ser diferentes desde que a Unidade Base destas sejam iguais.

* Unidade Tributável | Unidade Tributável no Exterior:

* + Podem ser diferentes das demais unidades de medida, uma vez que, a Unidade Base seja a mesma da Unidade Base selecionada em "Unidade de Controle".

* Fator de Conversão Tributável | Fator de Conversão Tributável no Exterior:

* + Índices multiplicadores na incisão de valor tributário nos comércios interno e externo.
  + Caso preenchido, possui precedência em relação ao mesmo indicador no cadastro de Unidades.
* Código de Barras Exterior
  + Código de Barras do tipo GTIN.

***Observação**:*O Fator de Conversão, é o valor pelo qual deverá ser multiplicada a quantidade do movimento nesta unidade. Será respeitada uma consistência que verificará se o fator de conversão, após ser truncado, será diferente de zero. Caso o fator de conversão seja diferente de zero, será gravado normalmente, caso contrário, uma mensagem será exibida para o usuário informando que o fator de conversão está errado e deverá ser alterado. As quantidades serão impressas, de acordo com a unidade, através do campo Nº Casas Decimais. O tamanho do Código Reduzido, está limitado a 2 caracteres e será utilizado para a integração com parceiros de automação comercial, devido à restrição existente nas impressoras fiscais, que limitam o tamanho do código da unidade de medida.

Não é possível alterar a Unidade de Controle no cadastro do Produto, quando ele se enquadrar em um dos quesitos abaixo:

* Existir saldo físico para o Produto;
* Houver movimentação de estoque para o Produto onde a unidade base atual é diferente da nova;
* Houver movimentações de pedido com os Status "Pendente / A Faturar" ou "Não Processado" existentes para o produto.

**Números de Série**: Nesta pasta, serão cadastrados os números de série do produto.

***Observações***:

* Os campos Filial e Local de Estoque somente podem ser modificados através de movimentos. O status inicial é sempre "Fora Estoque". Um número de série não poderá ser removido caso seu status seja diferente de "Fora Estoque" ou esteja incluído em um item de movimento.
* O número de série leva em conta a unidade usada no movimento, por exemplo, se a unidade de controle do produto é UND e a unidade de compra foi "Caixa com 10" o usuário deverá selecionar 10 números de série, pois será levado em conta a unidade de controle do produto. Após realizar a movimentação com o produto que apresenta o número de serie, os campos Lote e Data de Fabricação não poderão ser modificados.
* O número de série poderá ser utilizado em movimentação que afetam qualquer um dos saldos, como poderá afetar mais de um saldo. Criou-se um campo de Status de estoque para cada saldo ( campos Saldo Físico à Saldo Físico 10 na tabela TNUMSERIE). Se o valor do Saldo Físico for 1(Um), significa que o número de série está em estoque para o saldo 1, caso seja 0(zero), não estará em estoque . A mesma regra vale para os demais saldos. Na visão do Número de Série, na tela de produto, o Status aparecerá como "Em Estoque" se o número de série estiver em estoque para pelo menos um dos saldos, e ' Fora Estoque ' se para todos os saldos estiverem fora de estoque.
* Na definição da máscara dos números de série para o produto, pasta "Controle Estoque", quando composta apenas por símbolos: "Q - (Aceita caracteres alfanuméricos)", durante o cadastro de um item, não torna-se obrigatório completar a quantidade total definida pelo usuário. Desta forma, um cenário onde itens cadastrados com códigos do tipo "0100" e "100" serão identificados como itens distintos.

**Lotes de Produto***:*Nesta pasta serão cadastrados os lotes de produto.

**Grade Numerada:**Aparecerá se nos parâmetros do produto, se optou pela utilização de "Grade Numerada", a tabela de grade já deverá estar cadastrada através da opção Cadastro/Tabelas Auxiliares-Grade Numerada.  
***Observação**:*Não será possível alterar o campo 'Grade Numerada' de um Produto se este possui o saldo físico diferente de zero ou se existirem movimentações para ele com data posterior a data de fechamento de estoque.

**Custos:**Nesta pasta serão informados os campos para controle de custos do produto.  
***Observação**:*O custo específico refere-se ao processo de custo usado para mercadoria (geralmente de elevado valor unitário), que seja possível controlá-la por unidade vendida e unidade comprada, determinando se o preço específico de cada unidade estocada e dando-se baixa, em cada venda, por unidade. Dessa forma, cada artigo terá seu preço específico e, por este preço, será dada baixa no momento da venda. Quando selecionar para utilizar o tipo de custo no produto como específico, será obrigatório trabalhar com número de série. Este custo é para quem possui integração com  [TOTVS Gestão Planejamento e Controle da Produção](http://tdn.totvs.com/pages/viewpage.action?pageId=433238176) no qual o produto acabado possui número de série. Através do Número de Série, o Sistema calculará o custo distintamente, com base no valor específico cadastrado para cada um deles, exemplo:

4
incomplete
O TOTVS RM Factor produz um automóvel, e cada unidade está representada pelo número de série. Neste caso, o custo poderá ser diferenciado para cada item no momento da baixa, pois mesmo sendo o mesmo produto, ele pode conter diferenças criadas no processo produtivo que impactará no cálculo. Imagine que um carro que tem o número de série 123456 tem como custo, R$ 18.000,00, mas o mesmo carro, sendo do número de série 333333 terá seu custo R$ 22,000.00 pois foi agregado um outro acessório, devido diferenças no processo produtivo. Então o usuário poderá utilizar o Custo Específico, onde este será calculado de acordo com cada número de série. Este número de série será apresentado a numeração mais o custo do produto acabado.

6
incomplete
O TOTVS RM Factor pode utilizar custo de reposição A e B no custeio de componentes do item de ordem, neste caso é importante observar que os movimentos envolvidos estejam parametrizados para afetar custo de reposição, dessa forma esses custos serão registrados e podem ser utilizados no RM Factor.

Com a opção de Custo de Aquisição marcada, a avaliação de estoque do produto será pelo Custo de Aquisição e será levado em consideração o último custo unitário da tabela de estoque . No relatório de ficha física-financeira deverá aparece o título da coluna de custo como "C. Aquisi." com o valor do custo de aquisição para os movimentos de saída, exemplo:

* 5
  incomplete
  Suponha que em 11/10/02 seja incluído um movimento Compra Nota Fiscal com o produto 1.01(cálculo do custo feito por PEPS) com quantidade 10 e valor unitário 5 e no dia 12/10/02 seja incluído um outro mov. de Compra Nota Fiscal com o produto 1.01 quantidade 15 e valor unitário 13. Ao efetuar um mov. de venda com qte 12, ao emitir a Ficha Física Financeira deste produto será gerado para este movimento de venda duas linhas. A 1ª linha com quantidade10 e valor unitário 5 e a 2ª com quantidade 2 , valor unitário 13,00.

Se o campo cálculo do custo estiver em branco, o cálculo será feito através do custo médio. Se o método for alterado para PEPS ou UEPS é aconselhável a regeração total dos saldos e custos do produto. Se o método utilizado para o cálculo do custo unitário do produto for PEPS ou UEPS não será permitido trabalhar com controle de produto por lote.

**Integração:**Nesta pasta, serão informados os dados do Contrato do Produto e da Integração TOTVS Linha RM: Integração Contábil (TOTVS Gestão Contábil), de Patrimônio (TOTVS Gestão Patrimonial), de Serviço de Manutenção (TOTVS Officina), EPI (TOTVS Vitae) e TOTVS Saúde. Integração TOTVS Linha PROTHEUS: integração com TOTVS Manutenção de Ativos - SIGAMNT, integração TOTVS Rental - SIGALOC, TOTVS SIGALOJA e Integração com NG Quirons - Saúde e segurança do trabalho (produtos EPIs).

***Observação**:*Será possível informar um produto cujo valor é referente a encargos sobre o produto que está incluindo, exemplo:  
Vamos supor que vendemos o produto "Alfa" que tem o valor final de R$ 1.000,00, porém na nota fiscal, este valor deverá ser impresso da seguinte forma:

|  |  |
| --- | --- |
| Produto Alfa | 500,00 |
| Encargos sobre o produto Alfa | 500,00 |
| Valor Total | 1.000,00 |

Para isso, foi criado um produto "Encargos sobre o produto Alfa", com preço igual a R$ 500,00, informamos este no campo "Produto para Encargo" do produto "Alfa" e quando emitirmos a nota para esta venda, este aparecerá junto com o produto.  
***Observação***: Nesta pasta será possível indicar uma conta gerencial que poderá ser o default de todo lançamento gerencial executado para este produto, o sistema buscará este default através do evento contábil se indicar na pasta gerencial do item do evento, no campo origem da conta a opção "Default Tabelas". Em atendimento a NF-e 4.0, deve-se informar o código de produto na ANVISA para os produtos do ramo de medicamentos.

**Código de Barras:**Nesta pasta serão informados os Códigos de Barra para o produto.

***Observações**:*É possível utilizar o código EAN para digitar itens no movimento, para isto é necessário que nos parâmetros de tipos de movimentos, pasta itens/identificação, no campo "Código do Produto" selecione a opção "Código EAN". Se estiver parametrizado que este movimento busque o produto pelo código de barras. Será impedida a exclusão de um Código de Barra do Produto que esteja associado a uma movimentação. O botão Calcular Dígito Verificador calcula automaticamente o dígito verificador do código de barras, baseado na especificação do código interno padrão EAN/ UCC – 13 ou EAN / UCC – 14. Na seleção de Unidade, serão listadas todas as opções que contenham "Unidade Base" igual ao valor definido em "Cód. Unidade Base" da Unidade de Controle definida na pasta "Controle de Estoque", exemplo:

**Calcular Dígito Verificador (DV)**: O sistema tratará, para cálculo do dígito verificador, apenas os códigos EAN/UCC-13 e EAN/UCC-14. Se informado um código de barras com 12 dígitos, o sistema calculará o 13º dígito. Se informado um código de barras de treze dígitos, o sistema calculará o 14º.  
Como é calculado o dígito verificador para EAN/UCC-13 e EAN/UCC-14?  
*Passo 1*: Abaixo do código completo (sem o dígito verificador) e começando pela direita, situe alternadamente os pesos 3 e 1 para cada um dos dígitos, iniciando com peso 3.   
7 8 9 8 3 5 7 4 1 0 0 1 DV   
1 3 1 3 1 3 1 3 1 3 1 3 = pesos

*Passo 2*: Multiplique cada dígito pelo peso correspondente:   
7 8 9 8 3 5 7 4 1 0 0 1 DV   
1 3 1 3 1 3 1 3 1 3 1 3   
7 24 9 24 3 15 7 12 1 0 0 3 = resultado das multiplicações

*Passo 3*: Some todos os resultados das multiplicações:   
7  24  9  24  3  15  7  12  1  0  0  3 **=** 105   
*Passo 4*: O resultado obtido na soma (105) deve ser subtraído do múltiplo de 10 imediatamente maior do que ele. Então: 110 105 **=** 5   
O dígito de controle será o resultado dessa subtração. No exemplo acima, é o número 5. Quando a soma total resultar em um múltiplo de 10 (EX: 80,100, 120, etc.), o dígito de controle será "0" (zero).

**Lote**: Será possível vincular um Lote do produto ao Código de Barras. Para isso o produto deve estar com a opção "Controlado Por Lote" marcada. Recomendamos que a parametrização "Permitir Número de Lote Repetido", a qual pode ser parametrizada em: Movimento > Parâmetros Gerais > Tabela > Produtos > Lote, esteja desmarcada, isso se faz necessário para o melhor funcionamento do processo.

Recurso disponível na release 12.1.2205 ou superior.

**Num. Série**: Será possível vincular um Número de Série do produto ao Código de Barras. Para isso o produto deve estar com a opção "Usa Número de Série" marcada. O número de série informado não poderá estar sendo utilizado por outro código de barras já cadastrado.

Recurso disponível na release 12.1.2205 ou superior.

**Código de barra EAN de uso interno**: Ao marcar essa opção, o sistema desabilita o botão "Calcular Dígito Verificador" e gera um código de barras único por produto, esse código pode ser usado para fins de controle interno da empresa. O código de barras é gerado automaticamente e não permite edição. O padrão do código de barras gerado é o seguinte:

* 1º e 2º dígitos: é sempre o valor fixo de 25.
* 3º e 4º dígitos: se refere a Coligada do Produto.
* 5º ao 12º dígito: se refere ao Identificador do Produto (Campo IDPRD da tabela TPRODUTO).
* 13º dígito: é o dígito verificador do código de barras, ele é calculado conforme a mesma regra (cálculo descrito acima) realizada ao clicar no botão "Calcular Dígito Verificador".

Observação: Durante o processo de cadastro do produto, o valor exibido neste campo será -1. No entanto, ao salvar o produto, o valor será calculado corretamente. Já no processo de edição, o valor será exibido corretamente desde o início.

Ao criar novos produtos de Grade Numerada pelo menu Cadastros | Tabelas Auxiliares | [Grade Numerada por Produto](http://tdn.totvs.com/display/LRM/Grade+Numerada+por+Produto) | Processos | Assistente Grade Numerada, para facilitar a identificação de cada item da grade, os produtos da grade já são criados com o Código de Barras EAN de uso interno.

**Tipo do código de barras**: classificação quanto ao tipo de código de barras, podendo ser de dois tipos:

1. GTIN;
2. Interno.

É interessante o usuário se atentar aos pontos abaixo para classificar o código de barras:

* **O Tipo GTIN deverá ser escolhido para a situação abaixo:**  
  Conforme especificado na NT2017.001, os campos cEAN (I03) e cEANTrib (I12) devem ser utilizados exclusivamente para informação de códigos GTIN (Global Trade Item Number) do produto, antigo código EAN. Para esta opção é obrigatório que o código de barras tenha o tamanho 8, 12, 13 ou 14 caracteres caso contrário o sistema não permitira o seu cadastro.
* **O Tipo Interno deverá ser selecionado para a situações abaixo:**  
  Como existem outros códigos de barras em uso no Brasil, para que um contribuinte possa informar simultaneamente o código de barras utilizado por seu fornecedor e o seu (do contribuinte) código interno, ficam criados os campos cBarra (I03a) e cBarraTrib (I12a), sem validações, para que seja possível a informação de códigos de barras diferentes do padrão GTIN usados pelo emitente e pelo destinatário. Não existe qualquer tipo de validação do código de barras quando selecionada tal opção.

**Informações por Filial:** Nesta pasta serão informados os parâmetros referentes ao produto por filial. Desta forma, cada filial pode ter uma parametrização diferente.

**Produto estocável na filial:** Define se o produto é estocável ou não nesta filial.

**Tributação Cupom Fiscal:** Define o código de tributação do Cupom Fiscal.

**Consignado:** Utilizado exclusivamente para Cupom Fiscal. Define se o produto é consignado.

Quando sim. Se o Tipo de Movimento for "Venda Mercadoria Em Consignação" e possui Efeito sobre o Saldo Vendido de Terceiros, realiza a Quebra dos Itens de Cupom.

* **Prioridade:**
  + **Estoque próprio:** Baseia a quebra dos itens do cupom com base no estoque "próprio".
  + **Estoque de terceiros:** Baseia a quebra dos itens do cupom com base no estoque **"**de terceiros".

**Situação da Mercadoria:** Define qual é a situação da Mercadoria.

* Mercadoria para Revenda
* Matéria Prima
* Produto Em Elaboração
* Produto Acabado
* Material de Acondicionamento e Embalagem
* Mercadoria Recebida em Consignação
* Outras Mercadorias Ou Produtos
* Embalagem
* Subproduto
* Produto Intermediário
* Material de Uso e Consumo
* Ativo Imobilizado
* Serviços
* Outras
* Outros Insumos
* Bens Almoxarifado

IMPORTANTE

Conforme a **Norma Técnica 2020.005 v 1.10** que entrará em vigor em 09/2021, os códigos de barras do produto devem ser classificados conforme os tipos acima.

É de responsabilidade de cada cliente revisar e classificar de forma correta os códigos de barras cadastrados nos produtos, para que na rotina de envio de Nota Fiscal Eletrônica (NF-e) os campos cEAN (I03) e cEANTrib (I12) sejam preenchidos conforme a NT exige.

Caso seja utilizado a rotina de Assistente de Geração de Grade Numerada, é necessário classificar os códigos de barras gerados no produto pela rotina.

ATENÇÃO

Os códigos de barras compatíveis com as funcionalidades do Totvs Estoque, Compras e Faturamento são:

* EAN 13
* EAN 128
* DATA MATRIX

**Repositório de Arquivos**

A partir da versão 12.1.2402 a visão de Produto passa a exibir a nova funcionalidade [Repositório de Arquivos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=784778828).

---

Informações Adicionais

[Gráfico de Consumo de Materiais por Centro de Custo no Mês](http://tdn.totvs.com/pages/viewpage.action?pageId=4813450)
