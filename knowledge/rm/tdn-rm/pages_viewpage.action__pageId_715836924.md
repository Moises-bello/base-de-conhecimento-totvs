---
content_hash: c8abab516247a0d8cf83e162ac8dc257c0e7a52ac6de7a47ac0bb491c2b8b030
fetched_at: '2026-06-29T00:11:26.295725+00:00'
page_id: '715836924'
product: rm
source: tdn-rm
title: Gestão de Glosa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715836924
version: 75
---

## **CONTEÚDO**

**CONTEÚDO**

Importante!

A Gestão de Glosa foi remodelada na versão 12.1.2302, para que o usuário tenha maior facilidade e agilidade na conferência dos itens.

## **01. Visão Geral**

A Gestão de Glosa consiste em fazer a conferência de todos os itens retornados pelo convênio. Identificando os itens que foram glosados, pagos integralmente, ou até situações onde houve pagamento a maior.

O controle de glosa pode ser **total** ou **parcial** no nosso sistema.

### **Glosa Total**

É um tipo de glosa sintética. A **Glosa Total** refere-se ao não pagamento do valor total da **remessa** ou uma parte da **remessa,** sem especificar quais contas ou itens daquela conta que tiveram valores glosados. 

### **Glosa Parcial**

É um tipo de glosa analítica. A **Glosa Parcial** refere-se ao não pagamento do valor apresentado de parte de uma **remessa**, onde cada conta e seus respectivos itens do Grupos de Gastos vão estar identificados com os seus respectivos valores liberados e glosados.

Para esse tipo de glosa, para as Operadoras privadas que trabalham no padrão TISS, disponibilizam arquivos XML de retorno, onde os mesmos serão importados pelo nosso sistema, com cada um dos itens dos Grupos de Gastos com os seus valores liberados, glosados e motivos de glosa.

Para operadoras que não trabalham com o padrão TISS, geralmente são disponibilizados planilhas ou relatórios informando os mesmos dados acima, ou até em algumas situações, onde a Operadora informa somente o valor total ou percentual que será pago para aquela remessa, partindo do pressuposto que há alguma irregularidade.

### **Motivos de Glosas**

Os motivos justificados de glosas são os mais variados, mas podemos destacar os mais comuns como: falta de assinatura do usuário na guia/autorização, falta justificativa do médico para a realização do procedimento, falta do CID (Código Internacional de Doenças) que justifique o procedimento, valor cobrado incorreto, geralmente maior do que o negociado. 

Se o convênio glosar uma conta ou Remessa/Fatura o Prestador/Hospital pode corrigir o “problema” relatado pelo convênio e reapresentar a conta ou Fatura/Remessa no outro mês na tentativa de receber o valor original apresentado.

### **Fluxo do Processo**

## **02. Iniciar uma Glosa**

Para dar início à Gestão de Glosa de uma remessa, acesse o menu Faturamento/Gestão de Glosas.

Clique no botão incluir e em seguida clique no botão 3P para abrir a tela de pesquisa de remessas.

Na tela de pesquisa, preencha os campos conforme filtros disponíveis, somente o campo Unidade de Faturamento é obrigatório, porém quanto mais campos forem preenchidos, mais rápida e precisa será a pesquisa.

Informações

Na tela de pesquisa, são retornados somente faturas com o status "**Faturada**".

Após localizar a remessa desejada, dar um duplo clique na grid para que o sistema preencherá os dados da **Remessa** tela anterior. Os campos **Qtde Total Contas** e **Valor Total Cobrado** serão automaticamente carregados com base na remessa.

Clique em salvar o registro.

No anexo das **Contas**, serão exibidas todas as contas daquela remessa para que seja possível dar sequencia ao fluxo da Gestão de Glosas, todas contas iniciam com o status "**Pendente**".

## **03. Controle de Glosa pelo Total da Fatura**

Esse processo deve ser utilizado quando não existe valor a ser recursado ou quando o mesmo seja uma glosa acatada (perda).

Na tela de Gestão de Glosas, selecione apenas uma fatura e execute o processo **Glosa pelo Total da Fatura**.

Informe o valor recebido ou o valor glosado, que o sistema recalcula o outro valor. Caso o parâmetro "Associa Extrato/Nota Fiscal para realizar o controle de glosa" esteja marcado, o número do extrato deve ser informado para se prosseguir.

Após finalizar o processo, a Gestão da Glosa se finaliza e os valores informados são atualizados.

