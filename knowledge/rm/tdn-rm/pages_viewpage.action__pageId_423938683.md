---
content_hash: 244b7949cffd045e123fa98aa2823f69bb0a0273ca1083608e3996d1b133c6b4
fetched_at: '2026-06-29T00:09:28.483627+00:00'
page_id: '423938683'
product: rm
source: tdn-rm
title: Consistência de Lançamentos Gestão Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938683
version: 12
---

**LANÇAMENTOS DO ANTIGO MODELO BACKOFFICE**

A Consistência de Lançamentos tem como objetivo analisar os dados relacionados a todos os lançamentos existentes na base, aos seus respectivos rateios, datas e valores e apontar inconsistências encontradas corrigindo-as quando possível.

Algumas inconsistências poderão ser acertadas automaticamente, bastando marcar as opções desejadas. Outras serão apenas registradas em um relatório (LOG) que será apresentado no final do processo, devendo ser acertadas manualmente pelo usuário.

É muito importante que se faça um backup antes de iniciar a consistência dos lançamentos contábeis.

**Observação**

Para converter a base de dados para a versão 11.0 (BackOffice) e superiores, tornou-se obrigatória a realização deste processo. A consistência de lançamentos realizada com este propósito deve ser processada com a opção 'Preparar a base para Conversão Novo Modelo de BackOffice' marcada. Quando não forem encontradas mais inconsistências impeditivas, a data da execução da rotina será automaticamente gravada na tela do processo e terá validade de 7 dias para a realização da conversão para o novo modelo. Este processo dever ser realizado em todas as coligadas.

**1. Rotinas de Correção Automática**  
Antes de iniciar o processo de consistência é possível filtrar o período desejado e também selecionar quais correções deverão ser realizadas automaticamente pelo sistema.

**1.1 - Ajustar capa do lote automaticamente:**

Verifica se a data dos lançamentos existentes nos lotes está entre a data definida na capa dos respectivos lotes, assim como se os valores lançados no lote não ultrapassam ao valor definido na capa do lote.

Se a rotina de consistência for processada com esta opção marcada e forem encontrados lançamentos fora das datas das capas dos respectivos lotes, o sistema atualizará as datas, inicial e final, da capa do lote conforme as datas dos seus lançamentos, sendo a data inicial da capa do lote substituída pela menor data dos lançamentos do lote e a data final da capa do lote substituída pela maior data dos lançamentos do lote. Da mesma forma que se os valores lançados no lote ultrapassarem ao valor definido na capa do lote, o sistema atualizará o valor definido na capa. No relatório os registros corrigidos virão precedidos da mensagem: "Lotes que tiveram as datas e/ou valor da capa ajustados automaticamente".

Caso a opção esteja desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: "Lançamentos fora do Período e/ou valores divergentes da Capa do Lote".

**1.2 - Atualizar aplicação de origem do lançamento de acordo com o lote**

Verifica se a aplicação de origem nos lançamentos está diferente da aplicação de origem do lote N e do lote Zero.

Se a rotina de consistência for processada com esta opção marcada e forem encontrados lançamentos com estas inconsistências, o sistema atualizará automaticamente a aplicação de origem nos lançamentos de acordo com a aplicação de origem do lote. No relatório os registros corrigidos virão precedidos da mensagem: "Lançamentos que tiveram o campo Aplicação de Origem atualizado de acordo com lote".

Caso ocorra algum erro no processo de atualização, os registros serão apresentados precedidos da mensagem: "Lançamentos que não foram possíveis atualizar o campo Aplicação de Origem de acordo com lote".

Caso a opção esteja desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: "Lançamentos com aplicação de origem diferente do lote".

**1.3 - Atualizar data dos rateios de acordo com o respectivo lançamento**

Verifica se a data dos itens de rateio está diferente da data do respectivo lançamento.

Se a rotina de consistência for processada com esta opção marcada e forem encontrados lançamentos com estas inconsistências, o sistema atualizará a data do item de rateio de acordo com a data do seu respectivo lançamento. No relatório os registros corrigidos virão precedidos da mensagem: "Itens de rateio que tiveram suas datas atualizadas conforme seu lançamento".

Caso a opção esteja desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: "Rateios com a data diferente do lançamento".

**1.4 - Excluir rateios de contas que não exigem rateio**

Verifica se existe rateio para contas que não possuem distribuição gerencial (rateio).

