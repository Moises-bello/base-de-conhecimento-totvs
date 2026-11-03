---
content_hash: f406459df3883be12e12a7662b1e1f93cfbddc1370e871552f75b1684d9b4aa3
fetched_at: '2026-06-29T00:08:46.529065+00:00'
page_id: '317301097'
product: rm
source: tdn-rm
title: RMEDU00001_Especificação Técnica_Bolsa_Retroativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317301097
version: 104
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** |  |
| **Segmento Executor** |  | | |
| **Projeto1** | Bolsa Retroativa | **IRM1** | PCREQ-9515 |
| **Requisito1** | PCREQ-9516 | **Subtarefa1** | PDR\_EDU\_EDU019-40 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Flexibilizar o processo de Bolsa Retroativa, as contabilizações relacionadas e a origem de itens gerados. Dessa forma o processo de concessão e exclusão de bolsas será mais transparente mantendo inalterados os títulos financeiros já baixados.

## **Definição da Regra de Negócio**

### Funcionamento Geral

Será criado o parâmetro de sistema “***Usar bolsa retroativa sem alterar parcelas já baixadas***” que, caso esteja **MARCADO**, considerará o modelo proposto descrito no documento abaixo e, caso esteja **DESMARCADO**, considerará que o usuário deseja trabalhar com o modelo atual do processo (com cancelamento de baixa, inclusão / exclusão de bolsa no contrato, regeração de lançamentos, reconciliação de extrato e baixa novamente).

Considerando que o parâmetro acima esteja **MARCADO**, no caso de **INCLUSÃO** de bolsa retroativa, o sistema gerará lançamentos a pagar de devolução a fim de devolver o valor da bolsa que foi desconsiderado nas parcelas pagas pelo responsável financeiro do aluno ou gerará créditos na conta corrente do aluno a fim de conceder abatimentos nas cobranças futuras. Será disponibilizada a opção de se utilizar o maior crédito possível nas próximas parcelas ou proporcionalizá-lo nas parcelas em aberto para o contrato.

Considerando que o parâmetro acima esteja **MARCADO**, no caso de **EXCLUSÃO** de bolsa retroativa, o sistema gerará parcelas/lançamentos a receber a fim de cobrar o valor do responsável financeiro do aluno ou gerará débitos na conta corrente do aluno a fim de cobrar os valores de descontos referentes às bolsas agora excluídas. Será disponibilizada a opção de se gerar uma única parcela/lançamento ou proporcionalizar o valor em várias parcelas quantas forem as parcelas em aberto do contrato.

### Parâmetros gerais

As regras para o novo processo de bolsa retroativa serão utilizadas, somente, se o sistema for parametrizado para utilizá-lo.

O parâmetro “***Usar bolsa retroativa sem alterar parcelas já baixadas***” será criado para que o sistema entenda que houve a migração para o novo processo.

Caminho: ***Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | ***Fin - Bolsa Retroativa 1/3*** | "Usar bolsa retroativa sem alterar parcelas já baixadas"***

Juntamente com o parâmetro para uso do novo processo serão exibidos outros dois parâmetros para a seja realizada a definição da forma de utilização do crédito criado:

Parâmetro:

**Forma de utilização de crédito:**

* + **********Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa) = "D"**********
  + ****************Usar conta corrente = "C"****************

Caminhos:

***Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | Fin - Bolsa Retroativa 1/3 |** Grupo**: Forma de utilização de crédito | "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***"***

***Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | Fin - Bolsa Retroativa 1/3 |***Grupo: **Forma de utilização de crédito |*****"***Usar conta corrente***"***

Importante

A definição para se utilizar o novo processo de bolsa retroativa não poderá ser alterada. Uma vez que o parâmetro "**Usar bolsa retroativa sem alterar parcelas já baixadas**" for definido não será possível retornar para o modelo antigo.

Com a definição para a utilização do novo processo, será necessário informar a forma de utilização dos créditos gerados.

**Os parâmetros para migração para o novo modelo e a sua forma de utilização não poderão ser alterado depois que houver a inclusão de bolsas.** Antes da primeira inclusão, os parâmetros, ainda, ficaram habilitados para alteração.

* + - Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)

Com a forma de utilização do crédito definida como "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***", o processo de bolsa retroativa passará a criar devoluções quando uma bolsa for incluída e criar lançamentos a receber com a diferença dos valores, quando a bolsa for excluída.

A forma de utilização será habilitada, somente, quando o parâmetro “***Usar bolsa retroativa sem alterar parcelas já baixadas***” estiver marcado.

Será criado um grupo de parâmetros para um comportamento ***padrão*** na geração de devoluções durante o processo de bolsa retroativa:

Para **Inclusão de Bolsa (Devolução)**:

Caminho:***Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | ***Fin - Bolsa Retroativa 2/3*** |*** ***Inclusão de Bolsa***

Parâmetro:

**Forma de aproveitamento de crédito**

* + - * + - * *****Aplicar devolução no lançamento da primeira parcela em aberto** = "P"***
            * ***Dividir devolução pela quantidade de parcelas restantes = "R"***
            * ***Devolver em espécie = "E"***

Parâmetros default para geração do lançamento:

* + - Tipo de documento (Classificação Devolução)
    - Tipo contábil
    - Histórico
    - Data de contabilização
    - Evento para inclusão de lançamento
    - Centro de custo
    - Departamento
    - Conta caixa
    - Tabelas opcionais
    - Datas opcionais
    - Campos alfa

Parâmetros que serão exibidos no processo de bolsa retroativa para geração de devoluções:

Caminho:***Educacional | Educacional | Financeiro/Contábil | Assistentes | Incluir/Excluir bolsas retroativas***

* + - Tabelas opcionais (carregar valores defaults)
    - Datas opcionais (carregar valores defaults)
    - Campos alfa (carregar valores defaults)

Para **Exclusão de Bolsa**:

Caminho:***Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | ***Fin - Bolsa Retroativa 3/3*** |******Exclusão de Bolsa***

Parâmetros:

**Forma de cobrança de devolução**

* + ***Gerar uma única parcela para pagamento = "U"***

* + ***Dividir pela quantidade de parcelas restantes = "R"***

**Gerar lançamentos (S/N)**

Parâmetros default para geração de lançamentos:

* + - * Data de contabilização
      * Evento para inclusão de lançamento
      * Serviço
      * Tipo de parcela (adicional / extra)
      * Data de vencimento (Data do sistema, Data da última parcela ou número de dias após a data de concessão, informada manualmente). Esse parâmetro será utilizado somente no caso de geração de parcela única. Se estiver parametrizado para dividir pela quantidade de parcelas restantes, a data de vencimento será a mesma data da respectiva parcela com mesmo número.
      * Caso seja a opção seja informar manualmente, será exibido um campo para informar a data de vencimento no processo de inclusão/exclusão.

Parâmetros que serão exibidos no processo de bolsa retroativa para exclusões de bolsa:

Caminho:***Educacional | Educacional | Financeiro/Contábil | Assistentes | Incluir/Excluir bolsas retroativas***

Caso o parâmetro "**Gerar uma única parcela para pagamento**" seja marcado, os campos abaixo deverão ser exibidos:

* + Data de vencimento (quando for informada manualmente)
  + Competência

false

Deverá ser criada uma opção de perfil nos parâmetros educacionais para definir se o usuário terá ou não permissão para alterar os valores padrões informados nos parâmetros durante o processo.

***Serviços Globais | Segurança | Perfis |***Sistema***: Educacional |***Anexos***: Parâmetros educacionais***

* + - * + - Aba:******Bolsa Retroativa******
          - Parâmetro:***Alterar parâmetros de comportamento padrão na geração de devoluções***

