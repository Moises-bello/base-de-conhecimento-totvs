---
content_hash: cc333dbb13d2129648371fc5bc889b2ca2869febe7a22903e7275db98eabc212
fetched_at: '2026-06-29T00:09:28.035546+00:00'
page_id: '423938629'
product: rm
source: tdn-rm
title: Relatório Balancete Orçamentário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938629
version: 6
---

O Balancete é um relatório contábil oficial exigido pela Legislação. Ele reflete a contabilidade de uma empresa ou organização num determinado período.

O relatório de Balancete Orçamentário permitirá a visualização e controle dos Orçamentos confrontados com as contabilizações realizadas.

ATENÇÃO ÀS PARAMETRIZAÇÕES!

O relatório somente será impresso de maneira correta quando utilizados os formatos de **folha A4 ou Carta** (neste caso, a impressora padrão da máquina deve possuir estas configurações).

Para os demais formatos, o relatório será gerado mas virá com configurações incorretas.

Desenvolvimento/Procedimento

**1. Aba Dados**

**Data Inicial / Final:** Informe a faixa de datas desejada para a impressão do Balancete. Estas datas deverão estar dentro do Período Contábil vigente.

O campo data será carregado automaticamente com a última data informada no Relatório, salvo nas preferências.

Ao lado do campo data, que pode ser utilizado a opção "filtro automático de datas" que possibilita retornar os períodos fixos (Semanal, Mensal, Bimestral, Trimestral, Semestral, Anual) e aplicá-lo como período do Balancete.

**Basear na Data de Cotação:** Esta opção permite a impressão dos valores baseando na data da cotação dos lançamentos. Marcando esta opção, o sistema buscará os lançamentos que possuírem a data da cotação dentro do período informado no intervalo de datas.

Observação: Esta opção somente será visualizada nesta janela, se nos "Parâmetros/Lançamentos" a opção "Usa segundo valor" estiver marcada e for informada uma moeda no parâmetro "Símbolo moeda 2º valor".

**Tipo Balancete**

Para emissão do balancete, deve ser escolhido um tipo para o mesmo dentre as opções a seguir:

* Contábil: Processamento do relatório por saldo da conta contábil.
* Gerencial: Processamento do relatório por saldo gerencial.
* Contábil/Gerencial: Processamento do relatório por saldo da conta contábil, quebrando por saldo gerencial.
* Gerencial/Contábil: Processamento do relatório por saldo gerencial, quebrando por saldo da conta contábil.
* Contábil/Centro de Custo: Processamento do relatório por saldo da conta contábil, quebrando por saldo de Centro de Custo.
* Centro de Custo/Contábil: Processamento do relatório por saldo de Centro de Custo, quebrando por saldo da conta contábil.

**Lote:** Permite filtrar um ou mais Lotes, sendo Zero ou Lote N.

Serão considerados todos os registros que estiverem nos lotes informados pelo usuário.

Apenas os lotes das coligadas selecionadas no filtro de coligada estarão disponíveis para seleção.

Se informou lote que não o Lote 0, não serão exibidos os saldos anteriores de períodos já liberados de contas sem movimentação após a liberação e antes da data inicial de movimentação informada.

Caso nenhum lote seja informado no filtro será considerado o lote 0.

**Imprimir / Filtrar:**

As opções de Imprimir / Filtrar apresentadas na tela do processo de emissão do relatório, variam de acordo com tipo de Balancete selecionado na etapa anterior. Desta forma para cada tipo de Balancete veja quais opções de Imprimir / Filtrar estão disponíveis:

Balancete contábil:

Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis, que não possuam movimentação no período, mas que possuam saldo. ­

Contas com movimentação e sem saldo: Quando marcado esta opção, as contas que possuírem movimentação no período e que possuam saldo igual a zero serão impressas. ­

Contas sem movimentação e sem saldo: Quando marcado esta opção, todas as contas do seu plano de contas que não tenham movimentação e saldo igual ao zero no período informado serão impressas. ­

Contas com movimentação e com saldo: Quando marcado esta opção, todas as contas do seu plano de contas que possuírem saldo diferente de zero e movimentação no período informado serão impressas. ­

Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

Balancete Gerencial: ­

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que não possuam movimentação no período, mas que possuam saldo gerencial anterior. Essa opção em momento nenhum considera conta contábil apenas conta gerencial. ­
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que possuam movimentação no período, mas que possuam saldo igual ao zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial. ­
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que não possuam movimentação no período e que possuam saldo igual ao zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial. ­
* Contas com movimentação e com saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que possuam movimentação no período e que possuam saldo diferente de zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

