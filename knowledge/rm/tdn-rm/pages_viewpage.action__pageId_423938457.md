---
content_hash: fdc4b6d765e1972d63656bc0ac5f652cb19d1900f6382ef42abc30385c4ff9b3
fetched_at: '2026-06-29T00:09:27.237288+00:00'
page_id: '423938457'
product: rm
source: tdn-rm
title: Identificação - Eventos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938457
version: 6
---

Ao acessar uma das opções, Incluir ou Editar, o sistema abrirá uma janela de edição com todos os dados do Evento Contábil a ser incluído ou editado.

Para a identificação do evento contábil são apresentados os seguintes campos:

**Processo:**   
Informe para qual processo se aplicará este evento contábil.

**Inativo:**   
Com essa opção marcada, o evento contábil fica "Inativo", ou seja, ele não é apresentado em nenhum cadastro que utilize eventos contábeis.

**Número:**   
Informe o número do evento contábil a ser incluído.   
Esse número será o "código" do evento contábil.

**Nome:**   
Informe o nome do evento contábil a ser incluído.

**Calcular Valor a Partir de:**   
Defina como o evento contábil irá calcular o valor do lançamento, a partir de uma "Fórmula" ou de "Percentual".

**Fórmula:**   
Marque esta opção se desejar utilizar fórmulas para obter o valor contábil.   
Ao incluir os Itens de Evento, será apresentado o campo "Fórmula" para que o sistema calcule os valores do lançamento a partir da fórmula indicada.

**Percentual:**   
Marque esta opção se desejar utilizar percentuais para obter o valor contábil. Ao incluir os Itens de Evento, será apresentado o campo "Percentual" para que o sistema calcule os valores do lançamento a partir do percentual indicado.

**Buscar Filial/Departamento em:**   
Marque de onde o evento contábil irá buscar a Filial/Departamento para o preenchimento da contabilização assim como a prioridade da busca.

Ao marcar somente uma opção para busca, ela será automaticamente levada para a primeira posição da lista. Se for selecionada mais de uma opção, deve-se informar também a prioridade da busca, ou seja, se não for encontrada a Filial/Departamento na primeira opção o sistema irá buscá-la na segunda opção e assim sucessivamente.

Entende-se por prioridade a ordem em que as opções marcadas ficarão dispostas. Para mudar a ordem/prioridade, selecione a opção e em seguida utilize os botões de movimentação para cima ou para baixo.

**Observação**   
Quando a opção "Buscar Filial/Depto em" for igual a "Evento Contábil" e não utilizar prioridade, o campo "Filial" localizado na Pasta Dados Complementares dos itens de evento deverá ser preenchido.

**Buscar Centro de Custo em:**   
Marque de onde o evento contábil irá buscar o Centro de Custo para o preenchimento da contabilização assim como a prioridade da busca.

Ao marcar somente uma opção para busca, ela será automaticamente levada para a primeira posição da lista. Se for selecionada mais de uma posição, deve-se informar também a prioridade da busca, ou seja, se não for encontrado o Centro de Custo na primeira opção o sistema irá buscá-lo na segunda opção e assim sucessivamente.

Entende-se por prioridade a ordem em que as opções marcadas ficarão dispostas. Para mudar a ordem/prioridade, selecione a opção e em seguida utilize os botões de movimentação para cima ou para baixo.

**Aplicar Centro de Custo em:**Informe onde será aplicado o centro de custo do lançamento contábil.

**Agrupa Rateio Contábil:**   
Opção disponível para todos os processos! Marque este campo se desejar que o sistema agrupe os valores de mesma conta do lançamento.

**Observação**   
Marcando este campo, o sistema ainda irá consistir se as contas pertencem à mesma Filial. Centro de Custo, Departamento e Histórico Padrão. Do contrário não irá agrupar os valores.

**Exemplo**   
\*Contabilização de um lançamento com a opção "Agrupa Rateio Contábil" *desmarcada*:   
Foi criado um evento contábil com os seguintes itens de evento:  
  
Itens de Evento - Débito **Conta       Valor         Filial   Depto   C.Custo  Histórico**   
1º item 1.1.1.1.000     valor original    01          01           01              01   
2º item 1.1.1.1.001     juros                 01          01           01              01   
3º item 1.1.1.1.002     desconto          01          01           01              01

4º item 1.1.1.1.003 valor Op4 01 01  01  01

Itens de Evento - Crédito **Conta       Valor         Filial    Depto   C.Custo  Histórico**   
1º item 2.1.1.1.001     Valor original     01          01           01             01   
2º item 2.1.1.1.004     Juros                 01          01           01             01   
3º item 2.1.1.1.001     Desconto           01          01           01             01   
4º item 2.1.1.1.001     Valor Op4          01          01           01             01

Vamos supor um processo que utilize os seguintes dados:  
Valor original: 100,00   
Juros: 1,50   
Desconto: 3,00   
Valor Op4: 20,00

O lançamento contábil gerado por este evento será:    
Partidas a Débito:   
Conta contábil: 1.1.1.1.000 Valor: 100,00   
Conta contábil: 1.1.1.1.001 Valor: 1,50   
Conta contábil: 1.1.1.1.002 Valor: 3,00   
Conta contábil: 1.1.1.1.003 Valor: 20,00     
  