Esse parâmetro não deve ser exibido, caso a forma de aproveitamento seja ***"***Usar conta corrente***",*** ou não deve ser habilitado. Ele se refere a alterações das formas de utilização de crédito quando o sistema estiver parametrizado para criar devoluções "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***".

Será exibido, também, um parâmetro para se utilizar as devoluções pendentes, após término de contrato, nos próximos contratos com mesmo responsável financeiro e mesmo aluno. A utilização desses valores, em contratos futuros, irá gerar um vínculo automático da devolução utilizada com o contrato.

Caminho:***Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | ***Fin - Bolsa Retroativa 1/3******

Parâmetro:***"Usar devoluções pendentes após término de contrato nos próximos contratos"***

* + - Usar conta corrente

Com a forma de utilização do crédito definida como "***Usar conta corrente***", o valor será incluído da conta corrente do aluno, como crédito ou débito, dependendo da ação executada para inclusão ou exclusão de bolsa. Nos dois casos, não haverá nenhuma alteração nos lançamentos já baixados. Os parâmetros para inclusão e exclusão de lançamento serão desabilitados para essa situação.

O parâmetro "***Refaz automaticamente conciliação de extrato no processo de inclusão/exclusão de bolsa retroativa***” terá sua localização alterada.

Ele será retirado do caminho***Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | ***Fin - Geral 3/3****** e será movido para o caminho*********Educacional | Educacional | Configurações | Parâmetros | 15.05 - Integração | 15.05.03 - Financeiro | ***Fin - Bolsa Retroativa 1/3.************

Além da mudança de localização, ele será habilitado, somente, se o parâmetro***************"Usar bolsa retroativa sem alterar parcelas já baixadas"*************** estiver desmarcado, caso contrário ele será desabilitado.

### Processo de inclusão/exclusão de bolsa retroativa

Para o tratamento do novo modelo de Bolsa Retroativa, iremos utilizar o mesmo processo existente, hoje.

Caminho:***Educacional | Educacional | Financeiro/Contábil | Assistentes | Incluir/Excluir bolsas retroativas***

Caso o parâmetro “***Usar bolsa retroativa sem alterar parcelas já baixadas***” esteja marcado, o processo seguirá a regra do novo modelo de aplicação de bolsa retroativa, caso não esteja funcionará com o modelo anterior.

Integração com o Protheus

As restrições para uso de bolsa retroativa com o Protheus deverão ser mantidas, pois, hoje, ainda, não tratamos as informações de vínculos com os lançamentos de devolução. Precisariam, também, ser inclusos os envios de cancelamentos/exclusões de lançamentos quando forem tratadas as bolsas de crédito.

#### Etapas do processo

O processo terá um comportamento diferente se estiver parametrizado para utilizar o novo modelo de bolsa retroativa. Caso, utilize o modelo antigo o comportamento não será alterado.

##### Primeira etapa:

Será exibida a seleção dos contratos que terão a inclusão ou exclusão de bolsas. Essa etapa não será alterada.

##### Segunda etapa:

Essa etapa não terá o campo de tipo de cobrança no novo modelo, para exclusão. A forma de cobrança será definida nos parâmetros do Educacional.

A lookup de Bolsas deverá exibir, somente, as bolsas permitidas para o período letivo selecionado na etapa anterior.

Nessa etapa serão definidos todas as informações pertinente para a bolsa selecionada e incluída no Grid de Bolsas.

A permissão para alteração do valor da bolsa irá depender da flag "Permite alterar valor" no cadastro de bolsa.

Serão exibidos os campos para definição da validade da bolsa.

O campo de ordem não será exibido, pois as bolsas sempre entrarão na última posição.

**Para a inclusão de bolsas**, serão exibidos os campos de valores opcionais: Tabelas opcionais, Datas opcionais e campos Alpha.

**Para exclusão de bolsas**, serão exibidos os campos de valores opcionais: Tabelas opcionais, Datas opcionais e campos Alpha e um campo, somente leitura, com o***tipo de parcela (Adicional/Extra).***

Caso esteja parametrizado para a geração de uma única parcela:

* + - Deverá ser exibido o campo de Data de vencimento (quando for informada manualmente)
    - Deverá ser exibido o campo de Data de competência se houver integração contábil

Caso esteja parametrizado para a divisão pela quantidade de parcelas restantes:

* + - As datas de vencimento e competência assumirão as mesmas das parcelas restantes.

Se o sistema estiver parametrizado para utilizar o novo modelo de bolsa retroativa com o uso de valores em conta corrente, não será necessário a exibição dos campos para geração de lançamentos: Tabelas opcionais, Datas opcionais e campos Alpha.

##### Terceira etapa:

 Caso o usuário tenha a permissão "***Alterar parâmetros de comportamento padrão na geração de devoluções"***no perfil de usuários, será exibida essa etapa com a possibilidade de se alterar a forma de utilização do crédito, quando estiver parametrizado para criar devoluções.

Será carregada a definição padrão cadastrada nos parâmetros e será permitida que ela seja alterada para esse processo: 

Opções para inclusão:

* + Aplicar devolução no lançamento da primeira parcela em aberto
  + Dividir devolução pela quantidade de parcelas restantes
  + Devolver em espécie

Opções para exclusão:

* + Gerar uma única parcela para pagamento
  + Dividir pela quantidade de parcelas restantes
  + Gerar lançamentos (S/N)

 Caso o sistema esteja parametrizado para utilizar conta corrente, essa etapa não será exibida. 

##### Quarta etapa:

Essa será a etapa com informações para os usuários, como se tem hoje, e deverá ser exibida, somente, se o sistema estiver parametrizado para utilização do modelo antigo de bolsa retroativa.

Serão criadas as tabelas ***SBOLSARETROATIVACONTRATO***, ***SBOLSARETROATIVAPARCELA*** para registro dos créditos/débitos originados de valores pagos indevidamente, pelas baixas de lançamentos e exclusões de bolsas.

#### Inclusão de bolsa retroativa

As regras anteriores para inserção da bolsa no contrato e a validação de movimento gerado serão mantidas.

Para mantermos a mesma validação, não poderão ser inclusas bolsas em contratos cancelados.

Não poderão ser inclusas bolsas em contratos originados por acordo (Tipo = "Acordo").

O processo deverá ser capaz de verificar se o contrato possui parcelas com lançamentos gerados, de forma a entender se será aplicada uma bolsa retroativa ou uma bolsa normal. Caso haja lançamentos gerados deverá ser aplicada uma bolsa retroativa, caso não, será inclusa uma bolsa normal.

Caso a bolsa retroativa seja incluída após a geração da Nota Fiscal Eletrônica, o valor de desconto não sairá na nota das parcelas cuja NFe foi gerada, a não ser que as notas referente à essas parcelas onde o desconto está sendo aplicado possam ser canceladas e geradas novamente após a inclusão da bolsa retroativa.

A bolsa inserida como **retroativa** deverá ser marcada como retroativa, com o valor ***"S"***, através do campo ***BOLSARETROATIVA*** criado na tabela ***SBOLSAALUNO***.

A inclusão de uma bolsa retroativa irá afetar as parcelas que tenham lançamentos com status ***"Em aberto" e/ou*** ***"Baixados"***.

As parcelas com lançamentos já baixados ou baixados parcialmente não devem ser alteradas. Para esses casos, serão calculados os valores a serem devolvidos e um lançamento de devolução de crédito será criado.

As parcelas com lançamentos ***"Em aberto"*** terão um crédito vinculado, de acordo com a parametrização realizada para aproveitamento de seu crédito.

Ao se realizar a inclusão de uma bolsa retroativa, o sistema deverá:

* + Validar na tabela ***SBOLSARETROATIVACONTRATO*** se o valor total de crédito não irá ultrapassar o valor total do contrato.
  + Calcular o valor total de crédito, a ser devolvido, dos lançamentos gerados, já baixados integral e/ou parcialmente ou não baixados, para cada bolsa, respeitando a validade da bolsa. A validade por ser por data ou parcela.
  + Incluir um registro na tabela ***SBOLSARETROATIVACONTRATO*** com o valor total de crédito gerado pela bolsa e definir a sua classificação como ***CRÉDITO***.
  + Verificar se o sistema foi parametrizado para "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***" ou  "***Usar conta corrente***".
  + Caso seja uma bolsa de crédito, deverá ser criado um lançamento a receber para o sacado responsável que efetuará o pagamento do crédito.

Caso parametrizado para criar devolução:

* + - * Criar um lançamento a pagar, com o tipo de documento de devolução default, com o valor total de crédito por bolsa. Esse lançamento deverá ter o código de aplicação do Educacional ***"S"***.
      * Inserir na tabela ***SBOLSARETROATIVAPARCELA*** o registro das parcelas com lançamentos em aberto ou já baixados e que deram origem ao crédito. Incluir o valor de crédito gerado, o id do lançamento de devolução criado, o tipo como origem ***"O"*** e classificação como crédito ***"C"***.
      * Atualizar o campo ***IDLANCREDITO,*** na tabela ***SBOLSARETROATIVACONTRATO,*** com o id. do lançamento de devolução criado.
      * Caso não seja uma bolsa de crédito, inserir o registro de relacionamento do crédito utilizado na tabela ***SBOLSALAN***.

Verificar a forma de aproveitamento de crédito parametrizada: "**Aplicar devolução no lançamento da primeira parcela em abert*o"***, "***Dividir devolução pela quantidade de parcelas restantes***", "***Devolver em espécie***".

Atualizar o campo ***FORMAUTILIZACAO***, na tabela ***SBOLSARETROATIVACONTRATO,*** com a forma de aproveitamento de crédito definido nos parâmetros acima:

***P*** -Aplicar devolução no lançamento da primeira parcela em aberto

******R****** - Dividir devolução pela quantidade de parcelas restantes

*********E********* - Devolver em espécie

Caso parametrizado para "***Aplicar devolução no lançamento da primeira parcela em aberto***":

* + - * Para as parcelas que já tenham lançamentos gerados e não baixados:
        + Criar um vínculo entre o lançamento a receber da parcela e o lançamento de devolução de crédito passando o valor total líquido do lançamento da parcela.   
          Caso o valor líquido da parcela seja maior que o valor restante de crédito, deverá ser considerado o valor restante de crédito para o vínculo.  
          Deverá ser chamado o serviço do Financeiro ***"Vincular"*** da classe ***FinLanMod*** através da interface ***IFinLanMod***.
        + Criar os registros na tabela ***SBOLSARETROATIVAPARCELA*** com as parcelas que aproveitarão o crédito com o valor de crédito aplicado, o Id do lançamento de devolução vinculado, o tipo como destino ***"D"*** e a classificação como crédito ***"C"***.
        + Caso não seja uma bolsa de crédito, inserir o registro de relacionamento do crédito utilizado na tabela ***SBOLSALAN***.
      * Para as parcelas que não tenham lançamentos gerados, o registro na tabela ***SBOLSARETROATIVAPARCELA*** serão incluídos com as mesmas informações pelo serviço de geração de lançamentos. Serão informados o valor de crédito a ser aplicado, o Id do lançamento de devolução vinculado, o tipo como destino ***"D"*** e a classificação como crédito ***"C"***.

Caso parametrizado para "***Dividir devolução pela quantidade de parcelas restantes***"

* + - * Para as parcelas que já tenham lançamentos gerados:
        + Dividir o total de crédito restante, do contrato, pelo total de parcelas, com lançamentos com status "***Em aberto***", do plano de pagamento para se obter o valor por parcela.
        + Caso o valor líquido do lançamento da parcela seja menor que o valor do crédito calculado, aplica-se essa diferença em uma próxima parcela com saldo disponível ou a mesma ficará como crédito pendente no contrato.
        + Criar um vínculo entre o lançamento a receber da parcela e o lançamento de devolução de crédito passando o valor da divisão do crédito pelo número de parcelas.Deverá ser chamado o serviço do Financeiro ***"Vincular"*** da classe ***FinLanMod*** através da interface ***IFinLanMod***.
        + Criar um registro na tabela ***SBOLSARETROATIVAPARCELA*** com as parcelas que aproveitarão o crédito, o valor de crédito aplicado, o Id do lançamento de devolução vinculado, o tipo como destino ***"D"*** e a classificação como crédito ***"C"***.

* + - * Para as parcelas que não tenham lançamentos gerados:
        + Para as parcelas que não tenham lançamentos gerados, o registro na tabela ***SBOLSARETROATIVAPARCELA*** serão incluídos com as mesmas informações pelo serviço de geração de lançamentos. Serão informados o valor de crédito a ser aplicado, o Id do lançamento de devolução vinculado, o tipo como destino ***"D"*** e a classificação como crédito ***"C"***.
        + Deverá ser dividido o total de crédito pelo total de parcelas do plano de pagamento para se obter o valor por parcela.
      * Preenchimento da conta caixa no lançamento de devolução, gerado pela bolsa retroativa:

        Primeiramente o sistema verifica a conta caixa parametrizada nos parâmetros de inclusão de bolsa retroativa (Fin - Bolsa retroativa 2/3).  
        Se o parâmetro estiver preenchido, o lançamento a pagar que será incluído terá esta informação de conta caixa.  
        Se o parâmetro estiver nulo (sem valor), o lançamento a pagar irá considerar a conta caixa parametrizada para a geração de lançamentos:  
        (Educacional -> Financeiro Geral 2/4 -> Conta Caixa)

Caso parametrizado para "***Devolver em espécie***"

* + - * + O valor de crédito restante na tabela ***SBOLSARETROATIVACONTRATO*** será zerado, pois o valor não será vinculado devido ao pagamento em espécie.
        + Para a realização da baixa, o usuário deverá fazê-lo manualmente no financeiro, após o pagamento do valor.

Caso parametrizado para utilizar conta corrente:

* + - Incluir o valor do crédito na Conta Corrente do aluno.
    - Inserir na tabela ***SBOLSARETROATIVAPARCELA*** o registro do crédito lançado na conta corrente do aluno, vinculado ao contrato. Incluir o valor de crédito gerado, o id de conta corrente e a classificação como crédito ***"C"***.
    - Atualizar o campo ***FORMAUTILIZACAO***, na tabela ***SBOLSARETROATIVACONTRATO,*** com a forma de aproveitamento de crédito definido nos parâmetros acima:

***4***- Usar conta corrente

* + - Caso não seja uma bolsa de crédito, inserir o registro de relacionamento do crédito utilizado na tabela ***SBOLSALAN***.

VALOR DE MULTA A SER CREDITADO PARA O ALUNO

A inclusão uma bolsa retroativa levará em consideração os valores de multas já calculados no lançamento e, caso tenha cobrado um valor superior de multa no lançamento da parcela que está recebendo a bolsa, esse valor de multa cobrado indevidamente será acrescentado ao valor original do crédito do aluno.

Quando inserimos uma bolsa retroativa, os valores de multas serão considerados se as condições abaixo forem satisfeitas:

- Parâmetro Cobrar Multa marcado  
- Parâmetro "Desconsiderar valores de bolsas" desmarcado  
- O tipo da parcela que originou o lançamento é diferente de parcela extra ou a parcela de origem do lançamento é uma parcela extra e o parâmetro de aplicar multa aos serviços eventuais e extras estiver marcado  
- A bolsa a ser incluída é uma bolsa incondicional

O cálculo da multa será realizado conforme abaixo.

Considere as variáveis:

* valorOriginal: Valor original do lançamento
* valorMultaLan: Valor de multa do lançamento
* valorBolsa: Valor da bolsa que está sendo inserida
* valorDescontoConsiderado: Valor do desconto considerado na multa. Será maior do que zero, se houver desconto no lançamento e o parâmetro "Desconsiderar valores de desconto" para multa estiver desmarcado.
* valorBolsasIncondicionaisLancamento: Valor total das bolsas incondicionais do lançamento.
* fatorMulta: fator calculado a ser aplicado de multa. Será igual ao valor parametrizado para multa se o usuário não tiver alterado o valor do parâmetro após incluir o lançamento que está recebendo a bolsa.  
  fatorMulta = valorMultaLan / (valorOriginal - valorDescontoConsiderado - valorBolsasIncondicionaisLancamento);

Após calcularmos o fator de multa, será calculado o valor de multa a ser devolvido (acrescentado no valor original do crédito) da seguinte forma:

valorMultaASerDevolvido = (valorOriginal - valorDescontoConsiderado - valorBolsa) \* fatorMulta + (valorDescontoConsiderado \* fatorMulta) + (valorBolsasIncondicionaisLancamento \* fatorMulta);

#### Exclusão de bolsa retroativa

***Não poderão ser excluídas bolsas em contratos cancelados nem bolsas retroativas com repasse cadastrado. Independente de o repasse já ter sido executado, o simples fato de ter sido cadastrado já impossibilitará a exclusão através do processo de exclusão de bolsa retroativa.***

******Não poderão ser excluídas bolsas em contratos originados por acordo (Tipo = "Acordo")******

A exclusão de uma bolsa se refere a inativação da mesma como bolsa do contrato, quando for integral. A mesma não será excluída.

Quando houver uma exclusão de bolsa parcial, a mesma, não será inativada, pois terão outras parcelas vinculadas a bolsa.

Uma vez que a bolsa foi inativada pelo processo de exclusão de bolsa, não deverá ser permitido a alteração manual da flag para ativado. **O campo "Bolsa ativa" deve ficar desabilitado**.

Os lançamentos gerados por bolsa de crédito, que estiverem com status igual a ***"Em aberto"***, deverão ser cancelados. Se os lançamentos gerados por bolsa de crédito estiverem ***"Baixados" ou "Baixados Parcialmente",***não será permitido a exclusão .

A exclusão de uma bolsa retroativa irá afetar, apenas, as parcelas que tenham lançamentos igual a ***"Em aberto"*** ou que, ainda, não foram gerados.

As parcelas com lançamentos já baixados ou baixados parcialmente não devem ser alteradas. Os valores aplicados como crédito indevidamente, serão cobrados em novas parcelas ou gerados como débitos em Conta Corrente.

Ao se realizar a exclusão de uma bolsa retroativa, o sistema deverá:

* + Verificar se o sistema foi parametrizado para "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***" ou  "***Usar conta corrente***".  
      
    - Caso parametrizado para "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***":
      * Verificar a forma como será cobrado o valor aplicado indevidamente: "***Gerar uma única parcela para pagamento***" ou "***Dividir pela quantidade de parcelas restantes***".
      * Caso parametrizado para "***Gerar uma única parcela para pagamento***":

Caso seja realizada a exclusão de uma bolsa inclusa pelo processo de inclusão de ***bolsa retroativa***:

Caso seja uma exclusão ***integral***:

* A bolsa do aluno será inativada.
* Se as parcelas com as bolsas excluídas já tiverem lançamentos gerados:
  + Gerar uma parcela adicional/extra no contrato do aluno com o valor total a receber + valor de multa a ser cobrado e esse terá o campo "**ORIGEM**" marcado como Bolsa Retroativa***.***
    - O lançamento da parcela deverá ser gerado se o parâmetro "***Gerar lançamento***" estiver marcado.
    - Se gerado o lançamento, atualizar o campo ***IDLAN*** da tabela ***SBOLSARETROATIVAPARCELA*** com o ID do lançamento criado.

Caso seja uma exclusão ***parcial***:

* + Se a exclusão parcial da bolsa ocorrer no início do período de validade da mesma, será mantida a validade final e será alterada somente a validade inicial da bolsa do contrato do aluno ***SBOLSAALUNO***.
  + Se a exclusão parcial da bolsa ocorrer no final do período de validade da mesma, será mantida a validade inicial e será alterada somente a validade final da bolsa do contrato do aluno ***SBOLSAALUNO***.
  + Caso a exclusão aconteça no meio da validade da bolsa:
    - Será criada uma nova bolsa para o aluno com validade da parcela posterior à última parcela considerada na exclusão até a parcela ou data final.
    - Atualizar o campo ***IDBOLSAALUNOORIGEM*** da bolsa criada com o ***IDBOLSAALUNO*** da bolsa que teve sua validade alterada.
  + Se as parcelas com as bolsas excluídas já tiverem lançamentos gerados:  
    - Gerar uma parcela adicional/extra no contrato do aluno com o valor total a receber + valor de multa a ser cobrado e esse terá o campo "**ORIGEM**" marcado como Bolsa Retroativa***.***
    - O lançamento da parcela deverá ser gerado se o parâmetro "***Gerar lançamento***" estiver marcado.
    - Se gerado o lançamento, atualizar o campo ***IDLAN*** da tabela ***SBOLSARETROATIVAPARCELA*** com o ID do lançamento criado.

* + - * + Se as parcelas com as bolsas excluídas não tiveram lançamentos gerados:
          - Não teremos nenhum registro incluso na tabela ***SBOLSARETROATIVAPARCELA.***

Caso seja realizada a exclusão de uma bolsa inclusa pelo processo de inclusão de ***bolsa comum***:

* + - * + - * Deverá ser incluso um registro na ***SBOLSARETROATIVACONTRATO*** com o valor de débito da bolsa que está sendo excluída e sua classificação definida como ***DÉBITO***.
            * O valor restante irá ser igual a zero (0).
            * Gerar uma parcela adicional/extra no contrato do aluno com o valor total a receber + valor de multa a ser cobrado e esse terá o campo "**ORIGEM**" marcado como Bolsa Retroativa***.***
            * Inserir na tabela ***SBOLSARETROATIVAPARCELA*** o registro da parcela criada com o valor da parcela gerada e a classificação como débito ***"D"***
            * O lançamento da parcela deverá ser gerado se o parâmetro "***Gerar lançamento***" estiver marcado.
            * Se gerado o lançamento, atualizar o campo ***IDLAN*** da tabela ***SBOLSARETROATIVAPARCELA*** com o ID do lançamento de débito criado.

* + - * + - Caso parametrizado para "***Dividir pela quantidade de parcelas restantes***":

***Seguirá a mesma regra definida para a geração de parcela única***, com as diferenças abaixo:

* + - * + - * Obter o total de parcelas que não possuam lançamentos gerados.
            * Gerar o mesmo número da respectiva parcela e a cota será calculada com o próximo valor de cota disponível.
            * Os valores das parcelas serão o resultado do (total a receber + valor de multa a ser cobrado) dividido pelo número de parcelas obtidas.
            * Caso todas as parcelas possuam lançamentos gerados ou o contrato não possua parcelas, será incluída uma parcela única com o valor de bolsa excluído.

