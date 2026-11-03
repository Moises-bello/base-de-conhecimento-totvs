---
content_hash: 5953957fa298227b25d9a5ca69b9323ccaae25af08e4fdacf874d21d5d7231e6
fetched_at: '2026-06-29T00:08:12.670426+00:00'
page_id: '243645966'
product: rm
source: tdn-rm
title: DT_Novo_Modelo_Bolsa_Retroativa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Novo_Modelo_Bolsa_Retroativa
version: 147
---

Novo Modelo de Bolsa Retroativa

## Características do Requisito..

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Incluir/Excluir Bolsas Retroativas | Inclusão e exclusão de bolsas retroativas | | Desfazer a inclusão de bolsa retroativa | Desfazer uma inclusão de uma bolsa retroativa | | Geração de lançamentos | Geração de lançamentos financeiros | | Aproveitamento de créditos em conta corrente | Aproveita os créditos da conta corrente do aluno | | Vincular lançamentos | Vincula lançamentos de crédito a lançamentos a receber | |
| **Cadastros Iniciais:** | Cadastro de Bolsas, Contrato do Aluno |
| **Parâmetro(s):** | Parâmetros de Bolsa Retroativa no módulo Financeiro de integração do Educacional. |
| **Requisito (ISSUE):** | PCREQ-9516 |
| **País(es):** | Todos |
| **Tabelas Utilizadas:** | SBOLSARETROATIVACONTRATO,SBOLSARETROATIVAPARCELA,SPARCELA,  SBOLSAALUNO,SCONTACORRENTE |

## Descrição

Flexibilizar o processo de Bolsa Retroativa, as contabilizações relacionadas e a origem de itens gerados. Desta forma, o processo de concessão e exclusão de bolsas serão mais transparentes, mantendo inalterados os títulos financeiros já baixados.

## **Permissões do sistema**

Acessar o módulo**Serviços Globais | Segurança | Perfis**, selecionar o sistema "**Educacional**" e em seguida alterar o perfil desejado incluindo ou excluindo as permissões de acesso:

* + **Educacional - [04] Financeiro/Contábil - [04.01] Contratos - **[04.01.01] Contratos - **[04.01.01.18] Rastreabilidade da bolsa retroativa******
  + **Educacional - [04] Financeiro/Contábil - [04.01] Contratos - **[04.01.01] Contratos - **[04.01.01.18] Rastreabilidade de aproveitamento de créditos do contrato******
  + **Educacional - [04] Financeiro/Contábil - [04.05] Assistentes - **[04.05.01] Assistentes - **[04.05.01.04] Incluir/Exclui bolsas retroativas******
  + **Educacional - [04] Financeiro/Contábil - [04.05] Assistentes - **[04.05.01] Assistentes - **[04.05.01.04] Desfazer inclusão de bolsa retroativa******

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

Foi criada uma parametrização de definir se o sistema irá trabalhar com o modelo antigo de bolsa retroativa ou o novo.

A diferença entre o que chamamos de antigo e novo modelo, será não alterar o que já foi gerado. Quaisquer créditos ou débitos gerados pela inclusão ou exclusão de uma bolsa irão gerar créditos para aproveitamento em futuros lançamentos ou lançamentos a receber.

Para que isso funcione corretamente, será necessário a configuração de parâmetros específicos para o novo modelo de inclusão e exclusão de bolsas retroativas:

***Parâmetros para habilitar novo modelo:***

* + - * Parâmetro para utilização do novo modelo de bolsa retroativa: ***15.05 - Integração | 15.05.03 - Financeiro | Fin - Bolsa Retroativa 1/3 | "Usar bolsa retroativa sem alterar parcelas já baixadas"***
      * Definição de como o sistema irá trabalhar o crédito gerado pela bolsa retroativa: ***15.05 - Integração | 15.05.03 - Financeiro | Fin - Bolsa Retroativa 1/3 | "Selecione uma forma de devolução do valor de crédito"***
        + Utilização de lançamentos de devolução de crédito: ***"Criar devolução de crédito (inclusão de bolsa) / lançamento a receber (exclusão de bolsas)"***
        + Utilização de crédito em conta corrente: ***"Utilizar a movimentação em conta corrente"***
      * Parâmetro ***"Utilizar devoluções pendentes após término de contrato nos próximos contratos"***:  Caso o crédito gerado pela inclusão de uma bolsa retroativa não seja completamente aproveitado nos lançamentos gerados para as parcelas do contrato, será possível utilizar nos próximos contratos para o mesmo registro acadêmico.
      * Parâmetro **"Refaz automaticamente conciliação de extrato no processo de inclusão/exclusão de bolsa retroativa"**: Já utilizado no sistema, ele será habilitado, somente, para o modelo antigo de inclusão de bolsa retroativa.

Importante

Uma vez parametrizado para o novo modelo e determinada a forma de trabalho entre devolução de crédito e conta corrente, essas opções não poderão ser mais alteradas, após a primeira movimentação.

***Parâmetros necessários para a inclusão de uma bolsa retroativa:***

* + - Opção para devolução de crédito:
      * Aplicar devolução nas próximas parcelas ***("Utiliza a devolução de crédito nas próximas parcelas com lançamentos a gerar e, também, nas parcelas que geraram o crédito quando possuem lançamento, ainda, em aberto")***
      * Dividir devolução pela quantidade de parcelas restantes ***("Divide o valor da devolução de crédito pela quantidade de parcelas restantes sem lançamentos e aproveita, somente, o resultado dessa divisão, quando seu valor é menor ou igual ao valor líquido do lançamento.")***
      * Devolver em espécie ***("Gera um lançamento de crédito de devolução com o valor total para devolução para o cliente, em espécie, com a baixa manual a ser realizada no financeiro")***
    - Tipo de documento padrão
    - Centro de custo
      * O centro de custo não for parametrizado no parâmetro ***15.05 - Integração | 15.05.03 - Financeiro | Fin - Bolsa Retroativa 2/3 | "Centro de Custo" ,***o sistema irá buscar o centro de custo conforme a parametrização do parâmetro ***15.05 - Integração | 15.05.03 - Financeiro | Fin - Geral 2/4 | "Centro de Custo"***
    - Conta caixa padrão
    - Natureza orçamentária financeira
      * A natureza orçamentária financeira não for parametrizada no parâmetro ***15.05 - Integração | 15.05.03 - Financeiro | Fin - Bolsa Retroativa 2/3 | "Código da Natureza Financeira",***o sistema irá buscar a natureza orçamentária financeira do serviço da parcela que a bolsa retroativa foi incluída. Se a natureza orçamentária financeira presente no serviço da parcela não for do tipo de natureza ambos, o sistema não irá gerar o lançamento de devolução e informará ao usuário.
    - Histórico
    - Departamento
    - Tipo contábil padrão
    - Data de contabilização
    - Evento para inclusão do lançamento
    - Valores Opcionais:
      * Tabelas Opcionais
      * Campos alfa
      * Data opcionais

***Parâmetros necessários para a exclusão de uma bolsa retroativa:***

* + - Opção de cobrança do crédito devolvido:
      * Gerar uma única parcela para pagamento ***("Gera apenas um lançamento de cobrança para pagamento")***
      * Dividir pela quantidade de parcelas restantes ***("Divide o valor a ser pago pela quantidade de parcelas restantes do contrato e cria a mesma quantidade de novas parcelas")***
    - Gerar lançamento de cobrança automaticamente ***("Ao criar as novas parcelas para pagamento o lançamento é gerado automaticamente")***
    - Tipo de parcela
    - Data de vencimento
    - Serviço
    - Data de contabilização
    - Evento para inclusão de lançamento

***Parâmetros por perfil para alteração de comportamento padrão:***

* + - Parâmetro ***"Alterar parâmetros de comportamento padrão na geração de devoluções"***

Parâmetro utilizado para permitir que o usuário possa alterar a opção de devolução de crédito ou cobrança durante a execução do processo de Inclusão/Exclusão de bolsa retroativa.

* + - * ***Serviços Globais | Segurança | Perfis |***Sistema***: Educacional |***Anexos***: Parâmetros educacionais***
        + Aba:******Bolsa Retroativa******
        + Parâmetro:***Alterar parâmetros de comportamento padrão na geração de devoluções***

## Processo de inclusão/exclusão de bolsas retroativas