Se a rotina de consistência for processada com esta opção marcada e forem encontrados rateios com estas inconsistências, o sistema excluirá todos os rateios cuja conta contábil não possua distribuição gerencial (rateio). No relatório os registros excluídos virão precedidos da mensagem: "Foram excluídos os seguintes itens de rateios dos lançamentos em conta contábil que não exige distribuição gerencial."

Caso ocorra algum erro no processo de exclusão, os registros serão apresentados precedidos da mensagem: "Não foi possível excluir os seguintes itens de rateios dos lançamentos em conta contábil que não exige distribuição gerencial, pois, possuem referência em outras tabelas."

Caso a opção esteja desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: "Rateios de contas que não exigem rateio".

**1.5 - Excluir rateios sem lançamentos**

Verifica se existem rateios que não possuem os lançamentos correspondentes.

Se a rotina de consistência for processada com esta opção marcada e forem encontrados rateios com estas inconsistências, o sistema excluirá todos os rateios encontrados que não possuem os lançamentos correspondentes. No relatório os registros excluídos virão precedidos da mensagem: "Foram excluídos os seguintes itens de rateios por não estarem relacionados a algum lançamento"

Caso ocorra algum erro no processo de exclusão, os registros serão apresentados precedidos da mensagem: "Não foi possível excluir os seguintes itens de rateios que não estão associados a algum lançamento, pois, possuem referência em outras tabelas.."

Caso a opção esteja desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: "Rateios que não possuem lançamento".

**1.6 - Corrigir lançamentos originados do RM Nucleus sem registros na tabela TMovCont.**

Verifica se existem lançamentos que foram originados pelo RM Nucleus, mas não têm referência com a contabilização do movimento que o originou.

Exemplo: Existe o registro na tabela CLANCA, porém não existe o registro correspondente na tabela TMOVCONT, porém o campo INTEGRAAPLICACAO deste registro apresenta a letra T informando que o mesmo foi originado do RMNucleus.

A mesma inconsistência pode ocorrer para lançamentos originados do RM Liber.

Se a rotina de consistência for processada com esta opção marcada e forem encontrados lançamentos com estas inconsistências, o sistema atualizará estes lançamentos. Nesta atualização estes lançamentos passam a ter o valor C no campo INTEGRAAPLICACAO da tabela CLANCA , entretanto o campo da chave da integração passa a ter um indicador informando que aquele registro teve origem real no RMNucleus (INTEGRACHAVE passará para '#IDMOV'). No relatório os registros corrigidos virão precedidos da mensagem: "Lançamentos corrigidos que foram originados do RM Nucleus sem registro na tabela TMOVCONT"

Caso a opção esteja desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: "Lançamentos originados no RM Nucleus sem registros na tabela TMOVCONT."

**1.7 - Corrigir registros de rateio de outros sistemas que tem os campos Referência e Lote divergentes com a contabilização.**

Verifica se existem registros na tabela de rateios dos aplicativos de origem com campos que estão divergentes da tabela de contabilização dos aplicativos de origem.

Exemplo: Na tabela TMOVRAT (tabela de rateios do movimento) o campo CODLOTE ou LCTREF está diferente do campo CODLOTE ou LCTREF da tabela TMOVCONT (tabela de contabilização do movimento).

Se a rotina de consistência for processada com esta opção marcada e forem encontrados rateios com estas inconsistências, o sistema atualizará todos os registros da tabela de rateios (TMOVRAT/DLAFRAT) alterando os campos Referencia (LCTREF), Lote (CODLOTE) e Referencia da Integração (LCTREFINT) de acordo com os respectivos campos na contabilização (TMOVCONT/DLAFCONT), quando existir ligação com a tabela de rateios do RM Saldus (CrateioLc). Quando não existir esta ligação, os registros serão excluídos.

No relatório os registros virão precedidos com mensagens de acordo com as situações abaixo:

* Registros atualizados originados do RM Líber: "Rateios corrigidos do RM Líber que possuíam código do lote, referência do lançamento ou referência do lançamento integrado diferente da tabela de contabilização do RM Líber"
* Registros excluídos originados do RM Líber: "Rateios excluídos do RM Líber que possuíam código do lote, referência do lançamento ou referência do lançamento integrado diferente da tabela de contabilização do RM Líber e não tinham ligação com a tabela de rateios no RM Saldus"
* Registros atualizados originados do RM Nucleus: "Rateios corrigidos do RM Nucleus que possuíam código do lote, referência do lançamento ou referência do lançamento integrado diferente da tabela de contabilização do RM Nucleus"

