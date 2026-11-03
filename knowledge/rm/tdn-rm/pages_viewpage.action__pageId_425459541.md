---
content_hash: 658f60b0d700a286afc2eef98f0b634add293a54c4f7470f4e838b74674787fd
fetched_at: '2026-06-29T00:09:36.920804+00:00'
page_id: '425459541'
product: rm
source: tdn-rm
title: Financeiro - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459541
version: 101
---

---

Antes de mandarmos gerar o lançamento financeiro da parcela é preciso parametrizar o sistema (Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional) com as informações necessárias para a inclusão de lançamentos no sistema financeiro. Muitas das informações utilizadas nos parâmetros do sistema educacional já devem ter sido cadastradas e bem definidas dentro do próprio sistema financeiro, sendo apenas indicada nos parâmetros do sistema educacional a sua utilização.  
A geração do lançamento financeiro da parcela, além de promover a integração com o sistema financeiro, pode simultaneamente, promover a integração com o sistema contábil. Ambas integrações devem ser previamente parametrizadas.

Ao alterar alguma informação será gravado o  essa tela fica em Anexo do cadastro de Serviço.

Fin - Geral 1/4

**- Cobrar multa**Define qual será o comportamento do sistema em relação à multa quando uma parcela estiver vencida. Se será aplicada uma multa e se esta levará em conta as bolsas ou descontos para cálculo do valor.

**- Juros ao dia**  
Também é possível definir o percentual de juros ao dia para parcelas vencidas e qual será o período de carência para início do cálculo dos juros.

**- Permite regerar lançamentos**Marcando esse parâmetro será possível regerar os lançamentos financeiros 'Em Aberto', provenientes das parcelas dos contratos. Esse parâmetro é importante, por exemplo, para o caso de uma Bolsa ser concedida à um aluno após a geração das parcelas.

**- Regerar lançamentos cancelados**  
Permite que os lançamentos financeiros 'Cancelados' possam ser regerados.  
**Observação:** Para que os parâmetros anteriores 'Permite Regerar Lançamentos' e 'Regerar Lançamentos Cancelados' possam ser aplicados em lançamentos financeiros originados de parcelas que foram calculadas utilizando o resultado da divisão do total dos valores dos créditos das disciplinas matriculadas entre as parcelas do contrato, o parâmetro *'Permite Regerar Lançamentos utilizando a divisão de créditos entre as parcelas do contrato'* precisa estar marcado.

**- Utilizar faixa de crédito**   
Para que o cálculo do valor do lançamento seja feito conforme uma faixa de crédito este parâmetro deverá estar *marcado*. Após somar o número de créditos que o aluno está cursando, o sistema irá localizar a faixa de crédito, previamente cadastrada, à qual o aluno pertence. Se não houver a faixa, o sistema irá reportar um erro.   
Caso a faixa seja encontrada, o valor deverá ser calculado da seguinte forma:  
**- Valor Fixo:** se o Valor Fixo estiver informado na faixa de crédito, este será o valor do lançamento.  
**- Valor por Crédito:** se o valor fixo não estiver informado, então o sistema irá multiplicar o número de créditos que o aluno está cursando pelo Valor por Crédito informado na faixa à qual o aluno pertence.  
**Observação:**  
Para que o valor possa ser calculado pelo número de créditos cursados, primeiramente a opção *'Conta créditos financeiros (cobrança por créditos)*' localizado na *situação de matrícula* do aluno deve estar marcada. Em seguida, no contrato do aluno, para cada parcela cadastrada, a opção *'Valor calculado pelo número de créditos'* também deve estar marcada. Se assim for, o sistema irá verificar o número de créditos que o aluno está cursando e efetuar o cálculo necessário para se encontrar o valor do lançamento. Este cálculo então poderá será feito a partir de: uma *faixa de crédito* ou então, a partir do *número e valor do crédito financeiro das disciplinas da matriz curricular*.

**- Cancelar Remessa automaticamente ao regerar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado**  
Com este parâmetro *marcado* ao regerar um lançamento pelo TOTVS Educacional em que o status do boleto seja igual a ‘Remetido’ ou ‘Registrado’ o sistema automaticamente executará o cancelamento desta remessa, modificando o status de remessa do boleto para ‘Pendente Remessa’ e prosseguirá com a regeração do lançamento. Ressaltamos que, posteriormente, no módulo *TOTVS Gestão Financeira*, será necessário enviar para o banco uma nova remessa destes boletos.  
Com este parâmetro *desmarcado*, não será permitida a regeração de tais lançamentos através do TOTVS Educacional pois os seus boletos possuem status de remessa igual à ‘Remetido’ ou ‘Registrado’.

**- Copiar mês/ano da data de vencimento para a data de competência**Com este parâmetro marcado, os lançamentos financeiros gerados terão data de competência igual ao mês/ano da data de vencimento da parcela. Com o parâmetro desmarcado, os lançamentos financeiros gerados terão a data de competência igual à data de competência da parcela.

**- Gerar lançamentos de bolsa de crédito como Baixa Contábil**Para que os lançamentos referente à bolsa de crédito sejam contabilizados somente na baixa, este parâmetro deve estar *marcado*, com isso o tipo contábil do lançamento será igual a "Baixa contábil", independente do valor setado no parâmetro de tipo contábil para bolsa de crédito da etapa Fin - Geral 2/4 e o parâmetro de tipo contábil para bolsa de crédito ficará bloqueado.  
**Observação:**A partir da versão 12.1.23 o parâmetro "Gerar lançamento de bolsa de crédito como Baixa Contábil" **não existirá** no sistema e passará a ser considerado o parâmetro da etapa Fin - Geral 2/4

**- Dividir valores de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato**Este parâmetro terá efeito para plano de pagamento que calcula o valor do contrato/parcelas em função do número de créditos informados nas disciplinas cursadas.  
Se este parâmetro estiver marcado o valor total encontrado para o contrato será rateado entre as parcelas não geradas, subtraindo o valor das parcelas já geradas no mesmo contrato. Se estiver desmarcado, as parcelas terão o mesmo valor encontrado para o contrato.

**- Usar valor do crédito financeiro da matriz curricular do aluno**Para que o sistema calcule o valor do lançamento tomado como base o valor do crédito financeiro da matriz curricular do aluno (matriz em que ele está matriculado), este parâmetro deve ser *marcado*. Caso esteja *desmarcado*, o valor do crédito será o valor de onde o aluno está cursando as disciplinas.

**- Usar número de créditos financeiro da matriz curricular do aluno**Para que o sistema calcule o valor do lançamento tomando como base o número de créditos financeiro da matriz curricular do aluno este parâmetro deve ser marcado. Caso esteja *desmarcado*, o número do crédito será o valor de onde o aluno está cursando as disciplinas.

**- Usar nº créditos e valor do crédito da disciplina da matriz curricular do aluno ou da faixa de credito em caso de equivalência múltipla**Com esse parâmetro marcado, o valor da disciplina matriculada será substituída pelo valor da disciplina equivalente da matriz curricular do aluno.  Assim, em caso de equivalência múltipla o sistema não processará o valor e n° de crédito das disciplinas matriculadas, será utilizado o valor total equivalente das disciplinas da matriz curricular do aluno. Caso esteja desmarcado, o crédito será o valor de onde o aluno está cursando as disciplinas.

**Observação:**

