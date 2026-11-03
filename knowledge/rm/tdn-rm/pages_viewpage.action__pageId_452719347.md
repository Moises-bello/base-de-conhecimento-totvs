---
content_hash: 086dc376d6ab58d285d175c2003010bbfff66ed42c4dd25c24165a30a8687bbd
fetched_at: '2026-06-29T00:10:06.888351+00:00'
page_id: '452719347'
product: rm
source: tdn-rm
title: Rescisão - RHU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719347
version: 16
---

Rescisão é o rompimento do contrato de trabalho pelo empregador ou pelo empregado, quando não haverá mais continuidade na relação empregatícia e neste momento é feito o cálculo dos direitos legais. Estes direitos legais são assegurados por lei devendo ser calculados por proventos e descontos devidos.  
   
O termo de rescisão contratual deve ter discriminado cada parcela paga ao funcionário com seu respectivo valor. Dependendo do tipo e motivo de rescisão contratual cada parcela a ser paga será discriminado no recibo, tais parcelas são, por exemplo: saldo de salário, férias, 13º salário, FGTS, aviso prévio, etc.  
   
As informações necessárias controle do processo de demissão de funcionários devem ser cadastrados no módulo de rescisão, anexo do cadastro de funcionários.  
   
As tabelas de INSS e IRRF usadas no cálculo serão as referentes ao mês competência e mês caixa respectivamente.   
   
Quando o empregador ou o funcionário decide rescindir o contrato de trabalho deverá notificar através do aviso prévio. O aviso prévio tem a finalidade de possibilitar ao empregador o preenchimento da vaga ou ao funcionário tentar uma nova colocação no mercado de trabalho.  
   
**Observação:**

1. Quando o aviso prévio for trabalhado deverá ser cadastrado no anexo do cadastro de funcionários.
2. Quando a demissão for por aviso prévio indenizado a data será preenchida automaticamente com um dia subsequente à Data de demissão/Cálculo, podendo ser informada outra data conforme necessário O sistema calcula a data do aviso da seguinte forma: Diminui 30 dias na data da rescisão e soma 1 para que a contagem dos avos fique correta.
3. A data do aviso prévio indenizado é utilizada para cálculo dos avos referente a 13º salário e férias respectivamente, se o funcionário tem seu aviso trabalhado, a data Demissão/Cálculo continuará sendo a base para cálculo do número de avos.
4. O prazo estipulado é geralmente 30 dias. Não deverá ser digitado o número de dias de aviso, quando este aviso prévio for trabalhado.
5. O Executa Fórm. Dias aviso do Sind. executa a fórmula informada no cadastro de sindicatos para cálculo de dias de aviso.

Para rescisões de comum acordo (Tipo V), no campo Dias de Aviso Indenizado, deve ser informado com a metade da quantidade de dias total a ser indenizado. Quando a metade destes dias resultar em decimal, por exemplo 33 dias de aviso prévio indenizado deveria ser 16.5 dias de aviso prévio indenizado, o valor a ser informado no campo será o valor arredondado, no caso do exemplo 17 dias de aviso prévio indenizado. No momento do cálculo, ou seja, quando clicar em "Calcular Rescisão", deverá ser marcado ou não um parâmetro "Aviso Prévio Indenizado abate 0.5 dia" de acordo com o entendimento do usuário.    
**Atenção:** Este parãmetro influenciará apenas no cálculo do aviso prévio indenizado e no cálculo das médias de aviso prévio indenizado. Para o cálculo da projeção em férias indenizadas e 13º salário indenizado será considerado o valor inteiro informado no campo "Dias de Aviso Indenizado" na pasta Aviso Prévio do cadastro de Rescisão.  
   
A data de demissão serve como informação que o sistema utilizará para o cálculo das verbas rescisórias (Saldo salário, avos férias, avos de 13º salário, etc.). Através das informações da rescisão também será definida a situação do funcionário, ou seja, se a demissão for para o mês atual a situação será alterada para D – demitido e se for para o próximo mês a situação continuará A – ativo.  
   