Balancete Contábil/Gerencial ou Balancete Gerencial/Contábil:

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que não possuam movimentação no período, mas que possuam saldo, ou ainda, que possuam contas gerenciais informadas como default no Plano de Contas.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que possuam movimentação no período, mas que possuam saldo igual ao zero. ­
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que não possuam movimentação no período e que possuam saldo igual ao zero.  ­
* Contas com movimentação e com saldo:  Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que possuam movimentação no período e que possuam saldo diferente de zero.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.
* Contas com movimentação e sem rateios: Válido para relatórios do tipo Contábil/Gerencial. Quando marcado esta opção, todas as contas do seu plano de contas que não possuírem rateio, mas possuírem movimentação no período informado serão impressas.
* Contas Contábeis sintéticas: Ao habilitar esta opção, serão impressas as contas contábeis sintéticas. Observação: Esta opção está disponível apenas para Balancete Gerencial/Contábil.
* Contas gerenciais sintéticas: Ao habilitar esta opção, serão impressas as contas gerenciais sintéticas. Observação: Esta opção está disponível apenas Balancete Contábil/ Gerencial.

Balancete Centro de custo/Contábil ou Balancete Contábil/Centro de custo:

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que não possuam movimentação no período, mas que possuam saldo diferente de zero.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que possuam movimentação no período, mas que possuam saldo igual à zero.
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que não possuam movimentação no período e que possuam não saldo igual á zero.
* Contas com movimentação e com saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que possuam movimentação no período e que possuam saldo.
* Não exibir contas inativas sem movimentação e sem saldos: Válido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

Está disponível para todos os Tipos de Balancetes a opção de Imprimir/Filtrar:

**Orçamentário.** Esta opção só ficará visível se existirem um ou mais orçamentos cadastrados e permitirá que sejam considerados os dados existentes no orçamento contábil.

Desta forma será possível realizar um paralelo entre as movimentações e os orçamentos lançados nas contas contábeis. Os valores orçamentários serão calculados para os orçamentos existentes no intervalo de datas informado. Vale ressaltar que todos os tipos de balancete irão exibir as contas que não atenderem os filtros definidos pelo usuário, mas que possuírem valor, Orçado Período ou Orçado Total, diferentes de zero. Se a conta não atender as condições dos filtros e os valores citados anteriormente forem igual a zero, ela não será exibida pelo relatório.

**Filtros Coligada / Filial / Departamento**

Esta opção permitirá selecionar Coligadas, Filiais cujos dados serão processados e consolidados no relatório. Os Departamentos somente estarão visíveis caso a base esteja parametrizada para usar departamento.

**Todas as Coligadas:** Opção disponível apenas se o parâmetro 'Acessa Contas Globais' estiver marcado.

Marque esta opção para impressão do relatório consolidado. Assim, seu relatório será calculado, levando em conta as contas de todas as coligadas de seu sistema. Não marcando o campo "Todas as coligadas", somente a coligada corrente ficará disponível na opção abaixo.

Obs.: Para a impressão do relatório consolidado para todas as Coligadas, todas as máscara existentes terão de ser iguais para todas as coligadas existentes no sistema.

**Ativar filtro:** Neste campo é possível selecionar as coligadas/ filiais/departamentos deverão ser emitidos no relatório. Para fazer a seleção é necessário clicar no ícone do lookup (...) a frente da descrição Ativar filtro. Será aberta uma janela onde estará visível todas as Coligadas (se o campo Todas Coligadas estiver habilitado), Filiais e Departamentos (Caso o parâmetro usa departamentos esteja habilitado). A visualização é feita de acordo com a hierarquia de cada campo. Cada coligada visualizada, terá logo abaixo suas respectivas filiais que por sua vez terão seus respectivos departamentos.

**Totalizar** Totais da conta sintética embaixo: Esta opção está disponível para os dois tipos de relatório a seguir:

* Obs: Balancete Contábil: Quando marcado esta opção, os valores das totalizações das contas contábeis sintéticas serão apresentados ao final de suas contas analíticas, caso contrário, os totais serão apresentados à frente das respectivas contas.
* Obs: Balancete Gerencial: Quando marcado esta opção, os valores das totalizações das contas gerenciais sintéticas serão apresentados ao final de suas contas gerenciais analíticas, caso contrário, os totais serão apresentados à frente das respectivas contas.

