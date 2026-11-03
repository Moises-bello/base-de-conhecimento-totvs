---
content_hash: b600050fb4ec34dff4613d21e3cf70039f7b7a937e0597cfc829c4bcc05b67a3
fetched_at: '2026-06-29T00:09:25.443432+00:00'
page_id: '423938154'
product: rm
source: tdn-rm
title: Eventos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938154
version: 6
---

Neste tópico, serão abordados parâmetros específicos relacionados à integração com a Gestão de Estoques no auxílio à utilização dos Eventos Contábeis no sistema.

**Buscar Filial/Departamento em**: Marque de onde o evento contábil irá buscar a Filial/Departamento para o preenchimento da contabilização assim como a prioridade da busca.

Ao marcar somente uma opção para busca, ela será automaticamente levada para a primeira posição da lista.

Se for selecionada mais de uma opção, deve-se informar também a prioridade da busca, ou seja, se não for encontrada a Filial/Departamento na primeira opção o sistema irá buscá-la na segunda opção e assim sucessivamente. Para mudar a ordem/prioridade, selecione a opção e em seguida utilize os botões de movimentação para cima ou para baixo.

* ***Observação***: Quando a opção "Buscar Filial/Depto em" for igual a "Evento Contábil" e não utilizar prioridade, o campo "Filial" localizado na Pasta Dados Complementares dos itens de evento deverá ser preenchido.

**Itens do Evento:**Os itens contábeis em Gestão de Estoques poderão ser contabilizados por Tabelas Default ou por Contas Contábeis, bastando para isto informar a opção desejada no campo Origem da Conta.

**Informar Conta**

Selecionando Informar Conta, será disponibilizado um campo para que o usuário informe a conta contábil a ser utilizada para o item de evento em questão; se a crédito ou a débito.

**Tabelas Default:**Selecionando a opção Tabelas Default, serão disponibilizados os campos:

* **Buscar default em**: serão apresentadas as tabelas possíveis para o registro do default contábil da mesma.
* **Obter default de**: para que o usuário informe se o default será a crédito ou a débito.

**Classificação da Conta**: Este campo só aparecerá se a origem da conta for "Default". Se desejar, poderá informar neste campo a classificação da conta, cadastrada nos defaults contábeis das tabelas. Desta forma, caso existam mais de uma conta no default indicada, o sistema só buscará para a contabilização a conta que tiver a classificação aqui informada.

Deve ser indicada a tabela de Cliente/Fornecedor ou Movimento/Centro de Custo de onde serão selecionadas as contas contábeis do plano de contas a débito ou a crédito.  O Cliente/Fornecedor ou Movimento precisam ter seus defaults contábeis informados para que seja possível a utilização das Tabelas Default nos itens contábeis.

* ***Observação**:*Cadastro de Cliente/Fornecedor, lembramos que:
  + Cliente: temos a opção de defaults para Cliente;
  + Fornecedor: temos a opção de defaults para Fornecedor;
  + Ambos o default a ser buscado será de acordo com o tipo de emitente destinatário parametrizado no tipo de movimento.

Algumas combinações de parâmetros podem disponibilizar algumas opções específicas para utilização de defaults do sistema de Gestão de Estoques, omo é apresentado abaixo:

Aplicar: Esta opção tem como finalidade estabelecer em qual tabela default ou conta contábil os lançamentos contábeis serão obtidos. Abaixo serão apresentadas as opções quando o campo Aplicar incidir sobre alguma tabela e a origem da conta for obtida por alguma tabela default:

* **Aplicar Movimento:**Cliente/Fornecedor: Buscará o default contábil do Cliente/Fornecedor da movimentação.
* **Natureza de Operação**: Buscará o default contábil da Natureza de Operação utilizada no movimento.
* **Tributo**: Buscará o default contábil do(s) tributos(s) parametrizados(s) no movimento. Será apresentado o campo do Tributo, para que o mesmo seja identificado para que os defaults contábeis deste tributo, na movimentação, sejam carregados para a contabilização.
* **Filial**: Buscará o default contábil da Filial da movimentação.
* **Centro de Custo/Departamento**: Buscará o default contábil do cadastro para carregar a contabilização do movimento.
* **Tabelas de Faturamento/Classificação**: Buscará o default contábil do cadastro da tabela selecionada para buscar os defaults parametrizados nas respectivas tabelas.
* **Filial Destino**: Buscará o default contábil da Filial da movimentação. Usualmente, este processo será utilizado quando efetuado em movimentos de Transferência.
* **Representante**: Buscará o default contábil do Representante informado no movimento.
* **Transportadora**: Buscará o default contábil da Transportadora informada na movimentação.
* **Forma de Pagamento**: Buscará o default contábil da Forma de Pagamento (Meio de Pagamento) selecionada no movimento.
* **Cliente/Fornecedor Origem/Destino**: Buscará o default contábil do Cliente/Fornecedor informado no campo 'Cliente/Fornecedor Origem/Destino' da movimentação.
* **Local de Estoque**: Buscará o default contábil do Local de Estoque informado no movimento.

