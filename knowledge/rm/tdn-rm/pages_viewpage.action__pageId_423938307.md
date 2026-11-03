---
content_hash: 618dcbe12040286f6f4b617b8974332d20e3349cff086ffdafa36b3cdf80b4d0
fetched_at: '2026-06-29T00:09:26.506710+00:00'
page_id: '423938307'
product: rm
source: tdn-rm
title: Eventos Contábeis (Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938307
version: 5
---

Por esta opção, são cadastrados os eventos contábeis para utilização do sistema. Eventos Contábeis irão determinar as regras de contabilização utilizadas na empresa. Esta regra é a definição de como os lançamentos fiscais de entrada, saída e transferência serão contabilizados.   
Neste caso, ao incluir um lançamento, utilizando o evento contábil, não será necessário a digitação das contas contábeis pois o sistema irá contabilizar este de acordo com as regras e defaults de contas contábeis / gerenciais já definidas no Evento. A seguir são definidos os parâmetros para Utilização do Evento.

**Calcula Valor a Partir de:**Fórmula: Marque esta opção se deseja controlar os valores para os Itens do Evento contábil através de fórmulas.

***Observação:***Marcando esta opção, ao incluir os Itens do Eventos, será apresentado o campo "Fórmula" para que o sistema calcule os valores do lançamento  
Percentual: Marque esta opção se deseja controlar os valores para os Itens do Evento contábil através de Percentuais.  
Marcando esta opção, ao incluir os Itens do Eventos, será apresentado o campo "Percentual" para que o sistema calcule os valores do lançamento.

Na utilização da contabilização por Percentual, o sistema irá utilizar sempre o Valor Contábil do Lançamento Fiscal para aplicação dos percentuais informados para o Item do Evento Contábil.  
Ainda, na utilização de Percentual para a Conta Contábil, o percentual do Rateio Gerencial desta será calculado em cima do Valor Total da Conta Original.

**Buscar Filial/Departamento em:** Marque de onde o evento contábil irá buscar a Filial/Departamento para o preenchimento da contabilização assim como a prioridade da busca.  
Ao marcar somente uma opção para busca, ela será automaticamente levada para a primeira posição da lista. Se for selecionada mais de uma opção, deve-se informar também a prioridade da busca, ou seja, se não for encontrada a Filial/Departamento na primeira opção o sistema irá buscá-la na segunda opção e assim sucessivamente. Para mudar a ordem/prioridade, selecione a opção e em seguida utilize os botões de movimentação para cima ou para baixo.  
***Observação***: Quando a opção "Buscar Filial/Departamento em" for igual a "Evento Contábil" e não utilizar prioridade, o campo "Filial" localizado na Pasta Dados Complementares dos itens de evento deverá ser preenchido.

**Itens do Evento**

Os itens contábeis em Gestão Fiscal poderão ser contabilizados por Tabelas Default ou por Contas Contábeis bastando, para isto, informar a opção desejada no campo Origem da Conta.

**Aplicar:**Esta opção tem como finalidade estabelecer em qual tabela default ou conta contábil os lançamentos contábeis serão obtidos. Abaixo serão apresentadas as opções quando o campo Aplicar incidir sobre alguma tabela e a origem da conta for obtida por alguma tabela default.. Exemplos de aplicação:

1. Aplicar Lançamento Fiscal
2. Aplicar Item de Movimento
3. Rateio Centro de Custo
4. Rateio Departamento

**Fórmula:** Ao selecionar uma fórmula que calcule algo no contexto de itens (exemplo TABTRBITENS) é necessário que o campo Aplicar esteja parametrizado com a opção de "Aplicar Item de Movimento". Caso o contexto da fórmula seja de Lançamento o campo Aplicar pode ser parametrizado com a opção de "Aplicar Lançamento Fiscal" ou "Aplicar Item de Movimento".

**Origem da Conta:**Neste campo o usuário poderá definir:

**Informar Conta:**Selecionando Informar Conta, será disponibilizado um campo para que o usuário informe a conta contábil a ser utilizada para o item de evento em questão; se a crédito ou a débito.

**Tabelas Default::**Selecionando a opção Tabelas Default, serão disponibilizados os campos:

**Buscar default em:**  Serão apresentadas as tabelas possíveis para o registro do default contábil da mesma;

**Obter default de:**  Para que o usuário informe se o default será a crédito ou a débito

**Classificação da Conta:**  Este campo só aparecerá se a origem da conta for "Default". Se desejar, poderá informar neste campo a classificação da conta, cadastrada nos defaults contábeis das tabelas, desta forma, caso existam mais de uma conta no default indicada, o sistema só buscará para a contabilização a conta que tiver a classificação aqui informada.

**Classificação de Centro de Custo:**Neste item o usuário vai filtrar a classificação de centro de custo será aplicada as partidas Contábeis

**Aplicar Classificação de Centro de  Custo sobre:**

* **Item do evento (este item) =>** Indica que o filtro da classificação do centro de custo será aplicado somente sobre as partidas contábeis que serão geradas pelo default contábil do item parametrizado no campo "Buscar default em".

* **Itens gerenciais =>** Indica que o filtro da classificação do centro de custo será aplicado somente sobre os rateios gerenciais da partida contábil gerado pelo evento contábil.

* **Ambos (Item do evento / Itens gerenciais) =>** Esta opção aplica a regra da classificação do centro de custo tanto no item contábil quanto no item gerencial.

******Observação***:*** Cadastro de Cliente/Fornecedor: Lembramos que quando Cliente: temos a opção de defaults para Cliente; quando Fornecedor: temos a opção de defaults para Fornecedor; e, quando Ambos o default a ser buscado será de acordo com o tipo de emitente destinatário parametrizado no tipo de movimento.

Algumas combinações de parâmetros podem disponibilizar algumas opções específicas para utilização de defaults do sistema de Gestão Fiscal. Como é apresentado abaixo:
