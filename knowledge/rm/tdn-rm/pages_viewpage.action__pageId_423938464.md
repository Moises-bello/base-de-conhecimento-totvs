---
content_hash: e6e4846262e0dec958e5d304c608314304461693230ff3d321752b5b54ce8c41
fetched_at: '2026-06-29T00:09:27.259151+00:00'
page_id: '423938464'
product: rm
source: tdn-rm
title: Itens Evento - Eventos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938464
version: 26
---

**Conteúdo**

truesquare

## **01.  Visão Geral**

Na janela principal, é possível visualizar o cadastro geral dos Itens de Evento.

Os Itens de Evento representam as informações utilizadas na geração da contabilização. As regras para a contabilização do lançamento devem ser definidas separadamente para as partidas a Débito e para as partidas a Crédito. Caso as regras sejam definidas apenas para o Débito ou apenas para o Crédito, o lançamento contábil não será incluído automaticamente pelo sistema, ele será incluído somente após a inserção manual da partida ausente. Da mesma forma, o lançamento não será incluído automaticamente pelo sistema se a soma dos valores calculados para os débitos não for igual à soma dos créditos. Nesse caso, será necessário ajustar manualmente os valores para que o lançamento seja incluído.

## **02.  Configuração do Item do Evento Contábil**

Ao acessar uma das opções, Incluir ou Editar, o sistema abrirá uma janela de edição com todos os dados do Item do Evento Contábil a ser incluído ou alterado. Segue abaixo descrição detalhada de campos da aba Identificação:

**Aplicar:** Indique onde o lançamento contábil a ser gerado será aplicado. A opção selecionada determinará a abrangência ou incidência em que o lançamento contábil será gerado.

**Lançar como:** Este campo apenas indica se o item que está sendo incluído irá gerar partidas de débito ou crédito. A seleção entre débito ou crédito é feita anteriormente, ao acionar o botão para incluir um novo Item de Evento, optando por débito ou crédito.

**Origem da Conta:** Escolha de onde as contas contábeis serão obtidas no momento em que as entradas do lançamento contábil forem geradas. As opções disponíveis são:

falseEscolha de onde as contas contábeis serão obtidas no momento em que as entradas do lançamento contábil forem geradas. As opções disponíveis são:Informar Conta

Com esta opção selecionada, a entrada a ser gerada por este item de evento utilizará uma conta contábil informada manualmente. Nessa opção o seguinte campo será apresentado para preenchimento:

* **Conta Contábil:** Será solicitada a Conta Contábil a ser utilizada.
Tabela Default

Com esta opção selecionada, a entrada a ser gerada por este item de evento buscará a conta contábil indicada no default contábil de uma "Tabela" do sistema. Os seguintes campos serão apresentados a seguir:

* **Buscar Default em:**  Indique de qual "Tabela" o sistema irá obter a conta contábil.

* **Obter Default de:** Especifique se o sistema deve buscar a conta indicada no default contábil de crédito ou no de débito da "Tabela" selecionada.

* **Classificação da Conta:** Se desejado, você pode informar neste campo a classificação da conta, cadastrada no default contábil da "Tabela" selecionada. Dessa forma, caso haja mais de uma conta no default indicado, o sistema buscará apenas a conta associada à classificação informada.
* **Classificação Centro de Custo:** Se informada, a classificação de centro de custo será utilizada como filtro para os valores dos rateios por centro de custo. Para que isso funcione, é necessário utilizar uma fórmula com a função VALORRATCCUPORCLASSIF, que retorna a soma dos rateios de acordo com a classificação de centro de custo passada como parâmetro. O item do evento deve ser configurado para buscar o valor contábil a partir da fórmula com o filtro para a classificação desejada. Assim, o sistema buscará o default das contas gerenciais incluídas no cadastro dos centros de custos. Se nenhuma classificação de centro de custo for informada, o sistema seguirá a regra dos itens gerenciais do evento contábil para gerar os rateios no lançamento contábil.
* **Aplicar Classificação do C. Custo sobre:**

  + **Item do evento (este item):** Indica que o filtro da classificação do centro de custo será aplicado apenas às partidas contábeis que serão geradas pelo default contábil do item parametrizado no campo "Buscar default em".
  + **Itens gerenciais:** Indica que o filtro da classificação do centro de custo será aplicado apenas aos rateios gerenciais da partida contábil gerado pelo evento contábil.
  + **Ambos (Item do evento / Itens gerenciais):** Esta opção aplica a regra da classificação do centro de custo tanto no item contábil quanto no item gerencial.

Atenção!

Se na tabela default utilizada houver mais de uma conta contábil incluída como default a débito/crédito e a "Classificação da Conta" não for informada no item do evento contábil, o sistema buscará todas as contas encontradas, o que pode resultar em diferenças entre os valores de Débito/Crédito na contabilização.

Exemplo do resultado da Classificação da Conta

Suponha um item do evento contábil configurado da seguinte maneira:

* **Origem da Conta:** Tabela Default
* **Buscar default em:** Filial
* **Obter default de:** Débito
* **Classificação do Centro de Custo:** FIL01

No cadastro da filial (01- Filial Exemplo) , nos defaults a débito existem as seguintes contas informadas:

| Conta | Classificação |
| --- | --- |
| 1.1.1.0001 | FIL00 |
| 1.1.1.0002 | FIL01 |
| 1.1.1.0003 | FIL02 |

No exemplo dado, ao utilizar a filial (01- Filial Exemplo) com o evento contábil descrito, o sistema buscará apenas a conta contábil **1.1.1.0002** para o lançamento do débito.

**Valor:** Selecione em qual valor o percentual ou a fórmula serão aplicados.

* **Percentual:** Este campo só será apresentado se "Percentual" for selecionado na aba de identificação do evento para calcular o valor contábil do lançamento. Informe o percentual a ser utilizado para calcular o valor contábil da partida a ser gerada por este item de evento.
* **Fórmula:** Este campo só será apresentado se "Fórmula" for selecionado na aba de identificação do evento para calcular o valor contábil do lançamento. Informe a fórmula a ser utilizada para chegar ao valor contábil da partida a ser gerada por este item de evento.

## **03.  Particularidades por módulo**

60%VídeosleftfadeGestão FinanceiraGestão FinanceiraGestão Financeira

No módulo TOTVS Gestão Financeira, existe uma configuração de evento contábil que pode resultar na execução do processo duas vezes. Alguns detalhes dessa configuração são descritos abaixo:

Se o "Buscar Default em" estiver parametrizado como "Contabilização dos Lançamentos Faturados", o sistema utilizará um critério diferente das demais opções para buscar os valores que serão contabilizados. Abaixo segue a lógica:

O resultado da fórmula/valor percentual do item de evento do lançamento faturado é dividido pelo valor original do lançamento de vencimento da fatura e multiplicado por 100,00. Ao final, o valor resultante desta operação será o percentual (%) que será aplicado na fórmula/valor percentual utilizada no item de evento que está realizando a baixa do vencimento da fatura (item de evento que buscou a contabilização dos lançamentos faturados).

No cenário em que o evento contábil do lançamento faturado não retorna valor para que seja calculado o percentual, o sistema calcula esse percentual baseado na quantidade de lançamentos faturados, ou seja, uma fatura dividida pelo número de lançamentos faturados.

Atenção!

Esse tipo de Default Contábil possui algumas limitações de configuração, como por exemplo:

1. Se forem faturados dez lançamentos, serão processados o evento contábil de baixa dos dez lançamentos. Isso pode resultar em queda de performance.
2. Se o evento contábil de baixa do lançamento faturado possuir a opção "Não validar valor contabilizado zerado" desmarcada, caso o percentual ou a fórmula retorne valor zerado, não será retornado o lançamento contábil e consequentemente as contas não serão geradas para o default.
3. Se o evento contábil de baixa do lançamento faturado possuir fórmulas que usam funções do tipo "TABLANBAIXA" ou "TABLANBAIXAPF" que são respectivamente executadas no contexto da FLANBAIXA e FLANBAIXAHST, estas irão retornar o valor 0 (zero), pois o lançamento faturado não possui item de baixa e nem histórico de item de baixa. Diante disto é muito importante que a opção "Não validar valor contabilizado zerado" esteja marcada para que a partida gerada com essa fórmula não seja eliminada do processo e a conta contábil possa ser retornada, caso contrário essa conta contábil não será carregada no default em questão.
4. Os campos "Classif. Conta:" e "Classificação do Centro de Custo" podem não surtir o efeito esperado para este tipo de Default Contábil, pois as contas que são retornadas já vêm processadas dos Eventos Contábeis presentes nos Lançamentos Faturados e não no Vencimento de Fatura que está sendo baixado. Em outras palavras, se a conta no lançamento faturado foi classificada no default do mesmo como "LF", e no evento contábil do vencimento de fatura a classificação da conta no default for "FV", os itens não serão carregados na contabilização. Importante lembrar que se a opção "Agrupar Partida Contábil" do evento contábil do lançamento faturado estiver marcada muda o comportamento da "Classificação da Conta".
Gestão PatrimonialGestão PatrimonialGestão Patrimonial

Na opção Origem da conta, escolhendo Tabela Default, o campo "Aplicar classificação C. Custo Sobre" apresentará apenas a opção "Item do evento (este item)". 

---

**Veja também:**
