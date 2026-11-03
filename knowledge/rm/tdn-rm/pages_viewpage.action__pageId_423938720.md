---
content_hash: 5308697104e52c37beada8914e69230fad222a6b85be20a9e1bef7083d2673af
fetched_at: '2026-06-29T00:09:28.593125+00:00'
page_id: '423938720'
product: rm
source: tdn-rm
title: Estrutura Transferência de Grupos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938720
version: 15
---

A partir da versão **12.1.2306** a Transferência de Grupos Contábeis passa a ser um processo **multicoligada**, ou seja, é possível cadastrar estruturas/moldes e utilizar os processos para várias coligadas diferentes, sem ter que fazer a troca de contexto.

As transferências entre grupos contábeis poderão ser realizadas sempre que necessárias, movimentando contas sintéticas com grande facilidade ou grupos de contas conforme eventuais necessidades exigidas no controle das rotinas contábeis.

O sistema prevê dois tipos de transferências, que devem ser realizadas com finalidades distintas:  
  
**Apuração de Resultado do Exercício** deve ser executado com o objetivo de se apurar o resultado da empresa, ou seja, o lucro ou o prejuízo do exercício. Esta apuração consiste em encerrar as contas de receitas e despesas**/**custos, fazendo lançamentos contrários aos saldos apurados em cada uma delas, de modo  a deixá-las com saldo igual à zero, tendo como contra partida a conta de apuração de resultado do exercício. Após esta transferência, se o saldo da conta de apuração de resultado do exercício for credor, indica que a empresa teve um lucro, se for devedor, indica que a empresa teve um prejuízo.

**Transferência de Saldo** deve ser executado com o objetivo de transferir os saldos de determinadas contas ou grupos de contas, deixando-as também com saldo igual à zero, mas tendo como contra partida não uma conta de resultado de exercício e sim outra conta contábil de acordo com necessidade específica de cada empresa. O objetivo deste tipo de transferência não é a apuração de resultado do exercício, pode por exemplo ser utilizado para a transferência de saldo de um grupo denominado 'Estoque de produtos em elaboração' para o grupo 'Estoque de Produtos Acabados'.

Exemplos

---

### Cadastro da Estrutura

Para cada transferência a ser executada, deve-se cadastrar uma **estrutura**, informando-se a coligada, código da estrutura, descrição e o tipo de operação à qual será destinada.   
Cada estrutura, por sua vez, deverá ter cadastrado um ou vários **moldes** onde serão definidas as formas como cada apuração ou transferência deverá ser realizada.

Após o cadastro da estrutura e suas parametrizações, deve-se executar o processo de Execução de Transferência de Grupos Contábeis para que os lançamentos propriamente ditos de apuração ou transferência sejam gerados.

Observação: O processo só irá considerar departamentos caso o usuário marque nos parâmetros do sistema, uma opção para que os departamentos seja considerados na transferência de grupos contábeis.

Atenção

Não será permitida a alteração em estruturas de Transferência de Grupos Contábeis já processadas e para as quais existam históricos de Transferência Executada. Neste caso, para que a alteração na estrutura seja liberada, será preciso antes, executar o processo para Desfazer a Transferência de Grupos Contábeis.

---

**Cadastro de Molde de Transferência de Grupos Contábeis  
  
Todos os campos do molde são filtrados pela coligada informada na estrutura.**Dentro de uma estrutura podem ser incluídos vários moldes, cada um com suas parametrizações. Não será permita, porém, a inclusão de um novo molde, com mesma Data de apuração e mesma Filial de Origem, se neste for informada uma conta de origem que já esteja indicada em outro molde da mesma estrutura, ou que esta conta pertença a um grupo indicado em outro molde da mesma estrutura.  
   
**Exemplo**  
Molde 1 - Conta origem 4            - Será permitida a inclusão do molde  
Molde 2 - Conta origem 3.01       - Será permitida a inclusão do molde  
Molde 3 - Conta origem 3.02       - Será permitida a inclusão do molde  
Molde 4 - Conta origem 3.01.01  - Não será permitida a inclusão do molde, pois a conta 3.01.01 pertence ao grupo 3.01 já utilizado no Molde 2

Em cada molde devem ser definidos:

* **Data***:* Data em que na serão contabilizadas as transferências.
* **Grupo de contas**: devem ser informados todos os grupos de contas de origem, ou seja, as contas contábeis que serão zeradas a partir da geração do lançamento de transferência. Em um mesmo molde não há limite na quantidade de grupos de contas a serem indicadas para a transferência.
* **Contas de Origem**:Os saldos das contas indicadas como Contas de Origem serão apurados até a data informada no molde**,** para em seguida serem transferidos. Os saldos das contas de origem serão apurados levando-se em consideração a data de apuração, filial, centro de custo, contas gerenciais e departamento utilizadas.
* **Moeda Funcional:** Essa opção só será exibida se o usuário utilizar moeda funcional, a opção de utilizar moeda funcional está disponível nos parâmetros gerais do sistema.  
  Quando o usuário marcar o parâmetro para que seja utilizado moeda funcional, será exibido no cadastro de molde uma opção "Moeda Funcional". Tal opção consiste em realizar a apuração das contas de resultado que controlam moeda funcional separadamente, transferindo o saldo para uma conta patrimonial que também controla moeda funcional.  
  Exemplo:  
  A opção "moeda funcional" não foi selecionada.  
  Na origem foi informado o grupo 3, que representa:  
  3          RECEITAS  
  3.001    RECEITA DE VENDA DE MERCADORIA  
  3.002    PRESTAÇÃO DE SERVIÇO  
  3.003    RECEITAS DE APLICAÇÕES FINANCEIRAS - ESTÁ INFORMADA NOS PARÂMETROS DE MOEDA FUNCIONAL  
  Mesmo que esteja informada como conta de origem o grupo 3 (Sintético), a conta 3.003 não terá seu saldo apurado pelo processo, pois se trata de uma conta que controla moeda funcional. Neste caso deverá ser criado um novo molde marcando a opção de moeda funcional para que a conta 3.003 seja apurada separadamente, transferindo o seu saldo para uma conta patrimonial que também controle moeda funcional.  
  **Atenção**: Se a Data de apuração ou Filial de Origem for diferente será permitida a informação de qualquer conta no grupo de conta de origem.

* **Tipo de Transferência**: Indica como o lançamento da transferência será realizado. Veja as possibilidades:   
    
  **Origem -> Destino:** Neste tipo de transferência, o saldo apurado nas contas indicadas como Contas de Origem, independente se credor ou devedor, serão transferidos para a conta indicada como conta de Destino.  
   **Origem -> Destino -> Receptoras:** Neste tipo de transferência, o saldo apurado nas contas indicadas como Contas de Origem, independente se credor ou devedor, serão transferidos para a conta indicada como conta de Destino. Em seguida será verificado o saldo desta conta de Destino. Se o saldo da conta Destino for *credor*, será gerado um lançamento debitando a conta Destino e creditando a conta Receptora de saldo a crédito. Se o saldo da conta Destino for *devedor*, será gerado um lançamento creditando a conta Destino e debitando a conta Receptora de saldo a débito. Neste tipo de transferência é necessário indicar a Filial receptora do lançamento final. Para exemplos clique aqui.  
  **Observação:**Este tipo de transferência **não** deve ser utilizado caso o centro de custo seja enviado na ECD.   
  Quando é gerado o lançamento para a conta receptora não é possível recuperar o centro de custo, sendo assim, caso utilize este tipo irá gerar erro no registro J100,   
   já que os saldos inicial e final não irão ser compatíveis com a movimentação indicada pelo registro I155 que irá conter o centro de custo.  
    
  **Origem -> Receptoras:** Neste tipo de transferência, se a conta Origem tiver um saldo credor, será gerado um lançamento debitando a conta Origem e creditando a conta Receptora de saldo a crédito. Se a conta Origem tiver um saldo devedor, será gerado um lançamento creditando a conta Origem e debitando a conta Receptora de saldo a débito. Para exemplos clique aqui.
* **Transferir Rateio Gerencial**: Através dessa opção é possível definir se o lançamento gerado pela transferência irá ou não respeitar os rateios dos lançamentos de origem.  
    
  Marcando esta opção, o lançamento gerado pela transferência irá respeitar os rateios dos lançamentos de origem, desta maneira os saldos das contas gerenciais serão transferidos ou zerados. Neste caso é necessário informar uma conta gerencial para ajustes. Essa gerencial será usada apenas nos casos de contas contábeis que exigem rateio, mas que possuem saldo anterior na base e o mesmo não está rateado, então existindo este saldo anterior o mesmo será rateado para a conta gerencial de ajustes que foi informada.  
    
  Deixando esta opção desmarcada, o lançamento de transferência gerado terá, quando necessário, um rateio em 100% na gerencial que deve ser informada para o rateio, assim as contas gerenciais de origem não terão seu saldo  transferido ou zerado. No lançamento de transferência, todas as contas contábeis que possuírem distribuição gerencial irão utilizar a conta gerencial informada para o rateio.  
    
  **Exemplo**Os rateios dos lançamentos de origem estão nas contas gerenciais 5.01, 5.02 e 5.03, sendo que a conta gerencial para ajuste informada foi a conta 5.08. Ao executar a transferência de saldos, com a opção "Transferir Rateio Gerencial" *marcada*, o lançamento gerado pela transferência terá rateio igual aos lançamentos de origem utilizando as mesmas contas gerenciais 5.01, 5.02 e 5.03. Com a opção " Transferir Rateio Gerencial " *desmarcada*, os saldos gerenciais apurados terão um rateio de 100% na conta gerencial 5.08.  
  **Observações**Se a opção " Transferir Rateio Gerencial " estiver marcada será mostrado no campo abaixo a opção de "Conta Gerencial para Ajuste". Se estiver desmarcada, será mostrado "Conta Gerencial para Rateio".  
  Para obter mais informações sobre transferência de rateios gerenciais clique aqui.
* **Histórico Padrão**:Todo molde deve possuir um *Histórico*. O histórico a ser utilizado para os lançamentos de transferência respeitarão o tipo de operação escolhido na tela inicial de cadastro de estruturas:   
    
  **"Apuração de Resultado do Exercício"**: será permitido informar apenas históricos cadastrados como histórico fechamento. Cada apuração de resultado do exercício processada deve possuir um histórico de fechamento próprio, cadastrado única e exclusivamente para este fim. Se a apuração for anual deve-se ter um histórico de fechamento para esta apuração. Se a apuração for semestral ou trimestral, deve-se ter um histórico de fechamento distinto para cada semestre ou trimestre, pois não será permitida a utilização de um histórico de fechamento já utilizado anteriormente em outro molde. Porém, se para a apuração de resultado de um mesmo período for utilizado mais de um molde (por exemplo, um molde para as despesas e outro para as receitas), neste caso será permitida a utilização do mesmo histórico de fechamento no cadastro destes moldes, pois estes terão datas iguais de apuração e estarão dentro da mesma estrutura.  
    
   **"Transferência de Saldo"**: *não* será permitido informar históricos de fechamento.  
    
  Isto é necessário, pois ao gerar o SPED Contábil o sistema precisa ter informações sobre os tipos de lançamentos, distinguindo-os em lançamentos normais e de encerramento do exercício.

---

Processos

* Execução de Transferência de Grupos Contábeis.
Anexos

* Histórico do Processo da Transferência de Grupos Contábeis.