* + - * + - Caso parametrizado para utilizar ***conta corrente***:
            * Incluir o valor do débito na Conta Corrente do aluno.
            * Inserir na tabela ***SBOLSARETROATIVAPARCELA*** um registro com o id de conta corrente e a classificação como crédito ***"D"***.

VALOR DE MULTA A SER COBRADO

(**Cálculo do valor de multa quando estivermos trabalhando com devolução**)

Caso o lançamento que está perdendo a bolsa tenha uma multa e o parâmetro para "Desconsiderar bolsas" não esteja marcado, o valor de multa "influenciado" pela bolsa que estava no lançamento será cobrado e o valor será adicionado ao valor da parcela criada pela exclusão da bolsa.

O cálculo do valor de multa a ser cobrado é feito da seguinte forma:

Considere as variáveis abaixo:

- totalValorMulta: Soma dos valores de multas dos lançamentos envolvidos no processo  
- totalValorOriginal: Soma dos valores originais dos lançamentos envolvidos no processo  
- totalValorBolsaIncondicional: Soma dos valores de bolsas INCONDICIONAIS dos lançamentos envolvidos no processo. O valor será zerado se o parâmetro "Desconsiderar valores de bolsas" para multa estiver marcado.  
- totalValorDesconto: Soma dos valores de descontos dos lançamentos envolvidos no processo. O valor será zerado se o parâmetro "Desconsiderar valores de descontos" para multa estiver marcado.  
- fatorMulta: Valor parametrizado para multa nos parâmetros do Educacional (10% = 0,1).  
  Pelo fato de que o usuário pode ter alterado o parâmetro de sistema, o fator de multa será calculado da seguinte forma:   
  fatorMulta = totalValorMulta / (totalValorOriginal - totalValorBolsaIncondicional - totalValorDesconto)  
- valorMultaTotalBase: Valor de multa total referente aos valores originais dos lançamentos sem os valores de multa aplicados aos descontos.

Ao calcularmos os valores de todas as variáveis acima, temos que calcular o valor de multa a ser considerado para somar no valor da parcela

- (VALOR DE MULTA A SER COBRADO) = valorMultaTotalBase - totalValorMulta

(**Cálculo do valor de multa quando estivermos trabalhando com conta corrente**)

Caso o lançamento que está perdendo a bolsa tenha uma multa e o parâmetro para "Desconsiderar bolsas" não esteja marcado, o valor de multa "influenciado" pela bolsa que estava no lançamento será cobrado e esse valor será adicionado ao valor da conta corrente criada pela exclusão da bolsa.

O cálculo do valor de multa a ser cobrado é feito da seguinte forma:

Considere as variáveis abaixo:

- totalValorMulta: Valor de multa do lançamento que está sendo processado  
- totalValorOriginal: Valor original do lançamento  
- totalValorBolsaIncondicional: Soma dos valores de bolsas INCONDICIONAIS do lançamento. O valor será zerado se o parâmetro "Desconsiderar valores de bolsas" para multa estiver marcado.  
- totalValorDesconto: Valor de desconto do lançamento. O valor será zerado se o parâmetro "Desconsiderar valores de descontos" para multa estiver marcado.  
- fatorMulta: Valor parametrizado para multa nos parâmetros do Educacional (10% = 0,1). Pelo fato de que o usuário pode ter alterado o parâmetro de sistema, o fator de multa será calculado da seguinte forma:   
  fatorMulta = totalValorMulta / (totalValorOriginal - totalValorBolsaIncondicional - totalValorDesconto)  
- valorMultaTotalBase: Valor de multa total referente ao valor original do lançamento sem o valor de multa aplicado ao desconto.

Ao calcularmos os valores de todas as variáveis acima, temos que calcular o valor de multa a ser considerado para somar no valor da parcela.

- (VALOR DE MULTA A SER COBRADO) = valorMultaTotalBase - totalValorMulta

Exclusão de bolsas para mais de um responsável financeiro

Quando excluirmos retroativamente bolsas para mais de um responsável financeiro (parcelas com mais de um responsável que possua a bolsa ou parcelas diferentes com responsáveis distintos), as parcelas serão incluídas conforme parametrização citada acima (Parcela única ou Dividir pelas parcelas restantes) com os responsáveis financeiros considerados na exclusão e com o percentual de responsabilidade de cada responsável igual ao valor da respectiva bolsa excluída em relação ao valor total excluído.

**Exemplo**:  Exclusão de bolsa no valor de R$ 200,00 incidindo sob cada parcela de R$ 1000,00 para as parcelas P1 com responsável R1, P2 com responsável R1 e P3 com responsável R2 com o sistema parametrizado para geração de parcela única. Será gerada uma parcela única no valor de R$ 600,00 com dois responsáveis financeiros cujos percentuais de responsabilidade serão: 66,67% para R1 e 33,33% para R2

### Processo de geração de lançamentos Contratos/Parcelas

Caso o campo "ORIGEM" da parcela tenha o valor (BR - Bolsa Retroativa), o lançamento a ser criado será referente a um débito devido a uma exclusão de bolsa e esse lançamento será criado com os valores defaults dos parâmetros de geração de lançamentos para exclusão de bolsa. Os outros parâmetros de lançamento serão buscados dos parâmetros de integração com o financeiro ou informados no processo de geração de lançamentos em lote. A tabela **SBOLSARETROATIVAPARCELA** será atualizada com o campo *IDLAN* do lançamento gerado.

Se o sistema foi parametrizado para "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***"

* Verifica se o contrato possui créditos gerados por bolsa retroativa na tabela ***SBOLSARETROATIVACONTRATO,*** através do campo ***VALORRESTANTE,*** e se a parcela possui o mesmo serviço da bolsa. Poderá haver um ou mais créditos para um mesmo contrato.
* Caso a forma de aproveitamento do crédito esteja com o valor (**E** - Devolver em espécie), nenhum vínculo será feito entre o lançamento gerado e o lançamento de devolução.
* Caso a forma de aproveitamento do crédito seja (***P*** - Aplicar devolução nas próximas parcelas ou ******R****** - Dividir devolução pela quantidade de parcelas restantes), o sistema realizará as seguintes tarefas:
  + Calcula-se o valor correspondente ao crédito a ser aplicado de acordo com a forma de aproveitamento dentro do mesmo contrato.
  + Caso os parâmetros "******Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***"** e****"Usar devoluções pendentes após término de contrato nos próximos contratos"***estejam marcados, deverá ser verificado se há a existência de algum **contrato encerrado** (todas os lançamentos das parcelas baixados), **para o mesmo aluno**, no qual o crédito não foi totalmente aproveitado para um mesmo serviço da parcela. O maior valor possível do crédito encontrado de outros contratos será aproveitado pelo lançamento que estiver sendo gerado.
  + O aproveitamento citado acima será feito através de vínculos entre o lançamento a receber da parcela e o(s) lançamento(s) de devolução de crédito e o valor vinculado será o valor aproveitado de cada crédito. Deverá ser chamado o serviço do Financeiro ***"Vincular"*** da classe ***FinLanMod*** através da interface ***IFinLanMod***.
  + Criar um registro na tabela ***SBOLSARETROATIVAPARCELA*** com o valor de crédito aplicado, o Id do lançamento de devolução vinculado, o tipo como destino ***"D"*** e a classificação como crédito ***"C".***
  + Atualiza o saldo restante da tabela ***SBOLSARETROATIVACONTRATO*** de acordo com o valor de crédito aplicado
* Se houver o aproveitamento de crédito de outro contrato, deverá ser criado um registro na tabela ***SBOLSARETROATIVAPARCELA*** para a parcela em questão com o vínculo do ***IDLAN*** de crédito do contrato aproveitado e com o tipo definido como destino ***"D"*** e a classificação como crédito ***"C"***. Nesse caso, será aproveitado o maior valor possível do crédito na parcela.