Além de alterar o status da remessa, todas as contas também terão o status alterado para Finalizado e nenhuma operação poderá ser feita nas contas individualmente.

**Validações existentes:**

* + - Não pode existir contas com controle de glosa já iniciada
    - O número de extrato informado deve existir
    - O valor liberado informado deve ser maior ou igual a zero
    - A fatura não pode ter sido glosada anteriormente pelo total da fatura
    - Não pode ser executada com status diferente de pendente
    - Não pode ser executada quando existir contas da fatura retornadas para correção
    - Não pode ter repasse liberado ou pago
    - Não pode esta incluído numa folha de pagamento

## **04. Estorno da Glosa pelo Total da Fatura**

Este processo deve ser executado nos casos onde uma remessa foi processada pela rotina de **Glosa pelo Total da Fatura** de forma equivocada ou que precisa ser ajustada.

Localize a remessa que deseja ser estornada e na aba processos execute o processo **Estorno da Glosa pelo Total da Fatura.**

Ao término da execução do processo, os valores originais da fatura são retornados e o status retornado para Pendente, tanto da remessa quanto das contas.

## **05. Atualizar Dados da Fatura**

Essa rotina é necessária nas situações onde uma remessa passou por alguma etapa de reprocessamento, **onde contas foram alteradas, removidas ou incluídas na remessa**, essa rotina deverá ser executa para que os dados da remessa seja atualizados em relação a Gestão de Glosas.

Localize a remessa que deseja ser estornada e na aba processos execute o processo **Atualizar Dados Fatura.**

Ao término da execução do processo, as quantidades de contas e o valor total das faturas selecionadas, assim como suas contas serão atualizadas no **Gestão de Glosas**.

## **06. Liberação Automática**

A realização da integração do controle de recebimento deverá ser ativada via **parametrização de sistema.**

**Ambiente → Parâmetros → Gestão Hospitalar → Faturamento → Controle e Recurso de Glosa → Gera o Controle de Recebimento automático ao finalizar o Controle de Glosa/Recurso.**

Com este parâmetro ativado a integração com o controle de recebimento será possivel, caso não esteja ativado, a integração não será possivel diretamente pela gestão de glosa, ou seja continuará a necessidade de se realizar o controle de recebimento via Tesouraria.

Esse processo só poderá executado quando a conta estiver com status iniciado ou pendente.

A libera automaticamente preenche  o valor Liberado dos itens igual ao valor cobrado.

Selecione uma ou mais contas e execute o processo.

**Validações existentes:**

* + - O número de extrato informado deve existir

Caso o parâmetro "Associa Extrato/Nota Fiscal para realizar o controle de glosa" esteja marcado, o número do extrato deve ser informado para se prosseguir.

Ao executar o processo, todos os itens serão liberados, o controle de glosa dessa conta será finalizado. Uma vez finalizado, não é possível alterar os valores. 

O status do recurso, só muda para finalizado caso seja gerado recurso para a conta original. Se conta original for total liberada no controle de glosa da conta original  
 a coluna do status do recurso continuara pendente.

## **07. Glosa Total Automática**

Esse processe só poderá executado quando a conta estiver com status iniciado ou pendente.

A glosa total automaticamente preenche  o valor glosado dos itens igual ao valor cobrado.

Selecione uma ou mais contas e execute o processo.

**Validações existentes:**

* + - O número de extrato informado deve existir
    - O motivo da glosa deve ser informado
    - A data de controle deve ser informada

Caso o parâmetro "Associa Extrato/Nota Fiscal para realizar o controle de glosa" esteja marcado, o número do extrato deve ser informado para se prosseguir.

Ao executar o processo, todos os itens terão a glosa total, o controle de glosa dessa conta será finalizado. Uma vez finalizado, não é possível alterar os valores.

## **08. Controle de Glosa por Conta**

Essa rotina tem a finalidade de realizar a conferência de item a item pagos, glosados ou recebidos a maior pelo convênio de forma manual, digitando os dados em tela.

Para iniciar o controle de glosa por conta, selecione a conta desejada e preencha os dados em tela conforme necessidade.

Importante!

Para salvar as informações é necessário clicar no botão **Executar** o processo. Se a tela for fechada, todos os dados serão perdidos.

Ao abrir a tela, todos os itens da conta são carregados, tendo um resumo das informações no parte superior, campos para realizar pesquisar dos itens ou status.

