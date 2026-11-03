---
content_hash: a0f87c88df045759c2b87108a75ece2a469b5d62d29ad5153e1030e1a7573b23
fetched_at: '2026-06-29T00:09:36.050965+00:00'
page_id: '425459462'
product: rm
source: tdn-rm
title: Calcular os Descontos por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459462
version: 21
---

Os Descontos por Antecipação quando cadastrados e devidamente associados serão calculados sobre o valor original do lançamento referente aos serviços que estiverem devidamente marcados para considerarem os descontos nos seguintes momentos:

Na geração (inclusão) de lançamentos

No momento da geração (inclusão) do lançamento, não temos a certeza que o aluno receberá o benefício, muito menos qual item (ou faixa) de desconto será considerado, uma vez que o Desconto por Antecipação somente será concedido mediante a liquidação antecipada, mas como neste momento o sistema precisa calcular todos os valores que irão compor os lançamentos para registrar cada um destes valores nos seus devidos campos, então na geração (inclusão) do lançamento, para compor o valor base para os cálculos, o sistema irá considerar sempre o *maior* desconto a que o aluno tiver direito. Isto é necessário, pois as bolsas do tipo "*Aplicar bolsas em cascata*" (seja a bolsa por contrato ou bolsa por classificação) e do tipo "*Exclusiva*" (para bolsas por classificação), são calculadas somente após a aplicação dos devidos descontos.

O sistema irá calcular o desconto por antecipação se o 'serviço' da parcela estiver parametrizado para considerar desconto por antecipação.

Após selecionar o desconto por antecipação a ser utilizado no cálculo do valor de desconto, o sistema considerará o maior item de desconto calculado, independentemente da data limite calculada com base no dia fixo ou dia útil informado, para compor o valor base para os cálculos de bolsa (veja a regra no tópico "**Cálculo dos valores de bolsas**").

O valor original do lançamento será o valor base para o cálculo dos valores dos itens de desconto.

Após o lançamento da parcela gerado caso o desconto por antecipação sofro algum alteração no cadastro de vigência ou seja desassociado da matriz ou contrato, a parcela deverá ser regerada para que possa ser atualizados as informações do desconto no lançamento.

Para saber qual Desconto por Antecipação será considerado para compor o valor base para os cálculos, na geração (inclusão) do lançamento o sistema irá procurar um desconto por antecipação cuja vigência compreenda a *data de vencimento* da parcela e irá aplicar o *maior* desconto previsto dentro deste agrupamento de descontos.

**Exemplo:**  
Valor do serviço da parcela = 1000,00  
Data de vencimento da parcela = 10/01/2018  
Bolsa 'X' do tipo *Cascata* = 10%  
Vigência do Desconto por Antecipação associado no contrato = 01/01/2018  à  31/12/2018  
  
- Item de desconto 1 = 20% de desconto para pagamento até do dia Fixo = 5  
- Item de desconto 2 = 10% de desconto para pagamento até do dia Fixo = 10

-> Cálculo dos valores do lançamento:  
Valor original: 1000,00  
Bolsa 'X' de 10% = 80,00

-> Memória de cálculo da Bolsa 'X'  
    - Item utilizado para o cálculo do desconto = **Item 1** **= 20%** (pois sempre considera o *maior* desconto a que o aluno terá direito = 20%)  
    - Valor base para cálculo do valor da bolsa *cascata* = **800,00** (1000,00 – 20% desconto antecipação = 800,00)  
    - Valor calculado para a Bolsa 'X' de 10% = **80,00** (800,00 \* 10% = 80,00)  
 **Observação:**O valor do *maior* desconto por antecipação calculado no momento da geração (inclusão) do lançamento '200,00' ficará registrado internamente no banco de dados e receberá uma marcação especial para que o sistema possa utilizá-lo futuramente no momento da baixa, fazendo um confrontamento entre o maior valor previsto para o desconto (200,00) e o valor realmente concedido de desconto que neste caso dependerá diretamente da quantidade de dias em que a baixa estiver sendo realizada antecipadamente. Esta diferença, quando calculada, será apresentada a título de informação no respectivo item de baixa. Para obter mais informações sobre como .

