---
content_hash: 69e50f2a0cb3945fb08e113b4dd14646eb3d994154fb0788406e84248a82c506
fetched_at: '2026-06-29T00:09:28.527137+00:00'
page_id: '423938698'
product: rm
source: tdn-rm
title: Relatório Balancete - Opções de Impressão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938698
version: 2
---

Nesta etapa de parametrização, existem 3 abas: Opções, Layout e Campos.

**1º) Opções**

**Imprimir / Filtrar:**  
As opções de Imprimir / Filtrar apresentadas na tela do processo de emissão do relatório, variam de acordo com tipo de Balancete selecionado na etapa anterior. Desta forma para cada tipo de Balancete veja quais opções de Imprimir / Filtrar estão disponíveis:

**Balancete contábil:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis, que não possuam movimentação no período, mas que possuam saldo.
* Contas com movimentação e sem saldo: Quando marcado esta opção, as contas que possuírem movimentação no período e que possuam saldo igual a zero serão impressas.
* Contas sem movimentação e sem Saldo: Quando marcado esta opção, todas as contas do seu plano de contas que não tenham movimentação e saldo igual à zero no período informado serão impressas.
* Contas com movimentação e com saldo: Quando marcado esta opção, todas as contas do seu plano de contas que possuírem saldo diferente de zero e movimentação no período informado serão impressas.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

**Balancete Gerencial:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que não possuam movimentação no período, mas que possuam saldo gerencial anterior. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que possuam movimentação no período, mas que possuam saldo igual à zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que não possuam movimentação no período e que possuam saldo igual à zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Contas com movimentação e com saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que possuam movimentação no período e que possuam saldo diferente de zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

**Balancete Contábil/Gerencial ou Balancete Gerencial/Contábil:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que não possuam movimentação no período, mas que possuam saldo, ou ainda, que possuam contas gerenciais informadas como default no Plano de Contas.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que possuam movimentação no período, mas que possuam saldo igual à zero.
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que não possuam movimentação no período e que possuam saldo igual à zero.
* Contas com movimentação e com saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que possuam movimentação no período e que possuam saldo diferente de zero.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.
* Contas com movimentação e sem rateios: Válido para relatórios do tipo Contábil/Gerencial. Quando marcado esta opção, todas as contas do seu plano de contas que não possuírem rateio, mas possuírem movimentação no período informado serão impressas.
* Contas Contábeis sintéticas: Ao habilitar esta opção, serão impressas as contas contábeis sintéticas.   
  **Observação:** Esta opção está disponível apenas para Balancete Gerencial/Contábil.
* Contas gerenciais sintéticas: Ao habilitar esta opção, serão impresso as contas gerenciais sintéticas.   
  **Observação:** Esta opção está disponível apenas Balancete Contábil/ Gerencial.

**Balancete Centro de custo/Contábil ou Balancete Contábil/Centro de custo:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que não possuam movimentação no período, mas que possuam saldo diferente de zero.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que possuam movimentação no período, mas que possuam saldo igual à zero.
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que não possuam movimentação no período e que possuam não saldo igual á zero.
* Contas com movimentação e com saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que possuam movimentação no período e que possuam saldo.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

**Filtros Coligada / Filial / Departamento**

Esta opção permitirá selecionar Coligadas, Filiais cujos dados serão processados e consolidados no relatório. Os Departamentos somente estarão visíveis caso a base esteja parametrizada para usar departamento.  
   
**Todas as Coligadas**

Opção disponível apenas se o parâmetro 'Acessa Contas Globais' estiver marcado.

Marque esta opção para impressão do relatório consolidado. Assim, seu relatório será calculado, levando em conta as contas de todas as coligadas de seu sistema. Não marcando o campo "Todas as coligadas", somente a coligada corrente ficará disponível na opção abaixo.  
   
Obs.: Para a impressão do relatório consolidado para todas as Coligadas, todas as máscara existentes terão de ser iguais para todas as coligadas existentes no sistema.  
   
**Ativar filtro**

Neste campo é possível selecionar as coligadas/ filiais/departamentos deverão ser emitidos no relatório. Para fazer a seleção é necessário clicar no ícone do lookup (...) a frente da descrição Ativar filtro. Será aberta uma janela onde estará visível todas as Coligadas (se o campo Todas Coligadas estiver habilitado), Filiais e Departamentos (Caso o parâmetro usa departamentos esteja habilitado).

A visualização é feita de acordo com a hierarquia de cada campo. Cada coligada visualizada, terá logo abaixo suas respectivas filiais que por sua vez terão seus respectivos departamentos.

**Quebra por página**

* **Quebra por Filial:**Ao habilitar esta opção, o relatório será impresso realizando uma quebra a cada nova filial. Neste caso, os dados de cada filial serão apresentados separadamente no relatório.
* **Quebra por grupo contábil:**Balancete Contábil, Contábil/Centro de Custo: Ao marcar esta opção será realizada uma quebra de página a cada novo grupo contábil apurado.
* **Quebra por grupo gerencial:**Balancete gerencial/contábil: Ao marcar esta opção será realizada uma quebra de página a cada novo grupo gerencial apurado.
* **Quebrar página por centro de custo:**Balancete centro de custo/contábil: Ao marcar esta opção será realizada uma quebra de página ao fim de cada conta contábil vinculado ao centro de custo.   
  Não será gerado quebra de página para os centros de custo que não houver contas com saldo ou movimentação.