A grid permite que todas as colunas sejam ordenadas ou agrupados, facilitando a conferência dos registros.

* + Para ordenar, basta dar um clique na coluna.
  + Para agrupar, basta arrastar a coluna pela qual deseja agrupar.

Abaixo segue explicação de cada um dos campos do processo:

| ID | Campo | Descrição |
| --- | --- | --- |
| **1** | **Replicar itens glosados para outras contas da Remessa** | Durante o processamento da conta, o sistema irá pesquisar na mesma Remessa, **outras contas que possuam os mesmos itens através do código e irá replicar os seus dados.**  Exemplo: Se o item **90.50.9765 - ATADURA CREPON 08CM** teve o seu valor cobrado em **R$ 0,72** e o seu valor liberado foi de **R$ 0,72** na conta do João, e esse mesmo item **90.50.9765 - ATADURA CREPON 08CM** foi utilizado nas contas do Pedro, Maria e Antônio (da mesma remessa), esse item será replicado, já iniciando o processo de glosas dessas contas, e marcando esses itens como **Liberados**. O mesmo comportamento irá ocorrer para os itens que tiveram **Glosas**, **Valor Extra**, etc. |
| **2** | **Procurar** | Pesquisa rápida por qualquer coluna da grid. Muito útil quando se pesquisa todos os itens da conta e depois se deseja localizar itens na grid.  Cada coluna pode ser filtrada ou ordenada da forma que o usuário necessitar. Isso pode facilitar a análise dos itens de acordo com a maneira de cada usuário |
| **3** | **Grid** | Nessa grid são exibidos os itens pesquisados. |
| **4** | **Dados da Glosa** | Caso o item tenha glosa esses campos devem ser preenchidos, os dados ali digitados correspondem a linha selecionada na grid. |
| **5** | **Glosa Irrecuperável** | Indica que aquela glosa não pode ser recursada, ao marcar esse campo, será permitido preencher o valor irrecuperável que deverá ser igual ou menor ao valor cobrado. |
| **6** | **Desconto no Valor Unitário** | Quando operador e prestador negociam um adiantamento, o valor adiantado recebe um desconto, que pode ser em percentual ou em valor. O desconto é aplicado sobre o valor cobrado e não é considerado no valor da glosa. |
| **7** | **Replicar item** | Irá replicar os dados do item selecionado para os demais itens lançados que possuam o mesmo código ou descrição, e mesmo valor unitário |
| **8** | **Sem Informação de Pagamento** | Marca os itens selecionados com a informação que o convênio não retornou nenhuma informação sobre os itens. Assim, os mesmos serão separados para posteriormente serem analisados. É possível selecionar mais de 1 item de uma vez |
| **9** | **Liberar itens pendentes** | Libera automaticamente os itens pendentes, ou seja, não ocorreram glosas esses itens. |
| **10** | **Liberar itens** | Para agilizar, pode ser selecionados diversos itens na grid e liberados de uma só vez. Diferente do item anterior, esse libera os itens selecionados e não somente os pendentes |
| **11** | **Retornar para pendente** | Estorna a glosa lançada e retorna o item com o status de Pendente. É possível selecionar mais de 1 item de uma vez |

Com os registros digitados, clicar em **Executar**, para que as informações sejam processadas e salvas. Caso todos os itens sejam analisados, o status do controle de glosa será marcado como finalizado. Caso seja necessário realizar alguma correção nos dados da Glosa executar o processo "Retornar Conta para correção".

Informações

A réplica do item selecionado em tela tem comportamento diferente da réplica feita durante o processamento do Controle de Glosa. No botão **Réplica do item selecionado**, será feita a réplica dos itens com o mesmo **código** ou **descrição**. Já a réplica do processamento, somente itens **com o mesmo código em outras contas serão replicados**.

### Novos Campos

Os dados para informação da Glosa foram remodelados para separar informações do item de glosa e informações da conta.

#### Dados Glosa / Dados Conta

Foram criadas duas Abas para esta separação:

1 - **Dados Glosa**: Informações pertinentes a glosa do Item;

2 - **Dados conta**: Informações globais da Conta que esta sendo controlada;

3 - A partir da versão **12.1.2306** foi disponibilizado o campo *Data Controle,* que poderá ser utilizado para um controle externo da Clínica/Hospital. Este campo não afeta nenhum fluxo interno do sistema, é apenas informativo e poderá ser utilizado de formas diferentes para cada cliente, por exemplo, criação de fórmulas visuais;

4 - Grupo *Desconto no Valor Unitário* fica invisível se o parâmetro *Permite desconto no controle de glosa* estiver **desmarcado**;

5 - Grupo *Desconto no Valor Unitário* fica visível se o parâmetro *Permite desconto no controle de glosa* estiver **marcado**;

**Obs**.: Caminho do parâmetro → *Aba Ambiente / Parâmetros / Gestão Hospitalar / Controle de Recurso de Glosa*.

Na aba *Dados Conta* foram criados dois campos:

1 - *Data Controle*: Possui o mesmo conceito do campo Data Controle disponibilizado na Aba Dados Glosa, porém neste, o escopo do mesmo é a conta e não o item glosado.

2 - *Valor Cota Extra*: Este campo é utilizado para informar um valor extra disponibilizado pela operadora, como forma de bônus por exemplo, é um acordo entre a operadora e o prestador de serviço.

Caso o parâmetro "Associa Extrato/Nota Fiscal para realizar o controle de glosa" esteja marcado, o número do extrato deve ser informado para se prosseguir.

3 -  A partir da versão **12.1.2510** foi disponibilizado o campo *Ida da Baixa,* que poderá ser utilizado para um controle  do recebimento que foi feio ao executar o controle de glosa. 

### Nova Coluna

Foi criada uma nova coluna para exibir os Tipos de Repasse associados a cada item de lançamento.

Ao clicar na célula de cada Tipo de Repasse exibe uma breve descrição.

Tipos de Repasse:

1 - Normal - Normal pelos Critérios de Repasse (Cor: Lilás);

2 - Redirecionado - Repasse por Redirecionamento (Cor: Azul);

3 - Divisão - Repasse por Divisão (Cor: Verde);

4 - C. Custo - Repasse Automático por Centro de Custo (Cor: Laranja).

**Obs.: Quando o Item selecionado possuir Repasse Liberado o Grupo *Dados Glosa* fica desativado para edição e exibe uma mensagem descritiva do motivo do bloqueio.**

#### Visualização Contas

Foram adicionados os campos:

1 - Valor Cota Extra - Valor cota extra informado no momento do controle de glosa por conta

2 - Valor Estorno Cota Extra - Valor informado no processo de estorno do valor da cota extra

3 - Valor Total Recebido - **Valor Recebido + Valor Cota Extra - Valor Estorno Cota Extra**

4 - Status do Recurso - O status do recurso, só muda para finalizado caso seja gerado recurso para a conta original. Se conta original for total liberada ou for gerado uma glosa Irrecuperável no controle de glosa da conta original a coluna do status do recurso continuara pendente.

Caso algum item possua repasse liberado ou já pertença a alguma folha de pagamento, o mesmo não poderá sofrer glosa. A exceção é quando o critério de repasse estiver com o parâmetro "Libera repasse no lançamento" marcado.

## **09. Controle de Glosa por Grupo de Gastos**

Esta funcionalidade tem como objetivo permitir ao faturista que realize a glosa pelos Grupo de Gastos dos itens que compõem a conta.

Desta forma é possível agilizar o processo de gestão de glosa, pois em alguns casos o faturista não precisa ir item a item para informar o valor da Glosa, apenas verifica o valor total que foi pago pelo convênio e informa no Grupo de Gasto em questão.

Para ter acesso a esta funcionalidade, o usuário irá acessar o mesmo processo anterior (Controle de Glosa por Conta), nesta tela é possível acessar a aba Glosa por Grupo de Gasto, conforme imagem abaixo:

Os grupos disponíveis para realização da glosa são:

1. * **Diárias**
   * **Taxas**
   * **Serviços**
   * **Honorários**
   * **Exames**
   * **Materiais**
   * **Medicamentos**
   * **Órteses**
   * **Próteses**
   * **Honorários Não Credenciados**
   * **Exames Terceiros**
   * **Taxas Administrativas**
   * **Total da Conta**

Para um melhor controle, algumas regras são levadas em consideração para permitir que uma glosa seja informada por grupo, são elas:

1. * Um grupo de gasto só pode ser glosado se todos os itens estiverem pendentes.
   * Um grupo de gasto não pode ser glosado caso exista repasse para algum item desde grupo
   * Caso a glosa tenha sido realizada pelo campo Total Pago, todos os demais grupos ficarão indisponível para realizar a glosa
   * Caso um grupo de gasto tenha sido glosado não é possível realizar a glosa posteriormente pelo item, neste caso é necessário realizar o estorno da glosa por grupo e realizar a analise item a item.
   * Caso a conta exista algum item com o grupo de gasto **PACOTE**, a conta será considerada como conta pacote e nenhum grupo de gasto ficará disponível para ser glosado.
   * Grupos com valores zerados também não podem ser glosados.

Abaixo temos um exemplo onde o grupo de gasto Medicamentos foi glosado no valor de R$ 3,00, desta forma ao mudar a aba novamente para Glosa por Item é possível perceber que os campos para informação da glosa estão todos bloqueados.

#### Status dos Campos:

* + **Amarelo:** Se não for possível aplicar a glosa ao grupo de acordo com as regras estabelecidas. Nesse caso, o campo de glosa será destacado em amarelo e não poderá ser editado.
  + **Vermelho:** Se o grupo já tiver sido glosado anteriormente, o campo de glosa ficará destacado em vermelho. No entanto, será possível editar a glosa existente.
  + **Verde:** Se o grupo ainda não tiver sido glosado e não houver impedimentos com base nas regras, o campo de glosa ficará destacado em verde, permitindo que o usuário insira a glosa.

#### Estorno Glosa Grupos

Esta funcionalidade permite o usuário realizar o Estorno da Glosa feita na Aba Glosa por Grupo, tanto para Glosa pelo valor total ou pelo grupo de gasto.

Informação

Na versão RMSaude (antiga MDI) existiam dois botões, **Estorna Glosas Grupos** e **Estorna Glosa Valor Total**, na migração foi analisado e identificamos o comportamento similar, então unificamos em apenas um botão, **Estorna Glosa Grupos**.

Após realizar o estorno o valor pago é retornado ao original e o usuário poderá glosar novamente por item ou por grupo.

## **10.** **Integração com o Controle de Recebimento**

A realização da integração do controle de recebimento deverá ser ativada via **parametrização de sistema.**

**Ambiente → Parâmetros → Gestão Hospitalar → Faturamento → Controle e Recurso de Glosa → **Gera o Controle de Recebimento automático ao finalizar o Controle de Glosa/Recurso.****

Com este parâmetro ativado a integração com o controle de recebimento será possivel, caso não esteja ativado, a integração não será possivel diretamente pela gestão de glosa, ou seja continuará a necessidade de se realizar o controle de recebimento via Tesouraria.

Após a finalização dos apontamentos de glosa, o sistema apresentará a etapa de **Recebimento** para preenchimento dos campos obrigatórios do **Controle de Recebimento**, seguindo as mesmas validações já existentes na rotina atual.

Ao processar, o sistema executará automaticamente o controle de recebimento e a **integração da baixa financeira**.

Os itens que permanecerem pendentes serão marcados como **"Sem informação de pagamento"**. Esses itens serão incluídos em uma **nova conta**, que poderá ser analisada e recebida posteriormente.

Caso ocorram falhas de negócio durante a execução — tanto no controle de glosa quanto na integração com o Financeiro —, o sistema exibirá mensagens de erro com **orientações sobre como ajustar os dados** e realizar um novo processamento.

**Fluxo do processo:**

**10.1** Conclusão da digitação/analise da Glosa

**10.2** Após confirmação da mensagem, os itens **pendentes** serão marcados como **Sem Informação de Pagamento**.

**10.3** Próximo passo, será responsável pelo **preenchimento** dos campos para **controle de recebimento**.

**10.4** Após a execução, no log será informando que o **controle de recebimento** e as **respectivas baixas** foram realizadas com êxito. A mensagem inclui um resumo os valores processados.

**10.5** Caso existam itens marcados como **Sem Informação de Pagamento**, será gerada uma nova **conta do Tipo S – Sem Informação de Pagamento** na tela de Contas, para que o recebimento desses itens seja realizado posteriormente.

## **11. Importação de Arquivo Demonstrativo de Análise de Contas**

Este processo tem a finalidade de realizar a importação do arquivo xml enviado pelo convênio e identificar a fatura, as guias e os pagamentos e glosas dos itens.

Para executar o processo, selecione a remessa desejada na grid.

