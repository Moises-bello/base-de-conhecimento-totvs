---
content_hash: 2d8723ac5429ff6304bfcc0860cffe705098ce4b19934421db243e8e02bb0a01
fetched_at: '2026-06-29T00:09:27.861531+00:00'
page_id: '423938545'
product: rm
source: tdn-rm
title: Aba Dados - Balancete
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Dados+-+Balancete
version: 13
---

CardsPeríodo de datas

**Data Inicial / Final:** Informe a faixa de datas desejada para a impressão do Balancete. Estas datas poderão estar dentro do Período Contábil vigente ou não, basta que para uma data anterior ao período, seja marcada a opção "Buscar do Histórico contábil".

O campo data será carregado automaticamente com a última data informada no Relatório, salvo nas preferências.

Ao lado do campo data, que pode ser utilizado a opção "filtro automático de datas" que possibilita retornar os períodos fixos (Semanal, Mensal, Bimestral, Trimestral, Semestral, Anual) e aplica-lo como período do Balancete.

**Buscar do Histórico Contábil:** Esta opção permite a impressão do Relatório Balancete baseando o resultado em datas anteriores ao período contábil. Desta forma deve ser informado uma data que seja anterior ao inicio do período contábil. ( Exemplo: Período Contábil = 01/01/2009 á 31/12/2013. A data a ser informada deve ser inferior a 31/12/2008.)

**Basear na Data de Cotação:** Esta opção permite a impressão dos valores baseando na data da cotação dos lançamentos. Marcando esta opção, o sistema buscará os lançamentos que possuírem a data da cotação dentro do período informado no intervalo de datas.  
Observação: Esta opção somente será visualizada nesta janela, se nos "Parâmetros/Lançamentos" a opção "Usa segundo valor" estiver marcada e for informada uma moeda no parâmetro "Símbolo moeda 2º valor".

Filtros Coligada / Filial / Departamento

Esta opção permitirá selecionar Coligadas, Filiais cujos dados serão processados e consolidados no relatório. Os Departamentos somente estarão visíveis caso a base esteja parametrizada para usar departamento.  
   
**Todas as Coligadas**

Opção disponível apenas se o parâmetro 'Acessa Contas Globais' estiver marcado.

Marque esta opção para impressão do relatório consolidado. Assim, seu relatório será calculado, levando em conta as contas de todas as coligadas de seu sistema. Não marcando o campo "Todas as coligadas", somente a coligada corrente ficará disponível na opção abaixo.  
   
Obs.: Para a impressão do relatório consolidado para todas as Coligadas, todas as máscara existentes terão de ser iguais para todas as coligadas existentes no sistema.  
   
**Ativar filtro:** Neste campo é possível selecionar as coligadas/ filiais/departamentos deverão ser emitidos no relatório. Para fazer a seleção é necessário clicar no ícone do lookup (...) a frente da descrição Ativar filtro. Será aberta uma janela onde estará visível todas as Coligadas (se o campo Todas Coligadas estiver habilitado), Filiais e Departamentos (Caso o parâmetro usa departamentos esteja habilitado). A visualização é feita de acordo com a hierarquia de cada campo. Cada coligada visualizada, terá logo abaixo suas respectivas filiais que por sua vez terão seus respectivos departamentos.

Tipo de Balancete

Para emissão do balancete, deve ser escolhido um tipo para o mesmo dentre as opções a seguir:

* **Contábil**: Processamento do relatório por saldo da conta contábil.
* **Gerencial:** Processamento do relatório por saldo gerencial.
* **Contábil/Gerencial:** Processamento do relatório por saldo da conta contábil, quebrando por saldo gerencial.
* **Gerencial/Contábil:** Processamento do relatório por saldo gerencial, quebrando por saldo da conta contábil.
* **Contábil/Centro de Custo:** Processamento do relatório por saldo da conta contábil, quebrando por saldo de Centro de Custo.
* **Centro de Custo/Contábil:** Processamento do relatório por saldo de Centro de Custo, quebrando por saldo da conta contábil.
Imprimir / Filtrar

As opções de Imprimir / Filtrar apresentadas na tela do processo de emissão do relatório, variam de acordo com tipo de Balancete selecionado na etapa anterior. Desta forma para cada tipo de Balancete veja quais opções de Imprimir / Filtrar estão disponíveis:

**Balancete contábil:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis, que não possuam movimentação no período, mas que possuam saldo.
* Contas com movimentação e sem saldo: Quando marcado esta opção, as contas que possuírem movimentação no período e que possuam saldo igual a zero serão impressas.
* Contas sem movimentação e sem Saldo: Quando marcado esta opção, todas as contas do seu plano de contas que não tenham movimentação e saldo igual ao zero no período informado serão impressas.
* Contas com movimentação e com saldo: Quando marcado esta opção, todas as contas do seu plano de contas que possuírem saldo diferente de zero e movimentação no período informado serão impressas.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

**Balancete Gerencial:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que não possuam movimentação no período, mas que possuam saldo gerencial anterior. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que possuam movimentação no período, mas que possuam saldo igual ao zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que não possuam movimentação no período e que possuam saldo igual ao zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Contas com movimentação e com saldo: Quando marcada, permitirá que sejam impressas todas as Contas gerenciais, que possuam movimentação no período e que possuam saldo diferente de zero. Essa opção em momento nenhum considera conta contábil apenas conta gerencial.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