**Importante:**- Para o cálculo de Bolsas do tipo "*Aplicar bolsas em cascata*" (seja a bolsa por contrato ou bolsa por classificação) ou Bolsas do tipo "*Exclusiva*" (para bolsas por classificação)  
- Para o contrato que possuir Bolsas parametrizado do tipo "*Aplicar bolsas em cascata*"  
O sistema utilizará o seguinte valor base para o calculo do desconto por antecipação e bolsa:   
**Valor base** = (Valor original - Valor de desconto da parcela - Valor de desconto por antecipação)  
         O valor base será igual a zero caso o valor calculado seja negativo.  
Para Bolsa do tipo "*Somar bolsas*" ou "*Aplicar somente a maior bolsa*", o sistema calculará o valor de bolsas com base no valor original.

- O *maior* desconto, utilizado para compor o valor base para o lançamento, assim como todos os outros Descontos por Antecipação que estiverem associados no momento da geração (inclusão) do lançamento e que forem aplicáveis ao lançamento serão calculados separadamente e registrados internamente no banco de dados, para que possam ser consultados posteriormente e até mesmo utilizados em relatórios. Após a geração (inclusão) do lançamento, se desejar consultar os valores calculados para todos os descontos por antecipação aplicáveis ao lançamento financeiro da parcela, calculados conforme a data de vencimento de cada desconto, edite o cadastro da parcela e acesse o Anexo *'Descontos por antecipação da parcela'*.  
Todas as vezes que o lançamento financeiro de uma parcela for *regerado*, o sistema tornará a calcular os possíveis descontos por antecipação aplicáveis à parcela conforme cada data de vencimento indicada nos itens (ou faixas) de descontos e os gravará novamente no banco de dados.

Na Baixa dos lançamentos

Na baixa de lançamento financeiro proveniente do TOTVS Educacional, o desconto por antecipação poderá ser concedido para o aluno conforme as regras cadastradas nos itens do desconto por antecipação. O desconto por antecipação será efetivamente concedido para o aluno na baixa do lançamento, mas somente na baixa *total* do valor a ser pago. A ordem de verificação para conceder o desconto por antecipação na baixa de lançamento é:

* Contrato.
* Campus/Polo da Matriz Aplicada (Somente para Ensino Superior).
* Matriz Aplicada.

Desta forma, para conceder os Descontos por Antecipação aos alunos, o sistema sempre procurará pelos descontos que tiverem associados na seguinte ordem: primeiro procurará pelos descontos associados nos contratos dos alunos e os aplicará, caso não existam Desconto por Antecipação associados nos contratos, irá procurar por Descontos por Antecipação associados aos campus/polo das matrizes aplicadas às quais pertencem e os aplicará, caso não encontre, irá por último, procurar pelos Descontos por Antecipação associados às matrizes aplicadas às quais pertencem e os aplicará.

A data da baixa do lançamento financeiro será a data base para cálculo do desconto. E para os itens do desconto por antecipação do tipo percentual, o valor original do lançamento será o valor base para o cálculo.

Exemplo:

Um aluno possui um desconto por antecipação associado ao seu contrato com a seguinte regra:

* Pagamento até o dia 10 = R$ 100,00
* Valor da mensalidade de R$ 1000,00

O aluno tem um lançamento financeiro com valor original de R$ 1000,00 (valor da mensalidade), e com data de vencimento no dia 11/01/2018. O aluno realizou o pagamento do lançamento no dia 10/01/2018. O sistema irá calcular um valor de desconto por antecipação de R$ 100,00. E o valor a ser pago pelo aluno será de R$ 900,00.

Lançamento financeiro com data de vencimento no dia 11/01/2018 e com data de baixa no dia 10/01/2018:

Valores calculados na baixa no dia 10/01/2018:

Os lançamentos financeiros que **não** terão o Desconto por Antecipação concedidos para os alunos são:

* Lançamento financeiro de parcela onde o Serviço não irá considerar o desconto por antecipação.
* Lançamento financeiro com pagamento parcial do valor a ser pago, isto é, com a realização de uma baixa parcial.
  + Exemplos:  
    ( Desconto por antecipação não concedido )
  + A) Lançamento financeiro 1:
    - Valor original de R$ 1000,00
    - Valor desconto por antecipação de R$ 100,00
    - Valor restante a ser pago de R$ 900,00
    - Se o aluno realizar o pagamento no valor de R$ 500,00, ou seja, se  realizar uma baixa parcial, o desconto por antecipação não será concedido para o aluno, e o valor restante a ser pago será de R$ 500,00.( Desconto por antecipação concedido )
  + B) Lançamento financeiro 2:
    - Valor original de R$ 1000,00
    - Valor desconto por antecipação de R$ 100,00
    - Valor restante a ser pago de R$ 900,00
    - Se o aluno realizar a baixa do lançamento financeiro no valor de R$ 900,00, valor total a ser pago, o desconto por antecipação será concedido para o aluno.
* Lançamento financeiro com pagamento a menor via retorno bancário ou via baixa manual.
  + Valor original de R$ 1000,00
  + Valor desconto por antecipação de R$ 100,00
  + Valor restante a ser pago de R$ 900,00
  + Valor de integração configurado para registrar pagamentos a menor = 'Pgto a Menor'
  + O valor pago pelo aluno presente no arquivo de retorno bancário é de R$ 800,00. Na importação do arquivo de retorno bancário o desconto por antecipação *não* será concedido para o aluno, visto que o aluno realizou um pagamento a menor que o valor a ser pago (como se tivesse feito uma baixa parcial) . Desta forma, o desconto por antecipação *não* será considerado e o campo de valor de integração 'Pgto a Menor' configurado para registrar pagamentos a menor terá o valor da diferença entre o valor original e o valor pago, presente no arquivo de retorno bancário, que nesse exemplo é de R$ 200,00.

+ Exemplo:
+ A) Lançamento financeiro 3:
+ Observação: O pagamento a maior via retorno bancário não teve alteração no seu comportamento.

* Lançamentos de Acordo:

+ Os lançamentos oriundos do Educacional baixados pelo processo de Acordo, **caso estejam vencidos na data em que o acordo é realizado**, assim como os respectivos lançamentos gerados pelo processo de Acordo, **não** terão o Desconto por Antecipação aplicados.
Bolsa Condicional X Desconto Por Antecipação

Como observado acima, o valor de bolsa poderá ser calculado depois de aplicar o desconto por antecipação e, claro, isto vai depender da parametrização.

Existindo algum desconto por antecipação associado ao aluno, por padrão o sistema ao gerar o lançamento vai considerar o maior valor de desconto por antecipação calculado para calcular o valor da bolsa e, durante a baixa, independente da data de pagamento, o valor da bolsa não será alterado.

Dica:

É possível parametrizar o sistema para que durante a baixa o Educacional recalcule o valor da bolsa conforme o desconto por antecipação concedido, neste caso o valor da bolsa irá variar conforme o valor de pagamento.

**Exemplo:**

Parcela: 1000.00

Desconto por antecipação:

* Pagamento até dia  05 => 50%
* Pagamento até dia  15 => 5%

Bolsa Condicional (Considera o desconto):

* Bolsa você merece => 10%

Cenários:

* Se o aluno efetuar o pagamento no dia 05, o valor da bolsa será de:

1000,00 (Vlr Parcela) - 500,00 (Desconto Antecipação) = 500,00 (Vlr pagamento) = **50,00** (Vlr Bolsa de 10 %)

* Se o aluno efetuar o pagamento no dia 15, o valor da bolsa será de:

1000,00 (Vlr Parcela) - 50,00 (Desconto Antecipação) = 950,00 (Vlr pagamento) = **95,00** (Vlr Bolsa de 10 %)

Observe que o valor da bolsa varia conforme o valor de pagamento.

**Requisitos para utilizar este recurso:**

* Funcionará somente para bolsas condicionais
* O sistema deve estar parametrizado para processar o valor da bolsa condicional por fórmula
* Na fórmula deverá ser utilizada a função de fórmula VLRBOLSALANDESCANTPORDTBAIXA ou VLRBOLSALANDESCANT (*Veja no final deste documento como utilizar estas formulas*)

  Bolsa Condicional Condicionada ao Desconto Por Antecipação

  Conforme visto no início deste documento é possível condicionar a bolsa ao pagamento de qualquer desconto por antecipação, ou seja, se o aluno efetuar o pagamento no dia 05 ele ganha a bolsa, senão, ele perde a bolsa.

  Para que esta regra funcione, o cálculo da bolsa deverá ser realizado por fórmula no momento da baixa.