* Registros excluídos originados do RM Nucleus: "Rateios excluídos do RM Nucleus que possuíam código do lote, referência do lançamento ou referência do lançamento integrado diferente da tabela de contabilização do RM Nucleus e não tinham ligação com a tabela de rateios do RM Saldus"

Caso a opção esteja desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros virão precedidos da mensagem: "Rateios do RM Líber que possuem código do lote, referência do lançamento ou referência do lançamento integrado diferente da tabela de contabilização do RM Líber", para registros do RM Líber e "Rateios do RM Nucleus que possuem código do lote, referência do lançamento ou referência do lançamento integrado diferente da tabela de contabilização do RM Nucleus" para registros do RM Nucleus.

Além destas validações onde, se marcadas as opções, o sistema, conforme relatado anteriormente fará automaticamente a correção, existem outras verificações contempladas neste processo que não poderão ser corrigidas automaticamente, pois precisam de análise para definir a lógica a ser adotada para a correção. Neste caso, elas serão relacionadas no relatório para que sejam tomadas as devidas providências no sentido de acertá-las. São elas:

**2. Rotinas de Correção Manual**

**2.1- Lançamentos fora do período contábil – (Data inicial do Período) a (Data final do Período)**

Informa todos os lançamentos que têm data fora do período contábil definido no sistema.

**2.2- Lançamentos cuja diferença da soma dos débitos e créditos da tabela CLCTLOTE não está condizente com a diferença apresentada na tabela CDIFERENCA ou na tabela CLOTE**

Informa todos os lançamentos cuja soma dos débitos e créditos do lançamento do lote N não seja condizente com a diferença informada na tabela de Lote (quando só permite uma diferença), ou na tabela de Diferenças (quando estiver configurada para diversas diferenças).

**2.3 - Lançamentos que não possuem rateios exigidos**

Informa todos os lançamentos que não tem registros de rateios, mas sua conta exige rateios.

**2.4 - Lançamentos que possuem rateios com valor 0 (zero)"**

Informa todos os lançamentos que não tem registros de rateios, mas sua conta exige rateios.

**2.5 - Soma dos valores do rateio a crédito com valor diferente do valor do lançamento**

Informa todos os lançamentos cujo valor é diferente da soma dos rateios de crédito.

**2.6 - Soma dos valores do rateio a débito com valor diferente do valor do lançamento**

Informa todos os lançamentos cujo valor é diferente da soma dos rateios de débito.

**2.7 - Rateios a débito para conta a crédito**

Informa todos os rateios com contas de crédito que têm o valor de débito maior que zero.

**2.8 - Rateios a crédito para conta a débito**

Informa todos os rateios com contas de débito que tem o valor de crédito maior que zero.

**2.9 - Lançamentos com soma de rateios do RM Líber (DLafRat) diferente da soma de rateios do RM Saldus (CRateioLc)**

Informa todos os rateios que o valor de débito/crédito no RM Saldus não seja condizente com a soma dos valores de seus correspondentes no RM Líber.

**2.10 - Lançamentos com soma de rateios do RM Nucleus (TMovRat) diferente da soma de rateios do RM Saldus (CRateioLc)**

Informa todos os rateios que o valor de débito/crédito no RM Saldus não seja condizente com a soma dos valores de seus correspondentes no RM Nucleus.

**2.11 - Lançamentos com soma de rateios (DLafRat) diferente do valor da contabilização (DLafCont)**

Informa todos os rateios do RM Líber cuja soma de seus valores não seja condizente com do valor da sua contabilização.

**2.12 - Lançamentos com soma de rateios (TMovRat) diferente do valor da contabilização (TMovCont)**

Informa todos os rateios do RM Nucleus cuja soma de seus valores não seja condizente com do valor da sua contabilização.

**2.13 - Lançamentos com contabilização em datas diferentes das que se encontram no aplicativo de Origem**

Irá fazer uma busca, selecionando todos os registros da contabilização (TMOVCONT e DLAFCONT) que tenham registros de lançamentos (CLANCA e CLCTLOTE) com datas diferentes para o mesmo movimento, lote e coligada (IDMOV/IDLAF, CODLOTE e CODCOLIGADA) retornando um LOG ao final do processo para que o usuário escolha a melhor forma de correção.

