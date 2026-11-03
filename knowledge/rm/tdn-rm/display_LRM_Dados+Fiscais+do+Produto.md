---
content_hash: 0d8c70104e60c545169777332b83a1b5734e09dc04e1c669037fd654ae26e9e2
fetched_at: '2026-06-29T00:09:25.901211+00:00'
page_id: '423938199'
product: rm
source: tdn-rm
title: Dados Fiscais do Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+Fiscais+do+Produto
version: 12
---

A opção Dados Fiscais do Produto são informados os dados utilizados nas rotinas fiscais e geração dos impostos automáticos para financeiro.

* O código da receita deverá ter sido inicialmente cadastrado no menu Tabelas de Tributação/IRRF. Estes códigos deverão ser informados seguindo as normas da Receita Federal.
* O Indicador Especial será utilizado para geração do registro 54 da SEF PE.
* O contribuinte beneficiário dos incentivos relativos ao PRODEPE/FUNCRESCE deverá preencher o campo com 01 para produtos sem incentivo na entrada ou 02 para produtos com incentivo na entrada.
* O contribuinte não-beneficiário dos referidos incentivos deverá preencher este campo com zeros.
* A capacidade volumétrica será utilizada pelo RM Líber nas Rotinas Federais para a geração da Instrução Normativa 63 - DNF (Demonstrativo de Notas Fiscais).
* No RM Fest foi implementado o campo capacidade volumétrica na opção Características Fiscais, ao converter para o TOTVS Gestão de Estoque, Compras e Faturamento este campo virá preenchido.
* O campo Margem de Lucro é utilizado para informar o percentual utilizado nas fórmulas para base de cálculo de ICMS com substituição tributária.
* As informações do Código de Apuração serão utilizadas para geração do registro 54 da SEF PE. Essa geração é efetuada no RM Liber.
* O beneficiário dos incentivos relativos ao PRODEPE/FUNCRESCE deverá codificar os registros de forma distinta, para separar suas operações por apuração, utilizando um código específico para:
* Os produtos não-incentivados, adotando o código 01 nesta hipótese;
* Os produtos incentivados, adotando um código para cada hipótese de escrituração independente prevista na legislação e, se for o caso, na hipótese do crédito presumido ou do financiamento, para cada percentual distinto do incentivo, utilizando, do código 02 em diante, de forma seqüencial, um para cada hipótese;
* O contribuinte não-beneficiário dos incentivos relativos ao PRODEPE/FUNCRESCE deverá preencher este campo com zeros;
* Incentivo Fiscal CDI-MS é o campo que deverá ser utilizado se o produto gerar lançamentos fiscais para o Registro 88 - Saídas do estado do MS.
* O campo ISS Devido Município Cliente é utilizado para buscar a alíquota do ISS no município do Cliente da Nota Fiscal. Esta alíquota deverá ter sido inicialmente informada. Se este campo estiver desmarcado, será habilitado na pasta tabelas do movimento o campo "município", neste por default será apresentado o município do cliente da nota, cabendo neste caso ao usuário alterar para o município informado na filial no RM Liber.
* O ISS só incidirá sobre serviços.
* Não será permitida a inclusão de serviços que possuam ISS's retidos em municípios diferentes em uma mesma nota.
* A alíquota de ISS poderá ser diferenciada por município. Para isto será necessário informar no cadastro de produto a alíquota para o município.
* Comportamento das movimentações com a opção ISS Devido Município Cliente marcada:

Em se tratando de movimento de compra o comportamento será da seguinte maneira:

* Se o serviço prestado tem ISS devido no município do cliente (entenda-se "Tomador do serviço" e que na compra é a própria filial) devemos ter um município informado no movimento, mas este pode ser qualquer município (normalmente é o da própria filial).
* Se o serviço prestado 'Não tem ISS devido no município do Cliente' do tomador, ou seja, o ISS é devido no município do prestador, o município informado deve ser o do fornecedor.

Em se tratando de movimento de venda o comportamento será da seguinte maneira:

* Se o serviço prestado tem ISS devido no município do cliente (entenda-se "Tomador do serviço" e não o Cli/For do sistema) devemos ter um município informado no movimento, mas este pode ser qualquer município (normalmente é o do próprio cliente).
* Se o serviço prestado não tem ISS devido no município do tomador, ou seja, o ISS é devido no município do prestador, o município informado deve ser o da empresa emitente, no caso o da filial.
* O campo Produto Exige Inventário Fiscal será utilizado na geração da SISIF (RM Liber). O Registro 34 do SISIF, referente ao Inventário, somente conterá Produtos cujo esse campo esteja habilitado.
* O campo "Tipo de Medicamento" será utilizado para classificar o produto por seu tipo de medicamento.
* Campo "Código Atividade Econômica" será utilizado para informado o Código de Atividades, Produtos e Serviços sujeitos a Contribuição Sobre a Receita Bruta de acordo com a Tabela 9 da Reinf.
* Campo "Classificação do Serviço" será utilizado para informar o Código de Classificação do Serviço prestado mediante cessão de mão de obra/empreitada sujeito a retenção de contribuição previdenciária conforme Tabela 6 da Reinf.
* Campo "Código Natureza de Rendimento" será utilizado para informar a Natureza de Rendimento, definindo através da tabela 1 da Reinf.

Aba Tributação

* **Local Operação** - Este campo foi criado para atender as regras da Lei Complementar nº 214/2025 onde *local da operação* é o município e o estado que devem ser informados para fins de apuração e distribuição do IBS (Imposto sobre Bens e Serviços). De acordo com a legislação, o local da operação será, via de regra, o **local do destinatário da operação**, salvo disposições específicas previstas em lei para determinados tipos de operações. Selecione a opção Origem ou Destino.
* **Local de Prestação** - Este campo foi criado para Definir qual o local da Prestação deste Produto/Serviço (Origem, Destino ou Local de Incidência) para fins de apuração do ISS.
Base de Conhecimento

* [Buscas Alíquota do ISS por Município](http://tdn.totvs.com/pages/viewpage.action?pageId=315910268)