false

Caminho:***Educacional | Educacional | Financeiro/Contábil | Assistentes | Incluir/Excluir bolsas retroativas***

O processo de inclusão/exclusão de bolsas retroativas irá realizar tratar tanto o modelo antigo quanto o novo modelo.

O modelo tratado pelo processo segue a parametrização realizada nos parâmetros do módulo Educacional.

#### Etapas do processo

##### Primeira etapa:

Etapa para a seleção de contratos e a definição do tipo de operação: Inclusão/Exclusão de bolsas. 

##### Segunda etapa:

O campo de tipo de cobrança será exibido somente para exclusão de bolsas no modelo antigo de bolsa retroativa.  

A alteração do valor de bolsa seguirá a parametrização do cadastro de bolsa, através do campo: ***"Permite alterar valor"***. 

O campo ***"Ordem"*** não será mais exibido, pois as bolsas sempre entrarão na última posição.

 

**Para a inclusão de bolsas**, serão exibidos os campos de valores opcionais: Tabelas opcionais, Datas opcionais e campos Alpha. 

**Para exclusão de bolsas**, serão exibidos os campos de valores opcionais: Tabelas opcionais, Datas opcionais, campos Alpha e otipo de parcela (Adicional/Extra).

 

Caso esteja parametrizado para a geração de uma única parcela: 

* + - * O campo ***"Data de vencimento"*** será exibido quando o sistema estiver parametrizado para que seja informada manualmente
      * O campo ***"Data de competência"*** será exibido quando houver integração contábil

Caso esteja parametrizado para a divisão pela quantidade de parcelas restantes: 

* + - * As datas de vencimento e competência assumirão as mesmas das parcelas restantes.

falseImportante

A parametrização para utilização de conta corrente no novo modelo de bolsa retroativa, não utilizará os campos para geração de lançamentos: Tabelas opcionais, Datas opcionais e campos Alpha.

##### Terceira etapa:

Essa etapa será exibida, somente, se o usuário tiver no perfil a permissão "***Alterar parâmetros de comportamento padrão na geração de devoluções".*** 

Sá permitida a alteração do comportamento padrão definido nos parâmetros do sistema para o comportamento na geração de um devolução de crédito ou de um lançamento a receber para as operações de Inclusão e Exclusão de bolsa: 

Opções para inclusão: 

* + Aplicar devolução nas próximas parcelas
  + Dividir devolução pela quantidade de parcelas restantes
  + Devolver em espécie

Opções para exclusão: 

* + Gerar uma única parcela para pagamento
  + Dividir pela quantidade de parcelas restantes
  + Gerar lançamentos (S/N)

***\*\*****Caso o sistema esteja parametrizado para utilizar conta corrente, essa etapa não será exibida.*** 

##### Quarta etapa:

Essa etapa será exibida, somente, com a utilização do modelo antigo de bolsa retroativa e tem a função de alerta para a operação que está sedo realizada.

Integração com o Protheus

O processo de inclusão de bolsa retroativa não é tratado em integrações com os sistemas Protheus. Nesse caso, os menus relacionados a Bolsa Retroativa não serão disponibilizados.

## Inclusão de Bolsa Retroativa

#### Regras do processo

Não será permitida a inclusão/exclusão de bolsas retroativas a contratos cancelados.

A inclusão de uma bolsa retroativa irá considerar as parcelas que tenham lançamentos com status ***"Em aberto"*** e/ou ***"Baixados"***para a geração de uma devolução de crédito.

As parcelas com lançamentos já baixados ou baixados parcialmente não serão alteradas. Para esses casos, serão calculados os valores a serem devolvidos e um lançamento de devolução de crédito será criado.

As parcelas com lançamentos ***"Em aberto"*** serão considerados para a geração da devolução de crédito e, também, terão um crédito vinculado, de acordo com a parametrização realizada para aproveitamento de seu crédito no processo ou nos parâmetros do sistema.

***As bolsas incluídas como retroativas*** serão marcadas e terão um ícone diferenciado para classificá-las. 

Parametrização para a criação de uma devolução de crédito:

Será criado um lançamento a pagar, com o tipo de documento de devolução, com o valor total de crédito por bolsa.

Caso parametrizado para "***Aplicar devolução nas próximas parcelas***":

Parte do crédito será utilizado nos lançamentos das parcelas que geraram o crédito e tenham status ***"Em aberto"***. O crédito será utilizado por meio de vínculo de crédito utilizando o lançamento de devolução de crédito criado e será realizado pelo próprio processo de inclusão de bolsa.

O valor de crédito restante será vinculado na geração de lançamento das parcelas. Sempre será aproveitado o valor máximo do lançamento.

Caso o valor líquido da parcela seja maior que o valor de crédito a ser vinculado, será considerado o valor restante do crédito para o vínculo.

Caso tenhamos o caso contrário, será considerado o valor líquido do lançamento, quando houver um crédito maior que o valor líquido.

Caso parametrizado para "***Dividir devolução pela quantidade de parcelas restantes***"

O valor de crédito a ser aproveitado por lançamento será obtido pela divisão do total de parcelas do contrato que tenham lançamentos com status "***Em aberto***" ou que, ainda, não tenham lançamentos gerados.

Para os lançamentos com status ***"Em aberto",***o valor calculado será vinculado utilizando o lançamento de devolução de crédito e será realizado pelo próprio processo de inclusão de bolsa.

O valor de crédito restante será vinculado na geração de lançamento das parcelas. O valor do crédito será obtido da divisão pelo número de parcelas que, ainda, não tiveram seus lançamentos gerados.

Caso o valor líquido da parcela seja maior que o valor de crédito a ser vinculado, será considerado o valor restante do crédito para o vínculo.

Caso tenhamos o caso contrário, será considerado o valor líquido do lançamento, quando houver um crédito maior que o valor líquido.

Preenchimento da conta caixa no lançamento de devolução, gerado pela bolsa retroativa:

Primeiramente o sistema verifica a conta caixa parametrizada nos parâmetros de inclusão de bolsa retroativa (Fin - Bolsa retroativa 2/3).  
Se o parâmetro estiver preenchido, o lançamento a pagar que será incluído terá esta informação de conta caixa.  
Se o parâmetro estiver nulo (sem valor), o lançamento a pagar irá considerar a conta caixa parametrizada para a geração de lançamentos:  
(Educacional -> Financeiro Geral 2/4 -> Conta Caixa)

Caso parametrizado para "***Devolver em espécie***"

O valor de crédito calculado não será aproveitado nos lançamentos das parcelas, pois a opção para a devolução em espécie passa ao sistema que não existe crédito para ser aproveitado.

O lançamento de devolução de crédito ficará em aberto para pagamento do valor ao aluno. A baixa do lançamento deve ser realizado manualmente no ***Totvs Gestão Financeira***, após o pagamento do valor.

Parametrizado para utilização de conta corrente:

O valor de crédito gerado será incluso na conta corrente do aluno.

Processo de vínculos de lançamentos

A remoção de vínculo originado de créditos do processo de inclusão/exclusão de bolsa retroativa excluirá o crédito para o lançamento considerado e o valor restante para o crédito de bolsa retroativa do contrato será atualizado.

## Exclusão de Bolsa Retroativa

#### Regras do processo

Não será permitida a inclusão/exclusão de bolsas retroativas a contratos cancelados.

O processo de exclusão de uma bolsa se refere a inativação da mesma como bolsa do contrato, quando for integral. ***A bolsa não será excluída do contrato.***

Quando houver uma exclusão de bolsa parcial, a mesma, não será inativada, pois terão outras parcelas vinculadas a bolsa.

Uma vez que a bolsa foi inativada pelo processo de exclusão de bolsa, ela será marcado como **INATIVA** pelo campo ***"Bolsa ativa"*** que ficará desmarcado. ***O valor desse campo não será editável.***

A exclusão de bolsas retroativas de crédito resultarão no cancelamento dos lançamentos gerados para seus sacados, que estiverem com status igual a ***"Em aberto"***.

Se o lançamento de um sacado estiver com status ***"Baixado",***será gerado um lançamento a pagar para devolução do valor pago indevidamente.

A exclusão de uma bolsa retroativa irá afetar, apenas, as parcelas que tenham lançamentos igual a ***"Em aberto"*** ou que, ainda, não foram gerados.