* Matricula em uma disciplina com equivalência para duas disciplinas da matriz do aluno: o sistema considera a disciplina com maior número de crédito e a disciplina com maior valor do crédito da matriz do aluno.
* Matricula em duas disciplinas com equivalência para uma da matriz do aluno: o sistema considera o número de crédito e valor do crédito da disciplina da matriz do aluno. Logo, uma das disciplina matriculadas assumirá o total dos créditos enquanto a outra ficará zerada.

Para maiores informações sobre utilizar valor e número de crédito do aluno veja o documento .

**- Desconsiderar nº de créditos na matrícula da disciplina para geração e simulação de lançamento**

Com esse parâmetro marcado, o sistema irá desconsiderar o número de créditos financeiros presente na matrícula da disciplina do aluno calculado durante a matrícula. E irá calcular novamente o número de créditos financeiros para a matrícula da disciplina na geração e simulação do lançamento financeiro vinculado à parcela do contrato do aluno. Parâmetro disponível a partir dos patches: **12.1.2302.185 e 12.1.2306.130 ou superiores**

**- Baixar automaticamente lançamentos com valor líquido igual a zero**Em alguns casos é possível que um lançamento seja gerado pelo educacional com valor zerado, como por desconto de bolsa ou alunos com crédito na instituição com desconto em mensalidade futura. Marcando o parâmetro, os lançamentos serão baixados automaticamente, salvo quando o cliente/fornecedor tiver configurado com dados de pagamento como "Débito Automático" o lançamento financeiro gerado não será baixado.

Fin - Geral 2/4

Nesta etapa é possível configurar vários campos pertinentes ao lançamento financeiro que será gerado pelo TOTVS Educacional no TOTVS Gestão Financeira.

**- Histórico:** Informe a máscara de histórico que será convertida e gravada no lançamento financeiro, para compor o histórico poderão ser utilizadas tag's e esta informação não é obrigatória.

Tags para o campo de Histórico

As tag's são recursos que permitem ao usuário adicionar alguma informação acadêmica ou financeira específica do TOTVS Gestão Educacional no campo de Histórico, c[lique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425458850) para ver a listagem das tag's

**Observação:**A letra 'X' das variáveis serve para indicar qual bolsa será utilizada.  
Vamos supor que no contrato do aluno existem 2 bolsas associadas. Para que as duas bolsas sejam referenciadas no histórico, inclua a variável duas vezes e substitua o 'X' pelo número de ordem da bolsa.

**Exemplo:**  
Bolsas associadas: 'FIES' e 'Aproveitamento'  
Para que no lançamento financeiro seja impresso o nome das duas bolsas e seus valores, inclua no campo uma variável para cada bolsa e indique o número correspondente: \[BOL.D1\] = \[BOL.V1\] - \[BOL.D2\] = \[BOL.V2\]

**- Moeda**  
Selecione a moeda a ser considerada na geração dos lançamentos financeiros.

**- Tipo de documento**  
O tipo de documento é um cadastro feito dentro do sistema financeiro. O tipo de documento a ser utilizado pelo sistema educacional dever ser do tipo 'A Receber' ou 'A Receber e a Pagar'.  
Informe se o tipo de documento será indicado no **Tipo de documento por serviço** (neste caso, cada Serviço utilizado deverá conter a informação do tipo de documento a ser utilizado no lançamento financeiro e neste caso, se algum Serviço ficar sem esta informação, ocorrerá erro na geração do lançamento financeiro) ou se será utilizado um **Tipo de documento padrão** (neste caso escolha um tipo de documento para que todos os lançamentos a serem gerados o utilizem).

**- Utilizar conta caixa**A 'Conta Caixa' é um cadastro feito dentro do sistema financeiro e contém informações importantíssimas para a gestão financeira e integração bancária, tais como Banco, Agência, Conta Corrente, Convênio, Layout Bancário etc. e que são obrigatórios na geração de qualquer lançamento financeiro. As empresas podem relacionar-se com diversos bancos e de diversas maneiras, por isto temos que indicar ao sistema aonde encontrar os dados bancários no momento da geração dos lançamentos financeiros. Para uma maior flexibilização do sistema, a Conta Caixa a ser utilizada pode ser indicada dentro dos defaults de vários cadastros. Selecione o local desejado e certifique-se de que no local selecionado a Conta Caixa foi informada corretamente.

Se o local utilizado for a **'Conta caixa default'**, o campo **'Conta caixa padrão'** será habilitado para que a conta seja informada e, desta forma, todos os lançamentos gerados a partir do TOTVS Educacional utilizarão os dados bancários informados nesta Conta Caixa.  
Se o local utilizado for **'Default do responsável financeiro'**, certifique-se de que a conta caixa seja informada no cadastro de cada responsável financeiro.  
Se o local utilizado for **'Default do serviço'**, certifique-se de que a conta caixa seja informada no cadastro de cada serviço do educacional.  
Se o local utilizado for **'Default parametrizações por curso'**, certifique-se de que a conta caixa seja informada no cadastro de cada parametrização por curso.  
Quando se tratar de **matrícula isolada**, onde os contratos dos alunos não são relacionados à nenhuma parametrização por curso, a conta caixa a ser utilizada na geração dos lançamentos deverá ser indicada no campo **'Conta caixa padrão (Disciplinas Isoladas)'**.