**Totalizar**  
   
**Totais da conta sintética embaixo**

Esta opção está disponível para os dois tipos de relatório a seguir:

* **Balancete Contábil:** Quando marcado esta opção, os valores das totalizações das contas contábeis sintéticas serão apresentados ao final de suas contas analíticas, caso contrário, os totais serão apresentados à frente das respectivas contas.
* **Balancete Gerencial:** Quando marcado esta opção, os valores das totalizações das contas gerenciais sintéticas serão apresentados ao final de suas contas gerenciais analíticas, caso contrário, os totais serão apresentados à frente das respectivas contas.

**Totalizar ao final do relatório de débitos e créditos**

Valido para todos os tipos de balancete. Marcando esta opção, a totalização final de débitos e créditos serão impressas.

**Totais das contas sintéticas em cima:**

Esta opção está disponível para o tipo Centro de Custo/Contábil. Marcando esta opção, os valores das totalizações das contas contábeis sintéticas serão apresentados à frente das respectivas contas em cima das demais contas analíticas.

**Por níveis de Centros de Custo em cima:**

Esta opção está disponível para o tipo Centro de Custo/Contábil. Marcando esta opção, os valores das totalizações dos centros de custo serão apresentados em cima das listagens de contas contábeis.  
   
**Por níveis de Centros de Custo embaixo:**

Esta opção está disponível para o tipo Centro de Custo/Contábil. Marcando esta opção, os valores das totalizações dos centros de custo serão apresentados embaixo das listagens de contas contábeis.

**2º) Layout**

**Descrições das contas com tabulação:**

Valido para todos os tipos de balancete. Marcando esta opção, a descrição das contas será impressa respeitando uma tabulação por nível de conta.

**Observação:** Será descontado da descrição o espaço de tabulação.

**Ordens alfabéticas nas contas analíticas**

Marcando esta opção as contas analíticas serão impressas por ordem alfabética respeitando o seu grupo de conta sintético.

**Usar o parâmetro de formato de impressão de saldos para Débito/Crédito**

Valido para todos os tipos de balancete. Marcando esta opção os valores de débito, crédito e movimento serão impressos respeitando o parâmetro de formato de impressão de saldos das contas.

**Observação:** Ao habilitar esta opção, a opção de "não exibir sinais nos valores de débito/ crédito" fica desabilitada.

**Não exibir sinais nos valores de débito/crédito**

Valido para todos os tipos de balancete, ao marcar esta opção os valores das colunas de débitos e créditos serão impressos sem sinal.

**Observação:** Ao habilitar esta opção, a de "Impressão de débitos e créditos respeita o parâmetro de formato de impressão de Saldos" fica desabilitada.

**Alterar título do balancete**

Valido para todos os tipos de balancete. Caso esta opção seja habilitada, poderá ser definido um novo título para o relatório, conforme desejado. Com quantidade máxima de 70 caracteres.

**Inserir texto adicional no final**

Valido para todos os tipos de balancete. Caso habilite esta opção, será permitida a digitação de texto adicional ao final do relatório.

**Inserir observação abaixo do título**

Valido para todos os tipos de balancete. Marcando esta opção, você poderá inserir um texto adicional que sairá impresso no cabeçalho do relatório logo abaixo do título e que poderá ter o tamanho de no Máximo 10 linhas.

**Exibir nome fantasia da filial no cabeçalho**

Marcando esta opção, quando o relatório for impresso será apresentado o nome-fantasia das filiais, caso tenham sido cadastrados.

**Observação:** Este campo somente estará ativos se for selecionada apenas uma filial.

**Exibir CNPJ da Filial no cabeçalho**

Marcando esta opção, quando o relatório for impresso para apenas uma filial, será exibido no cabeçalho do relatório o CNPJ da coligada corrente e da Filial. Quando você não marcar esta opção, ou o relatório for impresso para mais de uma filial, será exibido apenas o CNPJ da coligada corrente.

**3º) Campos**

Nesta aba estão todos os campos existentes e que poderão ser ou não considerados no relatório, basta que selecionado o campo desejado, o mesmo esteja como ícone "Imprimir" habilitado, pois caso contrário o mesmo não será impresso. Nesta aba é possível também alterar o tamanhão dos campos desde que o total de caracteres não ultrapasse o limite que é 117.

Existem campos que são padrões em todos os tipos de balancete. São eles: Descrição da conta, saldo anterior, débitos, créditos, movimento, saldo atual. Os outros campos não ficarão ativados todo o tempo, pois, dependem das opções selecionadas. Abaixo serão explicadas suas regras e os tipos de campos a ser habilitado.

**Balancete contábil:** Campos padrões e código reduzido da conta contábil.

**Balancete gerencial:** Campos padrões e código reduzido da conta gerencial.

**Balancete Contábil/gerencial:** Campos padrões e para o código da conta gerencial o usuário pode definir se quer usar o código da conta gerencial ou reduzido.

**Balancete gerencial/ Contábil:** Campos padrões e para o código da conta contábil o usuário pode definir se quer usar o código da conta contábil ou reduzido.

**Balancete Centro de custo/Contábil ou Balancete Contábil/Centro de custo:** Campos padrões, código reduzido da conta contábil e Código de centro de custo reduzido.