Dia útil para descontos com dia fixo

Quando o sistema for processar o desconto por antecipação que estiver parametrizado como da fixo será respeitado para a data limite do vencimento do desconto por padrão o primeiro dia útil posterior. Respeitando o calendário do sistema se o dia fixo for correspondente a sábado, domingo ou feriado, o sistema irá considerar o próximo dia útil.

Esta mesma regra será levada em consideração nas informação que serão gravadas na tabela SLANDESCPONTUAL durante a geração do lançamento.

Na simulação dos valores da parcela

Ao simular o valor para uma determinada parcela, o sistema criará na visão novas colunas contendo cada uma o valor do respectivo desconto por antecipação calculado conforme a data de vencimento da parcela e data de vigência do desconto por antecipação. Ao posicionar o cursor do mouse sobre o valor do desconto apresentado na tela, o sistema mostrará a data limite à qual o aluno terá direito ao desconto.

O valor líquido apresentado na simulação irá sempre considerar o valor do *maior* desconto por antecipação.

Caso o valor original - valores de descontos - valores de bolsas resulte em um valor negativo, esse valor negativo calculado será apresentado na simulação.

A simulação levará em consideração a data de vencimento da parcela para a data base do cálculo do valor dos descontos por antecipação.

**Importante:**   
Os Descontos por Antecipação **não** serão calculados nas seguintes situações:  
- Em lançamentos financeiros de contratos gerados por Acordo.  
- Em lançamentos financeiros baixados por Acordo.  
- Em lançamentos financeiros de parcelas onde o [serviço](http://fwrm-wiki:9999/WikiHelp/EDU/EDU.servicos.aspx) estiver parametrizado para não considerar o desconto por antecipação.  
- Em lançamentos financeiros de parcelas onde o [contrato](http://fwrm-wiki:9999/WikiHelp/EDU/EDU.contratos.aspx) estiver parametrizado para não considerar o desconto por antecipação.  
- Em baixas de lançamentos financeiros vencidos.  
- Em baixas *parciais* realizadas manualmente ou através de retorno bancário.  
- Em baixas com *pagamento a menor* realizadas manualmente ou através de retorno bancário.

**Atenção**  
Os descontos por antecipação serão aplicados de acordo com o tipo de limite de desconto definido em seu cadastro.  
Para os itens de tipo de limite "Dia Útil" o desconto só será aplicável até o dia útil definido. Também é possível definir o tipo de limite para "Dia Fixo", nesse caso o desconto por antecipação será aplicável de acordo com a parametrização do financeiro: (Contas a Receber >> Baixas >> Manutenção de Baixas >> Baixa a Receber) "Aceita Baixa a Receber em Finais de Semana e Feriados".   
Opções:  
- Manter mesmo dia: A data limite do cálculo do desconto por antecipação será a mesma do dia fixo, independente se é fim de semana ou feriado;  
- Primeiro dia útil posterior: Respeitando o calendário do sistema, quando o dia fixo cair em um fim de semana ou feriado, o sistema irá considerar o próximo dia útil;  
- Primeiro dia útil anterior: Respeitando o calendário do sistema, quando o dia fixo cair em um fim de semana ou feriado, o sistema irá considerar o dia útil anterior.

* O valor líquido apresentado na visão considerará o maior valor do desconto por antecipação apresentado.
* A simulação levará em consideração a data de vencimento para a data base do cálculo do valor de desconto.
* A data limite para conceder o desconto por antecipação será apresentada através de um hint ao posicionar o cursor do mouse sobre o vencimento desejado.
Desconto por Antecipação das Parcelas / Lançamentos

Na tela de Desconto por Antecipação as Parcelas / Lançamentos é possível visualizar os valores calculados para o desconto por antecipação durante a geração do lançamento financeiro vinculado na parcela do contrato. E através do anexo "Cálculo da bolsa condicional conforme o desconto por antecipação" é possível visualizar dos valores calculados para as bolsas condicionais vinculadas ao contrato conforme o desconto por antecipação.

Os descontos por antecipação podem ser visualizados também pelo anexo "Desconto por Antecipação da parcela" presente na tela da parcela.

Alterar Vencimento do Desconto por Antecipação do Lançamento

Em função de alguma eventualidade poderão haver necessidades pontuais de alterar os vencimentos do descontos por antecipação que já foram processados para o lançamento.

Por exemplo:

Descontos por antecipação original:

* 1º - Até o dia 05 – 30 %
* 2º - Até o dia 10 – 20 %
* 3º - Até o dia 20 – 5 %

Supondo que do dia 04 ao dia 05 ocorreram instabilidade no portal do aluno no recebimento via cartão, neste caso a instituição irá prorrogar o vencimento do 1º desconto para o dia 08.

A realização da alteração deste vencimento deverá ser realizada através do processo “Alterar Vencimento do Desconto por Antecipação do Lançamento”.

Disponível em:

Crie um filtro que selecione as informações (parcelas, contratos...) dos alunos que terão os vencimentos dos desconto alterados. Este filtro tem o objetivo de facilitar e flexibilizar a seleção de dados de uma forma genérica.

O campo "Exibir os descontos por antecipação inativos" como padrão está marcado para exibir os descontos por antecipação inativos.

Após a seleção do filtro clique em “Carregar vencimentos dos descontos por antecipação”.

Após o processamento, serão apresentadas na aba “Alteração dos vencimentos” as informações dos vencimentos dos descontos por antecipação identificados através do filtro.

As informações serão apresentadas agrupadas pelo agrupador do desconto e vencimentos das parcelas. Para cada agrupador serão mostrados os descontos processados para a parcela. Preencha na coluna em destaque a data correspondente ao novo vencimento.

Como as informações serão apresentadas agrupadas, foi disponibilizado a opção “Pré-visualizar Aluno(s)”. Está opção apresenta todos os alunos que fazem parte do agrupamento da linha em questão e que terá o vencimento do desconto alterado.

Após o preenchimento da data correspondente ao novo vencimento, clique em executar o processo. O processo irá informar os descontos por antecipação que poderão ser desativados após a execução do processo.

Ao final da execução o será apresentado um log com as informações do processo e quais os alunos tiveram o vencimento alterado.

Importante

Importante

* O processo altera pontualmente o vencimento somente dos descontos processados para as parcelas / lançamentos filtrados no processo (tabela SLANDESCPONTUAL), ou seja, o cadastro oficial do desconto por antecipação não é alterado.
* Na geração dos lançamentos do mês seguinte o sistema respeitará o cadastro oficial do desconto que estiver vinculado à matriz ou ao contrato do aluno.
* Caso o lançamento que teve o vencimento do desconto alterado seja regerado o sistema vai reprocessar os descontos por antecipação considerando os desconto do cadastro oficial, ou seja, a alteração do vencimento é perdida.
Data do novo vencimento do desconto sobrepondo outros vencimentos

Dependendo da data do novo vencimento, a mesma poderá sobrepor a data de outros vencimentos.

Por exemplo:

Descontos por antecipação original:

* 1º - Até o dia 05 – 30 %
* 2º - Até o dia 10 – 20 %
* 3º - Até o dia 20 – 5 %

Supondo que do dia 04 ao dia 05 ocorreram instabilidade no portal do aluno no recebimento via cartão, neste caso a instituição irá prorrogar o vencimento do 1º desconto para o dia 10/05.

Observem que o dia 10/05 é quando finaliza o 2º vencimento, para este cenário o sistema realizará a alteração do 1º vencimento para o dia 10/05 e o 2º vencimento será inativado.

Visualização dos Descontos

Os descontos processados para as parcelas / lançamentos poderão ser consultados através do menu “Financeiro/Contábil >> Desconto por Antecipação das Parcelas / Lançamento” e a mesma informação também está disponível no anexo da parcela do contrato.

Através da visualização destes dados é possível consultar a data do vencimento original (preenchida somente quando for alterada), se o desconto está ativo e qual usuário realizou a alteração.

Lançamentos de Acordo

Os lançamentos oriundos do Educacional baixados pelo processo de Acordo, **caso estejam vencidos na data em que o acordo é realizado**, assim como os respectivos lançamentos gerados pelo processo de Acordo, **não** terão o Desconto por Antecipação aplicados.