**Balancete Contábil/Gerencial ou Balancete Gerencial/Contábil:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que não possuam movimentação no período, mas que possuam saldo, ou ainda, que possuam contas gerenciais informadas como default no Plano de Contas.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que possuam movimentação no período, mas que possuam saldo igual ao zero.
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que não possuam movimentação no período e que possuam saldo igual ao zero.
* Contas com movimentação e com saldo:  Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupada por conta gerenciais que possuam movimentação no período e que possuam saldo diferente de zero.
* Não exibir contas inativas sem movimentação e sem saldos: Valido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.
* Contas com movimentação e sem rateios: Válido para relatórios do tipo Contábil/Gerencial. Quando marcado esta opção, todas as contas do seu plano de contas que não possuírem rateio, mas possuírem movimentação no período informado serão impressas.
* Contas Contábeis sintéticas: Ao habilitar esta opção, serão impressas as contas contábeis sintéticas.
* Contas gerenciais sintéticas: Ao habilitar esta opção, serão impressas as contas gerenciais sintéticas.

**Balancete Centro de custo/Contábil ou Balancete Contábil/Centro de custo:**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que não possuam movimentação no período, mas que possuam saldo diferente de zero.
* Contas com movimentação e sem saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que possuam movimentação no período, mas que possuam saldo igual à zero.
* Contas sem movimentação e sem Saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que não possuam movimentação no período e que possuam não saldo igual á zero.
* Contas com movimentação e com saldo: Quando marcada, permitirá que sejam impressas todas as Contas Contábeis agrupadas por centro de custo que possuam movimentação no período e que possuam saldo.
* Não exibir contas inativas sem movimentação e sem saldos: Válido para todos os tipos de balancete. Ao marcar esta opção, todas as contas inativas e sem saldo e sem movimentação do seu plano de contas no período informado não serão impressas.

Performance do relatório

A opção **"****Contas sem movimentação e sem Saldo"** marcada faz com que todas as contas contábeis sejam retornadas no processamento do relatório, o que pode ser um ofensor na performance dependendo da quantidade de contas existentes na base de dados. Caso não seja necessário, recomendados que essa opção não seja marcada juntamente com as outras disponíveis.   
Para uma melhor avaliação dessas contas em específico, sugerimos que essa opção seja sempre utilizada de forma isolada.

Lote

* Permite filtrar um ou mais Lotes, sendo Zero ou Lote N.
* Serão considerados todos os registros que estiverem nos lotes informados pelo usuário.
* Apenas os lotes das coligadas selecionadas no filtro de coligada estarão disponíveis para seleção.
* Quando a opção de histórico contábil for marcada, o filtro por lote será desabilitado e será considerado o lote 0.
* Um aviso será exibido para que o usuário decida se prossegue ou não com a alteração.
* Se informou lote que não o Lote 0, não serão exibidos os saldos anteriores de períodos já liberados de contas sem movimentação após a liberação e antes da data inicial de movimentação informada.
* Caso nenhum lote seja informado no filtro será considerado o lote 0.
Totalizar

**As opções de Totalizar apresentadas na tela do processo de emissão do relatório, variam de acordo com tipo de Balancete selecionado na etapa anterior. Desta forma para cada tipo de Balancete veja quais opções estão disponíveis:**

**Balancete contábil ou Balancete Gerencial ou Balancete Contábil/Gerencial ou Balancete Gerencial/Contábil:**Totais da conta sintética embaixo:

* Obs. Balancete Contábil: Quando marcado esta opção, os valores das totalizações das contas contábeis sintéticas serão apresentados ao final de suas contas analíticas, caso contrário, os totais serão apresentados à frente das respectivas contas.  
  Obs. Balancete Gerencial: Quando marcado esta opção, os valores das totalizações das contas gerenciais sintéticas serão apresentados ao final de suas contas gerenciais analíticas, caso contrário, os totais serão apresentados à frente das respectivas contas.

**Válido para todos os tipos de balancete**Totalização no final do Relatório de Débitos e Créditos: Ao selecionar esta opção, o total geral de débitos e créditos será impresso.

**Balancete Centro de custo/Contábil ou Balancete Contábil/Centro de custo:**  
Totais das contas sintéticas em cima: Marcando esta opção, os valores das totalizações das contas contábeis sintéticas serão apresentados à frente das respectivas contas em cima das demais contas analíticas.  
Por níveis de Centros de Custo em cima: Marcando esta opção, os valores das totalizações dos centros de custo serão apresentados em cima das listagens de contas contábeis.  
Por níveis de Centros de Custo embaixo: Marcando esta opção, os valores das totalizações dos centros de custo serão apresentados embaixo das listagens de contas contábeis.

Quebrar página 

**Quebra por Filial:** Ao habilitar esta opção, o relatório será impresso realizando uma quebra a cada nova filial. Neste caso, os dados de cada filial serão apresentados separadamente no relatório.

**Quebra por grupo contábil:** Balancete Contábil, Contábil/Centro de Custo: Ao marcar esta opção será realizada uma quebra de página a cada novo grupo contábil apurado.

**Quebra por grupo gerencial:** Balancete gerencial/contábil: Ao marcar esta opção será realizada uma quebra de página a cada novo grupo gerencial apurado.

**Quebrar página por centro de custo:** (Balancete centro de custo/contábil) Ao marcar esta opção será realizada uma quebra de página ao fim de cada conta contábil vinculado ao centro de custo. Não será gerado quebra de página para os centros de custo que não houver contas com saldo ou movimentação