Se o sistema foi parametrizado para "***Usar conta corrente***":

Ao aproveitar um registro de **crédito** na conta corrente, o sistema verificará se esse registro é referente a uma bolsa retroativa (Campo ***ORIGEM*** da ***SCONTACORRENTE*** = "**BR**").

Caso possua o registro correspondente na tabela ***SBOLSARETROATIVACONTRATO***:

* + Atualiza o saldo utilizado da tabela ***SBOLSARETROATIVACONTRATO*** com o valor de crédito utilizado, através do campo ***VALORRESTANTE.***
  + Criar um registro na tabela ***SBOLSARETROATIVAPARCELA*** com o valor de crédito utilizado, o Id Conta Corrente vinculado, IDLAN do lançamento gerado, tipo como destino ***"D"*** e a classificação como crédito ***"C".***

Ao aproveitar um registro de **débito** na conta corrente, o sistema verificará se esse registro é referente a uma bolsa retroativa (Campo ***ORIGEM*** da ***SCONTACORRENTE*** = "**BR**").

Caso possua o registro correspondente na tabela ***SBOLSARETROATIVACONTRATO***:

* + Atualiza o saldo restante tabela ***SBOLSARETROATIVACONTRATO*** de acordo com o valor de débito utilizado, através do campo ***VALORRESTANTE.***
  + Criar um registro na tabela ***SBOLSARETROATIVAPARCELA*** com o valor do débito utilizado, o Id Conta Corrente vinculado, IDLAN do lançamento gerado, tipo como destino ***"D"*** e a classificação como débito ***"D"***

Não serão considerados os valores defaults de fórmula de juros, multa e desconto na inclusão da devolução.

Valores de multa não serão calculados para lançamentos gerados a partir de parcelas originadas por uma exclusão de bolsa retroativa.

### Simulação de valores na visão de parcelas do contrato

A simulação deverá levar em consideração o parâmetro de forma de aproveitamento do crédito (***P*** - Aplicar devolução no lançamento da primeira parcela em aberto ou ******R****** - Dividir devolução pela quantidade de parcelas restantes) para saber o valor da devolução a ser utilizado no cálculo do valor líquido da parcela se esta não possuir lançamento gerado. Se a parcela possuir algum lançamento gerado, a simulação somente exibirá um valor de crédito retroativo caso o lançamento gerado por essa parcela tenha aproveitado algum valor.

Caso a forma de aproveitamento do crédito esteja com o valor (**E** - Devolver em espécie) ou a forma de utilização do crédito estiver definida como "Conta Corrente", o valor do crédito será desconsiderado.

A coluna ***"Valor Crédito Retroativo"*** da Grid, somente, será exibida se a forma de utilização do crédito for Criar Devolução (***D***).

### Processo "Desfazer inclusão de bolsa retroativa"

Se o sistema foi parametrizado para "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***

Esse processo só poderá ser executado se as parcelas que tiveram lançamentos vinculados a créditos estiverem com os lançamentos "Em aberto" ou "Cancelados", ou a bolsa não estiver inativa.

Será responsável por excluir o vínculo da bolsa com o contrato, cancelar e excluir os vínculos de crédito, cancelar e excluir os lançamentos a pagar de devolução gerados,  cancelar e excluir os lançamentos a receber se estivermos desfazendo a inclusão de bolsa de crédito.

Serão excluídos também os registros inclusos das tabelas: ***SBOLSARETROATIVACONTRATO, SBOLSARETROATIVAPARCELA*** e ***SBOLSALAN.***

Se o sistema foi parametrizado para "***Usar conta corrente***"

Esse processo só poderá ser executado se os créditos em conta corrente gerados pela inclusão da bolsa não tiverem sido utilizados em outro lançamento.

Será responsável por excluir os respectivos registros de conta corrente gerados na inclusão bem como registros em ***SBOLSARETROATIVACONTRATO, SBOLSARETROATIVAPARCELA*** e ***SBOLSALAN.***

O menu de acesso ao processo deverá ser incluso no caminho:

Caminho:***Educacional | Educacional | Financeiro/Contábil | Assistentes | Desfazer inclusão de bolsa retroativa***

### Processo de vínculos de lançamentos

A remoção de vínculo originado de créditos do processo de inclusão/exclusão de bolsa retroativa excluirá o crédito para o lançamento considerado (***SBOLSARETROATIVAPARCELA***) e o valor restante para o crédito de bolsa retroativa do contrato será atualizado (***SBOLSARETROATIVACONTRATO***)

O relacionamento entre o lançamento e a parcela é realizado através das tabelas: ***FLAN***, ***SLAN,*** ***SPARCELA***e***SBOLSARETROATIVAPARCELA***.

Na tabela ***SBOLSARETROATIVAPARCELA***, o campo ***IDLAN*** contêm o código do lançamento de crédito que foi associado.

### Processo de exclusão/cancelamento de bolsas

Não será permitido a exclusão/cancelamento de bolsas retroativas através do processo **"Exclui/Cancelar bolsas"**na visão de contratos, bolsas do contrato e no assistente financeiro.

O processo deverá validar se a bolsa a ser excluída é retroativa e não deverá permitir a execução do mesmo.

Deverá ser exibida uma mensagem informando que bolsas retroativas só podem ser excluídas através do processo de Inclusão/Exclusão de bolsas retroativas.

Na tabela  ***SBOLSAALUNO*** será incluso o campo  ***BOLSARETROATIVA*** com o valor ***"S"*** na inclusão de bolsas retroativas.

Não poderemos excluir/cancelar também uma bolsa com ordem anterior a uma bolsa retroativa concedida cuja aplicação seja “**Em cascata**”.

### Cadastro de lançamentos

A tela de lançamentos, no financeiro, terá as mesmas restrições de edição para origens do Educacional e, também, campos de valores não poderão ser alterados quando for um lançamento de devolução com o campo ***CODAPLICACAO*** igual a ***"S"***.

### Cadastro de bolsas do contrato

Os campos, no cadastro de bolsas do contrato, deverão ficar desabilitados para edição quando a bolsa inclusa for retroativa.

Deverá ser bloqueado a exclusão de uma bolsa quando ela for classificada como retroativa.

Será criado uma nova coluna na visão de bolsas para informar que se trata de uma bolsa retroativa. A coluna referente deverá conter um ícone diferenciando para bolsas retroativas.

Na tela de edição do cadastro de bolsa do contrato deverá ser incluso um novo campo informando que se trata de uma bolsa retroativa.

A bolsa retroativa deverá ser identificada pelo campo  ***BOLSARETROATIVA*** na tabela  ***SBOLSAALUNO*** através do valor ***"S".***

A coluna que contêm a informação de bolsa ***"ATIVA"*** deverá ser exibida como um ícone diferenciando da situação ***"INATIVA"***. (Campo ***ATIVA*** na tabela ***SBOLSAALUNO)***

### Cadastro de parcelas do contrato

As parcelas do contrato geradas pelo processo de bolsa retroativa não poderão ser editadas ou excluídas manualmente.

Essas parcelas são marcadas com o valor ***"BR"*** no campo ***ORIGEM*** da tabela ***SPARCELA.***

### Geração de responsáveis financeiros no cadastro de aluno

Os responsáveis financeiros dos alunos serão cadastrados com a classificação ***AMBOS*** e não mais apenas como clientes, exceto no caso de ambientes com integração com o Protheus.

Nos casos onde houver integração com o Protheus, deverá ser mantida a regra para criação responsável apenas como ***CLIENTE***.

### Cadastro de serviços

Criado o campo "***Desconsiderar crédito de Bolsa Retroativa***" que, ao ser marcado, indicará que o serviço não aproveitará um crédito de bolsa retroativa na geração de lançamentos ou mesmo na inclusão de bolsa para parcelas com lançamentos em aberto. Nesse último caso citado da inclusão, o crédito será gerado mas não será vinculado automaticamente se o serviço estiver parametrizado para desconsiderar crédito.  
Esse campo ficará visível somente se o parâmetro "Forma de devolução do valor de crédito" estiver setado para criar devolução de crédito, ou seja, se o cliente decidir por utilizar conta corrente, o mesmo não estará disponível para o usuário.

### Anexos

### Cadastro de contrato

**Rastreabilidade de Bolsa Retroativa:**

* + - Serão exibidos todos os registros de Crédito/Débito lançados pela inclusão de bolsas para o contrato.
    - Os registros conterão todas as informações lançadas para o contrato contida na tabela ***"****SBOLSARETROATIVAPARCELA"**.*

***Rastreabilidade de aproveitamento de créditos do contrato:***

* + - Serão exibidos todos os registros de Crédito restantes que foram aproveitados por outro contrato.
    - Esse recurso será disponibilizado com a parametrização para aproveitar o crédito restante de contrato encerrados.

***Valores de débito/créditos gerados:*** 

* + - Serão exibidos, dentro da edição do formulário do contrato, os registros referentes aos valores de créditos/débitos gerados e os valores restantes, que não foram aproveitados.

### Cadastro de parcelas

**Rastreabilidade de Bolsa Retroativa:**

* + - Serão exibidos todos os registros de Crédito/Débito lançados pela inclusão de bolsas para o contrato da parcela selecionada
    - Os registros conterão todas as informações lançadas para a parcela do contrato contida na tabela ***"****SBOLSARETROATIVAPARCELA"***

### Cadastro de bolsa do aluno

**Rastreabilidade de Bolsa Retroativa:**

* + - Serão exibidos todos os registros de Crédito/Débito lançados pela inclusão da bolsa selecionada para o contrato do aluno.
    - Os registros conterão todas as informações lançadas para o contrato contida na tabela ***"****SBOLSARETROATIVAPARCELA"**.*

***Valores de débito/créditos gerados:*** 

* + - Serão exibidos, dentro da edição do formulário de bolsa do aluno, os valores de créditos/débitos gerados e os valores restantes, que não foram aproveitados.

A inclusão manual ou via processo "*Incluir Bolsas*" continuará permitindo o cadastro da bolsa no contrato do aluno mesmo para parcelas com lançamentos gerados. Essa inclusão não gerará créditos retroativos no contrato do aluno e, para que a mesma seja considerada, a parcela deverá ser gerada ou regerada.

### Visão de lançamentos

Foi alterada a visão de lançamentos a fim de possibilitar o filtro de lançamentos a pagar de devolução criados na inclusão de bolsa retroativa a partir de um filtro por RA.

### Baixa de lançamentos

A baixa de lançamentos de devolução de origem do Educacional (***"S"***) e que estiverem sendo utilizados como crédito para bolsa retroativa, deverá atualizar o respectivo saldo na tabela ***SBOLSARETROATIVACONTRATO***.

### Aproveitamento de valores em conta corrente

O processo de aproveitamento de valores em conta corrente executado por débito/crédito (visão de conta corrente) ou em lote criará um registro de ***SBOLSARETROATIVAPARCELA*** com o campo ***"****IDPARCELA = NULL", "IDCONTACORRENTE = ID"*** da conta corrente que está sendo incluído, IDLAN do lançamento que está sendo gerado (a receber ou a pagar). O saldo restante do registro existente em ***SBOLSARETROATIVACONTRATO*** não será alterado.

### Exclusão de parcela criada por exclusão de bolsa retroativa

Conforme descrito no funcionamento da exclusão de uma bolsa retroativa, o sistema cria uma ou mais parcelas no contrato do aluno com a finalidade de se cobrar bolsas excluídas de lançamentos já gerados (baixados ou não) que fizeram com que o valor a ser pago pelo aluno fosse menor do que deveria.

A exclusão dessas parcelas geradas pela exclusão da bolsa retroativa não são tratadas como exclusão de parcelas comuns tendo em vista a necessidade de se desfazer todo o processo de exclusão de bolsa retroativa que deu origem à(s) mesma(s).

O lançamento financeiro de bolsa de crédito que foi cancelado pelo processo de exclusão de bolsa, devem ser geradas novamente para que o lançamento de bolsa seja recriado.

### Permissão para exclusão de parcelas geradas por exclusão de bolsa retroativa

Foi criada um parâmetro educacional no perfil do usuário que permite conceder permissão de exclusão para esse tipo de parcela citado. Para se ter acesso à essa parametrização, acessar o seguinte caminho:

(Perfil do usuário → Anexo Parâmetros Educacionais → Financeiro → Bolsa Retroativa → **Permite excluir parcelas geradas por bolsa retroativa**

Após clicar na opção de exclusão da parcela gerada por bolsa retroativa, o sistema irá exibir a seguinte tela para o usuário:

O mesmo poderá clicar em "Sim" caso queira prosseguir com o processo e "Não" para a imediata interrupção da exclusão.

Caso o parâmetro educacional do perfil esteja **DESMARCADO**, o sistema exibirá a seguinte mensagem para o usuário:

Atenção

1) Não será permitida a exclusão de uma parcela com lançamento gerado. Esse comportamento é o mesmo comportamento da exclusão de uma parcela comum. Para que prossigamos com a exclusão da parcela, o(s) respectivo(s) lançamento(s) deverão ser excluídos.

2) Conforme mensagem exibida para o usuário, se o processo de exclusão de bolsa retroativa originou mais de uma parcela (isto acontece com o usuário marcando o parâmetro de exclusão de bolsa "Dividir pela quantidade de parcelas restantes", mesmo que as outras parcelas não forem marcadas, o sistema excluirá as mesmas pois foram geradas no mesmo processo da parcela original selecionada.

3) Caso o contrato esteja cancelado e o serviço para desfazer a exclusão de bolsa retroativa seja chamado, o sistema exibirá a mensagem de validação:

"**Excluindo: Coligada = 1; Identificador da parcela = 120590**

**Não é permitida a exclusão de parcela de bolsa retroativa em contrato cancelado.**

**- Código da coligada: 1**

**- RA: 20180304**

**- Código do contrato: 10255**

**- Id do período letivo: 104**"

### Exclusão de parcela gerada por bolsa retroativa (Processo de desfazer a exclusão da bolsa retroativa)

A exclusão de parcela gerada por bolsa retroativa voltará com o intervalo original das bolsas que foram excluídas retroativamente

### Exclusão de parcela de bolsa retroativa gerada por uma exclusão de bolsa retroativa no início do período da bolsa original

Ao excluir uma bolsa retroativa no início do intervalo da bolsa original, o período da bolsa é reduzido desconsiderando algumas parcelas iniciais.

Exemplo:

* Parcelas P1 a P6: 1000,00
* Bolsa FIES - 20%
* Intervalo original (Parcelas: P1 a P6)
* Exclusão da bolsa nas parcelas (P1 e P2)
* Após EXCLUSÃO RETROATIVA:  
  + Bolsa FIES com validade nas parcelas **P3** a **P6**
  + Criação da parcela P7 no contrato do aluno com valor R$ 400,00

Após selecionar a parcela P7 no contrato do aluno e processar a exclusão:

=> RESULTADO DA EXCLUSÃO:

* Bolsa FIES com validade nas parcelas **P1** a **P6**
* Exclusão da parcela P7 no contrato do aluno com valor R$ 400,00

### Exclusão de parcela de bolsa retroativa gerada por uma exclusão de bolsa retroativa no final do período da bolsa original

Ao excluir uma bolsa retroativa no final do intervalo da bolsa original, o período da bolsa é reduzido desconsiderando algumas parcelas finais.

Exemplo:

* + - Parcelas P1 a P6: 1000,00
    - Bolsa FIES - 20%
    - Intervalo original (Parcelas: P1 a P6)
    - Exclusão da bolsa nas parcelas (P5 e P6)
    - Após EXCLUSÃO RETROATIVA:  
      * Bolsa FIES com validade nas parcelas **P1** a **P4**
      * Criação da parcela P7 no contrato do aluno com valor R$ 400,00

Após selecionar a parcela P7 no contrato do aluno e processar a exclusão:

=> RESULTADO DA EXCLUSÃO:

* Bolsa FIES com validade nas parcelas **P1** a **P6**
* Exclusão da parcela P7 no contrato do aluno com valor R$ 400,00

### Exclusão de parcela de bolsa retroativa gerada por uma exclusão de bolsa retroativa no meio do período da bolsa original

Ao excluir uma bolsa retroativa no meio do intervalo da bolsa original, o período da bolsa é reduzido gerando duas bolsas sendo uma com intervalo final anterior à parcela inicial de exclusão e a outra com intervalo inicial posterior à parcela final de exclusão.

Exemplo:

* + - Parcelas P1 a P6: 1000,00
    - Bolsa FIES - 20%
    - Intervalo original (Parcelas: P1 a P6)
    - Exclusão da bolsa nas parcelas (P3 e P4)
    - Após EXCLUSÃO RETROATIVA:  
      * Bolsa FIES com validade nas parcelas **P1** a **P2**
      * Bolsa FIES com validade nas parcelas **P5** a **P6**
      * Criação da parcela P7 no contrato do aluno com valor R$ 400,00

Após selecionar a parcela P7 no contrato do aluno e processar a exclusão:

=> RESULTADO DA EXCLUSÃO:

* + - * Exclusão da Bolsa FIES com validade nas parcelas **P5** e **P6**
      * Bolsa FIES com validade nas parcelas **P1** a **P6**
      * Exclusão da parcela P7 no contrato do aluno com valor R$ 400,00

## Dicionário de Dados

Inclusão de campos:

| SPARCELA  Parcelas do contrato do aluno | | | |
| --- | --- | --- | --- |
| ORIGEM | VARCHAR(2) | NULL | Origem da parcela  - Bolsa Retroativa - 4 |

| SCONTACORRENTE  Parcelas do contrato do aluno | | | |
| --- | --- | --- | --- |
| ORIGEM | VARCHAR(2) | NULL | Origem da parcela  - Bolsa Retroativa - BR |

| SBOLSAALUNO  Bolsas lançadas para o contrato do aluno | | | |
| --- | --- | --- | --- |
| BOLSARETROATIVA | VARCHAR(1) | NULL | Indica se a bolsa lançada é retroativa |
| IDBOLSAALUNOORIGEM | INT | NULL | Identificador da bolsa de aluno que deu origem a ela |

Inclusão de tabela:

| SBOLSARETROATIVACONTRATO  Créditos/Débitos gerados para um contrato | | | |
| --- | --- | --- | --- |
| CODCOLIGADA | SMALLINT | NOT NULL | Código da coligada |
| RA | VARCHAR(20) | NOT NULL | RA do aluno |
| CODCONTRATO | VARCHAR(20) | NOT NULL | Código do contrato |
| IDPERLET | INT | NOT NULL | Identificador do período letivo |
| IDBOLSAALUNO | INT | NOT NULL | Identificador da bolsa |
| IDCONTACORRENTE | INT | NULL | Identificador de item de conta corrente |
| VALOR | DECIMAL(15,4) | NOT NULL | Valor de crédito por lançamentos baixados integral ou parcialmente |
| VALORRESTANTE | DECIMAL(15,4) | NOT NULL | Valor de crédito utilizado |
| CLASSIFICACAO | VARCHAR(1) | NOT NULL | Crédito/Débito |
| FORMAUTILIZACAO | VARCHAR(1) | NOT NULL | ***Forma de utilização do crédito de devolução***  Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa) = "D"  Usar conta corrente = "C" |
| FORMAAPROVEITAMENTO | VARCHAR(1) | NULL | ***Inclusão de Bolsa:***  Aplicar devolução no lançamento da primeira parcela em aberto = "P"  Dividir devolução pela quantidade de parcelas restantes = "R"  Devolver em espécie = "E"  ***Exclusão de Bolsa:***  Gerar uma única parcela para pagamento = "U"  Dividir pela quantidade de parcelas restantes = "D" |
| Primary Key | CODCOLIGADA, RA, CODCONTRATO, IDPERLET, IDBOLSAALUNO | | |
| Foreign Key | SCONTRATO | CODCOLIGADA,RA,CODCONTRATO,IDPERLET | |
| Foreign Key | SBOLSAALUNO | CODCOLIGADA, IDBOLSAALUNO | |

| SBOLSARETROATIVAPARCELA  Parcelas de contrato geradas pela inclusão/exclusão de bolsa retroativa | | | |
| --- | --- | --- | --- |
| CODCOLIGADA | SMALLINT | NOT NULL | Código da coligada |
| IDBOLSARETPARCELA | INT | NOT NULL | Identificador de registro |
| RA | VARCHAR(20) | NOT NULL | RA do aluno |
| CODCONTRATO | VARCHAR(20) | NOT NULL | Código do contrato |
| IDPERLET | INT | NOT NULL | Identificador do período letivo |
| IDPARCELA | INT | NULL | Identificador da parcela do contrato |
| IDBOLSAALUNO | INT | NOT NULL | Identificador da bolsa |
| IDLAN | INT | NULL | Identificador do lançamento gerado pela parcela |
| IDLANCREDITO | INT | NULL | Identificador do lançamento de devolução |
| IDCONTACORRENTE | INT | NULL | Identificador do item de conta corrente |
| VALOR | DECIMAL(15,4) | NOT NULL | Valor do crédito/débito |
| TIPO | VARCHAR(1) | NOT NULL | Origem/Destino |
| CLASSIFICACAO | VARCHAR(1) | NOT NULL | Crédito/Débito |
| CODCOLCFO | INT | NOT NULL | Código da coligada do Cliente/Fornecedor |
| CODCFO | VARCHAR(25) | NOT NULL | Código do Cliente/Fornecedor |
| IDPERLETORIGEM | INT | NULL | Identificador do período letivo de origem |
| IDBOLSAALUNOORIGEM | INT | NULL | Identificador da bolsa de origem |
| CODCONTRATOORIGEM | VARCHAR(20) | NULL | Código do contrato de origem |
| OPERACAO | VARCHAR(1) | NOT NULL | Operação de originou o crédito/débito |
| Primary key | CODCOLIGADA,IDBOLSARETPARCELA | | |
| Foreign key | SBOLSARETROATIVACONTRATO | CODCOLIGADA,RA,CODCONTRATO,IDPERLET,IDBOLSAALUNO | |
| Foreign key | SPARCELA | CODCOLIGADA,IDPARCELA | |
| Foreign key | FLAN | CODCOLIGADA,IDLAN | |
| Foreign key | FLAN | CODCOLIGADA,IDLANCREDITO | |
| Foreign key | SCONTACORRENTE | CODCOLIGADA,IDCONTACORRENTE | |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