**Totalizar ao final débitos e créditos:** Válido para os balancetes Contábil e Gerencial. Marcando esta opção, a totalização final de débitos e créditos serão impressas.

**Totais das contas sintéticas em cima:** Esta opção está disponível para o tipo Centro de Custo/Contábil. Marcando esta opção, os valores das totalizações das contas contábeis sintéticas serão apresentados à frente das respectivas contas em cima das demais contas analíticas.

**Por níveis de Centros de Custo em cima:** Esta opção está disponível para o tipo Centro de Custo/Contábil e Contábil/Centro de Custo. Marcando esta opção, os valores das totalizações dos centros de custo serão apresentados em cima das listagens de contas contábeis.

**Por níveis de Centros de Custo embaixo:** Esta opção está disponível para o tipo Centro de Custo/Contábil. Marcando esta opção, os valores das totalizações dos centros de custo serão apresentados embaixo das listagens de contas contábeis.

**Total Geral:** Esta opção está disponível para o tipo Contábil/Gerencial, Gerencial/Contábil, Centro de custo/Contábil e Contábil/Centro de custo. Quando esta opção estiver marcada os saldos das contas serão totalizados e apresentados no final do relatório.

**Quebra por página**

**Quebrar por Filial:** Ao habilitar esta opção, o relatório será impresso realizando uma quebra a cada nova filial. Neste caso, os dados de cada filial serão apresentados separadamente no relatório.

**Quebrar por grupo contábil:** (Balancete Contábil, Contábil/Centro de Custo) Ao marcar esta opção será realizada uma quebra de página a cada novo grupo contábil apurado.

**Quebrar por grupo gerencial:** (Balancete gerencial/contábil) Ao marcar esta opção será realizada uma quebra de página a cada novo grupo gerencial apurado.

**Quebrar página por centro de custo:** (Balancete centro de custo/contábil) Ao marcar esta opção será realizada uma quebra de página ao fim de cada conta contábil vinculado ao centro de custo. Não será gerado quebra de página para os centros de custo que não houver contas com saldo ou movimentação.

**Quebrar por conta gerencial:** (Balancete gerencial/contábil) Ao marcar esta opção será realizada uma quebra de página ao fim de cada conta gerencial.

**2. Aba Filtros**

**Conta Contábil:** Permite emitir o relatório filtrando por uma ou mais contas CONTÁBEIS especificas e por faixas de contas (Ex: Da conta Contábil 1.1.1.1.001 até a conta Contábil 1.1.1.1.008).

**Conta Gerencial:** Permite emitir o relatório filtrando por uma ou mais contas GERENCIAS especificas e por faixas de contas (Ex: Da conta Gerencial 1.01 até a conta Gerencial 1.08).

**Centro de Custo:** Permite emitir o relatório filtrando por um ou mais Centros de custos específicos e por faixas de centro de custos (Ex: Do Centro de Custo 01 até a Centro de custo 08).

**Histórico:** Permite emitir o relatório filtrando por um ou mais Históricos Padrões.  

**Grau Contábil:** Selecione na caixa de seleção o grau de contas desejado para geração do balancete. Esta opção estará disponível para os balancetes Contábil, Contábil/Gerencial, Gerencial/Contábil, Centro de Custo/Contábil, Contábil/Centro de Custo.

Exemplo:

* Grau TOTAL: Todas as contas serão selecionadas (do primeiro nível sintético até a última conta analítica do plano de contas).
* Grau 1: Somente as contas sintéticas dos grupos serão selecionadas, neste caso (1 - Ativo, 2 - Passivo etc.) conforme o plano de contas.

**Grau Gerencial:** Selecione, na caixa de seleção, o grau de Contas Gerenciais desejado para geração do balancete. Esta opção estará disponível para os balancetes Gerencial, Contábil/Gerencial e Gerencial/Contábil.

**Tipo de Valor / Moeda** Permite escolher o valor e/ou moeda que será utilizado para a impressão de seu relatório.

**Primeiro Valor:** Imprime o relatório utilizando o valor da moeda corrente.

**Segundo Valor:** Imprime o relatório utilizando o segundo valor cadastrado nos lançamentos.

**Cotação de Outra Moeda:** Marcando esta opção, você poderá imprimir os relatórios utilizando uma cotação específica de uma outra moeda, além da moeda principal e da segunda moeda. Desta forma você poderá escolher no ato da impressão em qual moeda seu relatório será impresso, e qual o valor da cotação. Observação: Você deverá informar qual a moeda desejada e qual o valor da cotação, pois o sistema utilizará uma cotação única nesta opção e todos os valores apresentados no relatório serão convertidos com base no valor informado neste campo.

