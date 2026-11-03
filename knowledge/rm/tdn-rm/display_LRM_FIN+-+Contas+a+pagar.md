---
content_hash: 74214b1b623e12ab20703547b5c164131b0811ac3056dd77cbd3ae501e6f7b5b
fetched_at: '2026-06-29T00:09:19.270621+00:00'
page_id: '421388835'
product: rm
source: tdn-rm
title: FIN - Contas a pagar
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar
version: 101
---

Manutenção de LançamentosLançamento

**Tabelas opcionais**

Usar tabelas opcionais:

Define as características gerais das tabelas opcionais e sua obrigatoriedade nos lançamentos e extratos.

Visualizar tabela opcional que não permita lançamento:

Os itens das tabelas opcionais que não permitam lançamentos serão listados na pesquisa.

**Centro de custo**

Máscara do centro de custo:

Define a máscara do centro de custo.

Exibir centro de custo que não permitem lançamentos:

Exibe centros de custo que não permite lançamentos na lista de seleção.   

Usa código reduzido:

Permite utilizar um código reduzido para o centro de custo.

Usa código estruturado por Módulo:

Permite que depois de marcado para utilizar o código reduzido do centro de custo um módulo específico continue trabalhando com o Código estruturado.

**Obs**: Alguns Módulos/Telas não utilizam o cadastro de centro de custo do módulo contábil, desta forma a parametrização feita aqui não será aplicada.

**Calendário oficial**

Calendário oficial:

Define o calendário que será utilizado no sistema. Estes calendários são cadastrados no menu Cadastros | Calendário. O calendário escolhido será utilizado nos lançamentos e nas fórmulas para cálculo de dias úteis.

Considerar sábado como dia útil:

Define que o sábado será considerado como dia útil nos processos de manipulação de datas. Este parâmetro não será considerado nas aplicações financeiras pois, não há indexador para sábados.

**Opções gerais**

Os parâmetros de Opções Gerais são utilizados para definir algumas regras gerais do sistema. 

Número de Casas Decimais 

Informe a quantidade de casas decimais que terão os campos de "Valores" do cadastro de Lançamento Financeiro.

**Cliente/fornecedor**

Permite globais:

Define se será utilizada a coligada global (coligada = 0) nos cadastros tipo de cliente/fornecedor e  cliente/fornecedor.

Default Cli/For global:

Define que na inclusão de novo cliente/fornecedor, o campo global será marcado automaticamente.

Estado obrigatório:

Define se o estado será de preenchimento obrigatório na inclusão de novo cliente/fornecedor.

Tipo de cliente/fornecedor obrigatório:

Define se o tipo de cliente/fornecedor será de preenchimento obrigatório na inclusão de novo cliente/fornecedor.

Usar código sequencial (se máscara for numérica):

Define se o código do cliente/fornecedor será sequencial numérica.

Permite nomes iguais para contatos para o mesmo cli/for:

Define se o sistema permitirá o cadastro de contatos com nomes iguais para o mesmo Cli/For.

Permite CPF/CNPJ de cli/for global repetido em coligadas distintas:

Permite incluir cliente/fornecedor global com CPF/CNPJ já cadastrado em coligada diferente.

Usar Dados Bancários Global do Cliente/Fornecedor:

Ao marcar este parâmetro, é exibida uma tela solicitando que o usuário informe uma coligada de referência. Ao concluir o assistente de parametrização, todas as informações de dados bancários da coligada selecionada são transformadas em globais (coligada zero). Em seguida, o processo faz com que todos os boletos e lançamentos financeiros de fornecedores globais passem a referenciar estes dados bancários globais. Esse processo é realizado em **todas** as coligadas que permitem dados globais.

**Importante**: Para que o processo seja executado corretamente, é necessário que a coligada selecionada como referência possua os dados de pagamentos de **todos** os fornecedores globais de **todas** as coligadas. As formas de pagamento de cada fornecedor também devem respeitar a mesma sequência (*IDPGTO*) nas diferentes coligadas. Caso haja um lançamento ou boleto em qualquer coligada de um fornecedor global que não esteja configurado nos dados bancários da coligada de referência, o banco de dados retornará um erro.

Mudança de comportamento 

A partir da **release 12.1.2602** esse parâmetro passa a ser **apenas para consulta de status** do uso dos dados bancários do cliente/fornecedor de forma global, para que ele possa ser ativado ou desativado será necessário executar o processo  através do menu: **Utilitários | Outros | Mais | Ativar/Desativar Dados Bancários Global**.

Máscara do Código

Define a máscara do código do cliente/fornecedor.  

* #  Somente números.
* l Somente letras.
* L Somente letras (converte para maiúsculas).
* a Letras e números.
* A Letras e números (converte para maiúsculas).
* Q Qualquer caractere, exceto os separadores.
* Separadores: Ponto, vírgula, traço, dois pontos, barra, espaço em branco e parênteses.

Código Cli/For Automático Protheus