* + Para iniciar a importação, através da tela de **Gestão de Glosas**, acesse o menu Processos > Importação de Demonstrativo de Análise da Conta e execute o processo
  + Informe a unidade de faturamento, o convênio e o arquivo xml enviado pelo convênio
  + Clique no botão Executar
    - O sistema valida se o arquivo corresponde ao convênio selecionado (através do CNPJ ou registro ANS)
    - Valida se o prestador principal da unidade de faturamento é o prestador contido no xml (através do CNPJ ou pela credencial no convênio)
    - Verifica se a gestão de glosa da fatura a ser importada, não está como finalizada ou encerrada
    - Verifica se a fatura possui contas retornadas para revisão. Caso possua, a contas contidas no xml não serão consideradas.
    - Verifica se o protocolo contido no xml é igual ao informado na fatura (caso tenha sido informado na fatura)
    - Identifica as contas dos paciente através do número da guia da operadora. Caso não encontre, pesquisa pelo número da guia do prestador
    - Guias contidas no xml com o status "Em análise", também serão desconsideradas, uma vez que não possui detalhes de pagamentos e glosas
    - A identificação dos recebimentos e glosas serão realizadas, somente se existirem informações dos procedimentos no xml.
    - Não serão realizados glosas somente pelo total da conta
    - No log da rotina serão exibidas mensagens como:
      * Situação da fatura com alguma restrição
      * Número da guia que não foi encontrada no sistema
      * Guia com o status de Em análise
      * Guias que não possuem itens
      * Itens não encontrados nos lançamentos da conta
    - Ao final do processo, as glosas e recebimentos identificados terão seus dados preenchidos com as informações contidas no xml
    - **Pode existir situações em que determinado item foi agrupado por código e data no xml. Quando o arquivo do demonstrativo for importado e o valor glosado dividido entre os registros que foram agrupados, gerar um valor unitário com mais de duas casas decimais, o sistema irá deduzir o valor com duas casas para cada lançamento e no último registro, o restante da glosa será aplicado. Assim o valor glosado sempre será igual ao informado pela operadora.****Exemplo:**

      Suponha a glosa de 0.40, mas com 3 itens lançados na mesma data. O valor de rateio seria de 0,1333.  
      Então os dois primeiros terão glosa de 0,13 e o último 0,14 para que o total seja de 0,40

* + Para visualizar o resultado da importação realizada, acesse a conta desejada e execute o processo Controle de glosa por conta.

## **12. Recurso de Glosa**

O processo de Recurso de Glosa estará disponível **após a finalização do Controle de Glosas**. No entanto, é importante destacar que o recurso só poderá ser realizado caso tenha sido identificada uma glosa durante o Controle de Glosas para apenas um dos itens na conta e se houver, que não tenha sido marcada como **Glosa Irrecuperável**.

Ao abrir a tela, os dados da conta são exibidos no cabeçalho. Na **grid**, são listados os itens que possuem glosa.

Nos campos abaixo da grid, são exibidos os valores correspondentes à linha selecionada. Para prosseguir, é necessário:

1. **Informar o valor a ser recursado**:
   1. Insira o valor que deseja contestar.
   2. Selecione o motivo do recurso dentre as opções disponíveis, o motivo que melhor justifica o recurso do item glosado.
   3. O campo **Data Controle** é um recurso opcional que pode ser utilizado para um controle externo pela Clínica/Hospital. Esse campo não interfere em nenhum fluxo interno do sistema, sendo apenas informativo. Ele pode ser utilizado de diferentes formas, de acordo com as necessidades de cada cliente, como, por exemplo, a criação de fórmulas visuais, relatórios ou outros critérios de organização.
   4. Caso necessário, adicione um texto de Observação/Justificativa com a explicação detalhada ou justificativa adicional sobre o recurso. O preenchimento deste campo é facultativo, mas recomendado para embasar a contestação.
2. **Recursar valor total**:
   1. Ao selecionar essa opção, o valor recursado será preenchido automaticamente com o mesmo valor da glosa.
3. **Retornar para pendente**:

   1. Essa função estorna os recursos lançados e retorna os itens ao status de **Perda**.
4. **Replicar item selecionado**:

   1. Ao utilizar essa opção, o sistema replicará o item selecionado, mantendo o mesmo valor recursado do item anterior.
5. **Imprimir**:

   1. O sistema disponibiliza o relatório padrão **SAUREL0134 - Relatório Recurso de Glosa** na ferramenta [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento). Caso o cliente deseje customizar o relatório, será necessário criar uma cópia do relatório padrão e realizar as alterações desejadas utilizando a ferramenta de relatórios da TOTVS.

Dica