As parcelas com lançamentos já baixados ou baixados parcialmente não serão alterados. Os valores vinculados como crédito, indevidamente, serão cobrados em novas parcelas ou gerados como débitos em Conta Corrente.

Parametrização para a criação de um lançamento:

Caso parametrizado para "***Gerar uma única parcela para pagamento***":

Caso seja realizada a exclusão de uma bolsa inclusa pelo processo de inclusão de ***bolsa retroativa***:

Exclusão de uma bolsa ***integral***:

A bolsa do aluno será inativada.

* Se as parcelas com as bolsas excluídas já tiverem lançamentos gerados:

Será gerada uma parcela adicional/extra no contrato do aluno com a diferença a receber.

Caso o parâmetro "***Gerar lançamento***" esteja marcado, o lançamento da parcela será gerado automaticamente.

Exclusão de uma bolsa ***parcial***:

Se a exclusão parcial da bolsa ocorrer **no início do período de validade** da mesma, será mantida a validade final e será alterada somente a validade inicial da bolsa do contrato do aluno.

Se a exclusão parcial da bolsa ocorrer **no final do período de validade** da mesma, será mantida a validade inicial e será alterada somente a validade final da bolsa do contrato do aluno.

Caso a exclusão aconteça **no meio da validade** da bolsa:

Será criada uma nova bolsa para o aluno com validade da parcela posterior à última parcela considerada na exclusão até a parcela ou data final.

Se as parcelas com as bolsas excluídas já tiverem lançamentos gerados:

* + Será gerada uma parcela adicional/extra no contrato do aluno com a diferença a receber.

Caso o parâmetro "***Gerar lançamento***" esteja marcado, o lançamento da parcela será gerado automaticamente.

Caso seja realizada a exclusão de uma bolsa inclusa pelo processo de inclusão de ***bolsa comum***:

Será gerada uma parcela adicional/extra no contrato do aluno com o valor total a receber***.***

Caso o parâmetro "***Gerar lançamento***" esteja marcado, o lançamento da parcela será gerado automaticamente.

Caso parametrizado para "***Dividir pela quantidade de parcelas restantes***":

***Seguirá a mesma regra definida para a geração de parcela única***, com as diferenças abaixo:

Os valores das parcelas serão o resultado do total a receber divido pelo número de parcelas que, ainda, não tenham lançamentos gerados.

Serão geradas a mesma quantidade de parcelas consideradas na divisão e a cota será calculada com o próximo valor de cota disponível.

Caso todas as parcelas possuam lançamentos gerados ou o contrato não possua parcelas, será incluída uma parcela única com o valor de bolsa excluído.

Caso parametrizado para utilizar ***conta corrente***:

O valor do débito será incluído na Conta Corrente do aluno.

Exclusão de bolsas para mais de um responsável financeiro

Quando excluirmos retroativamente bolsas para mais de um responsável financeiro (parcelas com mais de um responsável que possua a bolsa ou parcelas diferentes com responsáveis distintos), as parcelas serão incluídas conforme parametrização citada acima (Parcela única ou Dividir pelas parcelas restantes) com os responsáveis financeiros considerados na exclusão e com o percentual de responsabilidade de cada responsável igual ao valor da respectiva bolsa excluída em relação ao valor total excluído.

**Exemplo**:  Exclusão de bolsa no valor de R$ 200,00 incidindo sob cada parcela de R$ 1000,00 para as parcelas P1 com responsável R1, P2 com responsável R1 e P3 com responsável R2 com o sistema parametrizado para geração de parcela única. Será gerada uma parcela única no valor de R$ 600,00 com dois responsáveis financeiros cujos percentuais de responsabilidade serão: 66,67% para R1 e 33,33% para R2

Processo de exclusão/cancelamento de bolsas

Não será permitida a exclusão/cancelamento de bolsas retroativas através do processo **"Excluir/Cancelar bolsas"**na visão de contratos, bolsas do contrato ou no assistente financeiro.

### Processo de geração de lançamentos

Se o sistema foi parametrizado para "***Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***"

Caso a forma de aproveitamento do crédito seja  ***"Aplicar devolução nas próximas parcelas"*** ou ***"Dividir devolução pela quantidade de parcelas restantes"***, o sistema realizará as seguintes tarefas:

* + - Calcula-se o valor correspondente ao crédito a ser aplicado de acordo com a forma de aproveitamento dentro do mesmo contrato.
    - Caso os parâmetros "******Criar devolução (inclusão de bolsa) / lançamento (exclusão de bolsa)***"**e****"Usar devoluções pendentes após término de contrato nos próximos contratos"***estejam marcados, deverá ser verificado se há a existência de algum **contrato encerrado** (todas os lançamentos das parcelas devem estar baixados baixados),**para o mesmo aluno**, no qual o crédito não foi totalmente aproveitado para um mesmo serviço da parcela. Será aproveitado o máximo valor de crédito, possível, encontrado de outros contratos no lançamento que está sendo gerado.
    - O aproveitamento será realizado através de vínculos financeiros entre o lançamento a receber da parcela e o(s) lançamento(s) de devolução(ões) de crédito.

Valores de multa não serão calculados para lançamentos gerados a partir de parcelas originadas por uma exclusão de bolsa retroativa.

Lançamentos em aberto a serem regerados de parcelas que originaram crédito retroativo não terão os valores de bolsas preenchidos nos valores opcionais ou de integração após regeração.

### Processo "Desfazer inclusão de bolsa retroativa"

false

Caminho:***Educacional | Educacional | Financeiro/Contábil | Assistentes | Desfazer inclusão de bolsa retroativa***

A inclusão de uma bolsa retroativa só poderá ser desfeita se nenhum dos lançamentos/parcelas envolvidos sofreram alterações de status e se a bolsa retroativa não estiver com status inativo.

Esse processo será responsável por excluir o vínculo da bolsa com o contrato e retornar todos os lançamentos das parcelas caso tenham, ao seu estado original, excluir os vínculos de crédito, cancelar os lançamentos de crédito e cancelar os lançamentos a receber gerados.

Caso o crédito tenha sido aproveitado em conta corrente, seus registros serão excluídos.

### Histórico e Rastreabilidade da Bolsa Retroativa

Foram disponibilizados anexos com visões que irão permitir a rastreabilidade dos registros de crédito e débito gerados pela inclusão/exclusão de uma bolsa retroativa:

## Anexos:

### Cadastro de contrato

false

Caminho:***Educacional | Educacional | Financeiro/Contábil | Contratos***

**Rastreabilidade de Bolsa Retroativa:**

* + - * Serão exibidos todos os registros de Crédito/Débito lançados pela inclusão de bolsas para o contrato.

***Rastreabilidade de aproveitamento de créditos do contrato:***

* + - * Serão exibidos todos os registros de Crédito restantes que foram aproveitados por outro contrato.
      * Esse recurso será disponibilizado com a parametrização para aproveitar o crédito restante de contrato encerrados.

***Valores de débito/créditos gerados:*** 

* + - * Serão exibidos, dentro da edição do formulário do contrato, os registros referentes aos valores de créditos/débitos gerados e os valores restantes, que não foram aproveitados.

### Cadastro de parcelas

false

Caminho:***Educacional | Educacional | Financeiro/Contábil | Contratos | Anexos: Parcela***

**Rastreabilidade de Bolsa Retroativa:**

* + - * Serão exibidos todos os registros de Crédito/Débito lançados pela inclusão de bolsas para o contrato da parcela selecionada

### Cadastro de bolsa do aluno

false

Caminho:***Educacional | Educacional | Financeiro/Contábil | Contratos | Anexos: Bolsa***

**Rastreabilidade de Bolsa Retroativa:**

* + - * Serão exibidos todos os registros de Crédito/Débito lançados pela inclusão da bolsa selecionada para o contrato do aluno.

***Valores de débito/créditos gerados:*** 

* + - * Serão exibidos, dentro da edição do formulário de bolsa do aluno, os valores de créditos/débitos gerados e os valores restantes, que não foram aproveitados.

A inclusão manual ou via processo "*Incluir Bolsas*" continuará permitindo o cadastro da bolsa no contrato do aluno mesmo para parcelas com lançamentos gerados. Essa inclusão não gerará créditos retroativos no contrato do aluno e, para que a mesma seja considerada, a parcela deverá ser gerada ou regerada.

divs