**Observações:**  
1.     No processo de cadastro da rescisão individual, quando ocorrer algum erro no cálculo o sistema não calculará, porém a rescisão será cadastrada.  
2.     Ao informar a data de demissão o sistema preencherá automaticamente os campos: Data de desligamento, Data de pagamento e Data do último movimento, com a mesma data podendo ser alteradas se necessário.  
3.     O cancelamento da rescisão deve ser feito pelo módulo específico de cancelamento. Lembrando que, o sistema somente permitirá o cancelamento da rescisão que tiver data de demissão dentro do mês de competência.   
4.     É permitido informar data de rescisão retroativa a competência atual, porém o sistema apresenta uma mensagem alertando que a rescisão não será calculada porque a data de pagamento é anterior ao mês de competência. Porém para rescisão dos tipos: 5 ou 6 somente serão permitidos o cadastramento retroativo se o parâmetro "**Permite realizar rescisão por transferência com data retroativa à competência atual"** estiver marcado nos parâmetros do Folha de Pagamento.  
5.     Caso o funcionário possua férias cadastradas para o próximo mês é exibida uma mensagem de confirmação ao calcular sua rescisão.  
6.     Independente do parâmetro "Utiliza parâmetros específicos para média de férias na rescisão" no cadastro de sindicato, o cálculo da média de férias e 13º rescisão sempre considerará os eventos que incidem na média de rescisão.  
7.     Para informação do parâmetro "Soma avos ref. aviso após o cálculo" existente nos parâmetros do Folha de Pagamento, quando na rescisão o funcionário tem faltas que fazem ter menos de 15 dias trabalhados até a data de demissão, os cálculos da rescisão na contagem dos avos e da provisão no mês da rescisão ficarão:  
**Exemplo:** O funcionário foi demitido no dia 20/06, teve 6 faltas e 30 dias de aviso prévio indenizado.

* Com o parâmetro desmarcado o sistema considera 6/12 + 1/12 avos indenizado = 7/12 na rescisão e na provisão também considera 7/12 avos.
* Com o parâmetro marcado o sistema considera 5/12 + 1/12 avos indenizado = 6/12 na rescisão e na provisão também considera 6/12 avos.

8.     Ao demitir um funcionário no mês atual, sendo que este funcionário tem usuário do portal informado no cadastro, ao confirmar a mensagem "Existe um usuário relacionado a este funcionário. Deseja desativá-lo?" o sistema desativa o usuário, ou seja, o campo "Ativo" fica desmarcado. Porém quando a rescisão é para o próximo mês o sistema não desativa o funcionário apenas altera a data de validade para a Data de desligamento sendo a hora 0h.  
   
9.   Ao alterar a data de demissão do funcionário a referência do evento de saldo de salário não será alterada. Para que seja alterada e recalcula a verba de saldo de salário, esta verba deve ser excluída ou ter a referencia zerada ou o evento excluído através do botão movimento no cadastro de rescisão.   
   
   
**Exemplos práticos de datas de demissão e desligamento:**  
a) Usuário optando pelo cálculo da rescisão no mesmo dia do desligamento (Procedimento habitual) funcionário demitido no dia 10 de um determinado mês.  
Data Demissão/cálculo: Dia 10/XX/XX  
Data de Desligamento: Dia 10/XX/XX  
Aviso Prévio: Dia 11/XX/XX  
   
b) Rescisão no dia 11 de um determinado mês, e o usuário quer considerar para cálculo até o dia anterior ao desligamento:  
Data Demissão/cálculo: Dia 10/XX/XX  
Data de Desligamento: Dia 11/XX/XX  
Aviso Prévio: Dia 11/XX/XX  
   
c) Usuário demitindo funcionário em uma sexta-feira dia 13 de um determinado mês, optando por pagar o Sábado e o domingo  
Data Demissão/cálculo: Dia 15/XX/XX  
Data de Desligamento: Dia 13/XX/XX  
Aviso Prévio: Dia 16/XX/XX (Observando que neste caso o sistema poderá pagar um avo a mais de férias e/ou 13º salário, dependendo da parametrização do sistema)  
   
O sistema registra automaticamente a data de ultimo movimento, porém ele deve ser alterado pelo usuário no momento de calcular a rescisão complementar através do botão "Altera data do último movimento" existente na rescisão complementar. Através desta data, que será atualizada no momento do cálculo da rescisão complementar, serão calculados o INSS e o IRRF com tabelas referentes ao mês competência e mês caixa respectivamente.  
   
O período da rescisão é definido pelo sistema e informa em qual período a rescisão será calculada. Para a rescisão no próprio mês o sistema buscará o valor do período da rescisão do módulo de Parâmetros Locais do sistema. Para a rescisão no próximo mês o usuário poderá definir qual período deseja calcular a rescisão.  
   
**Observação:**  
1.   O movimento da rescisão deverá constar no último período da competência, salvo nos casos de rescisão complementar a ser calculada na mesma competência da rescisão.  
2.    O período sempre estará habilitado para rescisão para o próximo mês, observando o parâmetro *"Utiliza período fixo para rescisão no próximo mês"* existente em Parâmetros de Folha de Pagamento.  
**Regra**  
**Data de demissão = mês anterior** (o sistema apresenta o período atual, local e deixa editar)  
**Data de demissão = mês atual** (o sistema apresenta o período atual, local, e NÃO deixa editar)  
**Data de demissão = mês posterior** (o sistema apresenta o período atual, local e deixa editar, observando o parâmetro *"Utiliza período fixo para rescisão no próximo mês")*  
   
O tipo de demissão definirá quais verbas constarão no recibo rescisório do funcionário.  
   
**Observações:**  
1.    Os tipos de demissão são cadastrados nas tabelas dinâmicas.   
2.    A transferência de valores associados de funcionários para outra coligada só ocorrerá se na coligada de destino, existir os mesmos "Códigos de valores de funcionário" cadastrados nas tabelas dinâmicas da coligada originária. O mesmo ocorrerá para as tabelas de eventos, sindicatos, Acordo Coletivo / Reajuste por Lei (eSocial) que devem ter o mesmo código nas coligadas origem e destino.  
3.    Não é permitido a transferência de funcionários para o "Próximo Mês".  
4.    Os funcionários que foram transferidos para a mesma coligada e possuem benefícios vinculados através da Integração de Benefícios, serão transferidos os mesmos para o novo registro;  
5.    Os tipos de rescisão relacionados não poderão ser gerados para o próximo mês pois no manual do SEFIP diz que a data de movimentação · Deve estar compreendida no mês anterior ou no mês da competência, para os códigos de movimentação:

* H - Rescisão, com justa causa,por iniciativa do empregador;
* J - Rescisão do contrato de trabalho por iniciativa do empregado;
* K - Rescisão a pedido do empregado ou por inic.do empregador, não optante;
* M - Mudança de regime estatutário;
* N1- Transf.do empreg.p/outro estabelecimento da mesma empresa;
* N2- Transf.do empreg.p/outro estab.que tenha assumido os encargos, s/rescisão;
* S - Falecimento;
* U1- Apos.Tempo de serv.ou idade sem continuidade de vinculo empregaticio;
* U2- Apos.Tempo de serv.ou idade com continuidade de vinculo empregaticio.

O Contrato de Experiência pode ser acordado por qualquer prazo, desde que não exceda aos 90 dias estipulados pela CLT. E o contrato por prazo determinado pode ser de até 2 anos. Nestes casos o contrato pode ser rescindido utilizando as informações de contrato com prazo e data final do contrato da rescisão do tipo T – Término de contrato de trabalho.  
   
**Atenção:**  
1.     No caso de demissão antes do término do contrato de trabalho, para efetuar o lançamento correto através do CC 124 - Indenização art. 479, de acordo art. 479 da CLT, deverá ser cadastrada a demissão como do "Tipo 2", iniciativa do empregador sem justa causa. Pois, como o contrato de trabalho ainda não terminou o usuário não poderá calcular a rescisão utilizando o tipo T "Término de Contrato de Trabalho", porque ele demitiu o funcionário antes do término do contrato.  
Assim, ao gerar a GRFC no campo 20, ficará registrado o código 3 que significa Ausência/Dispensa.

* Tratando-se de término de contrato de trabalho por prazo determinado - (firmado nostermos da Lei 6.019/74) deve ser informado o código 3.
* Tratando-se de término de contrato de trabalho por prazo determinado - (firmado nos termos da Lei 9601/98) e rescisão por força maior, deve ser informado o código 1.
* Nos casos de rescisão antecipada do contrato de trabalho por prazo determinado - (firmado nos termos das Leis 9.601/98), deverá ser informado o código 3.

Sempre que este código deixar de ser informado ou for informado incorretamente, será adotado o código 1, ficando a empresa responsável por eventuais ônus.  
   
**Transferência**  
   
A transferência é feita através da rescisão contratual por transferência com os tipos: 5 (Transferência sem ônus p/ Cedente) ou 6 (Transferência com ônus p/ Cedente). Nestes tipos de rescisões existem particularidades que devem ser verificadas:

1. Se a transferência será realizada para a mesma coligada, caso contrário, será solicitado em qual a coligada será criado o novo registro. Vale ressaltar que somente serão apresentadas as coligadas que estão no mesmo mês da competência da coligada atual.

**Observações**

* Quando a Transferência é do tipo 5 (Transferência sem ônus p/ Cedente) e mesma coligada ou o usuário desmarca o parâmetro 'Realiza Transferência para mesma coligada' e informa a nova coligada com o CNPJ com a mesma raiz da coligada de origem, o processo desabilita as opções de Motivo da Transferência para o usuário selecionar e por default deixa o Motivo da Transferência 'Estabelecimentos da própria empresa' selecionado. Com este motivo de Transferência, o processo não irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial.
* Quando a Transferência é do tipo 5 (Transferência sem ônus p/ Cedente) e o usuário desmarca o parâmetro 'Realiza Transferência para mesma coligada'  e informa a nova coligada com o CNPJ com raiz diferente da coligada de origem, o processo habilita as opções de Motivo da Transferência para o usuário selecionar, podendo ser 'Empresa do mesmo grupo econômico', 'Empresa consorciada ou de consórcio' ou 'Sucessão, incorporação, cisão ou fusão'. Com estes motivos de Transferência, o processo irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial, conforme a Máscara para Matrícula do Trabalhador configurada em Configurações | Parâmetros | Parametrizador | 06.07- eSocial | Configurações Gerais.
* Quando a Transferência é do tipo 6 (Transferência com ônus p/ Cedente) as opções de Motivo da Transferência ficam desabilitadas para o usuário selecionar. Com este tipo de transferência o processo irá gerar para a Chapa ativa do Funcionário uma nova Matrícula eSocial, conforme a Máscara para Matrícula do Trabalhador configurada em Configurações | Parâmetros | Parametrizador | 06.07- eSocial | Configurações Gerais.

1. Se altera a chapa do funcionário demitido mantem o número da chapa antiga para o novo registro do funcionário ativo, apenas deve ser verificado que a transferência para o próximo mês altera a chapa do funcionário que ficará A – ativo e o chapa antiga ficará com o funcionário tipo Z - Admissão prox.mês, isto até a liberação de competência que altera a situação dos funcionários sem alterar a chapa.
2. Se transfere históricos, opção que somente será apresentada caso não haja transferência para mesma coligada. Serão copiados os históricos de Férias (incluindo os recibos), função, salário, afastamento, contribuição sindical, horário, provisão. Para estes históricos deve haver compatilibade dos códigos entre as coligadas, sob a responsabilidade do usuário. Serão feitas algumas verificações de inconsistências e caso ocorram a transferência será cancelada. Vale lembrar que, o Histórico de Seção não será copiado em caso de transferência entre coligadas. Isto é devido pelo fato de ocorrer incompatibilidade de códigos, descrições e demais dados das seções entre a coligada cedente e a coligada destino.
3. Se Transfere históricos de provisões serão copiados os históricos de provisões da chapa origem para a chapa destino. Com isso na transferência do histórico de provisões para a nova chapa Ativa constarão os valores acumulados do mês anterior. Para que seja considerado o valor total da provisão no primeiro mês da chapa Ativa, o histórico da chapa demitida não deve ser transferido.

   Exemplo com encargo 7

   Dados fictícios

   Funcionário transferido marcando "Transfere históricos de provisões" e não marcando provisão acumulada para o encargo 7 - Provisão de 13o. salário

   Para o funcionário Ativo será gerado abatendo o valor acumulado transferido

   **- Encargo: Provisão de 13o. salário**  
   **- Competência: 6/2025**   
   **- Calculando encargo: Provisão de 13o. salário**  
   **- Encargo = Provisão 13º mês atual - Provisão 13º mês anterior = 935,00 - 807,74 = 127,26**

   Funcionário transferido desmarcando "Transfere históricos de provisões" e não marcando provisão acumulada para o encargo 7 - Provisão de 13o. salário

   Para o funcionário Ativo será gerado

   **- Encargo: Provisão de 13o. salário**  
   **- Competência: 6/2025**   
   **- Calculando encargo: Provisão de 13o. salário**  
   **- Encargo = Provisão 13º mês atual - Provisão 13º mês anterior = 935,00**