**- Tipo contábil:**  
Esta opção determina qual o tipo contábil do lançamento.  
**Tipo contábil por serviço:** quando esta opção estiver marcada o sistema vai considerar na geração de lançamento o tipo contábil cadastrado no serviço.  
Se esta opção estiver desmarcada, o lançamento será gerado com o tipo contábil definido no parâmetro "Tipo contábil padrão".  
**Tipo contábil bolsa de crédito:** determina qual o tipo contábil do lançamento da bolsa de crédito. Se este parâmetro não for preenchido o tipo contábil do lançamento da bolsa de crédito será o mesmo tipo contábil do lançamento do aluno. Para maiores informações veja o [Documento técnico](http://tdn.totvs.com/pages/viewpage.action?pageId=415724236).  
**Observação:**- Se no cadastro da bolsa de crédito o campo “Tipo contábil do lançamento do outro sacado” estiver preenchido o lançamento será gerado considerando o tipo contábil definido no cadastro.  
- Se o parâmetros "Gerar lançamentos de bolsa de crédito como Baixa Contábil" da etapa Fin - Geral ¼ estiver marcado o lançamento da bolsa de credito será gerado como "Baixa Contábil" independente do que for parametrizado na opção "Tipo contábil bolsa de crédito".

**- Centro de custo**O Centro de Custo é uma informação que pode ser obrigatória ou não dentro dos lançamentos. Esta obrigatoriedade ou não é definida dentro dos parâmetros do sistema financeiro. A utilização do Centro de Custo no lançamento financeiro terá o seguindo o seguinte comportamento:  
Se o Contrato do aluno possuir Centro de Custo, então o sistema irá utilizá-lo. O caso mais claro da utilização do centro de custo no contrato é de matrícula em disciplina isolada. Neste caso o aluno não tem uma matrícula no período letivo, consequentemente não possui uma turma específica nem uma matriz aplicada.  
Caso o Centro de Custo do contrato não esteja valorado, então o sistema irá verificar o parâmetro para carregar o Centro de Custo para o lançamento, podendo ser:

* **Por Matriz Aplicada:**  
  O sistema buscará o Centro de Custo da matriz aplicada associada ao contrato. Se a informação for obrigatória, e se a matriz aplicada do contrato ou seu Centro de Custo, não tiverem sido valorados, o sistema irá gerar um erro.
* **Por Turma:**  
  O sistema irá verificar a turma associada à matrícula do aluno no período letivo e pegar o Centro de Custo associado à mesma. Se a informação for obrigatória, e se a turma da matrícula no período letivo ou seu Centro de Custo, não tiverem sido valorados, o sistema irá gerar um erro.

**- Aplicação de Bolsa**  
Define onde o sistema irá buscar as informações sobre o comportamento das bolsas concedidas aos alunos, podendo ser:

* **Contrato:**  
  Se esta opção estiver marcada, dentro do Contrato do aluno deveremos informar o *Tipo de Bolsa* que determinará o comportamento para todas as bolsas que forem incluídas no contrato do aluo, podendo ser:

**- Somar bolsas**  
Soma os percentuais e/ou valores das bolsas para uma determinada parcela.  
**- Aplicar bolsas em cascata**  
Será aplica as bolsas sobre a parcela sequencialmente, de acordo com uma ordem que poderá ser definida pelo usuário.  
Ao selecionar este comportamento para o contrato, o sistema habilitará o campo "Ordem" no cadastro de "Concessão de bolsas" do contrato, permitindo informar qual será a ordem para aplicação em cascata das bolsas. Quando existirem bolsas com mesma "Ordem", o sistema aplicará primeiro a bolsa de menor código.  
**- Aplicar somente a maior bolsa**  
Será aplicada somente a bolsa que acarretará o maior desconto. Caso haja duas bolsas com o mesmo valor, a bolsa aplicada será a de menor código.  
Para descobrir qual será a maior bolsa, o sistema calcula o valor de cada bolsa sobre o valor da parcela, sem subtrair o desconto, uma vez que este valor poderá sofrer alterações em outro sistema. No momento de aplicar a bolsa, entretanto, primeiro é aplicado o desconto e depois a bolsa.

* **Classificação de Bolsa:**  
  Se esta opção estiver marcada, os *Tipos de Bolsas* serão informados dentro do próprio cadastro de Bolsa, com isto teremos maior flexibilidade, permitindo que no mesmo contrato sejam concedidas bolsas de diferentes tipos.

**- Somar bolsas de mesma ordem e tipo de aplicação em cascata**  
Quando este parâmetro estiver *marcado* e o tipo de aplicação para as bolsas for *Cascata*, as bolsas do tipo cascata que forem definidas com a mesma ordem de aplicação (tanto na 'classificação de bolsa' como no 'contrato') terão primeiramente suas porcentagens ou valores somados para depois serem aplicados sobre o valor base da parcela.  
Se este parâmetro estiver *desmarcado*, as bolsas serão aplicadas uma a uma, sequencialmente, sobre as parcelas, conforme as ordens de aplicação. Quando existirem bolsas com mesma "Ordem", o sistema aplicará primeiro a bolsa de menor código.

**- Considerar desconto por antecipação para Somar Bolsas**  
Este parâmetro apenas ficará habilitado se a opção definida anteriormente para Aplicação de bolsa for por 'Contrato'.  
Quando este parâmetro estiver *marcado* o sistema irá subtrair o valor do Desconto por Antecipação do valor base no cálculo dos valores de bolsas quando o tipo da bolsa for Somar Bolsas.

**- Considerar desconto por antecipação para Maior Bolsa**  
Este parâmetro apenas ficará habilitado se a opção definida anteriormente para Aplicação de bolsa for por 'Contrato'.  
Quando este parâmetro estiver *marcado* o sistema irá subtrair o valor do Desconto por Antecipação do valor base no cálculo dos valores de bolsas quando o tipo da bolsa for Aplicar somente a maior bolsa.

**- Contabilização**  
**Data de Contabilização** Pode ser definida a data de contabilização conforme os valores abaixo:         
- Padrão do RM Fluxus: Data padrão da contabilização de inclusão a receber conforme parâmetro do Totvs Gestão Financeira (Contas a Receber -> Manutenção de Lançamentos -> Contab. Inclusão Receber -> Data default de inclusão a receber)        
- Data de Emissão: Data da emissão do lançamento financeiro         
- Data de Vencimento: Data de vencimento do lançamento financeiro         
- Data de Competência: Data de competência informada na parcela do contrato do aluno, no formato 01/mês/ano

**Observação**:  
Se o parâmetro "Copia mês/ano da data de vencimento para data de competência" da etapa Fin - Geral ¼ estiver marcado, a data de contabilização buscará a data de vencimento do lançamento financeiro.   
Caso o parâmetro esteja desmarcado e não seja informada uma data de competência na parcela, o sistema emitirá uma mensagem ao usuário de que não conseguiu setar a data de contabilização do lançamento financeiro de acordo com a data de competência da parcela e não gerará o lançamento.

**Evento para Inclusão de lançamento**   
Esse campo informará qual evento será definido na inclusão dos lançamentos financeiros.

**Evento para Inclusão de Bolsa Crédito** Esse campo informará qual evento será definido na inclusão dos lançamentos financeiros de bolsa de crédito.  
Para maiores informações veja o [Documento técnico](http://tdn.totvs.com/pages/viewpage.action?pageId=416842135).

Fin - Geral 3/4

**- Permite gerar lançamento sem nosso número**

Cada banco tem um formato para o campo *Nosso Número*. Ele é definido dentro do *Convênio* da Conta Caixa, no sistema financeiro.   
O 'Nosso Número' é uma informação necessária para a emissão dos boletos e geração de remessa de cobrança, porém os lançamentos enviados para remessa de débito automático podem ser gerados sem o preenchimento do nosso número.   
Isto significa que dependendo do Convênio, o preenchimento do Nosso Número não se torna obrigatório, podendo ficar sem esta definição em seu layout.  
Com este parâmetro marcado, o sistema permite gerar os lançamentos financeiros sem esta informação e sem que apresente erros.  
Funcionará assim:  
O sistema sempre tentará gerar os lançamentos com o Nosso Número preenchido, mas caso o layout do convênio não tenha esta informação e este parâmetro esteja marcado, o sistema permitirá a inclusão dos lançamentos sem esta informação, mas caso o layout do convênio não tenha a informação do nosso número e o parâmetro esteja desmarcado o sistema apresentará erro e não permitirá a inclusão dos lançamentos.

**- Permite regerar lançamentos utilizando a divisão de crédito entre as parcelas do contrato**  
Quando o valor de cada parcela é encontrado através do resultado obtido pela divisão do total dos valores dos créditos financeiros das disciplinas matriculadas entre as parcelas do contrato, este parâmetro precisa estar marcado para que o sistema aplique os parâmetros *'Permite Regerar Lançamentos'* e *'Regerar Lançamentos Cancelados'* sobre os lançamentos financeiros referentes às tais parcelas, permitindo que os mesmos possam ser regerados.  
**Observação:** Se este parâmetro estiver ***marcado***, tanto dos lançamentos 'Em aberto' como os 'Cancelados', calculados por crédito, poderão ser regerados.   
Se este parâmetro estiver ***desmarcado***, somente os lançamentos 'Cancelados', calculados por crédito, poderão ser regerados.

**- Refaz automaticamente conciliação extrato na inclusão/exclusão de bolsa retroativa**   
Se *marcado*, a data de contabilização da baixa após a inclusão de bolsa retroativa será sempre alterada para a data do sistema. Se *desmarcado*, a data de contabilização da baixa após a inclusão de bolsa retroativa não será alterada.

**- Data de contabilização de baixa igual ao Padrão RM Fluxus, ao reconciliar extrato no processo de inclusão/exclusão de bolsa retroativa**  
Permite escolher qual data de contabilização de baixa será considerada quando o sistema estiver parametrizado para reconciliar extrato no processo de inclusão/exclusão de bolsa retroativa.  
Ao incluir uma bolsa retroativa e utilizar a reconciliação de extrato, caso este parâmetro esteja *marcado*, a data de contabilização da baixa obedecerá à parametrização definida no TOTVS Gestão Financeira (RM Fluxus | Parâmetros | Contas a Receber | Contab. Baixa Receber). Caso este parâmetro esteja *desmarcado*, o processo continua como antes, onde a data de contabilização da baixa será igual à data atual do sistema.

**- Data de cancelamento de extrato igual à data de baixa, ao reconciliar extrato no processo de inclusão/exclusão de bolsa retroativa**  
Caso esteja *marcado*, a data de cancelamento de extrato ficará igual à data da baixa. O default é estar *desmarcado* e neste caso irá gravar a data atual do sistema como data de cancelamento de extrato.  
Este parâmetro somente ficará habilitado se estiver marcado o campo "Refaz automaticamente conciliação de extrato no processo de inclusão/exclusão de bolsa retroativa".

**- Gerar boleto de contra apresentação**  
Com esta opção *marcada*, ao gerar o lançamento e automaticamente seu respectivo boleto bancário, o Código de Barras e o IPTE do boleto serão gerados no modo de contra apresentação, onde as posições referentes à data de vencimento serão preenchidas com zero.

**- Não alterar a data de competência do lançamento, no processo de inclusão/exclusão de bolsa retroativa**  
Se marcado, não altera a 'competência' no lançamento financeiro nem a 'data de contabilização do lançamento de inclusão'. Se desmarcado, será alterada a competência e a data de contabilização de inclusão ao inserir bolsa retroativa para um lançamento baixado. A data de competência para lançamentos em aberto não é alterada na inclusão de bolsa retroativa.

**- Cancelar Remessa automaticamente ao cancelar contrato com lançamento(s) financeiro(s) cujo(s) boleto(s) estiver(em) com status Remetido ou Registrado**Com este parâmetro *marcado* será permitido o cancelamento automático de Remessa durante o cancelamento de um lançamento financeiro realizado através do TOTVS Educacional, em que o status de remessa do boleto seja igual à **'Remetido'** ou **'Registrado'.** As remessas canceladas ficarão *pendentes* no módulo *TOTVS Gestão Financeira*, sendo necessário enviar para o banco a remessa de cancelamento dos boletos afetados.

Com este parâmetro *desmarcado*, não será permitido o cancelamento de tais lançamentos através do TOTVS Educacional pois os seus boletos possuem status de remessa igual à **'Remetido'** ou **'Registrado'**.

**- Utilizar integração com o módulo Contratos**A marcação do parâmetro habilita o modulo de contratos.

Fin - Geral 4/4

**- Vencimento em dia não útil**  
Através deste parâmetro é possível configurar como o sistema irá se comportar no processo de *Criação de parcelas* do plano de pagamento quando a data indicada para uma parcela cair em um dia não útil. O sistema poderá:

* Buscar dia útil anterior
* Manter data
* Buscar próximo dia útil

Quando marcar **Manter data**, o parâmetro **TOTVS Gestão Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Inclusão a Receber | Aceita Vencimento a Receber em finais de semana e feriados** **e Aceita previsão de baixa a receber em finais de semana e feriados** devem ser configurados igualmente.

**- Sábado é dia útil**Ao processar informações relacionadas à parcela ou ao lançamento financeiro o sábado será considerado um dia útil.

Quando não estiver marcado essa opção, mas o parâmetro **TOTVS Gestão Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Calendário Oficial | Considerar Sábado como dia útil** estiver marcada, será considerado a regra do parametro do **TOTVS Gestão Financeira**

**- Domingo é dia útil**Ao processar informações relacionadas à parcela ou ao lançamento financeiro o domingo será considerado um dia útil.

**- Data de emissão do lançamento financeiro**   
Identifica se a data de emissão do lançamento financeiro será igual à *'Data do sistema'* ou à *'Data do contrato'*. Essa parametrização é aplicada para qualquer lançamento gerado através de uma parcela do plano de pagamento.  
**Importante:** Caso a opção selecionada seja a *'Data do contrato'*, nos casos onde no contrato do aluno o campo "Data do Contrato" não esteja preenchido, não será possível a geração do lançamento.

**- Utilizar em parcela extra**  
Informa se a parametrização realizada será aplicada para lançamentos gerados através de parcelas extras.

**- Utilizar em parcela adicional**  
Informa se a parametrização realizada será aplicada para lançamentos gerados através de parcelas adicionais.

**- Em dia não útil**  
Identifica como o sistema irá se comportar quando não for um dia útil. 

* Buscar dia útil anterior
* Manter data
* Buscar próximo dia útil

**Observação:**  
O sistema identificara os feriados através do calendário cadastrado e vinculado ao período letivo do contrato. Para demais lançamentos que não estão vinculados ao contrato (por exemplo, lançamentos a pagar) será considerado o calendário oficial parametrizado na integração financeira (Integração -> Financeiro -> Calendário Oficial).

**- Mantém data de emissão ao regerar lançamento**  
Marcando esta opção, ao regerar o lançamento financeiro o sistema irá manter a mesma data de emissão gerada na inclusão, ou seja, não mudará a data de emissão.

**- Tipo de parcela do acordo**  
Este parâmetro foi implementado apenas na versão **12.1.2302.** Através deste parâmetro é possível configurar como o sistema irá se comportar ao criar as parcelas de um contrato financeiro de tipo acordo.

* Parcela adicional: Essa é a opção padrão do sistema, quando selecionada as parcelas do contrato de tipo acordo serão do tipo adicional.
* Parcela extra: Quando selecionada as parcelas do contrato de tipo acordo serão do tipo extra.

Fin - Vlrs. Opcionais/Integração 1/3

Nessa etapa são parametrizados os campos Pagamento a Maior e Menor, o cliente tem a opção de parametrizar tanto nos Valor Opcional ou Valor de Integração.

Quando o campo Pagamento a Maior ou Menor for parametrizado como Valor Opcional ou Valor de Integração e nesse contexto já tiver lançamentos gerados, todos os novos contextos criados dentro da mesma coligada terão o mesmo comportamento.

VrOpcional/IntegraçãoValores OpcionaisValores Opcionais

Antes de parametrizar os Valores Opcionais, primeiramente é necessário criar os campos no TOTVS Financeira para a correta utilização e armazenamento dos valores pagos a maior e a menor e também os campos que serão utilizados no aproveitamento dos valores da Conta Corrente.

Acesse os parâmetros do TOTVS Financeira no caminho **BackOffice | Gestão Financeira | Ambiente | Parâmetros | TOVS Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Valores Opcionais.**

**Obs:** o mesmo pode ser acessado em:***Educacional | Integração | Financeiro | Contas a Receber (TOTVS Financeira) | Valores Opcionais***

Crie os quatro campos de Valores Opcionais conforme o exemplo a seguir:

* 1: Pgto a Maior                              com a Ação : Acrescentar

  2: Pgto a Menor                             com a Ação : Descontar

  3: Acrescenta no líquido                com a Ação : Acrescentar

  4: Desconta no líquido                  com a Ação : Descontar

Em seguida, agora no TOTVS Educacional, acesse os parâmetros referentes pagamento a maior e menor que está disponíveis no menu **Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin. Vlrs.Opcionais/Integração 1/3** e associe os *“Valores Opcionais”* criados anteriormente no TOTVS Financeira da seguinte forma:

Em **Pagamento a maior**: Informe o Valor Opcional criado no TOTVS Gestão Financeira ( ex: Pgto a Maior )

Em **Pagamento a menor** : Informe o Valor Opcional criado no TOTVS Gestão Financeira ( ex: Pgto a Menor )

Valores de IntegraçãoValores de Integração

Antes de parametrizar os Valores de Integração, primeiramente é necessário criar os campos no TOTVS Educacional para a correta utilização e armazenamento dos valores pagos a maior e a menor e também os campos que serão utilizados no aproveitamento dos valores da Conta Corrente.

Acesse os parâmetros do TOTVS Educacional no caminho **Educacional****| Financeiro / Contábil | Geração | Financeiro | Valores Integração Financeira**

Crie os quatro campos de Valores Integração conforme o exemplo a seguir:  
  
1: Pgto a Maior                              com a Ação : Acrescentar

2: Pgto a Menor                             com a Ação : Descontar

3: Acrescenta no líquido                com a Ação : Acrescentar

4: Desconta no líquido                  com a Ação : Descontar

Em seguida acesse os parâmetros no menu **Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin. Vlrs.Opcionais/Integração 1/3**e associe os *“*Valores Integração*”* criados anteriormente da seguinte forma:

Em **Pagamento a maior (Vr. Integração)** : Informe o Valor de Integração criado  (ex: Pgto a Maior)

Em **Pagamento a menor (Vr. Integração)** : Informe o Valor de Integração criado (ex: Pgto a Menor)

Fin - Vlrs. Opcionais/Integração 2/3

Nessa etapa são parametrizados os campos Acréscimo e Desconto, o cliente tem a opção de parametrizar tanto nos Valor Opcional ou Valor de Integração.

Na criação de novos contextos dentro da mesma coligada, quando parametrizado por Valor de Integração por default será replicado as configurações da ultimo contexto criado, o cliente poderá definir se irá manter as configurações ou trocar para trabalhar por Valor Opcional.

VrOpcional/IntegraçãoValores OpcionaisValores Opcionais

Os campos Pgto a Maior e Pgto a Menor cadastrados conforme descrito no **Fin. Vlrs.Opcionais/Integração 1/3** serão utilizados nessa etapa.

Acesse os parâmetros referentes pagamento a maior e menor que está disponíveis no menu **Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin. Vlrs.Opcionais/Integração** e associe os *“Valores Opcionais”* criados da seguinte forma:

Em**Valor opcional de desconto** : Informe o Valor de Opcional criado no TOTVS Gestão Financeira (ex: Desconta no Líquido).

Em**Valor opcional de acréscimo**: Informe o Valor de Opcional criado no TOTVS Gestão Financeira (ex: Acrescenta no Líquido).

Defina como os valores existentes na Conta Corrente do aluno deverão ser aproveitados, escolhendo entre as duas opções seguintes:

**Não efetuar operação:**Marcando esta opção, os valores existentes na Conta Corrente do aluno serão aproveitados somente com a execução manual do processo *‘Aproveitar valores em conta corrente’* que ao ser executado irá gerar novos lançamentos financeiros a Pagar, provenientes dos aproveitamentos dos valores de Créditos, ou lançamentos a Receber, provenientes dos aproveitamentos dos valores de Débitos. O processo *‘Aproveitar valores em conta corrente’* pode ser acionado dentro do anexo de Conta Corrente existente no cadastro do Aluno ou através do menu Financeiro/Contábil | Assistentes.

**- Efetuar operação com valor total na próxima mensalidade:**Marcando esta opção, ao gerar a próxima parcela o sistema utilizará os valores da Conta Corrente acrescentando (caso exista Débito) ou diminuindo (caso exista Crédito) o valor do lançamento financeiro da próxima parcela gerada. O sistema sempre aproveitará o valor máximo possível na geração da parcela e, caso ainda fique um saldo na Conta Corrente, este valor será aproveitado na geração da próxima parcela e assim sucessivamente. Os valores de Crédito aproveitados da Conta Corrente serão registrados no lançamento financeiro no campo de Valor Opcional definido em ‘*Valor opcional de desconto’*. Os valores de Débito aproveitados da Conta Corrente serão registrados no lançamento financeiro no campo de Valor Opcional definido em ‘*Valor opcional de acréscimo’*.

**- Valor mínimo**Campo de preenchimento *opcional*, indica o valor mínimo ser descontado ou acrescentado nas próximas parcelas. Se indicado, o sistema somente aproveitará os valores da Conta Corrente se o montante for no mínimo o valor indicado.

Valores de IntegraçãoValores de Integração

Os campos  Acrescenta no líquido e Desconta no líquido cadastrados conforme descrito no **Fin. Vlrs.Opcionais/Integração 1/3** serão utilizados nessa etapa.

Acesse os parâmetros no menu **Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin. Vlrs.Opcionais/Integração 2/3**e associe os *“*Valores Integração*”* criados anteriormente da seguinte forma:

Em**Valor Integração de desconto** : Informe o Valor de Integração criado  (ex: Desconta no Líquido).

Em**Valor Integração de acréscimo**: Informe o Valor de Integração criado (ex: Acrescenta no Líquido).

Defina como os valores existentes na Conta Corrente do aluno deverão ser aproveitados, escolhendo entre as duas opções seguintes:

**- Não efetuar operação:**Marcando esta opção, os valores existentes na Conta Corrente do aluno serão aproveitados somente com a execução manual do processo *‘Aproveitar valores em conta corrente’* que ao ser executado irá gerar novos lançamentos financeiros a Pagar, provenientes dos aproveitamentos dos valores de Créditos, ou lançamentos a Receber, provenientes dos aproveitamentos dos valores de Débitos. O processo *‘Aproveitar valores em conta corrente’* pode ser acionado dentro do anexo de Conta Corrente existente no cadastro do Aluno ou através do menu Financeiro/Contábil | Assistentes.

**- Efetuar operação com valor total na próxima mensalidade:**Marcando esta opção, ao gerar a próxima parcela o sistema utilizará os valores da Conta Corrente acrescentando (caso exista Débito) ou diminuindo (caso exista Crédito) o valor do lançamento financeiro da próxima parcela gerada. O sistema sempre aproveitará o valor máximo possível na geração da parcela e, caso ainda fique um saldo na Conta Corrente, este valor será aproveitado na geração da próxima parcela e assim sucessivamente. Os valores de Crédito aproveitados da Conta Corrente serão registrados no lançamento financeiro no campo de Valor Opcional definido em ‘*Valor opcional de desconto’*. Os valores de Débito aproveitados da Conta Corrente serão registrados no lançamento financeiro no campo de Valor Opcional definido em ‘*Valor opcional de acréscimo’*.

**- Valor mínimo**Campo de preenchimento *opcional*, indica o valor mínimo ser descontado ou acrescentado nas próximas parcelas. Se indicado, o sistema somente aproveitará os valores da Conta Corrente se o montante for no mínimo o valor indicado.

Fin - Vlrs. Opcionais/Integração 3/3

Nessa etapa são parametrizados os campos referente a Bolsas, o cliente tem a opção de parametrizar tanto nos Valor Opcional ou Valor de Integração.

Na criação de novos contextos dentro da mesma coligada, quando parametrizado por Valor de Integração por default será replicado as configurações da ultimo contexto criado, o cliente poderá definir se irá manter as configurações ou trocar para trabalhar por Valor Opcional.

**- Utilizar bolsas condicionais:**indica se a empresa trabalha ou não com escalonamento de bolsas/bolsas condicionais.  
O escalonamento pode ser definido como a perda progressiva de benefícios pela falta/atraso no pagamento. Assim, até a data de vencimento, o aluno terá todos os benefícios e após a data de vencimentos os benefícios serão gradativamente diminuídos. As perdas gradativas dos benefícios são calculadas a partir de Fórmulas.  
Se este parâmetro estiver selecionado, o sistema habilitará o campo 'Bolsas condicionais'. As fórmulas criadas para calcular as perdas gradativas deverão estar vinculadas a este campo opcional diretamente no financeiro.  
Os 'Valores opcionais para bolsas incondicionais/condicionais', à seguir, são utilizados para informar em quais valores opcionais do *TOTVS Gestão Financeira*serão gravados os valores das bolsas nos lançamentos financeiros originados no TOTVS Educacional. Estes campos deverão ser primeiramente configurados dentro do sistema financeiro e selecionados para utilização aqui no Educacional.

VrOpcional/IntegraçãoValores OpcionaisValores Opcionais

**- Bolsas incondicionais (Vlr. opcional)**

Este campo receberá os valores das bolsas, normais e de crédito, concedidas para os alunos. Os valores das bolsas gravados neste valor opcional serão válidos APÓS o vencimento do lançamento, não sendo possível "escalonar" estes valores. Estes valores poderão ser contabilizados na inclusão.

**- Bolsas condicionais (Vlr. opcional)**

Este campo somente poderá ser utilizado se a opção anterior 'Utilizar bolsas condicionais' for selecionada. Os valores gravados neste valor opcional poderão ser "escalonados" e não deverão ser contabilizados na inclusão, somente na baixa, pois só neste momento temos como saber o seu valor real.  
Deve-se ter especial atenção a estes campos relacionados à Bolsas, pois, uma vez realizada a Geração de Lançamentos Financeiros, não será mais permitida qualquer alteração nestes campos (inclusive habilitar/desabilitar a opção de escalonamento), portanto, os campos referentes à Bolsas devem ser parametrizados antes da geração de qualquer lançamento financeiro.  
Apesar deste procedimento não ser obrigatório, é extremamente recomendável a sua utilização. Caso contrário todos os valores referentes às Bolsas de estudo, que por ventura o aluno venha a receber, serão lançados no campo "Desconto" do Lançamento Financeiro, não sendo possível distinguir dos demais descontos que possam ocorrer neste processo.  
**Observação**: caso a opção 'Utilizar bolsas condicionais' não seja marcada, os valores de todas as bolsas serão enviados para o valor opcional selecionado em 'Bolsas incondicionais'.

Valores de IntegraçãoValores de Integração

**- Bolsas incondicionais (Vlr. Integração)**

Este campo receberá os valores das bolsas, normais e de crédito, concedidas para os alunos. Os valores das bolsas gravados neste valor opcional serão válidos APÓS o vencimento do lançamento, não sendo possível "escalonar" estes valores. Estes valores poderão ser contabilizados na inclusão.

**- Bolsas condicionais (Vlr. Integração)**

Este campo somente poderá ser utilizado se a opção anterior 'Utilizar bolsas condicionais' for selecionada. Os valores gravados neste valor opcional poderão ser "escalonados" e não deverão ser contabilizados na inclusão, somente na baixa, pois só neste momento temos como saber o seu valor real.  
Deve-se ter especial atenção a estes campos relacionados à Bolsas, pois, uma vez realizada a Geração de Lançamentos Financeiros, não será mais permitida qualquer alteração nestes campos (inclusive habilitar/desabilitar a opção de escalonamento), portanto, os campos referentes à Bolsas devem ser parametrizados antes da geração de qualquer lançamento financeiro.  
Apesar deste procedimento não ser obrigatório, é extremamente recomendável a sua utilização. Caso contrário todos os valores referentes às Bolsas de estudo, que por ventura o aluno venha a receber, serão lançados no campo "Desconto" do Lançamento Financeiro, não sendo possível distinguir dos demais descontos que possam ocorrer neste processo.  
**Observação**: caso a opção 'Utilizar bolsas condicionais' não seja marcada, os valores de todas as bolsas serão enviados para o valor opcional selecionado em 'Bolsas incondicionais'.

**- Manter fórmula default para valor opcional de bolsas condicionais**  
Mantem a fórmula utilizada no cálculo de bolsas condicionais associada ao valor opcional de bolsas condicionais na geração de lançamentos sendo que no momento da baixa a fórmula será processada para apresentar o valor da bolsa condicional. Com este parâmetro desmarcado, a geração de lançamentos calculará e atribuirá o valor das bolsas condicionais ao valor opcional parametrizado para bolsas condicionais do lançamento, desconsiderando a fórmula vinculada a esse campo.

**Observações**:

Com este parâmetro marcado, caso tenhamos fórmula utilizada no cálculo de bolsas condicionais associada ao valor opcional e o lançamento não possua bolsas condicionais ou total de bolsas condicionais igual a zero, a fórmula utilizada será associada ao valor opcional de bolsas condicionais na geração ou regeração de lançamentos.   
Com este parâmetro desmarcado, caso tenhamos fórmula utilizada no cálculo de bolsas condicionais associada ao valor opcional e o lançamento possua bolsas condicionais ou total de bolsas condicionais maior zero, os valores de bolsas condicionais serão mantidos e a fórmula utilizada NÃO será associada ao valor opcional de bolsas condicionais na geração ou regeração de lançamentos.

No caso de **bolsas incondicionais**, a aplicação da fórmula será feita somente quando a parcela não possuir alguma bolsa associada. No caso, quando a parcela possuir alguma bolsa, o valor aplicado continuará sendo o valor das suas bolsas, mesmo que a fórmula esteja associada.

**- Repasse de bolsas**O Educacional utilizará este recurso para registrar a diferença a **menor** entre o valor cadastrado para o repasse de bolsa e o valor do lançamento referente à bolsa de crédito que estará sendo baixado. .

Fin - Opcionais

Nesta etapa definem-se os valores dos campos das Tabelas Opcionais utilizadas para a geração dos lançamentos financeiros. Caso a Origem da tabela opcional seja 'Parâmetros' serão habilitadas as opções disponibilizadas pelos cadastros do TOTVS Gestão Financeira. Se o usuário optar por 'Responsável financeiro' ou 'Serviço', os demais campos serão desabilitados.

Fin - Agrupamento

Nesta etapa definem-se configurações para a geração de boletos.

O sistema permite gerar lançamentos financeiros agrupados em um único boleto para parcelas que possuírem o *mesmo responsável financeiro* e também a *mesma data de vencimento*. 

**-**Marque a forma como o sistema deverá agrupar os lançamentos no momento da sua geração, podendo ser por:

* **Responsável financeiro:**  
  O sistema tentará gerar em um único boleto o maior número de parcelas do mesmo responsável financeiro. Esta opção pode ser utilizada para os casos em que mais de um aluno, por exemplo irmãos, possuem o mesmo responsável financeiro. Neste caso, os lançamentos das parcelas destes alunos serão gerados em um único boleto.
* **Contrato:**  
  O sistema tentará gerar em um único boleto as parcelas do mesmo contrato. Esta opção pode ser utilizada quando os contratos possuírem mais de uma parcela com a mesma data de vencimento.
* **Aluno:**  
  O sistema tentará gerar em um único boleto as parcelas do mesmo aluno. Esta opção pode ser utilizada quando o aluno possuir mais de um contrato com a instituição de ensino.
* **Não agrupado:**  
  O sistema não irá agrupar mais de um lançamento em um mesmo boleto.

**- Não agrupar serviços diferentes**  
Agrupa quando possível, somente lançamentos de parcelas que forem do mesmo serviço.

**- Agrupar lançamentos de parcelas a serem geradas com lançamentos previamente gerados**  
Agrupa quando possível, um lançamento que está sendo gerado a um boleto já gerado e que esteja em aberto e não remetido.  
Executando a geração de novas parcelas juntamente com a regeração de outras parcelas com os mesmos dados de boleto, os respectivos lançamentos serão agrupados no mesmo boleto.

**-****Agrupar no mesmo boleto lançamentos de outras Filiais**Agrupa quando possível, parcelas da mesma coligada que possuem as mesmas regras para agrupamento de lançamentos em um único boleto, ao gerar uma parcela em uma filial o TOTVS Educacional realizará uma análise nos lançamentos de **todas as outras Filiais da coligada**, e se identificar que existem parcelas serão agrupadas no mesmo boleto.

- **Identificação** **automática****das parcelas que podem ser agrupadas no mesmo boleto independente do filtro selecionado no processo de geração de lançamento**Agrupa quando possível lançamento em um único boleto, ao gerar o lançamento de uma parcela o TOTVS Educacional irá verifica para cada parcela processada, se existe outra parcela ou lançamento que pode ser agrupado, levando em consideração as regras de agrupamento e parâmetros marcados.

**- Permite pagamento recorrente em boletos agrupados (A partir da versão 12.1.2402)**Marcando esse parâmetro, poderá ser realizado pagamento via recorrência em de boletos agrupados 

O parâmetro não ficará disponível na tela caso o parâmetro **Educacional | Tesouraria | Geral 3/4 | Permite habilitar pagamento automático**estiver desmarcado

Fin - Bolsa Retroativa 1/3

**- Usar bolsa retroativa sem alterar parcelas já baixadas**  
Esta opção **marcada** indicará ao sistema que o modelo escolhido para se trabalhar com Bolsa Retroativa é o modelo em que o lançamento financeiro original *não* é alterado com informações das bolsas incluídas ou excluídas retroativamente. Caso esteja **desmarcada**, o sistema entenderá que as movimentações efetuadas através de Bolsa retroativa serão registradas utilizando o outro modelo, onde estas movimentações são registradas diretamente no lançamento financeiro original através de alterações realizadas no mesmo.

**- Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)**  
Caso esta opção seja a escolhida, o processo de bolsa retroativa passará a criar lançamentos de devoluções a pagar com o valor da bolsa *incluída* retroativamente a fim de devolver o valor da bolsa ao responsável financeiro do aluno e incluirá no contrato, na parcela e na bolsa concedida registros com as informações das operações efetuadas indicando, entre outras informações, o valor total dos créditos referentes à devolução, ou então passará a criar lançamentos de cobrança a receber com o valor da bolsa *excluída* retroativamente a fim de cobrar o valor da bolsa ao responsável financeiro do aluno e também incluirá no contrato, parcela e na bolsa excluída registros com as informações das operações efetuadas.

Os lançamentos a pagar de devolução, gerados pela inclusão de bolsa retroativa, conterão somente o valor original não sendo preenchidos quaisquer tipos de valores de acréscimos ou descontos.

**- Utilizar a movimentação em conta corrente**  
Caso esta opção seja a escolhida, os valores referentes à inclusão ou exclusão de bolsas retroativas irão atualizar automaticamente a Conta Corrente do aluno, gerando *créditos* caso seja feita uma inclusão de bolsa retroativa ou gerando *débitos* caso seja feita a exclusão de bolsa retroativa em parcelas cujos lançamentos financeiros já foram gerados.

− As duas opções anteriores somente serão habilitadas nos casos em que a opção **'Usar bolsa retroativa sem alterar parcelas já baixadas'** estiver marcada.  
− Se  as  bolsas   incluídas  pelo processo  de  Bolsa  Retroativa  forem  aplicadas  em  parcelas  cujos lançamentos financeiros ainda não foram gerados, a bolsa será incluída, mas ela *não* ficará registrada como uma Bolsa Retroativa e sim como uma bolsa comum.  
− Se a opção escolhida anteriormente foi '**Utilizar a movimentação em conta corrente**' as outras opções de parâmetros, disponíveis nas próximas etapas do parametrizador sobre Bolsa Retroativa, ficarão desabilitadas, pois elas complementam a parametrização quando utilizada a outra opção '**Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)**'.  
− Depois que houver a inclusão ou exclusão de  alguma  bolsa  pelo processo de Bolsa Retroativa, as três opções citadas anteriormente ficarão desabilitadas, não sendo mais possível mudar a forma de trabalho!

**- Usar devoluções pendentes após término de contrato nos próximos contratos**  
Com esta opção *marcada*, após todas as parcelas do contrato já terem sido baixadas, ou seja, após o término deste contrato, os valores de crédito referentes às devoluções que ainda estiverem pendentes neste contrato poderão ser utilizados nos próximos contratos que tiverem o mesmo responsável financeiro e mesmo aluno. A utilização dos créditos pendentes no próximo contrato se dará automaticamente assim que o lançamento financeiro da próxima parcela for gerado, criando um *'Vínculo'* neste lançamento com o valor do crédito que estava pendente no contrato anterior, para ser descontado do valor original no momento da baixa do lançamento.  
Se esta opção estiver *desmarcada*, os créditos que ficarem pendentes em um contrato finalizado não serão aproveitados através de *'Vínculos'* ao serem geradas as próximas parcelas dos próximos contratos, para estes casos, a utilização se dará somente com a efetivação da baixa do próprio lançamento de devolução criado anteriormente no momento da inclusão da Bolsa Retroativa.

Esta opção somente estará disponível, caso a forma adotada anteriormente para registrar os valores das bolsas incluídas retroativamente seja *'Criar devolução de crédito (inclusão de bolsa) / lançamentos a receber (exclusão de bolsa)'*. 

**- Considerar valores de acréscimos no cálculo de crédito retroativo (apenas para parcelas já baixadas)**  
Com esta opção *marcada*, os valores dos créditos referentes às devoluções podem ultrapassar o valor original do lançamento vinculado desde que o mesmo esteja baixado. O comportamento deste parâmetro deve afetar o sistema da seguinte forma: Uma bolsa retroativa foi adicionada para um contrato com 6 parcelas de R$ 1000,00, sendo que destas, a primeira foi baixada em atraso, ou seja foi paga com juros e multa, contabilizando assim R$ 1050,00. Quando o este parâmetro está **desmarcado** o valor do crédito de devolução deve respeitar o valor original de cada lançamento da parcela, que neste caso é de R$ 1000,00 com o parâmetro **marcado**, o crédito de devolução será o valor baixado que é R$ 1050,00.

Fin - Bolsa Retroativa 2/3Fin - Bolsa Retroativa 2/3Fin - Bolsa Retroativa 2/3OpçõesOpçõesOpções

**- Aplicar devolução no lançamento da primeira parcela em aberto**  
Caso esta opção seja a escolhida, os créditos referentes às devoluções originadas pela inclusão de bolsa retroativa serão aproveitados automaticamente no lançamento da primeira parcela do contrato que ainda estiver com status 'Em aberto' através da criação de *'Vínculos'* entre os lançamentos financeiros de devolução e o lançamento da parcela possibilitando, assim, no momento da baixa do lançamento da parcela, abater do valor original do lançamento os créditos vinculados referentes às devoluções.  
Serão vinculados ao lançamento desta primeira parcela os valores máximos de créditos possíveis, não podendo, contudo, ultrapassar ao valor líquido da parcela. Se não for possível aproveitar o valor total dos créditos no lançamento financeiro desta primeira parcela em aberto, o sistema irá aproveitar o restante do crédito na próxima parcela do contrato que ainda estiver com lançamento em aberto e assim sucessivamente até zerar o valor total do crédito que fica armazenado no contrato do aluno, ou caso não tenha mais parcelas geradas, ficará como crédito pendente no contrato o qual será aproveitado nas gerações de lançamentos das próximas parcelas.

\* *'Vínculo'* é um recurso utilizado no sistema financeiro para compensar o valor de um lançamento (L1), descontando-o do valor original de outro lançamento (L2), vinculando, assim, os dois lançamentos. No momento da execução da baixa deste segundo lançamento (L2), o valor do primeiro lançamento (L1) será abatido do valor original deste segundo lançamento e no final da baixa, os dois lançamentos ficarão com status 'Baixado' no caso da baixa aproveitar o valor total do vínculo, se não aproveitar o valor total, o lançamento (L1) ficará parcialmente baixado.

**- Dividir devolução pela quantidade de parcelas restantes**  
Caso esta opção seja a escolhida, o sistema irá ratear o valor total do crédito a ser devolvido entre parcelas do contrato do aluno que não possuírem lançamentos gerados e parcelas que possuírem lançamentos financeiros gerados e estiverem 'Em aberto', através da criação de *'Vínculos'* entre os lançamentos financeiros de devolução criados na inclusão da Bolsa Retroativa e os lançamentos das parcelas que ainda estiverem em aberto. Os créditos não vinculados na inclusão da Bolsa Retroativa ficarão como créditos pendentes no contrato. 

**- Devolver em espécie**  
Caso esta opção seja a escolhida, não serão criados *'Vínculos',* pois os lançamentos financeiros a pagar criados referentes às devoluções originadas pela inclusão de Bolsa Retroativa serão pagos diretamente ao responsável financeiro do aluno, devendo a instituição de ensino executar a baixa destes lançamentos após o pagamento.

Dados do LançamentoDados do LançamentoDados do Lançamento

**- Parâmetros default para geração do lançamento:**  
Os dados informados serão adotados como um comportamento padrão na inclusão dos lançamentos financeiros de devolução.

* Tipo de documento (A Classificação deverá necessariamente ser = Devolução)
* Data de Vencimento:   
  *- Data do sistema (valor padrão): o lançamento será gerado com a data de vencimento igual à data do sistema, ou seja, a data de geração da bolsa retroativa.**- Número de dias após a inclusão: selecionando esta opção, será permitido informar quantos dias após a inclusão será definida a data de vencimento do lançamento.*
* Dias após a inclusão
* Centro de custo
* Departamento
* Natureza Orçamentária financeira
* Conta caixa padrão
* Histórico

Tags para o campo de Histórico

As tag's são recursos que permitem ao usuário adicionar alguma informação acadêmica ou financeira específica do TOTVS Gestão Educacional no campo de Histórico, c[lique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425458850) para ver a listagem das tag's

ContabilizaçãoContabilizaçãoContabilização

**- Parâmetros default para geração do lançamento:**  
Os dados informados serão adotados como um comportamento padrão na inclusão dos lançamentos financeiros de devolução.

* Tipo contábil padrão
* Data de contabilização
* Mês de Competência
* Evento para inclusão de lançamento ()
OpcionaisOpcionaisOpcionais

Os dados informados serão adotados como um comportamento padrão na inclusão dos lançamentos financeiros de devolução.

* Tabelas opcionais
* Campos alfa
* Datas opcionais
Fin - Bolsa Retroativa 3/3

**♦ Exclusão de Bolsa**

**- Gerar uma única parcela para o pagamento**  
Caso esta opção seja a escolhida, será criada automaticamente no contrato do aluno uma única parcela no valor total da bolsa que foi excluída.  
Os dados desta parcela tais como Tipo de parcela, Serviço e Data de vencimento obedecerão às informações parametrizadas neste local.

**- Dividir pela quantidade de parcelas restantes**  
Caso esta opção seja a escolhida, serão incluídas no contrato do aluno novas parcelas cujos valores serão iguais ao rateio do valor total da bolsa que foi excluída pelo número de parcelas que ainda não possuem lançamentos gerados do contrato. Estas parcelas serão incluídas utilizando o Serviço aqui definido e as suas Datas de vencimento serão iguais às datas das parcelas ainda não geradas do contrato.  
Se o contrato não possuir mais parcelas ainda não geradas, será incluída no contrato do aluno uma única parcela com o valor total da bolsa que foi excluída e, neste caso, a Data de vencimento obedecerá às informações parametrizadas para exclusão de bolsa retroativa.

**- Gerar lançamentos de cobrança automaticamente**  
Se desejar que estas parcelas de cobrança sejam incluídas no contrato do aluno já com os respectivos lançamentos financeiros gerados, *marque* a opção '**Gerar lançamentos de cobrança automaticamente**'. Se esta opção estiver *desmarcada* as parcelas serão incluídas sem os seus respectivos lançamentos financeiros e, neste caso, a geração dos lançamentos financeiros deverá ser feita manualmente.

**♦ Dados da parcela:**

Estas informações serão adotadas como um comportamento padrão para a inclusão das parcelas referentes à cobrança do crédito:

* Tipo de parcela: escolha entre *'Parcela Extra'* ou *'Parcela Adicional'*. Lembrando que parcelas do tipo *'Parcela Extra'* não podem ser agrupadas em um único boleto.
* Data de vencimento: a data aqui definida será utilizada quando a opção '*Gerar uma única parcela para o pagamento*' for a escolhida
* Dias após a exclusão: indique o número de dias que será utilizado para calcular a Data de vencimento da parcela de cobrança gerada
* Serviço: Indique o serviço que será utilizado na criação das parcelas de cobranças geradas

**♦** **Contabilização**

* Data de contabilização
* Evento p/ inclusão do lançamento ()