**Aplicar Item de Movimento**

* **Produto**: Buscará o default contábil cadastrado no Produto, carregando-o para a movimentação.
* **Produto/Bem**: Buscará o default contábil do Bem, definido no bem associado à este Produto.

**Natureza Orçamentária Financeira**: Buscará o default contábil da Natureza Orçamentária Financeira, utilizada na movimentação, para carregar a contabilização.

**Cliente/Fornecedor**: Aplicará o default de Contas Contábeis de acordo com cada Classificação de Conta definida no Evento Contábil, por exemplo, quando o Cliente possui contas diferentes para Fornecedor no Passivo (uma conta de Fornecedores de materiais aplicados diretamente em obras, e outra conta para Fornecedores de materiais diversos). Um mesmo fornecedor pode fornecer materiais que serão aplicados diretamente à obra e materiais diversos.

Para contabilizar de maneira correta, informa-se duas contas contábeis defaults no Cliente/Fornecedor (uma para cada situação) e, utilizando a Classificação de Contas, realizamos a contabilização para cada item, considerando se o Item é aplicação direta ou não. Além desta definição, deverá ser parametrizada uma fórmula que buscará a condição para contabilização de cada item, afim de que a fórmula executada no Item do Evento contabilize corretamente o Item de Movimento e sua respectiva Conta Contábil.

* ***Observação**:*As tabelas do Item de Movimento que existem no Movimento possuem a mesma usabilidade, porém, buscando a informação que estiver registrada no Item de Movimento.

**Aplicar Lançamento Financeiro**: buscará o default contábil cadastrado nas seguintes tabelas: Cliente Fornecedor, Filial, Centro de Custo, Departamento e Tabelas de Faturamento.

* ***Observação**:*Lembrando que, ao aplicar a contabilização do Lançamento Financeiro, serão buscados valores e dados do lançamento financeiro gerado pela movimentação, dados estes que podem diferir dos dados do movimento.

**Aplicar Pagamento:**Forma de Pagamento: Buscará o default contábil do Meio de Pagamento informado na movimentação.

**Aplicar Rateio de Centro de Custo**: Buscará o default cadastrado no rateio de Centro de Custo utilizado na movimentação. Nesta situação, será usado o rateio do Movimento se o default contábil aplicar no Movimento; e será usado o rateio do Item de Movimento se o default contábil aplicar no Item de Movimento.

**Classificação do centro de custo**: Se desejar, é possível informar a classificação no centro de custo.

* ***Observação**:* Informar a classificação da conta na conta contábil ou a classificação no centro de custo.

**Aplicar Departamento**: Poderá buscar o default contábil cadastrado em Departamento e Filial.

* ***Observação**:*Algumas combinações de parametrizações do Evento Contábil foram retiradas, por não fazerem sentido no contexto da integração contábil. São elas:
  + Quando o Item de Evento aplica em Movimento (também em Item de Movimento, Pagamento, Rateio de Centro de Custo/Departamento ou Lançamento) e possui um Item Gerencial que buscava a conta em 'Default Contábil'. Esta opção não mais existirá no sistema pois não é possível obter default para contas gerenciais a partir de uma conta contábil fixa.
  + Quando o Item de Evento aplica em Rateio de Centro de Custo/Departamento do Movimento e possui um Item Gerencial que buscava a conta em 'Rateio C.Custo/Departamento Movimento'. Esta opção não mais existirá no sistema pois seu resultado é um produto cartesiano e, assim, faz com que os cálculos não retornem valores corretos para a contabilização.

**Evento Contábil para Contrato de Arrendamento Mercantil**

Possui características idênticas as já apresentadas para o movimento, apresentando opções específicas para os campos de seleção: "Processo", "Buscar Filial/Depto em" e "Buscar Centro de Custo em", do cadastro do Evento Contábil; e para os campos: "Aplicar" e "Buscar Default em" do cadastro de Itens de Evento.