4. O Histórico de situação não pode ser copiado quando a transferência é realizada entre coligadas nem entre filiais, este histórico nunca foi copiado na transferência pois pode causar problemas na geração de relatórios em competências anteriores.
5. Na transferência entre coligadas também será validada a tabela Acordo Coletivo / Reajuste por Lei (eSocial) que deve ter o mesmo código nas coligadas origem e destino.
6. Ao transferir um funcionário com retorno de afastamento por acidente de trabalho e solicitar para não transferir a movimentação do mês, a base de FGTS é contada até a data de saída do funcionário. O histórico de afastamento deve ficar somente em um dos registros.
7. Se realiza transferência para outra base de dados opção que somente será apresentada caso não haja transferência para mesma coligada. O funcionário será demitido por transferência, porém, o sistema não fará nenhum outro tratamento interno, ou seja, o sistema apresentará um alerta de que este funcionário não será mais tratado pelo Folha de Pagamento.
8. Caso haja histórico salarial futuro no momento da transferência do funcionário veja informações na aba Transferência de Funcionários do TDN [Histórico Salarial Futuro](https://tdn.totvs.com/pages/viewpage.action?pageId=687158765)
9. Ao realizar a transferência de um funcionário com férias marcadas e data de pagamento anterior a data de demissão, será apresentado a mensagem 'Há cadastro de férias com a situação 'Marcadas' e data de pagamento anterior a data de demissão.  Verifique a necessidade do lançamento das férias antes de realizar a transferência do funcionário.', quando:

I. Há férias marcadas com o início de gozo das férias posterior a data de demissão;

          II. O pagamento das férias é até a data de demissão;

          III. O parâmetro **Permite transferência tipo 5 de funcionário afastados ou de férias**  existente em RH | Folha de Pagamento | Configurações | Parametrizador | Rescisão | Transferência estiver **desmarcado**.

Cancelamento do processo

O cancelamento de uma operação em execução está sujeito a restrições técnicas inerentes ao ciclo de processamento.  
Quando a solicitação de cancelamento é emitida, o sistema avalia o estado atual do processo. Entretanto, **caso a operação já esteja em fase crítica de execução ou em etapa de finalização, o cancelamento poderá não ser efetivado**.

Entre os fatores que podem impactar a efetividade do cancelamento, destacam-se:

* Latência ou falhas de rede;
* Condições da infraestrutura de execução;
* Arquiteturas em múltiplas camadas (3-tier);
* Concorrência e bloqueios transacionais.

Devido a essas variáveis, **não é possível estabelecer um percentual fixo de progresso que assegure a possibilidade de cancelamento**.

**Observações para aposentadoria:**  
1.   Aposentadoria por tempo de serv com rescisão – Não continuará o vínculo empregatício – Não marcar o campo aposentado e não preencher data de aposentadoria no cadastro de funcionários.   
2.   Aposentadoria por tempo de serv sem rescisão – Continuará o vínculo empregatício – Apenas marcar o campo aposentado e preencher data de aposentadoria no cadastro do funcionário para ser informado no SEFIP.  
3.   Aposentadoria por Invalidez – Alterar a **situação** do funcionário no cadastro de funcionários para I – Aposent. Por Invalidez e colocar a data e motivo de alteração da situação. Não deve cadastrar data de aposentadoria.Esta aposentadoria somente será informada no arquivo de SEFIP quando houver algum recolhimento ao FGTS, ou seja, nos afastamentos por acidente de trabalho ou doença ocupacional.  
   
O código de saque é o código que será informado no termo de rescisão contratual e deve ser definido de acordo com o tipo de rescisão. Os códigos de saque são cadastrados nas tabelas dinâmicas.   
   
O saldo atual de FGTS do funcionário só será lançado com o parâmetro "Lança Saldo de FGTS" em Parâmetros do Folha de Pagamento marcado.  
   
Na demissão de um funcionário deve ser informado na posição 185 a 185 do registro 40 – Registro de Recolhimento Rescisório do Trabalhador se será uma reposição e para isto existe o parâmetro "Reposição de vaga". Maiores informações consulte o layout da guia disponibilizado no site: www.caixa.gov.br .  
   
**Observação:**  
Esta informação será armazenada no cadastro de funcionário, campo REPOEVAGA , tabela PFUNC e será utilizada para geração da GRRF Eletrônica.  
   
Nos casos em que o funcionário é demitido e o FGTS do mês anterior à rescisão será recolhido via GRFC junto com o FGTS rescisório é necessário utilizar o parâmetro "FGTS mês anterior recolhido na GRFC" no momento do cálculo da rescisão.  
O parâmetro não ficará visível para demissões com tipo de dispensa igual a:

* 1 - justa causa
* 4 - pedido de demissão
* 8 - falecimento

Normalmente esta situação ocorre em demissões do mês seguinte à folha, entre os dias 01 e 07 do próximo mês.  
Nestas datas (01 a 07) normalmente o FGTS da folha ainda não foi gerado pelo arquivo SEFIP.RE, e as vezes o usuário opta por recolher o FGTS do mês da folha na própria GRFC, juntamente com o FGTS rescisório.  
Ao gerar o arquivo SEFIP.RE do mês da folha dos funcionários com demissão no mês seguinte e que terão o FGTS mês anterior recolhido na GRFC, sairão no arquivo com um registro 32 de movimentação de demissão, porém com o indicativo de recolhimento em GRFC com o status = 'S' - Sim. Onde o 'S' significa que o recolhimento do FGTS da folha ou do mês anterior à data de demissão foi recolhido pela GRFC.  
   
Homolognet é um sistema do Ministério do Trabalho e Emprego que visa a conferência da rescisão contratual do funcionário que está se desligando da empresa. No cadastro de itens para a rescisão existem parâmetros que devem ou não serem marcados de acordo com a situação do desligamento do funcionário.  
   
Através da edição do movimento ou movimento C/C poderão ser cadastrados manualmente os eventos referentes à movimentação de rescisão.   
   
**Observação:**  
Para o correto lançamento da pensão alimentícia na rescisão, o usuário deverá lançar obrigatoriamente os eventos de cálculo da pensão alimentícia CC13 - Pensão alimentícia, CC 113 - Pensão alimentícia nas férias, CC120 - Pensão alimentícia s/13º salário e/ou CC121 - Pensão alimentícia s/ participação nos lucros para que o sistema calcule de acordo com as parametrizações. Caso o usuário lance apenas um dos códigos de cálculos não será calculado o valor total sobre 13º salário, férias ou participação nos lucros, será lançado somente o desconto da pensão alimentícia sobre o movimento.  
   
Os códigos fixos são cadastrados no cadastro de funcionários e serão lançados na rescisão contratual do funcionário desde que, estejam cadastrados como tipo rescisão, esteja marcado nos parâmetros do Folha de Pagamento e seja marcado no momento do cadastramento dos dados da rescisão o parâmetro de lançamento de códigos fixos.  
   
Nas verbas rescisórias será calculado o desconto de vale transporte do funcionário demitido para o próximo mês utilizando o cadastro do campo referente a quantidade de vale transporte para o próximo mês no cadastro do funcionário.  
   
Eventos de salário composto são eventos que um funcionário que utiliza este tipo de recebimento tem no cadastro de funcionários.   
É possível lançar os eventos do cadastro de funcionários referentes ao salário composto na rescisão desde que marque o parâmetro especifico: "Lança Eventos de Salário Composto na Rescisão". Este parâmetro habilita os seguintes parâmetros relacionados a ele:

* Lança eventos que tomam por base o salário composto
* Lança eventos relacionados ao salário composto

**Atenção:**  
1.    Serão automaticamente proporcionalizados os eventos que possuírem código de cálculo de horas normais ou dias trabalhados e que não sejam do tipo valor. Para outros tipos de eventos deverá ser configurado para proporcionalizar eventos em parâmetros do Folha de Pagamento e no cadastro de eventos. Qualquer evento que não se encaixe em um destes casos não será proporcionalizado.  
2.   O salário composto será lançado na rescisão somente pelo módulo de cadastro da rescisão no cadastro de funcionários, caso haja o cancelamento do movimento e o recálculo da rescisão através do módulo de recálculo estes eventos de salário compostos não serão lançados automaticamente.  
   
Verbas com insuficiência de saldo são verbas existentes na ficha financeira do funcionário que utiliza este tipo de controle através do cadastro de funcionários. Estas verbas podem ser descontadas na rescisão do funcionário desde que seja marcado o parâmetro "Lança verbas com insuficiência de saldo".   
   
**Atenção:**  
Se houver cancelamento da rescisão, o controle do saldo de insuficiência de verbas deverá ser refeito manualmente.  
   
Quando a empresa opta por conceder ao funcionário empréstimos será possível descontar na rescisão contratual os valores referentes a estes empréstimos utilizando o parâmetro "Lança Saldo Devedor de Empréstimos". Este desconto será bem flexível para o empregador, podendo ser desde todos os tipos de empréstimos até a configuração de cada empréstimo optando por não debitar, debitar totalmente ou debitar apenas próxima parcela.

Dica:

Veja sobre a modalidade de empréstimo "Crédito do Trabalhador eSocial" em [Medida Provisória Nº 1.292, de 12 de Março de 2025 - Crédito do Trabalhador - Linha RM](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)

Observação:

Quando a modalidade de empréstimo for "Crédito do Trabalhador eSocial" e o lançamento for manual, deve-se ter o cuidado com a seleção da forma de debitar o valor a ser descontado na rescisão do funcionário.

Quando o parâmetro “Usa folha agrária” em Parametrizador / Folha Agrária estiver marcado será habilitado os seguintes parâmetros:

* **Lançar convênio** que servirá para lançar a soma por evento das parcelas da movimentação em que o campo Mês e Ano de pagamento não tenha sido informado em Administração de Pessoal / Controle de convênios / Movimento / Movimentação dos Funcionários / Anexo Parcelas do Movimento do Convênio. O evento deverá ser obtido no parâmetro do convênio em Administração de Pessoal / Controle de convênios / Cadastros / Parâmetros do Convênio vinculado no movimento cadastrado em Administração de Pessoal / Controle de convênios / Movimento / Movimentação dos Funcionários referente as parcelas da movimentação Administração de Pessoal / Controle de convênios / Movimento / Movimentação dos Funcionários / Anexo Parcelas do Movimento do Convênio. Ao lançar a informação de mês e ano de competência paga, quando houver o cancelamento de rescisão será retirada a competência de pagamento, para posterior novo lançamento na ficha financeira (envelope de pagamento).

* **Lançar comissão** que servirá para lançar a soma por evento dos valores de comissão que o campo Mês e Ano não tenha sido informado em Folha Agrária / Comissão.

* **Lançar eventos da produção agrária** que servirá para lançar a soma por evento os valores de produção em que o campo Mês e Ano não tenha sido informado em Folha Agrária / Produção Agrária. Ao lançar para rescisão, deverá preencher os campos mês, ano e período assumindo o mês e ano e o período da demissão. No lançamento deverá observar o campo Comportamento: Substituir, Somar, Ignorar.

Ao fazer a rescisão contratual do funcionário é necessário emitir o Termo de Rescisão Contratual através do menu Rescisão / TRCT.

Para gerar os relatórios de demitidos pela visão do funcionários em Processos / Relatórios / Relatórios de Rescisão, será necessário que o Tipo de Relatório seja de Rescisão. Pode ser vinculado, por exemplo, Relatório de Aviso Prévio Trabalhado ou qualquer outro relatório, desde que sejam do tipo Rescisão e possuam campos da tabela PFUNC. Caso contrário será emitida a seguinte mensagem:

   
**Quarentena**  
   
O campo refere-se a 'quarentena' remunerada de trabalhador desligado. O registro deve ser preenchido com a data do fim da quarentena apenas no caso do trabalhador que recebe remuneração após o desligamento por estar impossibilitado de exercer atividade remunerada.  
Esse campo será enviado ao eSocial nos eventos S-2299 ou S-2399.  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários

Integração Folha de Pagamento x Gestão de Pessoas
