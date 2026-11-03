---
content_hash: f70aebd762e053afba6073ef9b525bf650943e75962e2457b3a8fb03c7a1f7fe
fetched_at: '2026-06-29T00:09:25.956010+00:00'
page_id: '423938209'
product: rm
source: tdn-rm
title: 04.05 - Contratos - Gestão de Estoque, Compras e Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938209
version: 62
---

Definições Gerais

**Máscara do código do contrato**: Informe a máscara para o código do contrato.  
**Código do Produto**: Indique neste campo se a inclusão dos itens no contrato será feita através do Código Principal do Produto, Descrição, Código Reduzido, Número no Fabricante ou Código Auxiliar.

---

**Contrato 2.0**

* **Máscara do código**: Informe a máscara para o código do contrato 2.0. Exemplos: (+99) (99) 99999?-9999, 99999-999, 999.999.999-99. [Para mais informações acesse: Máscaras](https://tdn.totvs.com/pages/viewpage.action?pageId=846880352).
* **Expressão regular do código do contrato** : Informe uma expressão regular que represente a validação da máscara do contrato 2.0. [Para mais informações acesse: Expressões Regulares](https://tdn.totvs.com/pages/viewpage.action?pageId=846880352).

Obs.: os dois campos acimas obrigatoriamente deverão ser preenchido, para que o funcionamento da máscara do contrato seja realizado corretamente.

---

**Usar campos**

**Usa Número Série**: Marque esta opção se deseja utilizar Número de Série para cada item do Contrato. A cada item de Contrato incluído em Contratos/Manutenção de Contratos, deverá ser informado um Número de Série.  
**Número Série Sequencial**: Marcando este campo o sistema já preencherá o Número de Série do item de acordo com o contador indicado no campo "Tipo para Faturamento".  
**Representantes**: Marque esta opção se deseja utilizar o campo Representante no Contrato. Caso este parâmetro seja marcado passa a ser obrigatório o preenchimento de Representante na rotina .  
**Data Auxiliar no Contrato**: Marque esta opção para habilitar na tela de cadastro de Contrato uma data auxiliar que pode ser utilizada para controle do usuário.  
**Máscara do número de série**: Informe a máscara para o número de série do item de contrato.  
***Observações***:

* Se você utiliza número de série sequencial, o sistema só sequencia lizará a máscara LL/#####-###.
* Caso informe outra máscara, esta não poderá ser sequencial.

**Tipo Produto para Faturamento**: Marque esta opção para habilitar na tela de cadastro de Contrato um campo para que informe o tipo de produto para faturamento, de acordo com o cadastro incluído em Cadastro/Tabelas de Contratos/Tipo de Produto para Faturamento. Usa Funcionário Default nos Itens: Marcando esta opção o Funcionário informado para o Contrato será levado como default dos itens do Contrato.

**Funcionario default nos itens:**

---

**Rateios****Usa Rateio de Centro de Custo no Item**: Marque esta opção para habilitar na tela de cadastro do item de contrato a pasta Rateio/Centro de Custo.   
**Usa Rateio de Departamento no Item**:  Marque esta opção para habilitar na tela de cadastro do item de contrato a pasta Rateio/Departamento.

---

**Data Medição Utilizada:** Indique neste campo se a medicação do contrato será feita através da **Data Execução** do Processo ou a **Data** informada no campo data ao executar o processo de medição.

Preços

**Buscar Preços de Faturamento em:**Informe nesta pasta qual o preço do produto será utilizado como valor default para o preço de faturamento do item de Contrato.   
Poderão ser utilizados o campo: Valor do Preço no Cliente/Fornecedor do cadastro do produto ou a Tabela de Preço, exemplo:

* Insira um contrato e ao cadastrar o item escolha a opção de selecionar preço (Preço no Cliente/Fornecedor). O Sistema deverá buscar o preço que está cadastrado na pasta Cliente/Fornecedor do cadastro de produto para o item do contrato.

---

**Tabela de Preço**

Campos OpcionaisCampos Opcionais 1/2

**Contrato****Campos Livres do Contrato:**Informe o nome dos Campos Livres do Contrato.

---

**Item**  
**Campos Livres do Item:**Informe o nome dos Campos Livres do Item.

---

**Editar Campos Complementares:**• Marcando esta opção o sistema disponibilizará a utilização dos Campos Complementares no Contrato.  
***Observação**:*Os Campos Complementares de Contrato devem ser inseridos através da opção Cadastros/Campos Complementares/Contrato.

Campos Opcionais 2/2

**Editar Histórico:**Marque esta opção para editar histórico nos contratos e nos itens dos contratos.  
 **Copiar Histórico do Item de Contrato para o Item de Movimento:**Marcando esta opção ao faturar o contrato o histórico do item de contrato será copiado para o item do movimento.  
**Copiar Histórico do Contrato para o Movimento:**

* Marcando esta opção, ao faturar o contrato o histórico deste será copiado para o movimento.
* Caso mais de um contrato dê origem a um único movimento, os históricos destes contratos serão todos copiados para o movimento.

---

**Tipo Histórico**

**Histórico Curto:**Marcando esta opção o histórico a ser informado no contrato e no item poderá conter no máximo 255 dígitos.  
**Histórico Longo:**Marcando esta opção o histórico a ser informado poderá conter um número indeterminado de dígitos, dependendo da capacidade de armazenamento de seu equipamento.  
***Observação**:*Após a definição de utilização de "Histórico Longo", não será possível o retorno à opção "Histórico Curto". Já a alteração do histórico curto para o longo é possível, portanto, aconselhamos primeiro definir o trabalho utilizando o histórico curto. Se posteriormente houver necessidade de se informar para os contratos históricos com mais de 255 dígitos, isto poderá ser revertido. A utilização de histórico curto ocupará menos espaço em sua base de dados.

FaturamentoDefinições de Faturamento de Contrato 1/3

**Data Início de Operação:**Informe a data inicial de operação de contratos. Esta data será default para faturamento de contratos não periódicos e será apresentada como default no campo "Contratos iniciados a partir de:", na pasta Filtros dos Contratos/Lote de Faturamento.  
**Copiar Data de Vencimento/Medição para Movimento:**Informe neste campo a data do movimento para a qual a data do vencimento do item de contrato será copiada. As possíveis opções são: Data Extra1, Data Extra2, Data de Entrega, Data de Entrada/Saída.  
**Valor Mínimo das Notas Fiscais para Faturamento:**Informe neste campo o valor mínimo para emissão de uma nota fiscal, exemplo: Se informar neste campo 10,00, todas as notas de valor menor que 10,00 não serão faturadas.  
**Dias de Carência para Primeiro Faturamento:**Informe o número de dias default de carência para o faturamento.  
**Dias de Carência para Cancelamento do Faturamento:**Informe o número de dias default de carência para cancelamento de um contrato.  
**Dia de Término Carência:**Informe o dia para início do faturamento do contrato após os meses de carência.

Definições de Faturamento de Contrato 2/3

**Nº de Meses da Carência:**Informe o número de meses default de carência dos contratos, exemplo*:*Vamos supor que nos dois campos acima indicou: Dia final da Carência: 1 e Nº de meses da Carência: 2. Se o contrato foi fechado em Dezembro, só vai começar a faturar em 01 de Fevereiro.  
*Observações::*Caso esses parâmetros não estejam preenchidos, o sistema irá considerar os dias corridos de carência informado no campo "Primeiro Faturamento", na pasta cabeçalho do contrato. Para itens de contrato por medição, o sistema não trabalha com carência.

**Vencimento em dias fixos:**Selecionando essa opção, somente condições de faturamento múltiplas de 30 dias poderão ser visualizadas no campo "Intervalo de Faturamento". Se esta opção estiver desmarcada, serão visualizadas, além das condições de pagamentos múltiplas de 30, as demais condições, desde que tenham as seguintes características: % do valor total igual a 100, número de vezes igual a 1, prazo para a parcela diferente de 0 (zero) e intervalo igual a 0 (zero).

---

**Prioridade de origem das tabelas do movimento:**Esse parâmetro foi criado para determinar a prioridade das tabelas de classificação, dos campos Departamento, Centro de Custos e Representantes do Contrato ou do Item de Contrato, no faturamento.  
**Contrato:**Habilite este campo se desejar que o movimento gerado pelo faturamento do contrato contenha os dados: Tabelas de Classificação, Departamento, Centro de Custo e Representantes, copiados do Contrato.   
**Item de Contrato:**Habilite este campo se desejar que o movimento gerado pelo faturamento do contrato contenha os dados: tabelas de classificação, Departamento, Centro de Custo e Representantes, copiados do item de Contrato.

---

**Editar Tipo de Movimento:**Caso tenha a necessidade de faturar itens de um mesmo contrato para tipos de movimentos diferentes, marque esta opção para que você indique o tipo de movimento a ser gerado para cada item incluído no contrato. Marcando esta opção, na edição de um lote de contrato, acessado através da opção Contratos/Faturamento por Lote, aparecerá na pasta Filtro dos Contratos o campo "Tipo de Movimento". Neste campo será informado para qual tipo de movimento deverão ser faturados os itens. Assim, todos os itens do contrato incluídos através da opção Contratos/Manutenção de Contratos, que tiverem no campo "Tipo de Movimento a ser Gerado" o tipo indicado no campo "Tipo de Movimento" descrito acima, serão faturados.

**Tipo de Movimento de Compra Default e Tipo de Movimento de Venda Default:**Informe qual o tipo de movimento que será o default do contrato, ou seja, sempre que incluir um novo Contrato o campo Tipo de Movimento nos itens já virão preenchidos com o tipo aqui informado. O sistema apresentará todos os tipos de movimentos que podem ser selecionados na lista. Somente tipos parametrizados com numeração "Mostra" é que poderão ser informados como default.  
*Observações:*Caso no contrato existam outros itens com "Tipo de Movimento a ser Gerado" diferente, não serão faturados, para faturá-los é necessário acessar novamente o lote e no campo "Tipo de Movimento", indicar o tipo que deseja faturar. Desmarcando esta opção, na edição de um lote de contrato, o campo "Tipo de Movimento" não mais aparecerá na pasta Filtro dos Contratos. Este agora aparecerá na pasta Dados para os Movimentos Gerados. Sendo assim, todos os itens serão faturados para este tipo de movimento, já que nos itens do contrato também não será mais visualizado o campo "Tipo de Movimento a ser Gerado", exemplo:*:*

* Vamos supor que nos parâmetros de contrato foi informado que o campo tipo de movimento a ser gerado será editado. Assim, para cada item inserido em um contrato, deve-se informar o tipo de movimento a ser gerado para aquele item. Suponha ainda que no lote de contrato, na pasta Filtro dos Contratos, foi informado o tipo de movimento 2.2.02. O tipo de movimento servirá então como filtro, ou seja, serão faturados para este lote somente os itens de contrato que satisfaçam às condições do lote e que possuam tipo de movimento a ser gerado igual a 2.2.02.
* Vamos supor agora que o tipo de movimento a ser gerado não será editado. Desta forma, no cadastro dos itens de contrato, o campo "Tipo de Movimento a ser Gerado" não aparecerá. Suponha também que no lote de contrato foi informado agora, na pasta Dados para os Movimentos Gerados, o tipo de movimento 2.2.01. O tipo de movimento servirá agora como informação, ou seja, serão faturados para este lote todos os itens de contrato que satisfaçam às condições do lote e o tipo de movimento a ser gerado para todos estes itens será 2.2.01.
Quebra de Nota Fiscal

**Itens:**Informe se as quebras de nota devem ocorrer quando o item é Periódico ou Não Periódico.  
**Destinatário:**Informe se as quebras de nota devem ocorrer quando o Destinatário é Representante ou Cliente.

***Observações**:*

* Se na pasta identificação dos parâmetros do contrato, você marcou o campo Representante, significa que em cada lote incluído você determinará quem será o destinatário do contrato, os representantes ou os clientes, pois podem ter vários representantes e estes efetuam vendas a vários clientes. Portanto, o destino da nota será o representante, porém é o cliente quem efetuará o pagamento e o representante é quem enviará a nota ao cliente.
* Informando os campos acima, você parametrizará quais os dados do contrato que vão determinar a quebra de notas.
* Caso o destinatário selecionado for Cliente, os campos "Cliente Destino do Item" e "Condição de Pagamento do Item" são campos fixos como campos selecionados e não podem ser excluídos pois, não se pode faturar uma mesma nota para clientes diferentes e em uma mesma nota não pode existir mais que uma condição de pagamento.
* Caso o destinatário selecionado for Representante, os campos "Cliente do Contrato", "Condição de Pagamento do Item" e "Representante Destino do Item" são campos fixos como campos selecionados e não podem ser excluídos, assim como explicado na observação 1, acima. Exemplos:
* Vamos supor que você selecionou: Itens Periódicos e Destinatário: Cliente. Portanto se tiver em um contrato os seguintes itens:

| Item de Contrato | Cliente Destino | Condição de Pagamento do Item | C.C. do Item |
| --- | --- | --- | --- |
| 001 | C00001 | 30 dias | 011 |
| 002 | C00001 | 30 dias | 012 |
| 003 | C00001 | À Vista | 011 |

Cada um dos itens acima será faturado em notas diferentes, pois, apesar de mesmo cliente eles têm as diferenças:

* 001 - Tem o C.C. diferente do item 002 e a condição de pagamento diferente do 003;
* 002 - Tem o C.C. diferente do item 001 e a condição de pagamento diferente do 003;
* 003 - Tem o C.C. diferente do item 002 e a condição de pagamento diferente dos itens 001 e 002.

Se em um contrato tiver os seguintes itens:

| Item de Contrato | Cliente Destino | Condição de Pagamento do Item | C.C. do Item |
| --- | --- | --- | --- |
| 001 | C00001 | 30 dias | 011 |
| 002 | C00001 | 30 dias | 012 |
| 003 | C00001 | À Vista | 011 |
| 004 | C00001 | À Vista | 011 |

Os itens acima serão faturados em duas notas diferentes sendo:

1
incomplete
Os itens 001 e 002 serão faturados em uma única nota, pois, eles têm as mesmas características;

2
incomplete
Os itens 003 e 004 serão faturados em uma única nota, pois, eles têm as mesmas características.

4
incomplete
A única diferença entre os itens 001 e 002 dos itens 003 e 004 é a condição de pagamento.
Tabelas 1/4

**Editar Seção, Centro de Despesa, Contratos Vendedor, Portador e Natureza de Gasto:**Defina quais serão as tabelas que entrarão nos Contratos e os seus valores defaults.

Tabelas 2/4

**Editar Tipo, Status do Produto, Classe, Tabela de Estoque 4 e Tabela de Estoque 5:**Defina quais serão as tabelas que entrarão nos Contratos e os seus valores defaults.

Tabelas 3/4

**Edição Funcionário (número), Título do funcionário (número):**Esses parâmetros controlam a visibilidade e os títulos dos campos de funcionários e de % comissão dos contratos de Natureza: Compras e Arrendamento Mercantil.

Tabelas 4/4

**Edição Funcionário (número), Título do funcionário (número):**Esses parâmetros controlam a visibilidade e os títulos dos campos de funcionários e de % comissão dos contratos de Natureza: Vendas.

Reajuste Automático

**Tipo de Arredondamento do Valor Reajustado**: Informe o tipo de arredondamento do cálculo do valor do item de contrato (Não Arredonda, Dezena, Centavos, Centena).  
**Percentual Máximo de Reajuste dos Aditivos**: Defina qual será o Máximo percentual de reajuste dos aditivos.  
**Limite de Reajuste**: Limite em valor de arredondamento. Para dezena o máximo é 9 e para centavos e centenas o máximo é 99.

Workflow Fluig

Usa Aprovação: ao escolher a opção "Usa" estará disponível o processo de [geração de workflow no Fluig a partir de Contratos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938705).   
***Importante!!!*** Para a utilização da integração com o Fluig é necessário configurar em Parâmetros | Globais |Integração Fluig informando o Endereço do Servidor do Fluig, Usuário/Senha do administrador do Fluig e Id da Empresa do Fluig.  
Para maiores informações sobre a instalação e configuração do Fluig, [clique aqui](http://tdn.totvs.com/display/public/fluig/Home).  
Geração Automática de Workflow: Quando este parâmetro estiver marcado, ao incluir um contrato com um [tipo de contrato](http://tdn.totvs.com/display/LRM/Tipos+de+Contratos) que gera workflow, após salvar o contrato será gerado automaticamente o workflow no Fluig.  
Caso esse parâmetro esteja desmarcado, é habilitado na visão de [Manutenção de Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=423938074) processo "Geração de Workflow Fluig para Contrato", dessa forma somente será gerado o workflow no Fluig após selecionar o Contrato e executar esse processo.

ContabilidadeContabilidade 1/3

**Habilita Evento Contábil:**

* Não Usa evento.
* Usa Evento: Por esta opção o evento contábil será buscado diretamente no parâmetro **Evento Default** do item de contrato.

**Edição da Contabilização:**

* Edita: O sistema dará acesso à contabilização do contrato e o usuário poderá efetuar qualquer alteração que for necessária.
* Mostra: A contabilização somente será mostrada ao usuário sem que seja possível a alteração na mesma.

---

**Contabilização Obrigatória:**Marcando esta opção o contrato de Arredamento Mercantil só poderá ser salvo após serem indicados os eventos contábeis.

* ***Observação**:*Se o campo acima estiver marcado, não será permitida exclusão da contabilidade do movimento.

---

**Item de Contrato**

**Evento Default:** Informe qual evento contábil para ser utilizado no item de contrato. Estes eventos já deverão estar cadastrados através do menu **Cadastro/Contabilidade/Eventos Contábeis**.

**Código do Lote Contábil:** Informe qual o código do lote contábil.

**Código do Lote para Estorno:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados do item de contrato.

Contabilidade 2/3

**Reclassificação Contábil**

**Evento Default:** Informe qual evento contábil para ser utilizado para reclassificação contábil. Estes eventos já deverão estar cadastrados através do menu **Cadastro/Contabilidade/Eventos Contábeis**.

**Código do Lote Contábil:** Informe qual o código do lote contábil.

**Código do Lote para Estorno:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados para reclassificação.

---

**Reajuste do Contrato**

**Evento Default:** Informe qual evento contábil para ser utilizado no reajuste do contrato. Estes eventos já deverão estar cadastrados através do menu **Cadastro/Contabilidade/Eventos Contábeis**.

**Código do Lote Contábil:** Informe qual o código do lote contábil.

**Código do Lote para Estorno:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados para reajuste do contrato.

* ***Observação**:*Para cada um dos códigos de Lote definidos, caso o mesmo já possua registro na base de dados (chave composta pelo código da coligada + código do lote, da tabela de lotes do Contábil), será definido para este item em específico. Caso contrário, será criado um novo Lote com o código inserido nos respectivos campos e nomenclatura conforme funcionalidade à qual o item está destinado.
Contabilidade 3/3

Campos relacionados ao Contrato 2.0.

Aba Lotes

**Inclusão:** Informe qual o código do lote contábil de inclusão do contrato.

**Estorno Inclusão:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados para inclusão do contrato.

---

**Aditivo:** Informe qual o código do lote contábil de aditivo do contrato.

**Estorno Aditivo:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados para aditivo do contrato.

---

**Reajuste:** Informe qual o código do lote contábil de reajuste do contrato.

**Estorno Reajuste:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados para reajuste do contrato.

---

**Medição:** Informe qual o código do lote contábil de medição do contrato.

**Estorno Medição:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados para medição do contrato.

---

**Reclassificação:** Informe qual o código do lote contábil de reclassificação do contrato.

**Estorno Reclassificação:** Informe neste campo o código do lote contábil que guardará os lançamentos estornados para reclassificação do contrato.

---

**Baixa:**Informe qual o código do lote contábil para a baixa do contrato.

Aba Datas Defaults

**Data Inclusão:** Informe qual a default para contabilização de inclusão do contrato.

Opções

* Sistema - Data de execução do processo
* Data Contrato - Data do contrato
* Data Início Vigência

---

**Data Aditivo Valor/Quantidade:** Informe qual a default para contabilização de aditivo de valor/quantidade do contrato.

Opções

* Sistema - Data de execução do processo
* Data Assinatura - Data Assinatura informada no processo
* Data Início Vigência

**Data Aditivo Prazo:** Informe qual a default para contabilização de aditivo de prazo do contrato.

Opções

* Sistema - Data de execução do processo
* Data Assinatura - Data Assinatura informada no processo

**Data Reajuste:** Informe qual a default para contabilização de reajuste do contrato.

Opções

* Sistema - Data de execução do processo
* Data Reajuste - Data Reajuste informada no processo

**Data Medição:** Informe qual a default para contabilização de medição do contrato.

Opções

* Sistema - Data de execução do processo
* Data Medição - Data Medição informada no processo

**Data Reclassificação:** Informe qual a default para contabilização de reclassificação do contrato.

Opções

* Sistema - Data de execução do processo
* Último Dia Mês Corrente - Último dia do mês corrente

**Data Baixa:**Informe qual a data default para a contabilização da baixa do contrato.

Opções

* Sistema - Data de execução do processo
* Data Baixa - Data da baixa contábil
Patrimônio

**Motivo Baixa Total:** Informe o Motivo de Baixa utilizado para integração com patrimônio, este motivo será utilizado durante o cancelamento do contrato.

**Motivo Baixa Parcial:**  Informe o Motivo de Baixa utilizado para integração com patrimônio, este motivo será utilizado por ex. durante o processo de aditivo com redução de valor do item do contrato.