**2.14 Lançamentos com contabilização em datas diferentes das que se encontram no aplicativo de Origem**

Irá fazer uma busca, selecionando todos os registros da operação de contabilização (COPERACAO) que tenham registros de partidas (CPARTIDA) com datas diferentes para a mesma operação, sistema de origem e coligada (IDOPERAÇÃO, ORIGEM e CODCOLIGADA), retornando um LOG ao final do processo para que o usuário escolha a melhor forma de correção.

**LANÇAMENTOS DO NOVO MODELO BACKOFFICE**

A Consistência de Lançamentos tem o objetivo de analisar os dados relacionados a todos os lançamentos, aos seus respectivos rateios, datas e valores e apontar inconsistências encontradas. Este processo também inclui a validação de dados gerados pelo RM Nucleus e RM Líber.

Algumas inconsistências poderão ser acertadas automaticamente, basta marcar as opções desejadas. Outras serão apenas registradas em um LOG que será apresentado no final do processo.

É muito importante que se faça um backup antes de iniciar a consistência dos lançamentos contábeis.

**1 Rotinas de Correção Automática**

**1.1****Ajustar capa do lote automaticamente.**

Verifica se a data dos lançamentos existentes nos lotes está entre a data definida na capa dos respectivos lotes.

Se a rotina de consistência for processada com esta opção marcada e no lote a opção "Digitar Capa" estiver marcado e forem encontrados lançamentos fora das datas das capas dos respectivos lotes , o sistema atualizará as datas, inicial e final, da capa do lote conforme as datas dos seus lançamentos, sendo a data inicial da capa do lote substituída pela menor data dos lançamentos do lote e a data final da capa do lote substituída pela maior data dos lançamentos do lote. No relatório os registros corrigidos virão precedidos da mensagem: “Lotes que tiveram as datas da capa ajustadas automaticamente”.

Já se a rotina de consistência for processada com esta opção desmarcada e no lote a opção "Digitar Capa" estiver marcado, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: “Lançamentos fora do período da capa do lote”.

Caso a rotina de consistência for processada com esta opção marcada e no lote a opção "Digitar Capa" não estiver marcado, o sistema irá corrigir a capa do lote, mas não mostratá no log do processo esta alteração.

**1.2****Atualizar aplicação de origem do lançamento de acordo com o lote.**

Atualiza a campo aplicação (INTEGRAAPLICACAO) da tabela dos lançamentos do lote (CLCTLOTE) cujo mesmo não seja correspondente ao campo de homônimo da tabela de lotes (CLOTE)

No relatório os registros corrigidos vêm precedidos da mensagem: “**Lançamentos que tiveram o campo Aplicação de Origem atualizado de acordo com lote**”.

Caso ocorra algum erro no processo de atualização, os registros serão apresentados precedidos da mensagem: “**Lançamentos que não foram possíveis atualizar o campo Aplicação de Origem de acordo com lote**”.

Se a rotina de consistência for processada com esta opção desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: “**Lançamentos com aplicação de origem diferente do lote**”.

**1.3****Atualizar data dos rateios de acordo com o respectivo lançamento.**

Atualiza a data do item de rateio de acordo com a data do seu respectivo lançamento.

No relatório os registros corrigidos vêm precedidos da mensagem: “**Itens de rateio que tiveram suas datas atualizadas conforme seu lançamento**”.

Se a rotina de consistência for processada com esta opção desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: “**Rateios com a data diferente do lançamento**”.

**1.4****Excluir rateios de contas que não exigem rateios.**

Exclui todos os rateios cuja conta do lançamento não exige rateios.

No relatório os registros excluídos vêm precedidos da mensagem: “**Foram excluídos os seguintes itens de rateios dos lançamentos em conta contábil que não exige distribuição gerencial.**”

Caso ocorra algum erro no processo de exclusão, os registros serão apresentados precedidos da mensagem: “**Não foi possível excluir os seguintes itens de rateios dos lançamentos em conta contábil que não exige distribuição gerencial, pois, possuem referência em outras tabelas**.”

Se a rotina de consistência for processada com esta opção desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: “**Rateios de contas que não exigem rateio**”.

**1.5****Excluir rateios sem lançamentos.**

Exclui todos os rateios que não foram encontrados os seus respectivos lançamentos.