Se o valor original da cobrança era de R$ 70,00 e a operadora liberou R$ 50,00, o valor a ser recursado será de no máximo R$ 20,00. Esse valor refere-se à diferença entre o valor original e o valor já liberado, sendo o objeto do recurso.

Caso nenhum dos itens glosados seja objeto de recurso, basta executar o processo para que os itens sejam marcados como glosas definitivas.

Após concluir o processo, o sistema criará um **novo registro da conta recursada**, onde será possível realizar uma nova análise de glosa.

Quando a operadora responder, informando se os valores foram acatados ou não, essas informações deverão ser registradas na rotina de **Controle de Glosa para a conta do tipo Recurso**, seguindo os mesmos passos descritos no tópico **Controle de Glosa por Conta** deste documento.

Esse processo é **cíclico** e pode ser repetido várias vezes até que uma das partes (prestador ou operadora) acate o valor ou ceda. Durante esse período, o status do recurso da **conta Original** permanecerá como **Pendente**, mesmo que algum item tenha sido marcado como **glosa irrecuperável** na etapa de Controle de Glosa por Conta. O status só será alterado para **Finalizado** após a conclusão de todos os itens serem processados pelo **Recurso de Glosa** relacionados à conta original.

## **13. Cancelar Recurso de Glosa**

Uma vez finalizado o Recurso de Glosa, não é possível alterar os valores. Caso seja necessário corrigir alguma informação, o processo "**Cancelar Recurso de Glosa**" poderá ser executado. Essa função tem como finalidade desfazer o recurso finalizado, retornando o processo à etapa de definição dos valores a recursar e das justificativas.

Para realizar o cancelamento, a nova conta de recurso que contém os itens recursados, deve satisfazer os seguintes critérios:

* + - Não pode ter repasse liberado ou pago
    - Não pode pertencer a uma remessa de reapresentação
    - Não pode ter o controle de glosa feito. Caso possua, a glosa deve ser excluída e o controle retornado para pendente.
    - Não pode existir baixas parciais após o processamento do recurso

Para cancelar, o usuário possui as seguintes opções:

* + - Cancela e **apaga**todos os dados já informado.
      * Atualiza os valores opcionais do financeiro RM, caso parametrizado
      * Exclui o controle de recebimento analítico, caso esteja parametrizado
      * Retorna o status para poder recursar novamente
      * Remove o valor a recursar, o motivo do recurso e justificativa de todos os itens.
    - Cancela e **não apaga** os dados já informados.
      * Atualiza os valores opcionais do financeiro RM, caso parametrizado
      * Exclui o controle de recebimento analítico, caso esteja parametrizado
      * Retorna o status para poder recursar novamente

**Conta com glosas de 5,59**

**Recurso realizado**

**Recurso de Glosa** -  Relatório "**SAUREL0134 - Recurso de Glosa.TotvsReport** **"** Informar em Ambiente -Paramêtros - Gestão Hospitalar - Relatórios.

Importante!

Para controlar a exibição dos honorários fora da conta no relatório, acesse as **Condições Contratuais** do convênio e navegue até **Eletrônico III → Geral III**.

O parâmetro **"Soma Lançamento Fora da Conta no Recurso de Glosa"** define se os lançamentos realizados fora da conta devem ser incluídos na totalização do relatório de Recurso de Glosa (SAUREL0134).

* **Marcado**: os honorários fora da conta são somados e exibidos no relatório.
* **Desmarcado**: os honorários fora da conta são ignorados na somatória.

Opções para cancelamento do recurso

## **14. Retornar Conta para Revisão**

Essa funcionalidade serve para retornar as contas que já foram finalizadas o controle de glosa, para que sejam revisadas.

Somente contas com o status diferente de Pendente e Iniciada podem ser retornadas.

Caso a conta possua recurso gerado, também não poderá retorná-la. Para isso, deve cancelar o recurso e retornar a conta para revisão.

## **15. Estorno Cota Extra**

Esta funcionalidade foi criada para realização do estorno do valor informado em Cota Extra.

Apenas estará disponível, caso o valor de Cota Extra tenha sido gravado no momento da realização do Controle de Glosa por Conta.

Ao selecionar a opção Estorno Cota Extra, o sistema carregará a tela com as seguintes informações:

1 - Valor Cota Extra (somente leitura)- Valor informado em Cota Extra no momento da realização do controle de glosa por conta. 

2 - Valor Estorno - Valor que o usuário quer estornar. O valor deverá ser maior que 0 e menor que o valor da cota extra.