**Centro de Custo (Ativo/Inativo):** Permite ao usuário definir como filtro para o relatório o status do centro de custo, podendo ser ATIVO, INATIVO ou TODOS. Sendo assim serão considerados os registros onde o status do centro de custo for compatível com o filtro definido pelo usuário. Observação: Este campo não está visível quando o tipo do Relatório for Gerencial.

**Conta Contábil (Ativa/Inativa):** Permite ao usuário definir como filtro para o relatório o status das contas contábeis, podendo ser ATIVO, INATIVO ou TODOS. Sendo assim serão considerados os registros onde o status da conta for compatível com o filtro definido pelo usuário. Observação: Este campo não está visível quando o tipo do Relatório for Gerencial.

**3. Aba Layout**

**ATENÇÃOS ÀS PARAMETRIZAÇÕES!**

O relatório somente será impresso de maneira correta quando utilizados os formatos de **folha A4 ou Carta** (neste caso, a impressora padrão da máquina deve possuir estas configurações). Para os demais formatos, o relatório será gerado mas virá com configurações incorretas.

**Descrições das contas com tabulação:** Válido para todos os tipos de balancete. Marcando esta opção, a descrição das contas será impressa respeitando uma tabulação por nível de conta. Observação: Será descontado da descrição o espaço de tabulação.

**Usar o parâmetro de formato de impressão de saldos para Débito/Crédito:** Válido para todos os tipos de balancete. Marcando esta opção os valores de débito, crédito e movimento serão impressos respeitando o parâmetro de formato de impressão de saldos das contas.

Observação: Ao habilitar esta opção, a opção de "não exibir sinais nos valores de débito/ crédito" fica desabilitada.

**Não exibir sinais nos valores de débito/crédito:** Válido para todos os tipos de balancete, ao marcar esta opção os valores das colunas de débitos e créditos serão impressos sem sinal. Observação: Ao habilitar esta opção, a de "Impressão de débitos e créditos respeita o parâmetro de formato de impressão de Saldos" fica desabilitada.

**Alterar título do balancete:** Válido para todos os tipos de balancete. Caso esta opção seja habilitada, poderá ser definido um novo título para o relatório, conforme desejado. Com quantidade máxima de 70 caracteres.

**Inserir texto adicional no final:** Válido para todos os tipos de balancete. Caso habilite esta opção, será permitida a digitação de texto adicional ao final do relatório.

**Inserir observação abaixo do título:** Válido para todos os tipos de balancete. Marcando esta opção, você poderá inserir um texto adicional que sairá impresso no cabeçalho do relatório logo abaixo do título e que poderá ter o tamanho de no Máximo 10 linhas.

**Exibir nome fantasia da filial no cabeçalho:** Marcando esta opção, quando o relatório for impresso será apresentado o nome-fantasia das filiais, caso tenham sido cadastrados. Observação: Este campo somente estará ativos se for selecionada uma ou mais filiais.

**Exibir CNPJ da Filial no cabeçalho:** Marcando esta opção, quando o relatório for impresso para apenas uma filial, será exibido no cabeçalho do relatório o CNPJ da coligada corrente e da Filial. Quando você não marcar esta opção, ou o relatório for impresso para mais de uma filial, será exibido apenas o CNPJ da coligada corrente.

**Utilizar Numeração Sequencial:** Esta opção só ficará habilitada com o Parâmetro "Utilizar Numeração Sequencial de Páginas" marcado. Marque esta opção para que seu relatório obedeça à numeração sequencial informada nos parâmetros do TOTVS Gestão Contábil.

Este recurso auxiliará na emissão de relatórios legais com formatos diferentes em uma única sequência com finalidade de encadernação. Por exemplo, emite-se o Razão da 1ª a 20ª página, logo em seguida emite-se um balancete da página 21ª a 40ª e assim sucessivamente. Desta forma a sequência de página será continua feita automaticamente.

Com esta opção marcada, o campo de N.º Página Inicial assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**Data de Emissão:** Digite a data desejada para constar no cabeçalho do relatório como sendo a data de emissão do mesmo. Você poderá digitar simplesmente a data desejada, ou se preferir, poderá selecioná-la através do ícone que se encontra à frente deste campo. Após a seleção, confirme a data escolhida. A data default deste campo será sempre a data Atual. Dessa forma, a funcionalidade de salvar parâmetro por usuário para relatório para este campo não deve ser considerada. Observação: Se você quiser que no cabeçalho do relatório não seja impressa a data de emissão, você deverá deixar este campo em branco.