Quando integrado o RM com Protheus e EAI 2.0 esse parâmetro irá controlar o preenchimento manual ou automático do [código do Cliente/Fornecedor](https://tdn.totvs.com/x/8uEdGQ) na inclusão de um novo.  Quando o parâmetro "Usar código sequencial (se máscara for numérica" estiver marcado o parâmetro "Código Cli/For Automático Protheus" não ficará habilitado para edição.

**Pessoa Física**

CPF obrigatório

CPF obrigatório na inclusão de cliente/fornecedor do tipo pessoa física.   

CPF único

Define que não será permitido incluir mais de um cliente/fornecedor com o mesmo CPF.   

Permite CPF repetido para produtor rural com insc. estadual diferente

Define que poderá incluir CPF repetido para produtor rural com insc. estadual diferente. O parâmetro só habilitará caso o parâmetro CPF único esteja marcado.

**Pessoa Jurídica**

CNPJ obrigatório

CNPJ obrigatório na inclusão de cliente/fornecedor do tipo pessoa jurídica quando o campo país for igual à Brasil.   

CNPJ único

Define que não será permitido incluir mais de um cliente/fornecedor com o mesmo CNPJ.   

CNPJ com 8 primeiros dígitos únicos

Define que será possível incluir cliente/fornecedor com CNPJ que tenha os 8 primeiros dígitos únicos.   

Permite informar CEI no CNPJ

Define que será possível inserir CEI no campo de CNPJ.

Permite somente um CNPJ repetido ativo

Define que será possível inserir um CNPJ repetido apenas se os outros cliente/fornecedores com mesmo CNPJ estiverem inativos.

**Cli/For. Opcionais**

Usar campo alfa:

Define se o campo opcional alfabético do cliente/fornecedor será utilizado.

Usar valor opcional:

Define se o campo opcional valor do cliente/fornecedor será utilizado.

Usar data opcional:

Define se o campo opcional data do cliente/fornecedor será utilizado.

**Recursos adicionais**

Os parâmetros de Recursos Adicionais são utilizados para definir alguns recursos adicionais para os lançamentos financeiros. 

Rateio centro de custo / natureza orçamentária  

* Usar rateio para: Define em que nível será feito o controle financeiro de despesas e recebimentos.
* Obrigatoriedade: Define o nível de obrigatoriedade dos rateios por centro de custo / natureza orçamentária.

Rateio departamento    

* Obrigatoriedade: Define o nível de obrigatoriedade dos rateios por departamento.

Bloqueio para baixa     

* Usar bloqueio: Define o nível de bloqueio dos lançamentos (sem, simples ou duplo). Um [lançamento bloqueado](https://tdn.totvs.com/pages/editpage.action?pageId=421388717) não pode ser baixado, não permite a emissão de cheque nem remessa de cobrança/pagamento eletrônico.
* Valor mínimo: Define o valor mínimo para que o lançamento fique bloqueado.

Bloquear o lançamento para alterações automaticamente ao desbloquear da baixa:

Define que ao [desbloquear um lançamento para baixa,](https://tdn.totvs.com/pages/editpage.action?pageId=421388717) o mesmo ficará bloqueado para alteração.

Desbloqueio duplo deve ser feito por usuários diferentes:

Define que o bloqueio deverá ser feito por dois usuários diferentes.

**Datas opcionais**

Usar data opcional

Define as datas opcionais a serem utilizadas nos lançamentos.

Consistir valores das datas opcionais na geração de acordo de lançamento

Define que irá consistir os valores das datas opcionais na geração de acordo de lançamentos financeiros.

Não enviar as datas opcionais para os lançamentos gerados por acordo

Se desmarcada essa opção as datas opcionais do primeiro lançamento, serão enviadas para os lançamentos filhos.

**Alfa opcionais**

Alfa Opcionais são campos alfanuméricos que podem ser incluídos na janela de edição dos lançamentos financeiros.  
Marque o parâmetro e informe um nome para ele, ao gravar a parametrização o campo é apresentado na pasta "Opcionais" da janela de edição dos lançamentos.

Usar campo Alfa

Define os campos alfa opcionais a serem utilizadas nos lançamentos.

Consistir valores dos campos alfas na geração de acordo de lançamento

Define que irá consistir os valores dos campos alfas na geração de acordo de lançamentos financeiros.

Não enviar os campos alfa opcionais para os lançamentos gerados por acordo

Se desmarcada essa opção os valores dos campos alfas opcionais do primeiro lançamento, serão enviadas para os lançamentos filhos.

**Valores opcionais**

Através desses parâmetros, pode-se habilitar até 8 campos de valores, configurando o Nome e a Ação que esses campos terão no sistema.

Default

 O valor opcional pode ser preenchido no momento da edição do lançamento ou ser apresentado com uma porcentagem default, para isso, deve ser informado um default no campo Default.

Até o Vencimento

Essa opção fica disponível se a ação do valor opcional for "Descontar", "Descontar se a receber" ou "Descontar se a pagar".  
Com essa opção marcada, o valor opcional só é considerado até a data de vencimento. Quando a opção estiver desmarcada, o valor opcional sempre é considerado.

Dias de Atraso

Esse campo fica disponível se a ação do valor opcional for "Acrescentar", "Acrescentar se a receber" ou "Acrescentar se a pagar".

Não enviar valores opcionais com ação "Nada" para o item de baixa

Define que os valores opcionais que não interferem no líquido, não serão registrados no item de baixa.

IPTE/Cod. Barras

Visível somente se o parâmetro *Consiste IPTE/Código de barras* marcado, indica se o Valor Opcional será considerado na composição do valor do lançamento na consistência de IPTE/código de barras em lançamentos a pagar.

**Valores de Integração**

Permite configurar valores de integração para lançamentos financeiros somente para aqueles com origem de Aplicação como "Financeiro"**(F)**. Estes quando parametrizados estarão disponíveis nos lançamentos financeiros na inclusão e alteração.

Quando valor de integração estiver configurado com fórmula, a mesma é executada ao salvar o registro de lançamento na inclusão.

Parâmetros por módulo

Quando definido o módulo os valores de integração do financeiro que foram parametrizados na janela anterior serão carregados automaticamente na inclusão do lançamento no módulo de origem. Poderão ser parametrizados os seguintes módulos:

* Educacional
* Gestão de Estoque, Compras e Faturamento
* Obras e Projetos

**Inclusão**

Este parâmetro define a origem default de campos na inclusão do lançamento financeiro. Os campos que serão atualizados serão os disponíveis no cadastro default das tabelas selecionadas.

Conta/caixa obrigatório no lançamento

Define que a conta-caixa será obrigatória no lançamento

Permite data de vencimento menor que data de emissão

Define que será possível incluir lançamento com data de vencimento menor que a data de emissão do mesmo.

Permite data de vencimento menor que data do sistema

Define que será possível incluir lançamento com data de vencimento menor que a data do sistema.

Filtra cli/for de acordo com a natureza do lançamento

Define que a seleção de cliente/fornecedor será definida pela natureza do lançamento. Lançamentos a receber, apenas clientes disponíveis. Lançamentos a pagar, apenas fornecedores disponíveis.

Máscara tipo de documento:

Define a máscara do tipo de documento.   

* #:Somente números.
* l Somente letras.
* L Somente letras (converte para maiúsculas).
* a Letras e números.
* A Letras e números (converte para maiúsculas).
* Q Qualquer caractere, exceto os separadores.
* Separadores: Ponto, vírgula, traço, dois pontos, barra, espaço em branco e parênteses.

Permite lançamentos zerados

Define o tipo contábil de lançamento que permitirá incluir lançamento com valor zero.         

Fórmulas/valores defaults                    

* Valores

Define valores defaults para desconto, juros, multa e capitalização.  

Origem tabelas

* Conta/Caixa

As informações buscadas são as definidas no cadastro de Conta/Caixa como default (em Menu Cadastros | Conta/Caixa | Editar a Conta Caixa em questão | Anexos | Defaults de Conta/Caixa.

* Cliente/Fornecedor

As informações buscadas são as definidas no cadastro de Cliente/Fornecedor como default (em Menu Cadastros | Cliente/Fornecedor | Editar o Cliente/Fornecedor em questão | Anexos | Defaults de Cli/For. 

* Sem Default:

Não busca nenhuma informação.

Tamanho do número

Define o tamanho máximo do número do documento e segundo número.

Nº Decimais Percentual

Define o número de casas decimais nos percentuais do lançamento.

Permite alteração fora do período de emissão

Define alteração de lançamento fora do período de emissão que é definido na etapa de "inclusão a pagar". Este valida os lançamentos de acordo com o parâmetro 'Período para emissão'.

Não atualizar a data da última movimentação do cli/for

Esse parâmetro permitirá que o usuário defina se na inclusão de lançamento o sistema irá ou não atualizar a data da última movimentação Cli/For. Assim, se marcado o parâmetro, o sistema não fará a atualização da data de movimentação do cli/for. Se desmarcado, a inclusão de lançamento atualizará a data de movimentação.

Permite numeração repetida em lançamento quando já cancelado:

Esse parâmetro permite a inclusão de lançamento, com as mesmas informações dos campos Coligada, Filial, Tipo(a pagar/ a receber), Cliente/Fornecedor, Tipo de Documento, Número e Série, quando lançamento equivalente estiver cancelado.

**Inclusão a pagar**

Incluir lançamentos a pagar bloqueados para baixa

Define que os lançamentos a pagar serão incluídos bloqueados para baixa utilizando as parametrizações da etapa "Recursos adicionais".

Permite alterar lançamentos a pagar remetidos ao banco

Permite alteração em lançamentos a pagar que foram previamente remetidos ao banco.

Preencher números do lançamento com zeros

Define que os números utilizados nos lançamentos serão preenchidos com zero. São números do lançamento: Número do documento, segundo número, número contábil de inclusão, número contábil de baixa.

Consiste prazo mínimo de vencimento

Define que será consistido o número de dias entre data do sistema e data de vencimento na inclusão ou alteração de lançamentos a pagar. Na alteração a consistência ocorre apenas quando a data de vencimento é alterada.

Número de dias permitidos: [Data de vencimento (no mínimo) = Data sistema + número de dias].

Período para emissão

Define período de emissão para lançamentos a pagar.

Consiste IPTE/Código de Barras

Quando marcado este parâmetro o sistema irá consistir se os dados informados no lançamento como valor e data de vencimento, correspondem aos valores gravados na Linha Digitável (IPTE).  Assim quando alterado qualquer um desses campos o sistema fará a validação do parâmetro e não permitirá salvar a alteração.  Outra consistência é que o sistema não permitirá a inclusão de mais de um lançamento com o mesmo código de barras, evitando o pagamento em duplicidade dos títulos.

O valor que será considerado na validação é o Valor original - Valor IRRF - Valor INSS - Valor das retenções

Aceita vencimento a pagar em finais de semana e feriados

Define como será o vencimento de lançamentos em finais de semana e feriados. 

Aceita previsão de baixa a pagar em finais de semana e feriados

Define como será a previsão de baixa a pagar de lançamentos em finais de semana e feriados. Este comportamento é valido tanto para a operação de inclusão como para alteração de lançamentos financeiros.

**Alteração**

Restringe alteração de valor original em lançamentos originados do TOTVS Folha de Pagamento

Define que não será permitida alteração de valor original quando o lançamento for oriundo do TOTVS Folha de Pagamento.

**Situação cli/for**

Controla atualização do cadastro de Cliente/Fornecedor

Define se será controlada a atualização do cadastro de cliente/fornecedor e qual a ação sobre isso. Se apenas avisa, ou bloqueia a inclusão de lançamento para tal cliente/fornecedor.

Liberar o bloqueio de cliente/fornecedor com a senha de supervisor (clientes em atraso, vencidos e limite de crédito

Define se será possível incluir lançamento para casos de bloqueio de cliente/fornecedor através de senha de supervisor. Essa funcionalidade estará disponível apenas na tela de lançamento quando houver parametrização e edição do lançamento. No processo de "Alteração Global" o sistema fará a consistência do controle, porém não apresentará tal funcionalidade para execução, sendo preciso que a alteração com desbloqueio de senha seja realizada via tela de processo.

**Cancelamento da inclusão**

Histórico default de cancelamento do lançamento

Define histórico default de cancelamento de lançamento.

**Integração fiscal**

Lançamentos de tributos serão faturados pelo TOTVS Gestão Fiscal

Com o parâmetro marcado o sistema não permitirá gerar acordo, baixar, emitir cheque, faturar, realizar vínculo, importar arquivo de pagamento e importar baixa para os lançamentos que possuírem as seguintes classificações:

* 6 (IRRF/PJ)
* 7 (IRRF/PF)
* 13 (IRRF gerado pelo TOTVS Folha de Pagamento)
* 18 (CSLL/RF)
* 19 (PIS/RF)
* 20 (COFINS/RF)
* 21 (Tributos Agrupados)

Para todos esses lançamentos deverá ser feita a geração automática de DARF através do TOTVS Gestão Fiscal. 

Com o parâmetro "desmarcado" não será possível:

* Gerar Acordo
* Vínculos

**Observação** 

Dependendo de algumas configurações o sistema terá comportamentos diferentes: 

* Opção 1

TOTVS Gestão Fiscal x TOTVS Gestão Financeira Integrados Parâmetro "Lançamentos de Tributos serão faturados pelo TOTVS Gestão Fiscal": Ativo

Não será permitida a baixa sem antes processar o encerramento do período seguido de geração de lançamentos financeiros correspondentes aos tributos pelo TOTVS Gestão Fiscal.

* Opção 2

TOTVS Gestão Fiscal x TOTVS Gestão Financeira Integrados Parâmetro "Lançamentos de Tributos serão faturados pelo TOTVS Gestão Fiscal": Não Ativo

Ao baixar o lançamento financeiro correspondente ao tributo, será exibida a seguinte mensagem: "Em função da atual parametrização do aplicativo, os lançamentos associados aos tributos federais poderão ser faturados/baixados diretamente no TOTVS Gestão Financeira, porém os dados destes lançamentos não constarão na Rotina DCTF pelo TOTVS Gestão Fiscal".

* Opção 3

TOTVS Gestão Fiscal x TOTVS Gestão Financeira NÃO Integrados Parâmetro "Lançamentos de Tributos serão faturados pelo TOTVS Gestão Fiscal": Não Ativo

Ao baixar o lançamento financeiro correspondente ao tributo, não será feita nenhuma consistência porque nesse caso não existe integração entre o TOTVS Gestão Financeira e o TOTVS Gestão Fiscal.

**Natureza financeira**

Utiliza natureza orçamentária/financeira

Define se usará natureza orçamentária/financeira nos lançamentos.

* Permite globais
* Máscara

Define como será a máscara da natureza:      

* # Somente números.
* l Somente letras.
* L Somente letras (converte para maiúsculas).
* a Letras e números.
* A Letras e números (converte para maiúsculas).
* Q Qualquer caractere, exceto os separadores.
* Separadores: Ponto, vírgula, traço, dois pontos, barra, espaço em branco e parênteses.

**Integração Labore**

Pagamento Autônomo

Valor de ISS (Vr. Opcional) - Define o valor opcional que corresponde ao valor do ISS para pagamento de autônomo.

Cálculo de Tributos

**Geração IRRF**

Gerar imposto de renda automaticamente

Se esse parâmetro for ativado, o sistema passará a incluir automaticamente o documento referente a Imposto de Renda - DARF e RPA na inclusão ou baixa (depende do que foi definido como data base para geração) do lançamentos que tenham incidência de impostos. 

Origem default das tabelas  

Origem das tabelas: Define a origem default das tabelas para o lançamento de IRRF gerado (DARF/RPA). Se será fornecedor ou lançamento original.

Buscar dados no lançamento se não preenchidos no fornecedor

Define que os dados serão buscados no lançamentos se não preenchidos no fornecedor. 

Observação

Caso exista um período de apuração aberto para o tributo IRRF, na mesma coligada e filial do lançamento onde a data do período contempla a data de emissão do tançamento. Este parâmetro será sobreposto especificamente para a natureza orçamentária financeira respeitando primeiramente a informação preenchida no cadastro do tributo, caso esteja preenchida.

Histórico do lançamento de IRRF gerado

Define o histórico do lançamento de IRRF.

Valor mínimo

Define o valor mínimo para geração de IRRF.

Gerar número de documento de acordo com os parâmetros dos lançamentos

Define que o número do lançamento de IRRF (DARF/RPA) será gerado de acordo com os parâmetros do lançamento financeiro.  

Controla IRRF para residente ou domiciliado no exterior

Define o controle de IRRF para residente ou domiciliado no exterior. O cálculo do IRRF de Pessoa Física é calculado diretamente por alíquota informada no código de receita (similar ao cálculo de IRRF-PJ). Se utilizada o código de receita 9478 (Aluguel e Arrendamento), a data de vencimento do lançamento de IRRF gerado pelo TOTVS Gestão Financeira terá como data de vencimento a própria data de geração do tributo, em conformidade com o que dispõe no art. 70 da Lei 11.196/2005. Vide o link abaixo para maiores detalhes.

<https://tdn.totvs.com/display/public/ConSeg/DARF+-+Prazo+de+Recolhimento+-+Rendimentos+de+Aluguel+para+PF+Residente+no+Exterior>

**Geração IRRF - PF**

Data base para geração

Define a data base para geração de IRRF - PF (emissão, vencimento, contab. Inclusão ou baixa). 

Data base substituta para data de contabilização de inclusão para geração

Define data base substituta para data de contabilização de inclusão para geração (emissão, vencimento ou digitação). Só é habilitado caso a data base para geração seja Contab. Inclusão).     

Fornecedor

Define fornecedor para lançamento de geração de lançamento IRRF - PF, deve possuir País igual a 1 que é Brasil.

Tipo de documento

Define o tipo de documento a ser utilizado na geração de lançamento de IRRF - PF.

Acrescentar valor á base de cálculo

Permite definir uma fórmula, para acrescentar valor à base de cálculo para geração do IRRF PF. Esse acréscimo somente irá incidir sobre o código 3208 "IRRF - ALUGUÉIS E ROYALTIES PAGOS A PESSOA FÍSICA" e o parâmetro "Data Base para Geração" for igual a "Baixa".

**Observação:**

Funções de formula: VALORJUROS, VALORMULTA, VALORCAP, VALORLIQUIDO, VALORLIQUIDOPORDATA e VALORLIQUIDOPF não poderão ser utilizadas a fim de evitar referências circulares no processo.

Calcular valor de IRRF de pessoa física do lançamento faturado durante a baixa

Define se os valores de IRRF nos lançamentos faturados serão atualizados ao efetuar a baixa de um vencimento de fatura.

**Observação:**

No processo de geração de fatura, caso esse parâmetro seja marcado, o sistema permitirá apenas um vencimento de fatura e os campos Tipo de Documento e Quantidade ficarão bloqueados. Para que os valores do IRRF - PF sejam atualizados será preciso também marcar o parâmetro "Proporcionalizar valor baixado dos lançamentos faturados pelo valor líquido" que está disponível em Contas a Pagar | Geração de Lançamentos | Fatura. A combinação desses dois parâmetros resultará na atualização dos valores na baixa de vencimento de fatura.

**Geração IRRF - PJ**

Data base para geração

Define a data base para geração de IRRF - PJ (emissão, vencimento, contab. Inclusão ou baixa).

Geração do IRRF por documento fiscal

Ao marcar essa opção a geração de IRRF PJ para o mesmo Cliente/Fornecedor será por documento fiscal e não por dia.

Data base substituta para data de contabilização de inclusão para geração

Define data base substituta para data de contabilização de inclusão para geração (emissão, vencimento ou digitação). Só é habilitado caso a data base para geração seja Contab. Inclusão).

Fornecedor

Define fornecedor para lançamento de geração de lançamento IRRF - PJ, deve possuir País igual a 1 que é Brasil.

Tipo de documento

Define o tipo de documento a ser utilizado na geração de lançamento de IRRF - PJ.

Arredonda valor do IRRF

Define se o valor de IRRF será arredondado.

**Geração INSS**

Gera INSS automaticamente

Define se o sistema passará a incluir automaticamente o documento referente a INSS na inclusão de lançamentos que tenham incidência de impostos.

Empregador                    

* Origem das tabelas:

Define a origem default das tabelas para o lançamento de INSS gerado (fornecedor, lançamento original).   

* Percentual

Define percentual do INSS Empregador. Tal parametrização implicará no cálculo do INSS do empregador por coligada. O valor default para o parâmetro será de 20%.   

* Tipo de documento

Define tipo de documento do INSS empregador. Este tipo de documento será usado na inclusão do lançamento automático derivado do lançamento com incidência do imposto para o empregador. Este tipo de documento não precisa ter o campo classificação preenchido.

Empregado                    

* Origem das tabelas

Define a origem default das tabelas para o lançamento de INSS gerado (fornecedor, lançamento original).   

* Tipo de documento

Define tipo de documento do INSS empregado. Este tipo de documento será usado na inclusão do lançamento automático derivado do lançamento com incidência do imposto para o empregado. Este tipo de documento não precisa ter o campo classificação preenchido.

Fornecedor

Define fornecedor de lançamento de INSS.

Data base para geração

Define data base de geração de lançamento de INSS (emissão, vencimento).

Histórico do lançamento de INSS gerado

Define o histórico default de lançamento de INSS gerado.

Valor mínimo

Define o valor mínimo para geração de lançamento de INSS.

Arredonda valor do INSS

Define que o valor gerado de INSS será arredondado.

Gerar número de documento de acordo com os parâmetros dos lançamentos

Define que o número do documento do lançamento de INSS será gerado conforme os parâmetros do lançamento.  

Buscar dados no lançamento, se cli/for vazio

Define que as tabelas serão buscadas no lançamento quando o cliente/fornecedor estiver vazio.

Entidade beneficente de assistência social isenta das contribuições sociais patronais

Define que entidades beneficentes de assistência social serão isentas de contribuições patronais. Para as coligadas com esse parâmetro marcado, o cálculo do INSS do autônomo será realizado da seguinte maneira: Ao incluir um lançamento a pagar para pessoa física com um tipo de documento gerador de INSS, será gerado um lançamento de INSS de 20% do valor do lançamento original que deve ser descontado do autônomo considerando o teto máximo de contribuição e o valor do INSS pago em outras empresas. Nesse caso, não deverá ser gerado o segundo lançamento referente ao valor pago pelo empregador.

Consistir número do contribuinte na geração dos lançamentos de INSS

Define que na geração de lançamento de INSS será verificado se o campo "número do contribuinte" do cliente/fornecedor está preenchido.

Calcular o INSS sem gerar os lançamentos financeiros relacionados

Com este parâmetro é possível incluir lançamentos financeiros que calculem valores de INSS, mas não geram lançamentos de INSS. Os valores são calculados e deduzidos, mas os lançamentos de INSS não são gerados.

Baixa

**Valor líquido**

Os parâmetros de Valor Líquido são utilizados para definir algumas regras no cálculo do valor líquido dos lançamentos financeiros.

Capitalizar o valor indexado

Define que o sistema irá indexar e depois capitalizar o valor do lançamento.

Ignorar valor do desconto em lançamentos vencidos

Define que o sistema irá ignorar desconto ao baixar lançamento vencido.

Multa / Juros

Calcula Multa/Juros ao Dia Usando

* Valor Original

Com este parâmetro marcado o sistema irá aplicar a porcentagem informada no campo Multa ao Dia (%) sobre o Valor Original do lançamento financeiro.

* Valor Líquido Parcial

Com este parâmetro marcado o sistema irá aplicar a porcentagem informada nos campos Multa/Juros ao Dia (%) sobre o Valor Líquido Parcial do lançamento financeiro.

Conversão de moeda

* Data conversão

Define a data utilizada para conversão de moedas (sistema, baixa, vencimento, emissão e previsão de baixa).

Usar no cálculo do valor líquido

Define que a data de conversão de moedas será utilizada como data no cálculo do valor líquido do lançamento.

Exibir valores em outra moeda na tela de vínculo

Exibe na tela de vínculo, colunas com valores em outra moeda e cotação utilizada na conversão de valores.

Juros  

Calcula juros ao dia usando: Define como será calculado os juros.      

* Valor original: Define que o sistema irá calcular os valores incidentes no lançamento (juros, valores opcionais) com base no valor original.
* Valor líquido parcial: Define que o sistema irá calcular os juros informados no lançamento com base no valor líquido. O cálculo é realizado desta forma: O sistema realiza os cálculos de todos os valores opcionais (juros e descontos) em seguida aplica este valor em cima do valor original do lançamento e em seguida é realizado o cálculo do juro que é informado no lançamento com base no valor líquido que foi calculado anteriormente.

Usar juros compostos

Define que o sistema irá calcular os juros "compostos" (cumulativos) na baixa de lançamentos. Para isso, valor dos juros ao dia do lançamento deve ser informado sobre taxa.                 

Considerar os dias de carência no cálculo dos juros ao dia

Define que no cálculo de juros ao dia, os dias serão contados a partir do final da carência. 

Multa   

Calcula multa ao dia usando: Define como será calculada a multa ao dia.       

* Valor original: Define que o sistema irá aplicar a porcentagem informada no campo Multa ao Dia (%) sobre o Valor Original do lançamento.
* Valor líquido parcial: Define que o sistema irá aplicar a porcentagem informada no campo Multa ao Dia (%) sobre o Valor Líquido Parcial do lançamento.

Aplicar multa em lançamentos

Define a natureza dos lançamentos que calcularão multa (receber, pagar e todos).

Dias de atraso

Define a quantidade de dias em atraso para a carência da multa.

**Baixa 1/6**

Gerar extrato compensado na baixa

Define que ao baixar um lançamento sem cheque no cadastro de lançamentos, o extrato deste lançamento será compensado automaticamente.

Permite data de baixa menor que data de emissão

Define que será permitido baixar lançamento com data de baixa menor que a data de emissão.

Permite alterar valores de baixa

Define que o sistema permitirá a alteração manual de valores na baixa.

Copiar tabelas opcionais para o extrato ao baixar

Define que as tabelas opcionais do lançamento serão copiadas para o extrato ao baixar.

Na baixa de vários lançamentos copiar tabelas opcionais se forem iguais

Define que na baixa de múltiplos lançamentos as tabelas opcionais serão copiadas para o extrato apenas se forem iguais.   

Permite alterar os valores do lançamento na baixa via a sessão de caixa

Define a permissão para alteração de valores do lançamento na baixa via sessão de caixa.   

Permite baixar lançamentos a contabilizar

Define que o sistema permitirá baixar lançamentos do tipo a contabilizar.

Arredonda valor do tributo

Define que ao gerar lançamentos de tributos os valores dos lançamentos serão arredondados de acordo com a quantidade de casas decimais utilizada.          

Período para baixa

Define período inicial e final permitido para baixa. 

Permite alteração de lançamento com data de baixa fora do período de baixa

Define que será permitido alterar lançamento com data de baixa fora do período de baixa.  

Copiar natureza orçamentária e centro de custo do rateio do lançamento para o extrato

Define que as informações de natureza orçamentária e centro de custo do primeiro rateio do lançamento, serão preenchidas no extrato.

Obs: Para lançamentos de crédito de adiantamento quando selecionado esse parâmetro, na etapa 3/6 da baixa devem ser informados os parâmetros **"Natureza orçamentária default de crédito de adiantamento a receber"**e **"Natureza orçamentária default de crédito de adiantamento a pagar"**. Caso esses parâmetros não forem fornecidos, a natureza orçamentária do crédito de adiantamento deve ser **"Ambos"** ou uma natureza orçamentaria que corresponda a natureza do lançamento de crédito de adiantamento.

**Baixa 2/6**

Vínculo de lançamento

* Permite vínculo de lançamentos entre filiais: Define que será permitido vincular lançamentos de filiais diferentes;
* Filtrar lançamentos sem possibilidade de vínculos no editar vínculos apresentados antes da baixa: Ao realizar a baixa, não será apresentada na tela de edição de vínculos, lançamentos que não possuem devolução, credito de adiantamento, Nota de credito do mesmo cliente/fornecedor.
* Não permite vínculo de lançamentos entre cliente/fornecedores diferentes: Define que NÃO será permitido o vínculo de lançamentos entre clientes/fornecedores diferentes.

Contabilizar crédito de adiantamento em filiais distintas

* Esse parâmetro indicará se a contabilização da baixa de crédito de adiantamento ocorrerá quando marcado ou não quando desmarcado. E se aplica quando a operação é com filiais diferentes.  
  Este parâmetro é por coligada e único, ou seja, quando marcado ou desmarcado no Contas a Pagar o comando é automático para o Contas a Receber e vice versa.

Bloqueio de alteração

* Bloquear o lançamento para alterações automaticamente ao baixar: Define que após a baixa de algum lançamento não será permitida nenhuma alteração ou operação neste.

Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa

Define que o processo de baixa não será interrompido se algum lançamento selecionado apresentar inconsistência. Quando marcado a rotina de baixa irá montar pacotes de lançamentos que precisam ser baixados juntos segundo critérios de vínculo, retenção acumulada, compartilhamento de boleto e forma de pagamento.

[Controlar concorrência na baixa de lançamentos](http://tdn.totvs.com/pages/viewpage.action?pageId=274659034)

O parâmetro "Controlar Concorrência na baixa de Lançamentos" foi implementado com o objetivo de garantir que não seja gerado item de baixa duplicado quando mais de um usuário executar simultaneamente os seguintes processos:

* Baixa Manual;
* Importação de Baixas;
* Retorno Cobrança;
* Retorno Débito automático;
* Retorno de Pagamento;
* Acordo;
* Emissão de Cheque;
* Recebimento via Cheque;
* Borderô;
* Desconto Duplicata;
* Integrações com:

* + Incorporação;
  + Gestão de Estoque, Compras e Faturamento;
  + Educacional;

**Baixa 3/6**

Nota de crédito de adiantamento

* Tipo de documento: Define o tipo de documento de nota de crédito de adiantamento. A classificação do tipo de documento deve ser "crédito de adiantamento".
* Natureza orçamentária default de crédito de adiantamento a receber: Define a natureza orçamentária default a ser utilizada no lançamento a receber de crédito de adiantamento gerado pela baixa do lançamento a pagar de adiantamento.
* Natureza orçamentária default de crédito de adiantamento a pagar: Define a natureza orçamentária default a ser utilizada no lançamento a pagar de crédito de adiantamento gerado pela baixa do lançamento a receber de adiantamento.

Contabilizar crédito de adiantamento em filiais distintas

* Esse parâmetro indicará se a contabilização da baixa de crédito de adiantamento ocorrerá quando marcado ou não quando desmarcado. E se aplica quando a operação é com filiais diferentes.   
  Este parâmetro é por coligada e único, ou seja, quando marcado ou desmarcado no Contas a Pagar o comando é automático para o Contas a Receber e vice versa.

Desconto de duplicata

Meio de pagamento: Define o meio de pagamento de desconto de duplicata.

**Baixa 4/6**

Modo de cálculo dos valores da baixa parcial

* Baixa calculada por prioridade

Define a ordem de prioridade dos valores na baixa. O primeiro valor a ser calculado é o das retenções, cuja base de cálculo é recalculada proporcionalmente em relação ao valor baixado. Os valores de INSS e IR são os próximos a serem calculados, que são sempre descontados na 1ª parcela, ou 1º pagamento. Na sequência são considerados os valores a descontar, na seguinte ordem: primeiramente o valor de SEST/SENAT, depois os valores de devoluções, os valores de notas de crédito, os adiantamentos, descontos e os valores opcionais a descontar. Depois os valores a acrescentar, na seguinte ordem: os juros, multa, capitalização, juros vendor e os valores opcionais a acrescentar. E por último o valor original baixado, que será calculado.

* Baixa calculada por proporcionalização

Define a proporcionalização dos valores na baixa. O valor pago é distribuído proporcionalmente por cada valor do lançamento, inclusive os valores de Integração. 1º considera o valor das retenções do item de baixa e considera o valor total de: IRRF, INSS, SEST/SENAT, Devoluções, Notas de Crédito e Adiantamentos. 2º considera os valores proporcionais de: Desconto, Vr. Opcionais a DESCONTAR, Valores de Integração a DESCONTAR. 3º considera os valores a ACRESCENTAR proporcionalmente. 4º considera o valor ORIGINAL proporcionalmente. 5º ajusta a diferença de cálculo entre os valores Calculados e o efetivamente BAIXADO Baixa calculada por proporcionalização

* Calcular os valores opcionais, multa, juros e desconto por prioridade

Define que estes valores serão descontados ou acrescentados 100% na baixa do lançamento.

**Baixa 5/6**

Retorno bancário

Nesta etapa é definido o meio de pagamento que será utilizado na baixa dos lançamentos financeiros provenientes das rotinas de retorno de cobrança, pagamento e débito automático. Apenas os cadastros de meio de pagamento cujo tipo primitivo for igual a 'Dinheiro', 'Outros' e 'Tipo Boleto Bancário' serão exibidos nos campos de retorno de cobrança e retorno de pagamento, enquanto somente os tipos primitivo 'Dinheiro' e 'Outros' serão apresentados no campo pertinente ao retorno de débito automático.

**Baixa 6/6**

Fórmula validação de baixa

Define uma fórmula para ser executada na baixa dos lançamentos.

Para que o processo de baixa seja interrompido, o resultado da fórmula deve retornar a mensagem que será mostrada ao usuário como o motivo para a não permissão de baixa.  Segue exemplo de fórmula:

SE TABLANBAIXA('VALORDESCONTO','V') > (TABLAN('VALORORIGINAL','V') \* 0.02)

ENTAO

'Valor desconto maior que o valor autorizado para desconto.'

SENAO  1

FIMSE

No exemplo acima, caso o valor de desconto ultrapasse o permitido, o sistema irá emitir a mensagem "Valor Desconto Maior que o Valor Autorizado para Desconto", e barrar a baixa.

**Observações:**

O resultado retornado pela fórmula para que o processo continue sem erros deve ser o valor 1 ou vazio "".

A fórmula utilizada deve ser criada com bastante critério, pois no caso da baixa de vários lançamentos ao mesmo tempo, pode haver queda de performance, uma vez que a validação acima irá ser executada para cada item de baixa gerado.

Todos os processos que executam o serviço de baixa irão executar essa validação.

Fórmula composição Valor Original Crédito Adiantamento: O parâmetro define a fórmula para obter o valor de composição para o valor de composição para o valor original do lançamento de crédito de adiantamento, originado pela baixa do lançamento de adiantamento originado no Totvs Gestão de Estoque Compras e Faturamento com incidência de IRRF-PJ e outras retenções diferentes das contribuições sociais (PIS, COFINS,CSLL). O contexto da fórmula será o lançamento de adiantamento.

**Baixa a pagar**

Data default da baixa a pagar

Define a data default de baixa a pagar (sistema, vencimento, emissão, previsão de baixa e cheque).

Histórico default da baixa a pagar

Define o histórico default.

Permite baixar Lançamentos a Pagar com Borderô gerado e enviados para o Banco

Define que os lançamentos enviados para o banco poderão ser baixados.

Desvincular baixa da compensação do cheque para lançamentos a pagar

Define que a baixa a pagar e a compensação serão operações distintas.  Porém o parâmetro da tela no cancelamento de baixa só estará disponível para lançamentos com cheque emitido/recebido.

Base de cálculo dos tributos em lançamentos a pagar (substituiu o parâmetro "Informar base de cálculo dos tributos de lançamentos a pagar" a partir da versão 12.1.2302)

Este parâmetro determina a base de cálculo que será usada no processo de baixa parcial de retenções (PIS-RF, COFINS-RF, e CSLL-RF).

1. Quando selecionado "Valor da Baixa", será usado como base de cálculo o valor informado pelo usuário na tela de edição dos meios de pagamento como base de cálculo das retenções. Quando realizada a baixa total do lançamento, o sistema usará a base de cálculo do tributo que constar neste lançamento.
2. Quando selecionado "Valor Baseado no Valor Original Baixado", o valor da base de cálculo será calculado (fórmula abaixo) baseado no valor original baixado, desde que o usuário não indique um valor de base de cálculo na etapa em que é apresentado o detalhamento do valor líquido.
3. Quando selecionado "Valor Definido pelo Usuário", será usado com base de cálculo o valor informado pelo usuário durante a baixa na etapa em que é apresentado o detalhamento do valor líquido. Caso não indicado um valor, utiliza-se o "Valor da Baixa" como default. Quando realizada a baixa total do lançamento, o sistema usará a base de cálculo do tributo que constar neste lançamento.

*A base de cálculo usada no caso da opção "Valor baseado no valor original baixado" é basicamente um cálculo inverso: cada valor (exceto o PCC) que desconta no item de baixa (ex.: Irrf) deve ser considerado somando, e cada valor que acrescenta no item de baixa (ex.: juros), deve ser considerado descontando. Em valores significativos, a base de cálculo coincidirá com o valor original baixado, se porém o valor da base de calculo resultante seja insuficiente para gerar retenção de um ou mais tributos acima de R$ 10,00, o valor original baixado acompanhará o valor da retenção calculado. A base de cálculo utilizada no cálculo poderá ser observada no anexo de Retenções Acumuladas, no cadastro de lançamentos.*

Obs: Para mais detalhes sobre qual base de cálculo foi utilizada para cálculo do valor do tributo, consulte a opção 'Retenções Acumuladas', localizada nos anexos da visão de lançamentos.

Aceita baixa a pagar em finais de semana e feriados

Define o comportamento do sistema para baixas em finais de semana e feriados (manter o mesmo dia, primeiro dia posterior e primeiro dia anterior).

**IRRF/INSS**

IRRF

* Evento contábil pessoa física: Define o evento contábil para lançamento de IRRF pessoa física.
* Evento contábil pessoa jurídica: Define o evento contábil para lançamento de IRRF pessoa jurídica.

INSS

* Evento contábil: Define o evento contábil para lançamento de INSS. Taxa SELIC    \* % multa por dia: Define % de multa por dia.    \* % máxima multa por dia: Define % máximo de multa por dia.

**Cheque**

Porta serial leitora

Define a porta serial leitora de cheque (COM1, COM2, COM3, COM4 e teclado).

Cheque pré-datado

* Data default de vencimento: Define a data de vencimento default de cheque pré-datado (nula, sistema, vencimento, emissão e previsão de baixa).

Custódia cheque

* Data default custódia: Define a data default de custódia de cheques (sistema, vencimento ou emissão).

Origem do nome da cidade

Define a origem do nome da cidade a utilizar no cheque (coligada ou filial).

Datas do cheque em finais de semana e feriado

Define a data do cheque em finais de semana e feriado (manter o mesmo dia, primeiro dia posterior ou primeiro dia anterior).

**Cheque a pagar**

Data default cheque a pagar

Define a data default de pagamento com cheque (sistema, baixa, vencimento, emissão ou previsão de baixa).

Histórico default cheque a pagar

Define o histórico default de cheque a pagar

Permite emissão de cheques com número já utilizado

Define se poderá repetir os números dos cheques.

Valor cheque a pagar

Define os valores mínimos e máximos de cheque a pagar.

Meio de Pagamento Default para Emissão de Cheque

Define o Meio de Pagamento default para emissão de cheque na visão de lançamento.

**Impressora cheque**

Define configurações básicas de impressão de cheque

**Cancelamento da baixa**

Permite cancelamento da baixa de lançamentos bloqueados para alteração

Define cancelamento de baixa de lançamentos bloqueados para alteração.

Permite cancelamento da baixa com data de cancelamento fora do período da baixa

Define cancelamento de baixa com data de cancelamento fora do período de baixa.

Permite cancelamento da baixa com data de baixa fora do período de baixa

Define cancelamento de baixa com data de baixa fora do período de baixa.

Histórico do cancelamento da baixa

Define histórico do cancelamento de baixa.

**Contab. Baixa**

Permite data de baixa anterior à contabilização de inclusão

Define permissão para data de baixa ser anterior à contabilização de inclusão.

Buscar número do documento no lançamento faturado

Define que o número documento da baixa será buscado no lançamento.

Não contabilizar baixa com valor zero

Define que baixas de valor zero não serão contabilizadas.

Usar o default do evento contábil de baixa contábil apenas nos lançamentos gerados pelo financeiro

Define que o evento contábil de baixa contábil será utilizado apenas para lançamentos gerados no Financeiro.

Carregar automaticamente contabilização antes de efetuar a baixa de lançamentos na tela de baixa

Define que a baixa só será concluída se a contabilização estiver válida no formulário de baixa.

Não contabilizar a baixa de vinculados

Define se os lançamentos de nota de crédito e/ou devolução não serão contabilizados ao serem baixados vinculados aos lançamentos financeiros.

Número contábil da baixa

Define o default do número contábil da baixa: (Número do cheque, número contábil da inclusão, número do documento, número do mov. RM Nucleus, segundo número ou referência.

**Contab. Baixa pagar**

Data default de baixa a pagar

Define a data default de baixa a pagar (sistema, baixa, vencimento, emissão, previsão de baixa, cheque, inclusão, digitação ou comp. cheque).

**Estorno contab. Baixa**

Data default de estorno de baixa

Define a data default de baixa a pagar (sistema, digitação ou contab. Baixa).

**Saques**

Saques do Controle Bancário

O processo "Contas a Pagar" depende do processo "Saques". Desta forma, será necessário parametrizar todas as etapas do processo "Saques". São elas:

* Extrato caixa
* Contab. Extrato

**Geração de retenções**

Origem defaults das tabelas

Define a origem default das tabelas para lançamentos de retenções

Buscar dados no lançamento, se cli/for vazio

Define que os dados serão buscados no lançamento de origem caso estejam vazios no cli/for. Essa opção só é habilitada quando a origem das tabelas for Fornecedor.

Permitir vínculo entre lançamentos com retenção cuja raiz do CNPJ do cliente/fornecedor são diferentes Fornecedor

Define fornecedor de lançamento de retenção.

Tipo de documento

Define tipo de documento de lançamento de retenção.

Histórico  do lançamento de tributo gerado

Define histórico default de lançamento de tributo gerado.

Gerar número de documento de acordo com os parâmetros dos lançamentos

Define que o número do documento será gerado de acordo com os parâmetros do lançamento.

Usar cumulatividade de retenções (Lei 10.925)

**(Parâmetro descontinuado)** após a publicação da Lei 10.925 em 23 de julho de 2004, fica dispensada a retenção do valor devido a CSLL, COFINS e da contribuição para o PIS/PASEP para pagamentos de valor igual ou inferior a R$ 5.000,00 (cinco mil reais). Fica também estabelecido que ocorrendo mais de um pagamento no mesmo mês à mesma pessoa jurídica, deverá ser efetuada a soma de todos os valores pagos no mês para efeito de cálculo do limite de retenção, compensando-se o valor retido anteriormente. Desta forma, quando este parâmetro está ativo, os lançamentos a pagar para um mesmo fornecedor dentro do mesmo mês somente serão tributados se a soma desses lançamentos for maior que R$ 5.000,00.

Geração de Lançamentos

**Fatura**

Copiar ref. para fatura

Com este parâmetro marcado, o "Número do Documento" da Fatura incluída é preenchido com o número da referência da fatura no cadastro de fatura que é sequencial e nunca se repete.

Proporcionalizar valor baixado dos lançamentos faturados pelo valor líquido

* Com o parâmetro desmarcado, a proporção é feita utilizando o valor baixado do vencimento de fatura, considerando o valor original do lançamento para o cálculo.  
   Obs.: O lançamento faturado sem retenção terá o valor líquido proporcionado.
* Com o parâmetro marcado, a proporção é feita utilizando o valor líquido do lançamento faturado, não alterando o valor líquido do lançamento sem retenção.

**Acordo**

Detalhar valores do acordo (desconto, acréscimo, juros)

* Lançamento origem:

os valores do acordo (desconto, acréscimo, juros) serão gravados apenas no lançamento de origem. - Lançamento gerado: os valores do acordo (desconto, acréscimo, juros) serão gravados apenas no lançamento gerado por acordo.

* Lançamento origem e gerado:

os valores do acordo (desconto, acréscimo, juros) serão gravados em ambos os lançamentos.

**Observação**:

Ao alterar quaisquer um dos parâmetros acima, o novo comportamento será válido somente para os novos acordos. Os já existentes seguirão a regra definida ao criá-lo.   
   
Na visão de acordos, o campo DETALHELANORIGEMDESTINO irá armazenar o valor do parâmetro no momento de sua geração, são eles:

* 0  Lançamento Origem
* 1  Lançamento Gerado
* 2  Lançamento Origem e Gerado

Integração Bancária

**Pagamento eletrônico**

Valor limite inferior TED:

Define o valor mínimo que o TED pode ser realizado.

Valor default para diferença em retorno bancário:

Define onde serão creditados os valores de juros e descontos no Retorno de Cobrança e Retorno de Pagamento. 

Apresentar tela de vínculo ao Incluir Borderô de Pagamento/Vincular Borderô de Pagamento:  
  
Ao assinalar esta opção ao incluir um borderô de pagamento para um lançamento ou vincular a um lançamento a um borderô existente o sistema exibirá uma tela ao usuário informando que existem lançamentos passíveis para vínculos (crédito de adiantamento, nota de crédito ou devolução), possibilitando o usuário realizar o vínculo do lançamento antes de prosseguir com o processo de inclusão/vínculo do borderô de pagamento.

**Integração Bancária**

Data opcional para remessa:

Define qual data opcional o sistema deve gravar na data da remessa de cobrança ou pagamento. Ao gerar uma remessa para o banco, essa data opcional será atualizada com a data do sistema.

Campo alfa opcional remessa:

Define o código alfa do número da remessa bancária.

No retorno bancário utilizar os valores do arquivo (layout), sobrepondo os do lançamento:

Se o parâmetro estiver marcado, os valores de juros, desconto e multa, serão considerados do arquivo, senão serão considerados também os valores do lançamento.

Usa captura de DDA global:

Define se será utilizado a coligada global (coligada = o) ao efetuar a captura de títulos de cobrança (DDA).

Permite agendamento das remessas bancárias:

Define se será permitido o agendamento das remessas bancárias (cobrança, pagamento, débito automático e custódia de cheque).

Habilita LOG mais detalhado durante a baixa do retorno bancário:

Com este parâmetro marcado define que o sistema faça um detalhamento mais elaborado TECNICAMENTE no log do processo de baixa durante o retorno bancário. O LOG detalhado e mais voltado para que a equipe de desenvolvimento analise mais a fundo possíveis causas.

Conciliação bancária global:

Com este parâmetro marcado, o processo de conciliação poderá ser executado globalmente, ou seja, na visão de Conciliação Bancária os extratos de caixa e os registros lidos do banco filtrarão registros globais e os de outras coligadas. Com o parâmetro desmarcado continua o comportamento atual mostrando somente registros da coligada corrente.  
  
Executar leitor de QR Code como ícone na barra de tarefas:  
  
Com este parâmetro marcado, o aplicativo do leitor de QR Code será executado como ícone na barra de tarefas do sistema operacional.

**Retorno bancário**

Campo complementar das ocorrências do retorno bancário:

Define o campo complementar dos lançamentos que irá receber os códigos das ocorrências informadas no retorno bancário de Cobrança Eletrônica ou de Pagamento Eletrônico.

Veja Também
