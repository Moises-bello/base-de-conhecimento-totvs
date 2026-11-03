---
content_hash: ddb93b15eff6fb923c6d9cf520ceac3ac8e2456261682616dbc3c44aa647368f
fetched_at: '2026-06-29T00:09:32.671983+00:00'
page_id: '425458898'
product: rm
source: tdn-rm
title: Contabilização por Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458898
version: 50
---

---

**Contabilização por competência** é a que apropria [receitas](http://pt.wikipedia.org/wiki/Receita_%28economia%29) e [despesas](http://pt.wikipedia.org/wiki/Despesa) no período de sua [realização](http://pt.wikipedia.org/wiki/Princ%c3%adpios_cont%c3%a1beis), ou seja, é a contabilização realizada no período em que o serviço foi realmente prestado, independentemente do efetivo recebimento das receitas ou do pagamento das despesas que, quando ocorre, é contabilizado pelo *regime de caixa*. Na contabilização por competência, haverá a contabilização do valor total previsto para o contrato do aluno e, ao longo da prestação dos serviços, mês a mês, haverá a respectiva apropriação mensal.

**Exemplo:**  
No período letivo 2015, a instituição presta ao aluno o serviço MENSALIDADE.  
Meses em que o serviço será prestado: 1 a 12 de 2015.  
Alguns alunos irão pagar em 12 vezes, outros em 3 vezes, outros a vista...  
  
Com o processo de contabilização por competência teremos a contabilização realizada no período em que o serviço for realmente prestado ao aluno conforme o seu contrato (de 1 a 12 de 2015 conforme o exemplo acima) e não de acordo com a forma de pagamento que cada aluno pode adotar. A soma das parcelas existentes no contrato do aluno, de acordo com a forma de pagamento adotada, irá fornecer o valor total do contrato a ser contabilizado pelo regime de competência.   
  
Para que o sistema faça a contabilização por competência é necessário primeiramente que alguns parâmetros e informações sejam devidamente preenchidos, lembrando que neste caso o sistema fará a integração direta com o TOTVS Gestão Contábil. Neste caso devemos verificar as parametrizações específicas relacionadas abaixo, tanto no TOTVS Educacional como no TOTVS Gestão Contábil.   
  
Para obter detalhes sobre as parametrizações e exemplos de utilizações, clique nos respectivos links abaixo:

1 - Parametrizações necessárias no TOTVS Gestão Contábil:  
-  Contas contábeis e Contas gerenciais  
-  Período Contábil  
-   Período do Usuário para manutenção em lançamentos contábeis  
-   Lotes  
  
2 -    
-  Serviços  
-  Bolsas  
-  Situação de Matrícula  
-  Eventos Contábeis  
-  Defaults contábeis  
-  Parâmetros de Integração | Contabilidade (informações sobre o modelo de contabilização abaixo)

Modelos de Contabilização

A contabilização por competência pode ser realizada no sistema através de **dois modelos distintos**, a diferença básica entre os dois modelos de contabilização é a forma como as *alterações* ocorridas nos valores contratos, sejam elas devido à redução ou devido a aumento nos valores dos serviços, bolsas e/ou descontos que compõem o contrato, serão contabilizadas.

Nos parâmetros do sistema, *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade*, é que devemos indicar qual, entre os dois modelos, queremos que o sistema adote para a realização da contabilização por competência através das opções 'Utiliza contabilização por competência' e 'Registra separadamente contabilizações de cancelamento e aumento'.

Para exemplificar os dois modelos de contabilização, vamos supor o mesmo cenário, porém utilizando os dois modelos de contabilização.

**Vamos supor o exemplo abaixo:**  
-Competência - Mês/Ano Inicial: 01/2015  
-Competência - Mês/Ano Final  : 12/2015  
-Data do Contrato: 03/03/2015  
-Valor total dos serviços do contrato a ser contabilizado: 12.000,00  
-Em Maio o aluno cancelou uma disciplina, cujo valor total é de 1.000,00  
-Em Julho o aluno se matriculou em uma nova disciplina, cujo valor total é de 1.000,00

Independentemente do modelo de contabilização adotado, será incluído primeiramente e uma única vez, um lançamento no valor *total* do contrato firmado originalmente, como uma previsão total de recebimento, utilizando para isto o evento contábil indicado para a contabilização do 'Contrato'. Este lançamento, por padrão, terá como data, o último dia do mês em que os serviços começarem a ser prestados, conforme a competência contábil e data do contrato. À medida que os serviços forem sendo realizados, mês a mês, e até o final da prestação dos serviços previstos no contrato, será incluído o lançamento apropriando-se a sua efetiva realização, utilizando para isto o evento contábil indicado para a contabilização 'Mensal'. Estes lançamentos, por padrão, terão como data, o último dia do mês correspondente à sua competência.

Vejam a seguir a contabilização deste mesmo cenário em cada um dos dois modelos de contabilização:

modelocontabilizacao1°contabilizacaoPrimeiro Modelo Contabilização

Utilizando o **primeiro** modelo de contabilização por competência do contrato educacional, é necessário marcar **somente** a primeira opção 'Utiliza contabilização por competência'.   
Isto indica que a contabilização será realizada nas devidas competências, porém, qualquer mudança ocorrida nos valores de serviço, bolsa e/ou desconto que compõem o contrato, resultará no estorno da contabilização anteriormente realizada referente ao valor original do contrato e na inclusão de nova contabilização refletindo o novo valor do contrato e as apropriações realizadas para as próximas competências serão feitas levando em consideração o novo valor contratado, utilizando sempre os mesmos eventos contábeis para registrar o valor do 'Contrato' e das apropriações 'Mensais'.

Provisão e Apropriação do Contrato

**Evento contábil utilizado para 'Contrato':**  
D – 1.1.2.04.01.001 - Mensalidades a Receber  
C – 2.1.7.01.01.001 - Receitas de Graduação

**Evento contábil utilizado para 'Mensal':**  
D – 2.1.7.01.01.001 - Receitas de Graduação  
C – 3.1.1.01.01.001 - Receitas de Graduação

Lançamento referente à contabilização do valor do contrato:  
D – 1.1.2.04.01.001 – 12.000,00  
C – 2.1.7.01.01.001 – 12.000,00

Lançamento referente à contabilização da primeira competência do contrato (mês 03):  
D – 2.1.7.01.01.001 – 1.200,00  
C – 3.1.1.01.01.001 – 1.200,00

Lançamento referente à contabilização da segunda competência do contrato (mês 04):  
D – 2.1.7.01.01.001 – 1.200,00  
C – 3.1.1.01.01.001 – 1.200,00

Provisão e Apropriação do Cancelamento

- Em **Maio**o aluno cancelou uma disciplina, cujo valor total é de 1.000,00  
Como estamos utilizando o **primeiro**modelo de contabilização, o lançamento referente ao valor do contrato será estornado para a inclusão de outro lançamento no valor atual do contrato (12.000,00 – 1.000,00 = 11.000,00) e em seguida a  inclusão do lançamento referente à próxima competência que será calculada com base no novo valor do contrato menos o valor das competências já realizadas e apropriadas (1.200,00 referente à 03/2015 + 1.200,00 referente à 04/2015 = 2.400,00) dividido pelos número restante de competências a serem realizadas (05/2015 à 12/2015 = 8 meses).  
Teremos então: (11.000,00 – 2.400,00 = 8.600,00) / 8 =**1.075,00**.

Estorno do lançamento referente à contabilização do valor do contrato:  
D – 2.1.7.01.01.001 - 12.000,00  
C – 1.1.2.04.01.001 - 12.000,00

Lançamento do valor atual do contrato:  
D – 1.1.2.04.01.001 – 11.000,00  
C – 2.1.7.01.01.001 – 11.000,00

Lançamento referente à contabilização da terceira competência do contrato (mês 05):  
D – 2.1.7.01.01.001 – 1.075,00  
C – 3.1.1.01.01.001 – 1.075,00

Provisão e Apropriação do Aumento

- Em **Julho** o aluno se matriculou em uma nova disciplina, cujo valor total é de 1.000,00  
Novamente haverá o estorno do lançamento referente ao valor do contrato e a inclusão de outro lançamento no valor atual do contrato (11000,00 + 1000,00 = 12000,00) e em seguida a inclusão do lançamento referente à próxima competência que será calculada com base no novo valor do contrato – valor das competências já realizadas e apropriadas (1.200,00 referente à 03/2015 + 1.200,00 referente à 04/2015 + 1.075,00 referente à 05/2015 = 3.475,00) dividido pelos número restante de competências a serem realizadas (06/2015 à 12/2015 = 7 meses).  
Teremos então: (12.000,00 – 3.475,00 = 8.525,00) / 7 = **1.217,85**.

Estorno do lançamento referente à contabilização do valor do contrato:  
D – 2.1.7.01.01.001 – 11.000,00  
C – 1.1.2.04.01.001 – 11.000,00

Lançamento do valor atual do contrato:  
D – 1.1.2.04.01.001 – 12.000,00  
C – 2.1.7.01.01.001 – 12.000,00

Lançamento referente à contabilização da quarta competência do contrato (mês 06):  
D – 2.1.7.01.01.001 – 1.217,85  
C – 3.1.1.01.01.001 – 1.217,85

- Se mais nenhuma alteração ocorrer, mensalmente, de **Julho** até **Dezembro** o seguinte lançamento será incluído:  
D – 2.1.7.01.01.001 – 1.217,85  
C – 3.1.1.01.01.001 – 1.217,85

**Observação:**Ao gerar a contabilização para uma determinada competência e o sistema detectar que houve alguma alteração entre os valores contratados e os valores já contabilizados o sistema fará os ajustes necessários. Antes, porém, irá verificar se os lançamentos contábeis já realizados estão no lote N ou já foram integrados ao lote oficial da contabilidade, lote 0 (zero).  
Se os lançamentos ainda estiverem no **lote N,**o sistema *não fará o lançamento de estorno*referente à contabilização do valor original do contrato, ele simplesmente irá *excluir*o lançamento original e fará a *inclusão*de outro lançamento com o valor atualizado do contrato.  
Se os lançamentos já tiverem sido integrados ao **lote 0 (zero)**eles não poderão sofrer alterações, então nestes casos, o sistema fará o *estorno*, como nos exemplos acima, com o intuito de *anular ou cancelar '*o lançamento referente à contabilização do valor original do contrato. O lançamento de estorno receberá o status '**E**= Estorno' e será incluído no lote criado especificamente para receber os estornos. O lançamento original, que está no Lote 0 (zero), não será excluído, mas terá o status alterado para '**I**= Incorreto'. Será incluído então um novo lançamento com o valor atualizado do contrato. Este lançamento receberá o status **'C**= Correto'.

2°contabilizacaoSegundo Modelo Contabilização

Utilizando o **segundo** modelo de contabilização por competência do contrato educacional, é necessário marcar a opção 'Utiliza contabilização por competência' **e também** a opção 'Registra separadamente contabilizações de cancelamento e aumento'.

Isto indica que mesmo havendo mudança nos valores de um contrato, devido à redução ou aumento nos valores dos serviços, bolsas e/ou descontos que o compõe, não será realizado o estorno referente à contabilização do valor original contratado e o valor original continuará sendo apropriado mensalmente nas respectivas competências. As alterações nos valores dos serviços, bolsas e/ou descontos passarão a ser registradas e apropriadas separadamente, em contas contábeis destinadas para este fim, utilizando-se eventos contábeis específicos para registrar tais 'Cancelamentos' e/ou 'Aumentos'. Desta forma a contabilização original será mantida até o final da prestação dos serviços, porém os cancelamentos e/ou aumentos que modificam os valores da receita, serão registrados e evidenciados separadamente no momento em que ocorrerem e, da mesma forma, apropriados até o final da prestação dos serviços.

Para o segundo modelo de contabilização, é necessário que se parametrize e se indique todos os eventos contábeis solicitados na tela de parâmetros da contabilização: Um evento para a contabilização do valor original do 'Contrato' e outro para registrar as apropriações 'Mensais' (estes dois primeiros eventos são utilizados nos dois modelos de contabilização). Um evento para contabilizar os 'Cancelamentos' de valores ocorridos nos serviços, bolsas e/ou descontos contratados e outro para registrar as apropriações mensais deste cancelamento ou diminuição de valores contratados. Um evento para contabilizar os 'Aumentos' de valores ocorridos nos serviços, bolsas e/ou descontos contratados e outro para registrar as apropriações mensais deste aumento de valores contratados. Desta forma, toda alteração realizada ficará devidamente evidenciada contabilmente.

Provisão e Apropriação do Contrato

**Evento contábil utilizado para 'Contrato':**  
D – 1.1.2.04.01.001 - Mensalidades a Receber  
C – 2.1.7.01.01.001 - Receitas de Graduação

**Evento contábil utilizado para 'Mensal':**  
D – 2.1.7.01.01.001 - Receitas de Graduação  
C – 3.1.1.01.01.001 - Receitas de Graduação

Lançamento referente à contabilização do valor do contrato:  
D – 1.1.2.04.01.001 – 12.000,00  
C – 2.1.7.01.01.001 – 12.000,00

Lançamento referente à contabilização da primeira competência do contrato (mês 03):  
D – 2.1.7.01.01.001 – 1.200,00  
C – 3.1.1.01.01.001 – 1.200,00

Lançamento referente à contabilização da segunda competência do contrato (mês 04):  
D – 2.1.7.01.01.001 – 1.200,00  
C – 3.1.1.01.01.001 – 1.200,00

Provisão e Apropriação Cancelamento

Em **Maio** o aluno cancelou uma disciplina, cujo valor total é de 1.000,00  
Como estamos utilizando o **segundo** modelo de contabilização, o lançamento referente ao valor original do contrato *não* será estornado e continuará havendo a respectiva contabilização mensal da sua realização. Haverá, porém, a inclusão de um novo lançamento para registrar o valor total do serviço cancelado e outros para registrar as respectivas realizações mensais deste cancelamento que será realizada até o final da prestação dos serviços, sendo que estes lançamentos utilizarão eventos específicos para tais registros. O valor da apropriação ou realização mensal do cancelamento será de 1.000,00 dividido pelo número restante de competências a serem realizadas (05/2015 à 12/2015 = 8 meses).  
Teremos então: 1.000,00 / 8 = **125,00**

**Evento contábil utilizado para 'Cancelamento do Contrato':**  
D – 2.1.7.01.03.001 – Cancelamento de Matrícula  
C – 1.1.2.04.01.001 – Mensalidades a Receber

**Evento contábil utilizado para 'Cancelamento Mensal':**  
D – 3.1.1.01.99.001 – Cancelamentos  
C – 2.1.7.01.03.001 – Cancelamento de Matrícula

Lançamento referente à contabilização da terceira competência do contrato (mês 05) – valor original:  
D – 2.1.7.01.01.001 – 1.200,00  
C – 3.1.1.01.01.001– 1.200,00

Lançamento referente ao valor *total* do serviço cancelado - utilização do evento contábil 'Cancelamento do Contrato':  
D – 2.1.7.01.03.001 – 1.000,00  
C – 1.1.2.04.01.001 – 1.000,00

Lançamento referente à contabilização da *primeira competência do cancelamento* (mês 05) - utilização do evento contábil 'Cancelamento Mensal':  
D – 3.1.1.01.99.001 –  125,00  
C – 2.1.7.01.03.001 –  125,00

Provisão e Apropriação Aumento

Em **Julho** o aluno se matriculou em uma nova disciplina, cujo valor total é de 1.000,00  
Como sabemos, neste modelo as alterações não geram estorno de contabilizações já realizadas. Como houve aumento do valor do serviço contrato, será incluído novo lançamento para registrar este aumento e outros para registrar as respectivas realizações mensais deste aumento que será realizada até o final da prestação dos serviços, sendo que estes lançamentos utilizarão eventos específicos para tais registros. O valor da apropriação ou realização mensal do aumento será de 1.000,00 dividido pelo número restante de competências a serem realizadas (06/2015 à 12/2015 = 7 meses).  
Teremos então: 1.000,00 / 7 = **142,85**

**Evento contábil utilizado para 'Aumento do Contrato':**  
D – 1.1.2.04.01.001 - Mensalidades a Receber  
C – 2.1.7.01.01.001 - Receitas de Graduação

**Evento contábil utilizado para 'Aumento Mensal':**  
D – 2.1.7.01.01.001 - Receitas de Graduação  
C – 3.1.1.01.01.001 - Receitas de Graduação

Lançamento referente à contabilização da quarta competência do contrato (mês 06) – valor original:  
D – 2.1.7.01.01.001 – 1.200,00  
C – 3.1.1.01.01.001 – 1.200,00

Lançamento referente à contabilização da segunda competência do cancelamento (mês 06):  
D – 3.1.1.01.99.001 – 125,00  
C – 2.1.7.01.03.001 – 125,00

Lançamento referente ao valor *total* do aumento do serviço- utilização do evento contábil 'Aumento do Contrato':  
D – 1.1.2.04.01.001 – 1.000,00  
C – 2.1.7.01.01.001 – 1.000,00

Lançamento referente à contabilização da *primeira competência do aumento* (mês 06) - utilização do evento contábil 'Aumento Mensal':  
D – 2.1.7.01.01.001 – 142,85  
C – 3.1.1.01.01.001 – 142,85

- Se mais nenhuma alteração ocorrer, mensalmente, de **Julho** até **Dezembro** os seguintes lançamentos serão incluídos:  
D – 2.1.7.01.01.001 – 1.200,00  
C – 3.1.1.01.01.001 – 1.200,00

D – 3.1.1.01.99.001 – 125,00  
C – 2.1.7.01.03.001 – 125,00

D – 2.1.7.01.01.001 – 142,85  
C – 3.1.1.01.01.001 – 142,85

**Temos a possibilidade de contabilizar somente a provisão de contrato no processo de contabilização a partir da versão 12.1.25, com a contabilização no modelo revitalizado**

No processo de contabilização será possível contabilizar somente o contrato sem necessidade de contabilizar as apropriações mensais no mesmo momento, essa funcionalidade foi criada visando provisionar o contrato no momento do fato gerador. já as apropriações poderão ser feitas mês a mês, junto com o contrato ou apropriar mensal via regime de caixa realizando somente a apropriação do contrato via competência. 

Ao executar o processo de contabilização e marcar a opção "Contabiliza apenas a provisão" o sistema irá gerar contabilização somente para o contrato.

* Contabilização apenas da provisão de contrato sem informar "Data de Contabilização"  
  - Quando não possui data no contrato, será contabilizada a provisão com a data atual  
  - Quando o contrato possui data, será contabilizada a provisão respeitando a data do contrato
* Contabilização da provisão do contrato informando a "Data de Contabilização"  
  - Quando o contrato não possui data, será contabilizado a provisão respeitando a data informada no processo  
  - Quando o contrato possui data, será contabilizado a provisão respeitando a data informada no processo

Ao executar o processo de contabilização e não marcar a opção "Contabiliza apenas a provisão" o sistema irá gerar contabilização para o contrato e apropriação mensal, caso não exista provisão de contrato contabilizado.

* Contabilização da provisão do contrato e apropriação mensal sem informar a "Data de Contabilização"  
  - Quando o contrato não possui data, será contabilizada a provisão buscando a data no mês/ano da primeira apropriação mensal.  
  - Quando o contrato possui data, será contabilizada a provisão respeitando a data do contrato

* Contabilização da provisão do contrato e apropriação mensal informando a "Data de Contabilização"  
  - Quando o contrato não possui data, será contabilizado a provisão respeitando a data informada no processo  
  - Quando o contrato possui data, será contabilizado a provisão respeitando a data informada no processo

* Contabilização da provisão do contrato e apropriação mensal sem informar a "Data de Contabilização", marcando o parâmetro do sistema, *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade  | Contabilidade 2/2 -*Considera a data do contrato para a data de contabilização da provisão*.*  
  - Quando o contrato não possui data, será contabilizada a provisão buscando a data no mês/ano da primeira apropriação mensal.  
  - Quando o contrato possui data, será contabilizada a provisão respeitando a data do contrato

Existe também a opção nos parâmetros do sistema, *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade  | Contabilidade 2/2,*que podemos indicar se será feito somente a provisão do contrato "Contabiliza apenas a provisão do contrato", com essa opção marcada mesmo informando o "Período de Contabilização" será executado somente a provisão dos contratos ainda não diferidos, para os contratos diferidos será apropriado mensalmente conforme data de contabilização.   
Saiba mais sobre o novo processo, [clicando aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=487391427)

  Informações Complementares

---

Geração da contabilização por competência  
[Competência contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=425458867)[Eventos Contábeis - Educacional](http://tdn.totvs.com/pages/viewpage.action?pageId=425458832)Ativa / Desativa Log de Evento Contábil

 Veja Também

---

   
Cálculo do valor de bolsas X Contabilização