**Quantidade de página por arquivo:** Esta opção foi criada para base de dados com grande volume de dados, por que existe uma limitação da quantidade de página que cada máquina consegue processar e exibir. Quando informado a quantidade de páginas por arquivo o relatório será quebrado quando a quantidade informada for atingida tornando possível o processamento e a exibição do relatório.

**Margem Esquerda, Direita, Superior e Inferior:** Esta opção permite que você configure as Margens Direita, Esquerda e Superior do relatório. Você poderá aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 8 para a margem Direita, entre 0 e 15 para margem Esquerda e entre 0 e 10 para margem Superior e inferior.

**Exportar para Arquivo:** Nesta opção estarão disponíveis vários formatos como Word (RTF), PDF, Arquivo texto (TXT), Excel, dentre outros, do qual o usuário poderá utilizar para a exportação do resultado do relatório para seu armazenamento.

**4. Aba Campos**

Nesta aba estão todos os campos existentes e que poderão ser ou não considerados no relatório, basta que selecionado o campo desejado, o mesmo esteja como ícone "Imprimir" habilitado, pois caso contrário o mesmo não será impresso. Nesta aba é possível também alterar o tamanhão dos campos desde que o total de caracteres não ultrapasse o limite que é variável de acordo com cada tipo de relatório.

Existem campos que são padrões em todos os tipos de balancete. São eles: Descrição da conta, saldo anterior, débitos, créditos, movimento, saldo atual. Os outros campos não ficarão ativados todo o tempo, pois, dependem das opções selecionadas. Abaixo serão explicadas suas regras e os tipos de campos a ser habilitado.

Balancete contábil: Campos padrões e código reduzido da conta contábil.

Balancete gerencial: Campos padrões e código reduzido da conta gerencial.

Balancete Contábil/gerencial: Campos padrões e para o código da conta gerencial o usuário pode definir se quer usar o código da conta gerencial ou reduzido.

Balancete gerencial/ Contábil: Campos padrões e para o código da conta contábil o usuário pode definir se quer usar o código da conta contábil ou reduzido.

Balancete Centro de custo/Contábil ou Balancete Contábil/Centro de custo: Campos padrões, código reduzido da conta contábil e Código de centro de custo reduzido.

Se a opção **"Orçamentário"** estiver marcada serão exibidos os campos citados acima e os campos listados abaixo.

**Saldo Anterior %**

Calculo = (Saldo anterior / Orçado no período) \* 100

**Débitos %**

Calculo = (Débito / Orçado no período) \* 100

**Créditos %**

Calculo = (Crédito / Orçado no período) \* 100

**Movimentado %**

Calculo = (Débito – Crédito / Orçado no período) \* 100

**Realizado**

Este campo substituirá o Saldo atual quando a opção Orçamentário estiver marcada. Calculo = Saldo anterior + Débito – Crédito

**Realizados %**

Calculo = (Realizado / Orçado Período) \* 100

**Orçado Período**

Valor orçado no período.

**Orçado – Realizado**

Calculo = Orçado – Realizado

**(Orçado - Realizado) %**

Calculo = (Orçado – Realizado) / Orçado \* 100

**Orçado Total**

Valor orçado para o período informado na opção "Informar período de cálculo para a opção Orçado Total". Esta opção será detalhada mais adiante.

**Orçado Total – Realizado**

Calculo = (Orçado Total – Realizado)

**(Orçado Total – Realizado) %**

Calculo = (Orçado Total – Realizado) / Orçado Total \* 100

Também serão exibidas as seguintes opções:

**Considerar Valor Realizado = Movimento (Déb - Créd)** Este campo, quando marcado, imprime o valor do campo Realizado igual ao valor do Movimento. Desta forma todos os cálculos realizados neste relatório, que utilizam o valor do Realizado, utilizarão o valor do movimento, ou seja, irá desconsiderar o Saldo Anterior e utilizará apenas o Débito + Crédito do período.

**Período de Cálculo para Orçado Total** Através deste campo será possível definir a data inicial e final utilizadas no cálculo do campo Orçado Total. Se o usuário optar por não informar uma data o sistema usará, por padrão, a data inicial do período contábil e a data final informada no intervalo de datas, existente na aba Dados do relatório.

Veja Também

* [Boletim Técnico Balancete Orçamentário](http://tdn.totvs.com/pages/viewpage.action?pageId=189316171)
