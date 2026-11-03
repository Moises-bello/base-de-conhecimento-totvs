---
content_hash: 1cdaae7c92961e12cf043a46814be741778c4447d73286b865bc5be5944e6f96
fetched_at: '2026-06-29T00:09:18.479815+00:00'
page_id: '421388704'
product: rm
source: tdn-rm
title: Geração de Retenções Tributárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388704
version: 15
---

(Assistente de Implantação de Processos | Etapa Geração de Retenções na Baixa dos Lançamentos a Pagar)

Os parâmetros de Retenções são utilizados para definir algumas regras e funcionalidades para a geração dos lançamentos de Retenções.

Para o perfeito funcionamento da rotina de controle de Retenções Tributárias, é necessário seguir os passos informados no roteiro de Retenções Tributárias.

**Origem Default das Tabelas**

A Filial, a Conta/Caixa, o Departamento, o Centro de Custo, as Tabelas Opcionais, as Datas Opcionais, o Rateio por Centro de Custo e o Rateio por Departamento, podem ser apresentados por default nos lançamentos de Tributos gerados pelo sistema.

Selecione de qual cadastro o sistema irá buscar estas informações: do Fornecedor (Fornecedor incluído no lançamento de Tributo. Exemplo: Secretaria da Receita Federal) ou Lançamento Original (lançamento gerador de Tributos).

Exemplo

O fornecedor possui as seguintes informações:

* Filial = 01
* Departamento = 01
* Centro de Custo = 01
* Conta/Caixa = 01
* Tabela Opcional 01 = 01
* Tabela Opcional 02 = 01
* Tabela Opcional 03 = 01
* Tabela Opcional 04 = 01
* Tabela Opcional 05 = 01
* Rateio por Centro de Custo = 01
* Rateio por Departamento = 01

O lançamento gerador de Tributos possui as seguintes informações:

* Filial = 02
* Departamento = 02
* Centro de Custo = 02
* Conta/Caixa = 02
* Tabela Opcional 01 = 02
* Tabela Opcional 02 = 02
* Tabela Opcional 03 = 02
* Tabela Opcional 04 = 02
* Tabela Opcional 05 = 02
* Rateio por Centro de Custo = 02
* Rateio por Departamento = 02

Selecionando a opção "Lançamento Original", ao baixar um lançamento gerador de Tributos, o sistema apresentará por default no lançamento de Tributo as informações do lançamento gerador de Tributos.

**Buscar dados no lançamento, se Cli/For vazio**

Este parâmetro só estará disponível se a opção "Fornecedor" for selecionada no parâmetro "Origem das Tabelas".

Com o parâmetro desmarcado:

Quando o cadastro do fornecedor "possuir" informações nas tabelas, o sistema buscará as informações do cadastro do Fornecedor (fornecedor incluído no lançamento de Tributo);

Quando o cadastro do fornecedor "não" possuir informações nas tabelas, o sistema buscará a Filial e os Rateios do cadastro do Lançamento Original (lançamento gerador de Tributos) e os outros campos ficarão em branco;

Quando o cadastro do fornecedor "possuir" informações para algumas das tabelas, o sistema buscará as informações do cadastro do Fornecedor (fornecedor incluído no lançamento de Tributo). Se no cadastro não existir Filial e Rateios, eles serão buscados do cadastro do Lançamento Original (lançamento gerador de Tributos) e os outros campos ficarão em branco.

Com o parâmetro marcado:

Quando o cadastro do fornecedor "possuir" informações nas tabelas, o sistema buscará as informações do cadastro do Fornecedor (fornecedor incluído no lançamento de Tributo);

Quando o cadastro do fornecedor "não" possuir informações nas tabelas, o sistema buscará as informações do cadastro do Lançamento Original;

Quando o cadastro do fornecedor "possuir" informações para algumas das tabelas, o sistema buscará informações do cadastro do Fornecedor (fornecedor incluído no lançamento de Tributo) e os campos que não possuírem informações no cadastro do Fornecedor serão preenchidos com as informações do cadastro do Lançamento Original.

**Fornecedor**

Informe para qual fornecedor o sistema irá gerar o lançamento de Tributos, no caso a Secretaria da Receita Federal.

**Tipo de Documento**

Informe qual o tipo de documento será usado na inclusão do lançamento automático de tributo.  
Este tipo de documento não precisa ter o campo "Classificação" preenchido.

**Gerar Número do Documento****Sequencialmente**

Com esse parâmetro Ativo, o número do documento para o lançamento de tributo será sequencial, respeitando a parametrização de número de documento do sistema. Se ele estiver desmarcado, terá o mesmo número de documento do lançamento origem onde ocorreu a retenção.

Atenção, quando este parâmetro estiver marcado, a sua funcionalidade sofrerá alterações dependendo do parâmetro "Copiar Referência para número do Documento".

**Histórico do lançamento de Tributo gerado**

Informe um histórico default para os lançamentos de Tributos. O aplicativo já fornece o histórico  *Tributação referente a lançamento Ref. "[NUM]", Cód. Tributo "[TRB]", Cód. Retenção "[RET]"* como default, podendo ser alterado a qualquer momento.

Você pode utilizar as seguintes variáveis:

* [TRB] para o Código do Tributo
* [RET] para o Código de Retenção
* [CCF] para o Código do Cliente/Fornecedor
* [FAN] para o Nome Fantasia do Cliente/Fornecedor
* [NOM] para o Nome do Cliente/Fornecedor
* [NUM] para o Número do Documento
* [HIS] para o Histórico
* [MDC] para o Mês de Competência
* [EMI] para a Data de Emissão
* [VEN] para a Data de Vencimento
* [SNU] para o Segundo Número
* [TDO] para o Tipo de Documento
* [DTD] para a Descrição do Tipo de Documento
* [DCG] para a Descrição do Centro de Custo Global
* [DDG] para a Descrição do Departamento Global
* [CPF] CNPJ/CPF do Cliente/Fornecedor

Observação: se nenhum histórico for informado, os lançamentos de Tributos terão o mesmo histórico informado no lançamento de origem.

**Alterações nas regras de retenção do PIS, COFINS e CSLL nos pagamentos efetuados de PJ A PJ pela prestação de serviços (Lei nº 13.137/2015)**  
Valor mínimo para a retenção até o dia 21/06/2015

Era dispensada a retenção para pagamentos de valor igual ou inferior a R$ 5.000,00, caso ocorresse mais de um pagamento a mesma pessoa jurídica no mês, deveria ser efetuada a  
soma de todos os valores pagos no mês para efeito de cálculo do limite de retenção, compensando-se o valor retido anteriormente. Ocorre apenas para data de referência menor que 21/06/2015.

Valor mínimo para a retenção a partir de 22/06/2015

A dispensa da retenção deverá ocorrer quando o valor das contribuições resultar em valor menor ou igual a R$ 10,00. Assim, podemos perceber que não deve ser mais considerado o valor do pagamento do serviço como parâmetro para o valor mínimo de retenção, mas o valor dos tributos calculados. Esse valor mínimo de retenção (R$ 10,00) deve ser composto pelo somatório das contribuições calculadas no pagamento (PIS, COFINS e CSLL), haja vista que, neste caso, não são recolhidas individualmente.

Quando o parâmetro *Usar cumulatividade diária para cálculo das retenções dos tributos* está marcado e o parâmetro *Usar cumulatividade conforme as Leis 10.485 e 13.137* desmarcado a cumulatividade ocorre de forma diária para as retenções, de acordo com o valor mínimo informado. Para que a retenção seja feita por cada tributo de forma individual, é necessário uma flag interna não acessível para parametrização direta (entre em contato caso necessite). Se o valor mínimo estiver zerado não há cumulatividade.

Quando o parâmetro *Usar cumulatividade diária para cálculo das retenções dos tributos* está marcado e o parâmetro *Usar cumulatividade conforme as Leis 10.485 e 13.137*  também está marcado a cumulatividade será sempre por tributo, de acordo com o valor mínimo definido no parâmetro. Se o valor mínimo estiver zerado não há cumulatividade.

Quando o parâmetro *Usar cumulatividade diária para cálculo das retenções dos tributos* não está marcado não há geração dos lançamentos de tributos na baixa.

Exemplos:

\*\*Mesmo prestador e tomador de serviços

* 01/06/2015 - Pagamento de R$ 4.000,00 , sem retenção porque não atingia o valor mínimo de retenção de R$ 5.000,00
* 24/06/2015 - Pagamento de R$ 300,00 \* 4,65% = R$ 13,95, com retenção porque o valor das contribuições é superior a R$ 10,00

Vale ressaltar que é necessário verificar se na data do pagamento por um serviço tomado não teremos outros pagamentos para a mesma pessoa jurídica. Pois, se tivermos outros pagamentos na mesma data, para a mesma pessoa jurídica, deverá ser feitar a soma de valores e assim proceder à retenção.

Se o resultado da aplicação da alíquota de 4,65% sobre a soma de valores a serem pagos na mesma data e para a mesma pessoa jurídica superar R$ 10,00, deverá haver a retenção. Assim, a soma passa a ser diária. Reiterando de que não há mais a soma mensal.

Para outros exemplos e maiores informações a respeito da nova regra, favor consultar abaixo o link nas informações complementares.

**Gravação da tabela FRETENCAOACUMULADA**

Os processos que calculam a cumulatividade dos tributos são:

* A baixa de lançamentos;
* A emissão de cheques;
* A remessa de pagamento.

No caso da baixa, a data é a data de baixa do lançamento. No caso do cheque, é a data de emissão do cheque. No caso da remessa, o usuário poderá escolher a data no momento de realizar a remessa. As datas possíveis são: emissão, vencimento, previsão da baixa, datas opcionais (1 a 5). Essa opção está disponível na tela de remessa de pagamento.

**Facilitador para inclusão de tributos no lançamento financeiro**

Caso exista natureza orçamentária default informada no cadastro de um tributo (IRRF e CSRF - CSLL-RF, PIS-RF e COFINS-RF), o sistema irá substituir, no lançamento gerado relacionado ao tributo, a natureza orçamentária financeira de todos os rateios por centro de custo caso existam.

 Informações Complementares

* [DT - PIS - COFINS - CSLL – Novas Regras de Retenção – Lei 13.137/2015](https://tdn.totvs.com/x/TRCIF)