No relatório os registros excluídos vêm precedidos da mensagem: “**Foram excluídos os seguintes itens de rateios por não estarem relacionados a algum lançamento**”

Caso ocorra algum erro no processo de exclusão, os registros serão apresentados precedidos da mensagem: “**Não foi possível excluir os seguintes itens de rateios que não estão associados a algum lançamento, pois, possuem referência em outras tabelas.**.”

Se a rotina de consistência for processada com esta opção desmarcada, o sistema apenas apresentará uma lista no relatório contendo os registros que contemplam tal inconsistência. Estes registros serão precedidos da mensagem: “**Rateios que não possuem lançamento**”.

**1.6 Atualizar o sincronismo dos campos do Lançamento/Rateio com o AUTOINC correspondente..**

O processo ajusta nos campos que são chave para o lançamento e rateio de forma automática para sua AUTOINC correspondente.

Quando executar o processo com está opção marcada?

Apenas nos casos em que algum processo da contabilidade apresente erros relacionados a PK (Chave Primaria Duplicada) ou FK (Chave Estrangeira Duplicada).

**2****Rotinas de Correção Manual**

Haverá alguns casos que o processo de consistência não poderá corrigir automaticamente os problemas apresentados, pois precisa de um analise para definir a lógica a ser adotada na correção, pelo fato de existir diversas variáveis possíveis para a solução. Segue as mensagens retornadas:

**2.1****Lançamentos fora do período contábil - {Data inicial do Período} a {Data final do Período}”**

Informa todos os lançamentos que tem data fora do período contábil definido no sistema.

**2.2****Lançamentos que a diferença da soma dos débitos e créditos da tabela CLCTLOTE não está condizente com a diferença apresentada na tabela CDIFERENCA ou na tabela CLOTE**

Informa todos os lançamentos cuja soma dos débitos e créditos do lançamento do lote N não seja condizente com a diferença informada na tabela de Lote, quando só permite uma diferença, ou na tabela de Diferenças, quando estiver configurada para diversas diferenças.

**2.3****Lançamentos que não possuem rateios exigidos**

Informa todos os lançamentos que não tem registros de rateios, mas sua conta exige rateios.

**2.4****Lançamentos que possuem rateios com valor 0 (zero)”**

Informa todos os lançamentos que não tem registros de rateios, mas sua conta exige rateios.

**2.5****Soma dos valores do rateio a crédito com valor diferente do valor do lançamento**

Informa todos os lançamentos que o valor é diferente da soma dos rateios de credito.

**2.6****Soma dos valores do rateio a débito com valor diferente do valor do lançamento**

Informa todos os lançamentos que o valor é diferente da soma dos rateios de débito.

**2.7****Rateios a débito para conta a crédito**

Informa todos os rateios com contas de crédito que tem o valor de débito maior que zero.

**2.8****Rateios a crédito para conta a débito**

Informa todos os rateios com contas de débito que tem o valor de crédito maior que zero.

**2.9****Lançamentos que contém datas de partidas diferentes.**

Informa todas as partidas que tem datas não condizente com a data do seu Lançamento.

**2.10****Operações sem registro de contabilização.**

Informa todas as operações que não tem um registro de contabilização vinculada ao mesmo.

**2.11****Contabilização sem registro de operação.**

Informa todas as contabilizações que não tem um registro de operação vinculada ao mesmo.

**2.12****Lançamentos com soma de rateios do RM Líber (DLafRat) diferente da soma de rateios do RM Saldus (CRateioLC)**

Informa todos os rateios que o valor de débito/crédito no RM Saldus seja incondizente com a soma dos valores de seus correspondentes no RM Líber.

**2.13****Lançamentos com soma de rateios (DLafRat) diferente do valor da contabilização (DLafCont)**

Informa todos os rateios do RM Líber cuja soma de seus valores seja incondizente com do valor da sua contabilização.

**2.14 Lançamentos com contabilização em datas diferentes das que se encontram no aplicativo de Origem**

Irá fazer uma busca, selecionando todos os registros da operação de contabilização (COPERACAO) que tenham registros de partidas (CPARTIDA) com datas diferentes para a mesma operação, sistema de origem e coligada (IDOPERAÇÃO, ORIGEM e CODCOLIGADA), retornando um LOG ao final do processo para que o usuário escolha a melhor forma de correção.
