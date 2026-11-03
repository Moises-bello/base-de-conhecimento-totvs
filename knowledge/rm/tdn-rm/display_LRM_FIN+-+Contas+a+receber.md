---
content_hash: f557c3a11ef89f5318f45cc040942b98132f607c8e53a4d6aa4400ecc0e88b8f
fetched_at: '2026-06-29T00:09:19.323262+00:00'
page_id: '421388839'
product: rm
source: tdn-rm
title: FIN - Contas a receber
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber
version: 98
---

**Fatura**

Copiar ref. para fatura

Com este parâmetro marcado, o "Número do Documento" da Fatura incluída é preenchido com o número da referência da fatura no cadastro de fatura que é sequencial e nunca se repete.

Proporcionalizar valor baixado dos lançamentos faturados pelo valor líquido

* Com o parâmetro desmarcado, a proporção é feita utilizando o valor baixado do vencimento de fatura, considerando o valor original do lançamento para o cálculo.  
   Obs.: O lançamento faturado sem retenção terá o valor líquido proporcionado.
* Com o parâmetro marcado, a proporção é feita utilizando o valor líquido do lançamento faturado, não alterando o valor líquido do lançamento sem retenção.

**Acordo**

Detalhar valores do acordo (desconto, acréscimo, juros)

* Lançamento origem

Os valores do acordo (desconto, acréscimo, juros) serão gravados apenas no lançamento de origem.

* Lançamento gerado

Os valores do acordo (desconto, acréscimo, juros) serão gravados apenas no lançamento gerado por acordo.

* Lançamento origem e gerado

Os valores do acordo (desconto, acréscimo, juros) serão gravados em ambos os lançamentos.

**Observação**:

Ao alterar quaisquer um dos parâmetros acima, o novo comportamento será válido somente para os novos acordos. Os já existentes seguirão a regra definida ao criá-lo.

Na visão de acordos, o campo DETALHELANORIGEMDESTINO irá armazenar o valor do parâmetro no momento de sua geração, são eles:

* 0 Lançamento Origem
* 1 Lançamento Gerado
* 2 Lançamento Origem e Gerado

**Cobrança eletrônica**

Os parâmetros de Cobrança Eletrônica são utilizados para definir algumas regras e funcionalidades para o processo de Cobrança Eletrônica.

Usar número do documento no retorno de cobrança sem registro

Define o modo de pesquisa do lançamento no retorno de cobrança sem registro.

Valor default para diferença em retorno bancário

Define onde serão creditados os valores  no Retorno de Cobrança.

Quando o valor líquido especificado no arquivo de retorno bancário for diferente do valor líquido do lançamento financeiro, é possível definir que o sistema realize alguns processos, que podem ser definidos através da janela de "Importação de Cobrança" ou através desse parâmetro. Ao definir alguns processos nos parâmetros, a definição será refletida na janela de Importação de Cobrança, podendo ser alterada no momento da importação.

* Se diferença: A maior.
* Se diferença: A menor.
* Diferença para geração de baixa parcial
* Diferença para geração de adiantamento
* Código de adiantamento default
* Convênio default para registro online de boleto

Será utilizado no registro online dos portais somente convênios com o campo "Permite registro de boleto online" marcado, que serão apresentados para seleção.

Comportamento do sistema para diferença a maior ou menor

**Integração bancária**

Data opcional para remessa

Define qual data opcional o sistema deve gravar na data da remessa de cobrança ou pagamento, ao gerar uma remessa para o banco, essa data opcional será atualizada com a data do sistema.

Campo alfa opcional remessa

Define o código alfa do número da remessa bancária.

No retorno bancário utilizar os valores (juros, multa, desconto e opcionais) do arquivo (layout), sobrepondo os do lançamento

Se o parâmetro estiver marcado, os valores de juros, desconto, multa e opcionais (este último também será atualizado no item de baixa do lançamento mesmo que o valor indicado nas posições correspondentes do layout bancário esteja zerado), serão considerados somente do arquivo, senão serão considerados também os valores do lançamento. Caso exista mais de um lançamento no boleto contido no arquivo de retorno, o sistema irá proporcionalizar o valor dos juros em cada lançamento. O mesmo vale para os campos nativos "Multa" e "Desconto".

**Obs.:** O "Desconto" segue uma lógica de proporcionalização específica onde, existindo mais de um lançamento no boleto esse desconto será aplicado apenas nos lançamentos que tem desconto cadastrado, caso nenhum lançamento possua desconto cadastrado todos receberão proporcionalmente o desconto do arquivo. A seguir, exemplos para demonstrar como é feito a proporcionalização do Desconto:

Boleto 1: R$ 200,00 com desconto de R$ 20,00 no arquivo, valor líquido do Boleto R$ 180,00

* Lançamento 1 com desconto: R$ 150,00, valor líquido R$ 135,00
* Lançamento 2 com desconto: R$ 50,00, valor líquido R$ 45,00

Boleto 2: R$ 200,00 com desconto de R$ 20,00 no arquivo, valor líquido do Boleto R$ 180,00

* Lançamento 1 com desconto: R$ 150,00, valor líquido R$ 130,00
* Lançamento 2 sem desconto: R$ 50,00, valor líquido R$ 50,00

Boleto 1: R$ 200,00 com desconto de R$ 20,00 no arquivo, valor líquido do Boleto R$ 180,00

* Lançamento 1 sem desconto: R$ 150,00, valor líquido R$ 135,00
* Lançamento 2 sem desconto: R$ 50,00, valor líquido R$ 45,00

No caso dos valores opcionais, o sistema irá considerar os valores somente do lançamento que possuir tal valor. Se existir valor no arquivo de retorno referente aos valores opcionais mas não existir no (s) lançamento (s) vinculado (s) ao boleto, o sistema irá proporcionalizar tais valores em cada lançamento.

Atenção: Esse parâmetro deve ser usado somente para situações onde o boleto gerado possui a mesma data de vencimento do lançamento. Para outros boletos gerados com vencimento posterior, o cálculo no retorno bancário pode resultar num valor a maior.

Data para cálculo do valor líquido dos lançamentos do boleto não vencido:  
  
Opção disponível apenas quando a flag 'No retorno bancário utilizar os valores (juros, multa, desconto e opcionais) do arquivo (layout), sobrepondo os do lançamento' está desmarcada. Existem duas opções para uso:

Data do pagamento: É a opção padrão do sistema e continua da mesma forma, com o sistema calculando o valor líquido dos lançamentos envolvidos sendo a data do pagamento como data de referência. Ao utilizar esta opção, quando o arquivo de retorno de cobrança for importado, o sistema irá calcular o valor líquido do lançamento na mesma data de pagamento que constar no arquivo de retorno.  
Data do vencimento do boleto: Nova opção, com o objetivo de calcular o valor líquido dos lançamentos envolvidos com a data de referência sendo a data de vencimento do boleto. Ao utilizar esta opção, quando o arquivo de retorno de cobrança for importado, o sistema irá calcular o valor líquido do lançamento conforme a data de vencimento do boleto.

Usa captura de DDA Global

Define se será utilizada a coligada global ao efetuar a captura dos títulos de cobrança DDA.

Permite agendamento das remessas bancárias

Define se será permitido o agendamento das remessas bancárias, cobrança, débito automático, pagamento e custódia de cheque.

Habilita LOG mais detalhado durante a baixa do retorno bancário

Com este parâmetro marcado define que o sistema faça um detalhamento técnico mais elaborado **tecnicamente** no log do processo de baixa durante o retorno bancário. O log detalhado e mais voltado para que a equipe de desenvolvimento analise mais a fundo possíveis causas.

Conciliação bancária global:

Com este parâmetro marcado, o processo de conciliação poderá ser executado de forma global, ou seja, na visão de Conciliação Bancária os extratos de caixa e os registros lidos do banco, poderão ser selecionados de todas as coligadas. Com o parâmetro desmarcado continua o comportamento atual mostrando somente registros da coligada corrente.

**Retorno bancário**

Campo complementar das ocorrências do retorno bancário

Define o campo complementar dos lançamentos que irá receber os códigos das ocorrências informadas no retorno bancário de Cobrança Eletrônica ou de Pagamento Eletrônico.

**Desconto de duplicata**

Deduzir tributos no processo de desconto de duplicata

Define que o valor do lançamento utilizado no desconto de duplicata deve ser deduzido os tributos (PIS, COFINS, CSLL).

**Tabelas opcionais**

Usar tabelas opcionais

Define as características gerais das tabelas opcionais e sua obrigatoriedade nos lançamentos e extratos.

Visualizar tabela opcional que não permita lançamento

Os itens das tabelas opcionais que não permitam lançamentos serão listados na pesquisa.

**Centro de custo**

Máscara do centro de custo

Define a máscara do centro de custo

Exibir centro de custo que não permitem lançamentos

Exibe centros de custo que não permite lançamentos na lista de seleção.

Usa código reduzido

Permite utilizar um código reduzido para o centro de custo.

**Calendário oficial**

Calendário oficial

Define o calendário que será utilizado no sistema. Estes calendários são cadastrados no menu Cadastros | Calendário. O calendário escolhido será utilizado nos lançamentos e nas fórmulas para cálculo de dias úteis.

Considerar sábado como dia útil

Define que o sábado será considerado como dia útil nos processos de manipulação de datas. Este parâmetro não será considerado nas aplicações financeiras pois, não há indexador para sábados.

**Opções gerais**

Os parâmetros de Opções Gerais são utilizados para definir algumas regras gerais do sistema. 

Número de Casas Decimais 

Informe a quantidade de casas decimais que terão os campos de "Valores" do cadastro de Lançamento Financeiro.

**Cliente / Fornecedor**

Permite globais

Define se será utilizada a coligada global (coligada = 0) nos cadastros tipo de cliente/fornecedor e cliente/fornecedor.

Default cli/for global

Define que na inclusão de novo cliente/fornecedor, o campo global será marcado automaticamente.

Estado obrigatório

Define se o estado será de preenchimento obrigatório na inclusão de novo cliente/fornecedor.

Tipo de cliente/fornecedor obrigatório

Define se o tipo de cliente/fornecedor será de preenchimento obrigatório na inclusão de novo cliente/fornecedor.

Usar código sequencial (se máscara for numérica)

Define se o código do cliente/fornecedor será sequencial numérica.

Permite nomes iguais para contatos para o mesmo cliente/fornecedor

Define se o sistema permitirá o cadastro de contatos com nomes iguais para o mesmo Cliente/Fornecedor.

Permite CPF/CNPJ de cli/for global repetido em coligadas distintas

Permite incluir cliente/fornecedor global com CPF/CNPJ já cadastrado em coligada diferente.

Usar Dados Bancários Global do Cliente/Fornecedor

Ao marcar este parâmetro, é exibida uma tela solicitando que o usuário informe uma coligada de referência. Ao concluir o assistente de parametrização, todas as informações de dados bancários da coligada selecionada (tabela FDADOSPAGTO) são transformadas em globais (coligada zero). Em seguida, o processo faz com que todos os boletos e lançamentos financeiros de fornecedores globais passem a referenciar estes dados bancários globais. Esse processo é realizado em **todas** as coligadas que permitem dados globais.

**Importante**: Para que o processo seja executado corretamente, é necessário que a coligada selecionada como referência possua os dados de pagamentos de **todos** os fornecedores globais de **todas** as coligadas. As formas de pagamento de cada fornecedor também devem respeitar a mesma sequência (*IDPGTO*) nas diferentes coligadas. Caso haja um lançamento ou boleto em qualquer coligada de um fornecedor global que não esteja configurado nos dados bancários da coligada de referência, o banco de dados retornará um erro.

Mudança de comportamento 

A partir da **release 12.1.2602** esse parâmetro passa a ser **apenas para consulta de status** do uso dos dados bancários do cliente/fornecedor de forma global, para que ele possa ser ativado ou desativado será necessário executar o processo  através do menu: **Utilitários | Outros | Mais | Ativar/Desativar Dados Bancários Global**.

Máscara do código

Define a máscara do código do cliente/fornecedor.

* # Somente números.
* l Somente letras.
* L Somente letras (converte para maiúsculas).
* a Letras e números.
* A Letras e números (converte para maiúsculas).
* Q Qualquer caractere, exceto os separadores.
* Separadores: Ponto, vírgula, traço, dois pontos, barra, espaço em branco e parênteses.

Código Cli/For Automático Protheus

Quando integrado o RM com Protheus e EAI 2.0 esse parâmetro irá controlar o preenchimento manual ou automático do [código do Cliente/Fornecedor](https://tdn.totvs.com/x/8uEdGQ) na inclusão de um novo. 

Pessoa física

CPF obrigatório

CPF obrigatório na inclusão de cliente/fornecedor do tipo pessoa física.

CPF único

Define que não será permitido incluir mais de um cliente/fornecedor com o mesmo CPF.

Permite CPF repetido para produtor rural com insc. estadual diferente

Define que poderá incluir CPF repetido para produtor rural com insc. estadual diferente. O parâmetro só habilitará caso o parâmetro CPF único esteja marcado.

Pessoa jurídica

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

Habilita o uso dos dados de Histórico de Alteração dos Lançamentos no Relatório de Extrato de Cliente/Fornecedor

Quando o **[Histórico do Controle de Alterações de Lançamentos/ Extrato de Caixa e Baixas](https://tdn.totvs.com/pages/viewpage.action?pageId=421388636)** está habilitado, ao marcar essa opção, define que o Relatório de Extrato de Cliente/Fornecedor passará a utilizar os dados de histórico de alteração de lançamentos na geração do relatório de Extrato de Cliente/Fornecedor. Caso esse parâmetro seja marcado, mas o **[Histórico do Controle de Alterações de Lançamentos/ Extrato de Caixa e Baixas](https://tdn.totvs.com/pages/viewpage.action?pageId=421388636)** não está habilitado, o relatório de Extrato de Cliente/Fornecedor mantém o comportamento padrão, sem considerar os dados das tabelas de histórico.

**Cli/For - Opcionais**

Campos alfa e valores opcionais

Define os campos opcionais do cadastro de cliente/fornecedor.

**Recursos adicionais**

Os parâmetros de Recursos Adicionais são utilizados para definir alguns recursos adicionais para os lançamentos financeiros.

Rateio centro de custo / natureza orçamentária

* Usar rateio para

Define em que nível será feito o controle financeiro de despesas e recebimentos.

* Obrigatoriedade

Define o nível de obrigatoriedade dos rateios por centro de custo / natureza orçamentária.

Rateio departamento

* Obrigatoriedade

Define o nível de obrigatoriedade dos rateios por departamento.

Bloqueio para baixa

* Usar bloqueio

Define o nível de bloqueio dos lançamentos (sem, simples ou duplo). Um [lançamento bloqueado](https://tdn.totvs.com/pages/editpage.action?pageId=421388717) não pode ser baixado, não permite a emissão de cheque nem remessa de cobrança/pagamento eletrônico.

* Valor mínimo

Define o valor mínimo para que o lançamento fique bloqueado.

* Bloquear o lançamento para alterações automaticamente ao desbloquear da baixa

Define que ao [desbloquear um lançamento para baixa](https://tdn.totvs.com/pages/editpage.action?pageId=421388717), o mesmo ficará bloqueado para alteração.

* Desbloqueio duplo deve ser feito por usuários diferentes

Define que o bloqueio deverá ser feito por dois usuários diferentes.

**Datas opcionais**

Define as datas opcionais a serem utilizadas nos lançamentos.

Consistir valores das datas opcionais na geração de acordo de lançamentos.

Não enviar as datas opcionais para os lançamentos gerados por acordo

Com a opção desmarcada será enviada as datas opcionais do primeiro lançamento para os lançamentos filho.

**Alfa opcionais**

Alfa Opcionais são campos alfanuméricos que podem ser incluídos na janela de edição dos lançamentos financeiros.  
Marque o parâmetro e informe um nome para ele, ao gravar a parametrização o campo é apresentado na pasta "Opcionais" da janela de edição dos lançamentos.

Usar campo Alfa

Define os campos alfa opcionais a serem utilizadas nos lançamentos.

Define os campos alfa opcionais a serem utilizadas nos lançamentos.

Consistir valores dos campos alfa opcionais na geração de acordo de lançamentos.

Não enviar os campos alfa opcionais para os lançamentos gerados por acordo

Com a opção desmarcada será enviada os campos alfa opcionais do primeiro lançamento para os lançamentos filho.

**Valores opcionais**

Através desses parâmetros, pode-se habilitar até 8 campos de valores, configurando o Nome e a Ação que esses campos terão no sistema.

Default

O valor opcional pode ser preenchido no momento da edição do lançamento ou ser apresentado com uma porcentagem default, para isso, deve ser informado um default no campo Default.

Até o Vencimento

Essa opção fica disponível se a ação do valor opcional for "Descontar", "Descontar se a receber" ou "Descontar se a pagar".  
Com essa opção marcada, o valor opcional só é considerado até a data de vencimento. Quando a opção estiver desmarcada, o valor opcional sempre é considerado.

Dias de Atraso

Esse campo fica disponível se a ação do valor opcional for "Acrescentar", "Acrescentar se a receber" ou "Acrescentar se a pagar".

IPTE/Cod. Barras

Quando o flag "Consiste IPTE/Código de barras" está marcado esta opção configurada no valor opcional indica que o mesmo irá compor o valor consistido no código de barras/IPTE de lançamentos a pagar.

Compõe valor Relatório Extrato Cliente/Fornecedor

Quando marcado o valor opcional comporá o valor da movimentação no Relatório Extrato Cliente/Fornecedor. Não pode ser usado quando ação configurada como "Nada" ou uma fórmula parametrizada.

Compõe valor cálculo do AVP

Quando marcado o valor opcional comporá o valor do cálculo futuro do Ajuste Valor a Presente (AVP). Não pode ser usado quando ação configurada como "Nada" ou uma fórmula parametrizada.  
Observação: na versão 12.1.2402 é necessário atualizar a base através do RM Atualizador antes do uso desta opção.

**Inclusão**

Este parâmetro define a origem default de campos na inclusão do lançamento financeiro. Os campos que serão atualizados serão os disponíveis no cadastro default das tabelas selecionadas.

Conta/Caixa obrigatório no lançamento

Define que a conta/caixa será obrigatória no lançamento.

Permite data de vencimento menor que data de emissão

Define que será possível incluir lançamento com data de vencimento menor que a data de emissão do mesmo.

Permite data de vencimento menor que data do sistema

Define que será possível incluir lançamento com data de vencimento menor que a data do sistema.

Filtra cli/for de acordo com a natureza do lançamento

Define que a seleção de cliente/fornecedor será definida pela natureza do lançamento. Lançamentos a receber, apenas clientes disponíveis. Lançamentos a receber, apenas fornecedores disponíveis.

Cálculo valor líquido na visão de lançamentos

Define como será apresentando o valor líquido na visão de lançamento, não calcular valor líquido automaticamente na visão, calcular valor líquido automaticamente na visão ou calcular valor líquido ao selecionar lançamento.

Máscara tipo de documento

Define a máscara do tipo de documento.

* #: Somente números.
* l: Somente letras.
* L: Somente letras (converte para maiúsculas).
* a: Letras e números.
* A: Letras e números (converte para maiúsculas).
* Q: Qualquer caractere, exceto os separadores.
* Separadores: Ponto, vírgula, traço, dois pontos, barra, espaço em branco e parênteses.

Permite lançamentos zerados

Define o tipo contábil de lançamento que permitirá incluir lançamento com valor zero.

Fórmulas / valores defaults

* Valores

Define valores defaults para desconto, juros, multa e capitalização.

Origem das tabelas

* Conta/Caixa

As informações buscadas são as definidas no cadastro de Conta/Caixa como default (em Menu Cadastros | Conta/Caixa | Editar a Conta Caixa em questão | Anexos | Defaults de Conta/Caixa.

* Cliente/Fornecedor

As informações buscadas são as definidas no cadastro de Cliente/Fornecedor como default (em Menu Cadastros | Cliente/Fornecedor | Editar o Cliente/Fornecedor em questão | Anexos | Defaults de Cli/For. 

* Sem Default:

Não busca nenhuma informação.

Tamanho do número

Define o tamanho máximo do número do documento e segundo número.

Permite alteração fora do período de emissão

Define alteração de lançamento fora do período de emissão que é definido na etapa de "inclusão a receber".

Permite numeração repetida em lançamento quando já cancelado:

Esse parâmetro permite a inclusão de lançamento, com as mesmas informações dos campos Coligada, Filial, Tipo(a pagar/ a receber), Cliente/Fornecedor, Tipo de Documento, Número e Série, quando lançamento equivalente estiver cancelado.

**Inclusão a receber**

Incluir lançamentos a receber bloqueados para baixa

Define que os lançamentos a receber serão incluídos bloqueados para baixa utilizando as parametrizações da etapa "recursos adicionais".

Permite alterar lançamentos a receber remetidos ao banco

Permite alteração em lançamentos a receber que foram previamente remetidos ao banco.

Preencher números do lançamento com zeros

Define que os números utilizados nos lançamentos serão preenchidos com zero. São números do lançamento: Número do documento, segundo número, número contábil de inclusão, número contábil de baixa.

Consiste prazo mínimo de vencimento

Define que será consistido o número de dias entre data do sistema e data de vencimento na inclusão e alteração de lançamentos a receber. Na alteração a consistência ocorre apenas quando a data de vencimento é alterada.

Número de dias permitidos: [Data de vencimento (no mínimo) = Data sistema + número de dias].

Período para emissão

Define período de emissão para lançamentos a receber.

Aceita vencimento a receber em finais de semana e feriados

Define como será o vencimento de lançamentos em finais de semana e feriados.

Aceita previsão de baixa a receber em finais de semana e feriados

Define como será a previsão de baixa a receber de lançamentos em finais de semana e feriados. Este comportamento é valido tanto para a operação de inclusão como para alteração de lançamentos financeiros.

**Alteração**

**Situação cliente**

Controla e bloqueia quando houver lançamentos vencidos de cliente

Define que a inadimplência do cliente será controlada pelo financeiro.

* N° dias em atraso: Define o número de dias padrão que serão considerados no controle de inadimplência do cliente. Este parâmetro só será aplicado quando o campo "n° de dias em atraso" estiver vazio.
* Bloquear cliente em atraso: Define que o cliente será bloqueado quando inadimplente.

Obs: Controla e bloqueia quando tem lançamentos vencidos. Com o bloqueio marcado não permite alteração global ou manual. Se o lançamento está realmente vencido irá validar (mostrar no processo a mensagem) e não fará o processo de alteração

Limite de crédito 

* Bloquear lançamento quando o limite de crédito do cliente for atingido

Define o bloqueio do lançamento quando o limite de crédito do cliente for atingido.

* Desconsiderar lançamentos a receber no limite de crédito do cliente

Define que os lançamentos a receber serão desconsiderados no cálculo do limite de crédito.

**Situação cli/for**

Controla atualização do cadastro de Cliente/Fornecedor

Define se será controlada a atualização do cadastro de cliente/fornecedor e qual a ação sobre isso. Se apenas avisa, ou bloqueia a inclusão e edição de lançamento para o cliente/fornecedor.

* Controlar cadastro de Cliente/Fornecedor: É possível selecionar as opções "Não Controla", "Controla a Receber", "Controla a Pagar" ou "Controla Todos".
* Controlar após (dias): É a partir dessa quantidade de dias que o cadastro do Cliente/Fornecedor estiver desatualizado que o controle irá alertar ou bloquear.
* Bloquear cliente / fornecedor vencidos: Caso esteja com essa opção desmarcada, o controle irá apenas avisar que o cadastro está desatualizado, levando em consideração o número de dias informado. Com esta opção marcada, ele bloqueia.

Liberar o bloqueio de cliente/fornecedor com a senha de supervisor (clientes em atraso, vencidos e limite de crédito)

Define se será possível incluir lançamento para casos de bloqueio de cliente/fornecedor através de senha de supervisor. Na validação feita com o usuário e senha informados será liberado quando o usuário é supervisor ou está vinculado a um perfil do módulo Gestão Financeira com permissão para "Liberar bloqueios de clientes" (item 02.01.01.22). Essa funcionalidade estará disponível apenas na tela de lançamento quando houver parametrização e edição do lançamento.

No processo de "Alteração Global" o sistema fará a consistência do controle, porém não apresentará tal funcionalidade para execução, sendo preciso que a alteração com desbloqueio de senha seja realizada via tela de processo.

**Cancelamento da inclusão**

Histórico default de cancelamento do lançamento

Define histórico default de cancelamento de lançamento.

**Natureza financeira**

Utiliza natureza orçamentária/financeira

Define se usará natureza orçamentária/financeira nos lançamentos.

Permite globais 

Máscara**Situação cli/for**

Define como será a máscara da natureza

* # Somente números.
* l Somente letras.
* L Somente letras (converte para maiúsculas).
* a Letras e números.
* A Letras e números (converte para maiúsculas).
* Q Qualquer caractere, exceto os separadores.
* Separadores Ponto, vírgula, traço, dois pontos, barra, espaço em branco e parênteses.

**Geração IRRF - PJ**

Reter IRRF - PJ na inclusão automaticamente

Define se irá reter IRRF - PJ na inclusão de lançamento a receber automaticamente.

Data base para retenção

Define data base para retenção (emissão, vencimento ou contab. inclusão).

Data base substituta para data de contabilização de inclusão para geração

Define data base substituta para data de contabilização de inclusão para geração (emissão, vencimento ou digitação). Só é habilitado caso a data base para geração seja Contab. inclusão).

Valor mínimo

Define valor mínimo para geração.

Arredonda valor do IRRF

Define se o valor de IRRF será arredondado.

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

* Usar no cálculo do valor líquido

Define que a data de conversão de moedas será utilizada como data no cálculo do valor líquido do lançamento.

Juros

Calcula juros ao dia usando

* Valor original

Define que o sistema irá calcular os valores incidentes no lançamento (juros, valores opcionais) com base no valor original.

* Valor líquido parcial

Define que o sistema irá calcular os juros informados no lançamento com base no valor líquido. O cálculo é realizado desta forma: O sistema realiza os cálculos de todos os valores opcionais (juros e descontos) em seguida aplica este valor em cima do valor original do lançamento e em seguida é realizado o cálculo do juro que é informado no lançamento com base no valor líquido que foi calculado anteriormente.

Usar juros compostos

Define que o sistema irá calcular os juros "compostos" (cumulativos) na baixa de lançamentos. Para isso, valor dos juros ao dia do lançamento deve ser informado sobre taxa.

Considerar os dias de carência no cálculo dos juros ao dia

Define que no cálculo de juros ao dia, os dias serão contados a partir do final da carência.

Multa

Calcula multa ao dia usando:

* Valor original

Define que o sistema irá aplicar a porcentagem informada no campo Multa ao Dia (%) sobre o Valor Original do lançamento.

* Valor líquido parcial

Define que o sistema irá aplicar a porcentagem informada no campo Multa ao Dia (%) sobre o Valor Líquido Parcial do lançamento.

Aplicar multa em lançamentos

Define a natureza dos lançamentos que calcularão multa (receber, receber e todos).

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

Define que ao gerar lançamentos de tributos os valores dos lançamentos serão arredondados de acordo com a quantidade de casas decimais utilizadas.

Período para baixa

Define período permitido para baixa, compreendendo data inicial e data final.

Permite alteração de lançamento com data de baixa fora do período de baixa

Define que será permitido alterar lançamento com data de baixa fora do período de baixa.

Copiar natureza orçamentária e centro de custo do rateio do lançamento para o extrato

Define que as informações de natureza orçamentária e centro de custo do primeiro rateio do lançamento, serão preenchidas no extrato.

Obs: Para lançamentos de crédito de adiantamento quando selecionado esse parâmetro, na etapa 3/6 da baixa devem ser informados os parâmetros **"Natureza orçamentária default de crédito de adiantamento a receber"**e **"Natureza orçamentária default de crédito de adiantamento a pagar"**. Caso esses parâmetros não forem fornecidos, a natureza orçamentária do crédito de adiantamento deve ser **"Ambos"** ou uma natureza orçamentaria que corresponda a natureza do lançamento de crédito de adiantamento.

**Baixa 2/6**

Vínculo de lançamento

* Permite vínculo de lançamentos entre filiais

Define que será permitido vincular lançamentos de filiais diferentes.

* Filtrar lançamentos sem possibilidade de vínculos no editar vínculos apresentados antes da baixa

Ao realizar a baixa, não será apresentada na tela de edição de vínculos, lançamentos que não possuem devolução, Crédito de adiantamento, Nota de credito do mesmo cliente/fornecedor.

* Não permite Vínculo de lançamentos entre cliente/fornecedores diferentes: Define que NÃO será permitido o vínculo de lançamentos entre clientes/fornecedores diferentes.

Bloqueio de alteração 

* Bloquear o lançamento para alterações automaticamente ao baixar

Define que após a baixa de algum lançamento não será permitida nenhuma alteração ou operação neste.

Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa.

Define que o processo de baixa não será interrompido se algum lançamento selecionado apresentar inconsistência. Quando marcado a rotina de baixa irá montar pacotes de lançamentos que precisam ser baixados juntos segundo critérios de vínculo, retenção acumulada, compartilhamento de boleto e forma de pagamento.

[Controlar concorrência na baixa de lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=274659034)

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
* Natureza orçamentária default de crédito de adiantamento a receber: Define a natureza orçamentária default a ser utilizada no lançamento a receber de crédito de adiantamento gerado pela baixa do lançamento a pagar de adiantamento.
* Natureza orçamentária default de crédito de adiantamento a pagar: Define a natureza orçamentária default a ser utilizada no lançamento a pagar de crédito de adiantamento gerado pela baixa do lançamento a receber de adiantamento.

Contabilizar crédito de adiantamento em filiais distintas

* Esse parâmetro indicará se a contabilização da baixa de crédito de adiantamento ocorrerá quando marcado ou não quando desmarcado. E se aplica quando a operação é com filiais diferentes.   
  Este parâmetro é por coligada e único, ou seja, quando marcado ou desmarcado no Contas a Pagar o comando é automático para o Contas a Receber e vice versa.

Desconto de duplicata

* Meio de pagamento

Define o meio de pagamento de desconto de duplicata.

**Baixa 4/6**

Modo de cálculo dos valores da baixa parcial 

* Baixa calculada por prioridade

Define a ordem de prioridade dos valores na baixa. O primeiro valor a ser calculado é o das retenções, cuja base de cálculo é recalculada proporcionalmente em relação ao valor baixado. Os valores de INSS e IR são os próximos a serem calculados, que são sempre descontados na 1ª parcela, ou 1º pagamento. Na sequência são considerados os valores a descontar, na seguinte ordem: primeiramente o valor de SEST/SENAT, depois os valores de devoluções, os valores de notas de crédito, os adiantamentos, descontos e os valores opcionais a descontar. Depois os valores a acrescentar, na seguinte ordem: os juros, multa, capitalização, juros vendor e os valores opcionais a acrescentar. E por último o valor original baixado, que será calculado.

* Baixa calculada por proporcionalização

Define a proporcionalização dos valores na baixa. O valor pago é distribuído proporcionalmente por cada valor do lançamento, inclusive os valores de Integração. 1º Considera o valor das retenções do item de baixa e considera o valor total de: IRRF, INSS, SEST/SENAT, Devoluções, Notas de Crédito e Adiantamentos. 2º Considera  os valores proporcionais de: Desconto, Vr. Opcionais a DESCONTAR, Valores de Integração à DESCONTAR. 3º Considera os valores a ACRESCENTAR proporcionalmente. 4º Considera o valor ORIGINAL proporcionalmente. 5º Ajusta a diferença de cálculo entre os valores Calculados e o efetivamente BAIXADO.

Obs. Caso lançamento tenha valor de devolução ou valor de adiantamento ou valor de nota de crédito maior que o valor original, a baixa será efetuada por prioridade, para que o valor vinculado seja totalmente consumido, evitando assim que ocorra valores negativos na proporção devido ao valor original ser menor que o valor vinculado.

Baixa calculada por proporcionalização

* Calcular os valores opcionais, multa, juros e desconto por prioridade

Define que estes valores serão descontados ou acrescentados 100% na baixa do lançamento.

**Baixa 5/6**

Retorno bancário

Nesta etapa é definido o meio de pagamento que será utilizado na baixa dos lançamentos financeiros provenientes das rotinas de retorno de cobrança, pagamento e débito automático. Apenas os cadastros de meio de pagamento cujo tipo primitivo for igual a 'Dinheiro', 'Outros' e 'Tipo Boleto Bancário' serão exibidos nos campos de retorno de cobrança e retorno de pagamento, enquanto somente os tipos primitivo 'Dinheiro' e 'Outros' serão apresentados no campo pertinente ao retorno de débito automático.

**Baixa 6/6**

Fórmula validação de baixa

Define uma fórmula para ser executada na baixa dos lançamentos.

Funcionamento:

Para que o processo de baixa seja interrompido, o resultado da fórmula deve retornar a mensagem que será mostrada ao usuário como o motivo para a não permissão de baixa. Segue exemplo de fórmula:

SE TABLANBAIXA('VALORDESCONTO','V') > (TABLAN('VALORORIGINAL','V') \* 0.02)

ENTAO  'Valor desconto maior que o valor autorizado para desconto.'

SENAO  1

FIMSE

No exemplo acima, caso o valor de desconto ultrapasse o permitido, o sistema irá emitir a mensagem "Valor Desconto Maior que o Valor Autorizado para Desconto", e barrar a baixa.

**Observações:**

* O resultado retornado pela fórmula para que o processo continue sem erros deve ser o valor 1 ou vazio "".
* Fórmula utilizada deve ser criada com bastante critério, pois no caso da baixa de vários lançamentos ao mesmo tempo, pode haver queda de performance, uma vez que a validação acima irá ser executada para cada item de baixa gerado.
* Todos os processos que executam o serviço de baixa irão executar essa validação.

Fórmula composição Valor Original Crédito Adiantamento

O parâmetro define a fórmula para obter o valor de composição para o valor de composição para o valor original do lançamento de crédito de adiantamento, originado pela baixa do lançamento de adiantamento originado no Totvs Gestão de Estoque Compras e Faturamento com incidência de IRRF-PJ e outras retenções diferentes das contribuições sociais (PIS, COFINS,CSLL). O contexto da fórmula será o lançamento de adiantamento.

**Baixa a receber**

Data default da baixa a receber

Define a data default de baixa a receber (sistema, vencimento, emissão, previsão de baixa e cheque).

Histórico default da baixa a receber

Define o histórico default.

Permite baixar Lançamentos a Receber enviados para o Banco

Define que os lançamentos enviados para o banco poderão ser baixados.

Desvincular baixa da compensação do cheque para lançamentos a receber

Define que a baixa a receber e a compensação serão operações distintas. Porém o parâmetro de tela no cancelamento de baixa só estará disponível para lançamentos com cheque emitido/recebido.

Não gerar outro boleto para lançamento após baixa parcial

Após a baixa parcial do lançamento, o sistema não vai gerar outro boleto, apenas alterar o status para baixado parcialmente.

Informar base de cálculo dos tributos de lançamentos a receber

Permite ao usuário informar a base de cálculo que será utilizada no cálculo dos tributos do lançamento. Parâmetro utilizado no processo de baixa completa e 'Baixar Créditos/Devoluções Vinculados'. No processo de recebimento via cheque, é apresentado o campo 'Base de Cálculo dos Tributos' para que seja informada a base de cálculo que deve ser utilizada para geração de tributos em baixa parcial. Observações: Se este parâmetro estiver marcado e o usuário não informar a base de cálculo, ou inserir um valor maior do que o valor da nota, o sistema fará o cálculo já existente.

Atualizar histórico de alteração de boleto

Se habilitado o sistema irá guardar as alterações dos boletos em anexos "Histórico de alteração dos boletos" e na tabela FBOLETOHISTORICO.

Aceita baixa a receber em finais de semana e feriados

Define o comportamento do sistema para baixas em finais de semana e feriados (manter o mesmo dia, primeiro dia posterior e primeiro dia anterior).

**Cheque**

Porta serial leitora

Define a porta serial leitora de cheque (COM1, COM2, COM3, COM4 e teclado).

Cheque pré-datado

* Data default de vencimento

Define a data de vencimento default de cheque pré-datado (nula, sistema, vencimento, emissão e previsão de baixa).

* Custódia cheque

Data default custódia: Define a data default de custódia de cheques (sistema, vencimento ou emissão).

Origem do nome da cidade

Define a origem do nome da cidade a utilizar no cheque (coligada ou filial).

Datas do cheque em finais de semana e feriado

Define a data do cheque em finais de semana e feriado (manter o mesmo dia, primeiro dia posterior ou primeiro dia anterior).

**Cheque a receber**

Data default cheque a receber

Define a data default de pagamento com cheque (sistema, baixa, vencimento, emissão ou previsão de baixa).

Histórico default cheque a receber

Define o histórico default de cheque a receber.

Permite emissão de cheques com número já utilizado

Define se poderá repetir os números dos cheques.

Valor cheque a receber: Define os valores mínimos e máximos de cheque a receber.

**Impressora cheque**

Define configurações básicas de impressão de cheque.

**Cancelamento da baixa**

Permite cancelamento da baixa de lançamentos bloqueados para alteração

Define cancelamento de baixa de lançamentos bloqueados para alteração.

Permite cancelamento da baixa com data de cancelamento fora do período da baixa

Define cancelamento de baixa com data de cancelamento fora do período de baixa.

Permite cancelamento da baixa com data de baixa fora do período de baixa

Define cancelamento de baixa com data de baixa fora do período de baixa.

Histórico do cancelamento da baixa

Define histórico do cancelamento de baixa.

**Contab. baixa**

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

Número contábil da baixa: Define o default do número contábil da baixa

(Número do cheque, número contábil da inclusão, número do documento, número do mov. RM Nucleus, segundo número ou referência.

**Contab. baixa receber**

Data default de baixa a receber

Define a data default de baixa a receber (sistema, baixa, vencimento, emissão, previsão de baixa, cheque, inclusão, digitação ou comp. cheque).

**Estorno contab. baixa**

Data default de estorno de baixa

Define a data default de baixa a receber (sistema, digitação ou contab. baixa).

**Depósito - extrato caixa**

Centro de custo obrigatório

Define a obrigatoriedade de centro de custo em extrato de caixa.

Compensar saque/depósito de transferência separadamente

Define que extratos de saques e depósitos gerados através de transferências bancárias serão compensados separadamente.

Gerar CPMF automaticamente

Define que ao incluir um extrato de caixa manual ou gerar extratos de caixa por outros módulos do sistema, o sistema irá calcular e gerar um extrato de caixa do tipo "Saque CPMF " automaticamente.

Número do documento 

* Tamanho: Define o tamanho do número do documento de extrato de caixa.
* Preencher com zeros a esquerda: Define o preenchimento com zeros a esquerda até completar o tamanho do número do documento.
* Copiar ref. Para o número do documento: Define que a referência será copiada para o número do documento nos extratos manuais (depósito manual, saque manual, saque CPMF e transferência).

Fechamento do extrato

Define a data que restringirá a inclusão de extrato. Isso inclui cheques e baixas.

Período inclusão do extrato

Define o período para inclusão de extrato.

Permitir data de emissão posterior à data de compensação no extrato

Define que será permitido incluir extrato com data de emissão posterior à data de compensação no extrato.

**Depósito - contab. extrato**

Usar contabilização de mútuo

Define se utilizará os recursos de contabilização de mútuo.

Permite contabilizar com valor maior que o valor do extrato

Define se será permitido contabilizar com valor maior que o valor do extrato.

CPMF

* Evento contábil

Define evento contábil para CPMF.

Default contábil no extrato

Define o default contábil no extrato de caixa (não contábil, contábil, à contabilizar).

Data default do extrato

* Contabilização: Define data default de contabilização do extrato (sistema, vencimento, emissão ou compensação).
* Estorno: Define data default de estorno (sistema ou contab. extrato).

**Desconto por Antecipação**

Considerar a data de vencimento do lançamento na regra de validação da vigência

Define que deve considerar a data de vencimento do lançamento na regra de validação da vigência do cálculo do desconto por antecipação.

**Tributo**

Inclusão de tributos defaults para lançamentos a receber

Através deste parâmetro você pode cadastrar Tributos defaults para serem buscados na edição de Lançamentos Financeiros. Para o perfeito funcionamento da rotina de controle de Retenções Tributárias, é necessário seguir os passos informados no roteiro de Retenções Tributárias.

**Configurações globais de cartão de crédito**

Modelo E-commerce

Modelo E-commercefadeBuyPage Cielo

Ambiente ativo  
Define se o ambiente ativo é de Teste ou de Produção

Código de afiliação  
Código de identificação único do estabelecimento comercial junto à adquirente

Chave de acesso  
Chave de acesso do lojista

URL ambiente de teste  
URL do processo de transação do recebimento com cartão no ambiente de testes

URL ambiente de produção  
URL do processo de transação do recebimento com cartão no ambiente de produção

Checkout Cielo

MerchantId  
Código de identificação único do estabelecimento comercial junto à adquirente

URL de Post  
URL de retorno de informações

Gravar arquivo de log quando ocorrer erro no processamento de notificação e mudança de status

IFrame Getnet

Código de acesso  
Chave de acesso do lojista

Nº máximo de parcelas  
Número máximo de parcelas permitidos no recebimento com cartão

URL de checkout  
URL de checkout da Getnet

URL de autenticação  
URL para a autenticação do processo

URL de cancelamento  
URL para o cancelamento da transação

Client Id  
Identificador público da aplicação

Client Secret  
Chave confidencial conhecida apenas pela aplicação e pelo servidor de autorização

e-RedeAutenticação OAuth 2.0

A REDE comunicou a **descontinuação do modelo de autenticação Basic Auth a partir de 05/01/2026**, passando a adotar **exclusivamente o modelo OAuth 2.0**.

Para a correta adequação do sistema, será necessário:

* Solicitar à REDE a **URL de Autenticação OAuth 2.0**;
* Atualizar a **URL de transações para a versão v2**, também fornecida pela REDE.

⚠️ **ATENÇÃO**  
A configuração da **URL de Autenticação OAuth 2.0 exige obrigatoriamente a utilização da URL de transações na versão v2**.  
Caso a URL de transações permaneça em versão anterior, o **processo de recebimento por cartão no E-Commerce REDE não será executado com sucesso**, ocasionando falhas nas transações.

Nº máximo de parcelas  
Número máximo de parcelas permitidos no recebimento com cartão

URL  
URL do processo de transação do recebimento com cartão

URL de Autenticação  
URL para a obtenção do token de acesso (protocolo OAuth 2.0) - *só deve ser preenchido se estiver sendo utilizada a v2 da URL de transações.*

Client Id (Número de afiliação)  
Identificador público da aplicação

Client Secret (Token)  
Chave confidencial conhecida apenas pela aplicação e pelo servidor de autorização da e-Rede

CyberSource

**CyberSource**

Ambiente ativo  
Define se o ambiente ativo é de Teste ou de Produção

Merchant Id  
Código de identificação único do estabelecimento comercial junto à adquirente

Nº máximo de parcelas  
Número máximo de parcelas permitidos no recebimento com cartão

Key Id  
Identificador associado a uma chave de segurança específica (Shared Secret Key)

Shared Secret Key  
Identifica qual chave deve ser usada pela Cybersource para verificar a assinatura de uma solicitação

Tipo da Adquirente  
Sistema ou empresa que processa os pagamentos (Cielo, Rede ou Getnet)

Módulo de Antifraude  
Antifraude utilizado (Nenhum ou TOTVS Gestão Educacional)

**CyberSource Cardinal**

Identificador comerciante  
Código de identificação único do estabelecimento comercial junto à adquirente

Identificador da API  
Chave criptografada para identificação da API

Chave privada API  
Chave privada da API

Adyen

Ambiente ativo  
Define se o ambiente ativo é de Teste ou de Produção

Merchant account  
Código de identificação único do estabelecimento comercial junto à adquirente

Nº máximo de parcelas  
Número máximo de parcelas permitidos no recebimento com cartão

API Key  
Chave de segurança para autenticação de requisições a partir do servidor

Origin Key  
Chave de segurança legada da Adyen

Public Key  
Chave pública para autenticação e criptografia no lado do cliente

**Configurações cartão de Crédito/Débito**

**Baixas**

Ativar Bandeira Visa

Parametriza se a bandeira Visa será utilizada para pagamentos com cartão de crédito.

* Conta caixa Visa

Campo para parametrizar a conta caixa da bandeira Visa.

Ativar Bandeira Visa

Parametriza se a bandeira Visa será utilizada para pagamentos com cartão de débito.

* Conta caixa Visa

Campo para parametrizar a conta caixa da bandeira Visa.

**Bandeira 2/3**

Ativar Bandeira Master

Parametriza se a bandeira Master será utilizada para pagamentos com cartão de crédito.

* Conta caixa Master

Define a conta caixa da bandeira Master.

Ativar Bandeira Master

Parametriza se a bandeira Master será utilizada para pagamentos com cartão de débito.

* Conta caixa Master

Define a conta caixa da bandeira Master.

**Obs**.:

A função Débito para a bandeira Master só esta disponível para o modelo CheckOut.

**Bandeira 3/3**

Esta opção só está disponível para o modelo CheckOut na função crédito.

* Conta caixa

Define a conta caixa para pagamento.

* Meio de pagamento

Define o meio de pagamento na baixa para a função crédito.

**Conciliação**

Novo Modelo de previsão de recebimento com cartão

Define em que momento será gerado o extrato de taxa da transação de pagamento com cartão. Aplica-se em pagamento e-commerce e TEF

Marcado a geração ocorre no momento da baixa.

Desmarcado a geração ocorre no momento da conciliação.

O extrato de taxa de cartão é gerado de acordo com o [cadastro de taxas de cartão](https://tdn.totvs.com/pages/releaseview.action?pageId=520118509)

**Configurações por Filial**

Define as configurações do modelo para pagamento de cartão de crédito/débito por filial.

**Autenticação do Caixa**

Usa autenticação mecânica

Define que ao registrar ou estornar pagamento/recebimento pelo módulo de caixa, o sistema apresenta a opção para imprimir a autenticação mecânica.

Permite não imprimir autenticação

Define que ao registrar ou estornar pagamento/recebimento pelo módulo de caixa, será permitido não imprimir autenticação mecânica.

Permite reimprimir autenticação

Define que ao registrar ou estornar pagamento/recebimento pelo módulo de caixa, será permitido reimprimir autenticação mecânica.

Obrigatória a impressão de abertura do caixa

Define que ao abrir caixa será obrigatória a impressão de abertura.

Saída de impressão

Define a saída de autenticação de caixa (impressora windows ou porta LPT1).

**Configuração Layout**

Define a configuração de layout de autenticação de caixa.

**Número autenticações**

Define as características do número de autenticações do caixa.

**Relatórios do caixa**

Balanço da sessão de caixa

* Relatório da sessão de caixa

Define relatório da sessão de caixa.

Usa recibo

Define relatórios de recibo do módulo de caixa (caixa, estorno e extrato).

**TEF**

TEF na sessão de Caixa

Define a utilização do TEF na sessão de caixa e a inclusão de dados para utilização, por coligada:

* Usa

Permite ao usuário definir na abertura da sessão de caixa se habilita ou não a opção do TEF.

* Não usa

Define que o usuário não usará o TEF na sessão de caixa e não permitirá na abertura da sessão habilitar a opção.

* Uso obrigatório

Define que o uso do TEF é obrigatório na sessão de caixa e não permitirá desmarcar a opção na abertura da sessão.

**TEF por filial**

Define a utilização do TEF na sessão de caixa a inclusão de dados para utilização, por filial cadastrada.

As opções de uso do TEF são as mesmas do TEF por coligada, desde que parametrizada por filial também. (Usa, Não usa e Uso obrigatório)

**TOTVS Pagamento Instantâneo-** **Configurações**

Define as configurações gerais da integração com o TOTVS Pagamento Instantâneo, para cobrança via PIX.

Credenciais:

* Tenant

Define o nome da tenant gerada para acesso ao TOTVS Pagamento Instantâneo.

* Usuário

Define o usuário de acesso ao TOTVS Rac

* Senha

Define a senha do usuário de acesso ao TOTVS Rac

Baixa:

* Conta/Caixa (**Se a solução escolhida for 'TOTVS Pagamento Digital (TPD)', este campo ficará desabilitado para alteração e será considerada a mesma Conta/Caixa utilizada na conciliação (liquidação)**)

Define a conta/caixa usada na baixa dos boletos. Esta é uma conta transitória criada apenas no sistema TOTVS, e não deve possuir vínculo bancário.  
  
**Importante**:A partir dos patchs 12.1.2502.230, 12.1.2506.179 e 12.1.2510.112 da BibliotecaRM o sistema dispõe do tratamento de múltiplas chave PIX. Considerando que o TPI/TPD só permite utilizar uma conta bancária, agora o sistema permite trabalhar com várias contas, podendo utilizar a chave PIX que for informada na [aba 'TOTVS Pagamento Instantâneo' da conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837#ContaCaixa--669937268) associada no lançamento financeiro. Vale ressaltar que mesmo que, por default, a conta/caixa informada neste campo seja utilizada no item de baixa do lançamento baixado via PIX, será considerada a chave pix que for informada na aba 'TOTVS Pagamento Instantâneo' da conta/caixa associada no lançamento financeiro.

Meio de Pagamento

Define o meio de pagamento usado na baixa dos boletos.

* Taxa

Define a taxa, valor ou percentual, a ser cobrada por cada transação.

Conciliação:

* Conta/Caixa

Define a conta/caixa a ser utilizada na conciliação dos recebimentos referente as transações.

* Evento Contábil:

Define o evento contábil utilizado na geração do extrato de saque transferência na conciliação.

* Dias para busca retroativa na conciliação de transação PIX:

Determina o número de dias anteriores à data da importação da conciliação quando se utiliza a opção de importação "TOTVS WebService", marcando a opção para conciliação diária. O número de dias deve ser definido com um valor entre 2 e 15.

* Tempo de espera do servidor (time out) na conciliação de transação PIX (em minutos):

Determina o tempo máximo para expiração da conexão com o servidor para busca de arquivo de conciliação PIX. O número de minutos deve ser definido com um valor entre 2 e 5.

**TOTVS Pagamento Instantâneo- Configurações por Filial**

Define as configurações da integração com o TOTVS Pagamento Instantâneo, para cobrança via PIX por Filial.