Partidas a Débito:   
Conta contábil: 2.1.1.1.001 Valor: 100,00   
Conta contábil: 2.1.1.1.004 Valor: 1,50   
Conta contábil: 2.1.1.1.001 Valor: 3,00   
Conta contábil: 2.1.1.1.001 Valor: 20,00

\*Contabilização de um lançamento com a opção "Agrupa Rateio Contábil" *marcada*:

Utilizando o mesmo evento contábil com os mesmo dados.

Será gerada a seguinte contabilização:  
Partidas a Débito:  
Conta contábil: 1.1.1.1.000 Valor: 100,00   
Conta contábil: 1.1.1.1.001 Valor: 1,50   
Conta contábil: 1.1.1.1.002 Valor: 3,00  
Conta contábil: 1.1.1.1.003 Valor: 20,00

Partidas a Crédito:   
Conta contábil: 2.1.1.1.001 Valor: 123,00   
Conta contábil: 2.1.1.1.004 Valor: 1,50

\*Contabilização de um lançamento com a opção "Agrupa Rateio Contábil" marcada e uma das contas com um dado diferente:

Utilizando o mesmo evento contábil. No evento contábil apenas a última conta possui um dado diferente, ou seja, o departamento de todas as contas é "01" e somente o da última conta é "02".

O lançamento contábil gerado por este evento será:    
Partidas a Débito:   
Conta contábil: 1.1.1.1.000 Valor: 100,00   
Conta contábil: 1.1.1.1.001 Valor: 1,50   
Conta contábil: 1.1.1.1.002 Valor: 3,00   
Conta contábil: 1.1.1.1.003 Valor: 20,00

Partidas a Crédito:   
Conta contábil: 2.1.1.1.001 Valor: 103,00  
Conta contábil: 2.1.1.1.004 Valor: 1,50   
Conta contábil: 2.1.1.1.001 Valor: 20,00

**Fechar percentual com valor contábil:**   
Esta opção NÃO estará disponível para todos os processos! Nos casos em que o cálculo da contabilização for por percentual, marque esta opção para indicar que a soma das partidas geradas a débito ou a crédito deve ser igual ao valor contábil.

**Exemplo**   
Vamos supor o seguinte evento contábil:   
Calcular valor a partir de: "Percentual".

Itens de Evento – Débito:   
1º item - Buscar default no débito da tabela cli/for e lançar como débito, percentual = 100.   
2º item - Buscar default no débito da tabela natureza e lançar como débito, percentual = 100

Item de Evento – Crédito:   
1º item – Informar a conta "1.1.1.001" com percentual = 100.

No cadastro de cli/for, para o fornecedor F00001, está informado como conta default de débito:

2.1.1.001 - percentual 20. No cadastro de naturezas, para a natureza 1.11.03, está informado como conta débito: 2.1.1.003 - percentual 30

Vamos supor uma entrada no sistema utilizando este evento com valor contábil = 1000,00, neste caso:  
Se o campo "Fechar percentual com valor contábil" estiver desmarcado, os valores contabilizados serão:   
Débito:   
2.1.1.001 - valor 200,00 (20% de 1000,00)   
2.1.1.003 - valor 300,00 (30% de 1000,00)

Crédito:   
2.1.1.003 - valor 1000,00 (100% de 1000,00)

Neste caso, não seria possível a esta inclusão no sistema, pois os valores de débitos e créditos não estão fechando, você deveria informar manualmente nova(s) conta(s) a débito para que o valor fechasse em 1000,00.

Se o campo "Fechar percentual com valor contábil" estiver marcado, os valores contabilizados serão:  
Débito:   
2.1.1.001 - valor 200,00 (20% de 1000,00)   
2.1.1.003 - valor 800,00 (valor restante para fechar valor contábil)

**Observação**

Neste caso, na última conta a ser contabilizada, o sistema contabiliza o que resta para se chegar ao valor contábil, que no nosso exemplo é 1000,00. Como na primeira conta foi contabilizado, de acordo com o percentual, o valor de 200,00 na segunda conta serão contabilizados os 800,00 restantes.   
Crédito:   
2.1.1.003 - valor 1000,00 (100% de 1000,00)   
O valor de crédito continuaria inalterado.

**Consistir percentuais do default contábil:**

Esta opção NÃO estará disponível para todos os processos!

Marcando esta opção e selecionando no campo "Origem da conta" a opção "Default tabelas", o percentual somado das contas contábeis informadas no default não poderá ultrapassar 100%. Caso ultrapasse, os lançamentos contábeis não serão gerados para todas as contas do default contábil.

**Observação**   
Se o parâmetro "Consistir percentuais do default contábil" do Evento Contábil for habilitado e Origem da Conta for Default tabela, o último item do lançamento contábil será ajustado para totalizar 100% do Valor Contábil Total.

A finalidade deste parâmetro é evitar erro na ordem de décimos (dízimas periódicas) por isto é aplicado apenas para a última conta. Este parâmetro já era válido quando calculando por Fórmula, passa a ser válido também quando calculando por Percentual.