3 - Data Estorno - Data que o estorno foi realizado.

## **16.** **Itens Sem Informação de Pagamento**

Caso o convênio não envie informações de pagamento para determinados itens, selecione o item e clique no botão "**Sem Info**". Dessa forma, o sistema separará esses itens, para que os mesmos sejam conferidos posteriormente.

Assim é possível concluir o controle de glosa dos demais itens e realizar o recurso, caso seja necessário.

**Note que cada conta possui um tipo:**

* + N: conta normal. É aquela que foi enviada para o convênio
  + R: conta de recurso: É aquela que foi gerada pelos itens recursados
  + S: conta com itens sem informação de pagamento

## **17. Conversor Gestão de Glosas**

Para visualizar as remessas antigas e que já tiverem o processo de glosa iniciado ou finalizado, é necessário executar o processo para convertê-las para a nova Gestão de Glosas. Uma vez realizado a conversão, não se deve utilizar mais as rotinas na antiga MDI Delphi.

Para executar o processo é necessário que o perfil tenha acesso à funcionalidade.

Acesse o menu Faturamento | Gestão de Glosas. Não é necessário selecionar nenhum registro, basta executar o processo.

Informe o período de geração das remessas que deseja importar.  
Caso encontre divergência de valores de valor recebido, valor da perda não sendo considerado, marcar a opção "Recalcular os valores do controle de glosa para remessas já convertidas", que o sistema fará o recálculo.  
Este processo somente importará as remessas que ainda não estejam na nova Gestão de Glosas, portanto não há problema de se executar o processo mais de uma vez.

Por se tratar de uma grande volume de dados, este processo deve ser executado em períodos de pouca movimentação na instituição e em períodos menores. É importante que se façam simulações em base de testes para se ter uma noção do tempo de execução.

## **18.** **Parâmetro Integração com Controle de Recebimento**

O sistema possui um parâmetro, que quando ativo irá gerar o controle de recebimento de forma automática associando o número do Extrato/Nota Fiscal no momento de concluir a glosa ou recurso.

## **19.** **Parâmetro Motivo de Glosa ANS ou Motivo de Glosa RM**

Importante!

O motivo de glosa informado nos arquivos XML da ANS sempre será gerada com os códigos conforme a tabela de domínio 38 - Terminologia de mensagens, de acordo com a versão TISS.

No contrato da operadora, é possível definir qual a codificação será utilizada nas rotinas de **Controle de Glosa** e **Recurso de Glosa**.

A opção **Motivo de Glosa ANS** é indicada para as operadoras que utilizam o padrão TISS para troca de mensagens, isso facilita a transcrição dos dados no momento do preenchimento manual do controle da glosa.

Caso a operadora trabalhe com um padrão próprio, é possível trabalhar com os motivos cadastrados diretamente no sistema, nesse caso a opção a ser escolhida será **Motivo de Glosa RM.**

## **20. Tabelas Utilizadas**

* SZCONTROLEGLOSA
* SZCONTROLEGLOSAITEM
* SZRESUMORECGLOSA
* SZMOTRECGLOSA
* SZATENDIMENTOREC
* SZRESUMORECGLOSA
* SZATENDHONORARIO
* SZATENDTAXASERV
* SZATENDTAXASERV
* SZATENDMATMED
* SZATENDSADT
* SZCONTROLREPASSE
* SZCONTROLREPASSEDIV
* SZATENDRESUMOCOMPCCUSTOESPEC
* SZANSATENDAUTORIZCAB
* SZATENDAUTORIZ
* SZCONTROLRECEB
* SZATENDRESUMO
* SZPARCIALATEND
* SZATENDIMENTO

## **20. Controle de Recebimento**

Efetuando o Controle de Glosa por Conta, ao avançar a etapa, exibirá a rotina de Controle de Recebimentos, se o usuário possuir as permissões de acesso necessárias.

Para utilizar este recurso, deve-se acessar o módulo Serviços Globais > Segurança > Acesso > Perfil > selecionar e editar o perfil desejado > Acesso a Menus.  
Depois disso navegar até a opção Hospitais e Clínicas > Tesouraria > Controle de Recebimentos e permitir "Incluir Recebimentos".

Com isso o usuário terá acesso ao Controle de Recebimentos.

Então agora no Controle de Glosa por Conta, ao avançar, será exibida a rotina do COntrole de Recebimentos.
