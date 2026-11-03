---
content_hash: 7ad236ce31cbf80e21049507e437f40bafc25de413c67749eb741eb699e1e8be
fetched_at: '2026-06-29T00:11:17.118681+00:00'
page_id: '676590403'
product: rm
source: tdn-rm
title: Repasse de Honorários Médicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676590403
version: 21
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Cadastro do Desconto do Repasse**
3. **Cadastro de Critério Geral de Repasse**
4. **Cadastro do Grupo de Prestadores**
5. **Configurações do Prestador**
6. **Configurações das Condições Contratuais**
7. **Parâmetros do Repasse Particular**
8. **Parâmetros do Repasse Convênio**
9. **Parâmetro Dias de Liberação do Repasse**
10. **Parâmetro Dias de Pagamento do Repasse**
11. ## **Integração Backoffice**
12. **Folha de Produção**
13. **Elaboração de Contas**
14. **Repasse de Honorários Médicos**
15. **Repasse por Indicação**

## **01. VISÃO GERAL**

O repasse médico consiste no pagamento de valores (fixos ou percentuais) a profissionais médicos por serviços prestados em procedimentos. Nos hospitais, a maioria dos médicos não possui vínculo empregatício (CLT), diferentemente de outros profissionais como enfermeiros, nutricionistas e técnicos de radiologia que são contratados diretamente pela instituição.

Quando os médicos fazem parte do corpo clínico mas não possuem credenciamento direto com o convênio, seu pagamento ocorre através do hospital - que realiza a cobrança ao convênio e depois repassa o valor correspondente ao profissional. Isso acontece porque, nestes casos, o convênio não tem relação contratual direta com o médico.

Importante destacar que, para médicos credenciados diretamente pelos convênios, os valores são pagos conforme acordado entre o médico e operadora, de acordo com a produção enviada nas guias TISS. O módulo de Repasse não gerencia nenhuma dessas informações.

Os repasses podem ser realizados de duas formas principais: após a confirmação do recebimento dos valores pelo convênio/paciente (modelo mais seguro) ou com base no valor faturado (modelo mais ágil). A definição do modelo depende sempre do processo definido pelo Hospital.

O sistema oferece ampla flexibilidade na configuração das regras de repasse, permitindo estabelecer critérios específicos por prestador, função profissional, faixas de procedimento, grupos ou listas de itens, convênios, planos de saúde e até mesmo por indicação médica. Essa versatilidade permite adaptar o processo às diversas realidades operacionais encontradas nos diferentes estabelecimentos de saúde.

## **02. CADASTRO DE DESCONTO EM REPASSE**

Nessa opção é realizado o cadastro de Desconto em Repasse, que é o desconto no valor apurado (fixo ou percentual) do critério de repasse, normalmente acordado com o médico.

1. 1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Desconto em Repasse**.
   2. Clique em **Incluir** (página em branco).
   3. Preencha o Nome do desconto.
   4. Preencha o nome reduzido (abreviatura).
   5. Informe o Percentual de desconto ou o Valor de desconto

## **03. CADASTRO DE CRITÉRIO GERAL DE REPASSE**

Nessa opção, é realizado o **cadastro de Critério Geral de Repasse** no sistema. Os **Critérios de Repasse** são regras definidas pelo **Prestador Principal** para determinar as porcentagens e valores que serão repassados aos **Prestadores de Serviço** envolvidos

#### **Passo a Passo:**

1. 1. Acesse: **Cadastros > Faturamento > Critério Geral de Repasse.**
   2. Clique em **Incluir** (página em branco).

#### **Guia Identificação:**

* + **Descrição:** Preencha o nome do repasse.
  + **Período de Vigência:** Informe a data de início. A data final é opcional.
  + **Unidades:** Selecione a **Unidade de Faturamento** e a **Unidade de Atendimento**.
  + **Tipo de Base de Cálculo:** Escolha uma das opções:

    - Valor total do Procedimento.
    - Valor total com deduções.
    - Valor total com acréscimos.

#### **Tipo de Distribuição:**

* + **Normal:** Regra aplicável a toda a instituição (não é definido um profissional específico).
  + **Individual:** Regra para um profissional específico. Caso selecione essa opção, informe o profissional responsável.
  + **Indicação:** No **Registro de Atendimento**, informe o profissional que indicou o paciente. Essa regra pode ser utilizada na **Folha de Produção de Indicação**, se aplicável.

#### **Tipo de Repasse:**

Selecione uma das opções:

* + Grupo de Itens.
  + Lista de Itens.
  + Item.
  + Faixa de Codificação.
  + Grupo.
  + Especialidade.

#### **Configurações Adicionais:**

* + **Valor Recebido:** Marque essa opção se o repasse deve ser calculado com base no valor recebido (ou seja, o repasse só será liberado após o item ser recebido pelo convênio).
  + **Plantonista Recebe Repasse:** Marque essa opção se os plantonistas devem receber repasse. Caso os plantonistas sejam CLT, mantenha desmarcado.
  + **Não Incluir Custo Operacional no Repasse:** Marque para excluir o custo operacional do cálculo do repasse.
  + **Não Incluir Valor do Filme no Repasse:** Marque para excluir o valor do filme de radiologia do cálculo do repasse.

#### **Painel Faixa:**

* + Clique em **Incluir** (página em branco) para adicionar uma faixa de codificação.

#### **Guia Complemento:**

* + **Aplicação do Critério:**

    - Atribua o critério a um **Convênio/Plano/Subplano** ou a um **Prestador**.
    - Aplique o critério somente a **prestadores cooperados** (essa informação deve estar cadastrada no prestador).
  + **Tipo de Paciente:** Selecione uma das opções:

    - Interno.
    - Externo.
    - Ambos.
  + **Classe de Atendimento:** Selecione uma das opções:

    - Eletivo.
    - Urgência.
    - Ambos.

#### **Guia Observação:**

* + Nessa guia, é possível incluir **observações** referentes ao critério de repasse.

#### **Guia Deduções/Acréscimos:**

* + Essa guia permite cadastrar **deduções** e **acréscimos** para cada Critério de Repasse.
  + **Disponibilidade:** A guia estará disponível somente se o campo **"Tipo de base de cálculo"** for igual a:

    - Valor total com deduções.
    - Valor total com acréscimos.

#### **Guia Descontos:**

* + Nessa guia, são informados os **descontos** aplicáveis em repasses para **Prestadores de Serviços de Saúde**.
  + **Pré-requisito:** Os descontos devem estar previamente cadastrados na funcionalidade:

    - **Cadastros > Faturamento > Desconto em Repasses.**
  + **Campo "Quantidade do mesmo item para aplicar o desconto":**

    - Valor padrão: **1**.
    - Esse campo será diferente de **1** quando houver desconto no valor do repasse a partir de um número **"x"** de lançamentos do mesmo item.

#### **Guia Valores de Repasse:**

* + Nessa guia, são definidas **regras específicas** para os repasses, como possíveis descontos para **Prestadores de Serviços de Saúde**.

#### **Destinatário "Outros Prestadores":**

* + Ao utilizar essa opção, é possível definir **regras especiais** para um prestador específico.

#### **Campo "Valor Restante":**

* + Se essa caixa estiver marcada, o cálculo do repasse será feito por último.
  + O valor base de cálculo será o **valor total** menos o **somatório dos valores de repasse** para os outros prestadores.

## **04. CADASTRO DO GRUPO DE PRESTADORES**

O cadastro de **Grupo de Prestadores** está diretamente relacionado ao **Repasse de Honorários Médicos**, pois alguns médicos faz parte de uma **empresa** com outros prestadores para realizar o recebimento dos serviços prestados ao Hospital.

* + Os **Honorários** são registrados em nome dos **Médicos**, mas o pagamento é realizado a um **Grupo de Prestadores** (como uma Clínica).
  + O **Hospital** faz o pagamento para o **Grupo de Prestadores** e gera uma **Folha de Produção** que contempla todos os procedimentos realizados pelos prestadores da Clínica.
  + A **empresa representada através do Grupo de Prestadores** é responsável por efetuar o pagamento aos prestadores.

#### **Passo a Passo:**

1. 1. Acesse **Cadastros > Uso Geral > Grupos de Prestadores.**
   2. Clique em **Incluir**.
   3. Clique em **"..."** para selecionar o **Prestador** que irá fazer parte do **Grupo de Prestadores**

Tela de inclusão dos prestadores ao grupo. Nele, deve-se informar se para o prestador em questão o grupo receberá o repasse ou não.   
Existem 4 configurações possíveis:

* 1. O repasse é para o grupo quando o lançamento for para o prestador, tanto nas regras de plantão, quanto para execução de procedimentos  
     Esta opção é utilizada para todas as rotinas que calculam o repasse, ou seja, todos os lançamentos que caem na "Elaboração de Contas" e na rotina de "Apuração de Plantões Realizados"
  2. O repasse é para o grupo quando o lançamento for feito para o prestador na execução de procedimentos  
     Esta opção é utilizada para todas as rotinas que calculam o repasse para os lançamentos que caem na "Elaboração de Contas"
  3. O repasse é para o grupo quando o lançamento for feito para o prestador na apuração do plantão  
     Esta opção é utilizada para todas as rotinas que calculam o repasse na rotina de "Apuração de Plantões Realizados"
  4. O grupo não recebe o repasse quando for executado para o prestador  
     Nenhum grupo é selecionado automaticamente

## **05. CONFIGURAÇÕES DO PRESTADOR**

No cadastro de **Prestador**, é necessário realizar configurações específicas relacionadas ao recebimento de **Repasse de Honorários**.

#### **Passo a Passo:**

1. 1. Acesse **Cadastros > Uso Geral > Prestador.**
   2. Dê um **duplo clique** no cadastro do prestador para realizar alterações.
   3. Clique na guia **Repasse**.

#### **Configurações na Guia Repasse:**

* + **Recebe Repasse:** Marque essa caixa se o prestador deve receber repasse.
  + **Sócio/Cooperado:** Defina se o prestador recebe repasse de acordo com as regras para **Sócio/Cooperado** no **Critério de Repasse**.
  + **Itens de Repasse:** Marque as caixas correspondentes aos itens que o prestador recebe:

    - **Diária.**
    - **Taxa.**
    - **Serviço.**
    - **MatMed (Materiais Médicos).**
  + **Repasse Automático por Centro de Custo:**

    - Configure, se necessário, e informe as **taxas por centro de custo**.

## **06. CONFIGURAÇÕES DAS CONDIÇÕES CONTRATUAIS**

**Parâmetro "****Configurações na Guia Repasse"**

Em cada **contrato**, é possível definir se o sistema deve calcular os repasses com base em:

* + **Somente a parte do convênio.**
  + **Somente os gastos particulares.**
  + **Ambos (convênio e gastos particulares).**

## **07. PARÂMETROS DO REPASSE PARTICULAR**

Para configurar os parâmetros de repasse do Particular, acesse **Ambiente > Parâmetros > Gestão Hospitalar** e navegue até as opções **Faturamento > Repasse Particular**.

**1. Liberação automática do repasse para pacientes Particulares:**

Indica se o sistema deverá ou não calcular repasses para pacientes particulares. Caso não seja necessário calcular repasses para esse tipo de atendimento, mantenha essa opção desmarcada.

**2. Seleciona condição de pagamento na geração do pedido de NF/Recibo**

Quando essa opção estiver marcada, a tela de geração do pedido de NF/Recibo exibirá o campo para seleção da condição de pagamento. Isso permite que o usuário mude a condição de pagamento acordada com prestador. 

**3. Condição de Pagamento (Gestão Estoque, Compras e Faturamento)**

Defini qual será a condição de pagamento padrão utilizada como sugestão no momento de realizar a integração com o Backoffice.

## **08. PARÂMETROS DO REPASSE CONVÊNIO**

Para configurar os parâmetros de repasse do Particular, acesse **Ambiente > Parâmetros > Gestão Hospitalar** e navegue até as opções **Faturamento > Repasse Convênio**.

**1. Repasse será feito somente para o grupo de prestadores (se o médico pertencer à um grupo)**

Indica que o pagamento do repasse será feito somente ao grupo do prestador. 

**2. Ordenar relatórios por**

Informa qual será a forma de ordenação do relatórios do repasse.

Importante!

Esse parâmetro é utilizado exclusivamente pelos relatórios da **MDI Antiga**. Para os relatórios desenvolvidos na nova MDI, a ordenação pode ser ajustada diretamente nos relatórios utilizando o **RM Reports** ou **Smart View**, conforme necessário.

**3. Parâmetro:** **Liberação de Repasse**

Nesse painel são definidas as regras para liberação de repasse podendo ser uma das opões:

* + **Controlado pelo Usuário**: Existe um usuário que controla o repasse e este usuário vai fazer todo o processo de liberação.
  + **Quando Gerar o Faturamento**: O repasse só será liberado após a geração da fatura ou arquivo que será enviado ao Convênio.
  + **Quando Confirmar Recebimento**: O repasse será realizado após recebimento.
  + **Quando Confirmar Recebimento com prazo definido para pagamento**: Quando essa opção estiver ativa, o sistema realizará o pagamento de acordo com as regras predefinidas. Caso utilize essa opção, é necessário configurar as regras no parâmetro **Dias de Liberação do Repasse**, para mais detalhes, consulte o tópico correspondente na documentação para orientações completas sobre a sua configuração.

## **09. PARÂMETRO DIAS DE LIBERAÇÃO DO REPASSE**

Informação

Esta configuração só será ativada quando o parâmetro **Liberação de Repasse** estiver definido como *'***Quando Confirmar Recebimento com prazo definido para pagamento**

Para que a aba seja exibida, você precisará primeiro salvar as configurações e depois reabrir o assistente de parâmetros.

Esse parâmetro será utilizado para informar os dias de recebimento e o prazo em dias para liberação após o recebimento.

O sistema calculará a liberação do pagamento com base na data atual, identificando a regra com a data mais próxima e somando o dias configurados para determinar a data final de pagamento.

Essa configuração afetará várias rotinas, incluindo:

* + **Repasse > Processos > Liberar Repasse**: Ao abrir a tela do processo, a **data de previsão de pagamento** não será preenchida automaticamente. Em vez disso, será aplicada a regra definida para os **dias de liberação**.
  + **Gestão de Glosa > Controle de Glosa**: A configuração influenciará o tratamento de glosas, seja por **glosa por conta**, **glosa total** ou **liberação automática**.

Exemplo: No dia 01 do mês X, há duas regras definidas. A regra mais próxima da data atual é a de recebimento até o dia 03. Nesse caso, a liberação ocorrerá após o 5º dia a partir da data de hoje (01). Portanto, a próxima data de liberação será no dia 06 (5 + 1).

## **10. PARÂMETRO DIAS DE PAGAMENTO DO REPASSE**

Atenção!

Esta configuração só está disponível nas versões antigas Delphi, não tendo sido migrada para a nova MDI devido à sua baixa adoção.

Este parâmetro automatiza o pagamento aos prestadores de acordo com os parâmetros configurados.

Para que essa parametrização fique ativa, é necessário que todos os prestadores que recebem repasses devem estar devidamente configurados, informando a forma de pagamento e dias de fechamento e liberação

**Se algum prestador não estiver configurado, **o pagamento automático não ocorrerá** para nenhum prestador.**

## **11. INTEGRAÇÃO BACKOFFICE**

No **TOTVS Gestão Hospitalar** em **Ambiente/Parâmetros/Integrações/Integrações Backoffice** são configurados parâmetros de Integração. Em **Folha de Pagamento de Prestadores**, são configurados movimentos para Pessoa Física e Jurídica (definindo o movimento a pagar e o movimento a receber) e qual o produto do tipo de movimento.

## **12. FOLHA DE PRODUÇÃO**

Na **Elaboração de Contas**, no ato do lançamento do item na conta do paciente o  sujeitos às regras de **Repasse**, que são apuradas e calculadas para a emissão de uma **Folha de Produção**.

Na **Elaboração de Contas**, são lançados os itens na conta do paciente. Todos os itens lançados nessa etapa têm suas regras de repasse apuradas e calculadas, permitindo a emissão de uma **Folha de Produção**.

A **Folha de Produção** é gerada por meio da funcionalidade descrita abaixo. A tela de geração da folha inclui parâmetros que permitem a criação de um **Relatório de Folha de Produção customizado**, conforme as necessidades do usuário.

**Gerando a Folha de Produção:**

1. No **TOTVS Gestão Hospitalar** acesse **Faturamento/ Repasses/Folha de Produção**.
2. Utilize os filtros para visualizar todos os lançamentos: Somente já recebidos ou Somente a receber.
3. Informe o Período de Execução do item.
4. Selecione um Prestador clicando no ícone de pesquisa (raio) ou marque a caixa **Todos os Prestadores**.
5. Selecione um Convênio clicando no ícone de pesquisa (raio) ou marque a caixa **Todos os Convênios**.
6. No painel **Tipo** selecione qual item deseja na folha de produção.
7. Marque a opção **Inclui Procedimentos dos Grupos dos Prestadores** para que sejam exibidos os repasses do Prestador selecionado e do grupo do prestador.

## **13. ELABORAÇÃO DE CONTAS**

Na **Elaboração de Contas**, durante o lançamento de itens na conta do paciente, ao selecionar o Prestador, se ele for credenciado diretamente no Convênio, o repasse será direcionado automaticamente para ele. Caso o Prestador esteja relacionado a um **Grupo de Prestadores**, será necessário informar se o repasse será direcionado para o **Grupo** ou para o **Prestador** individualmente.

Para que o Prestador receba o repasse, é essencial que, no cadastro do Prestador (**Cadastros > Uso Geral > Prestador**), esteja configurada a opção de **recebimento de repasse**.

Caso necessário, é possível realizar o **Redirecionamento de Repasse**. Essa funcionalidade permite indicar que o repasse será direcionado para outro Prestador. Para isso, basta clicar com o botão direito sobre o item desejado e selecionar a opção **“Redirecionamento de Repasse”**.

Informações

Itens lançados na conta do paciente através do Prontuário Eletrônico ou através do Registro de Informação de Cirurgia também passam pelo processo de Repasse.

## **14. REPASSE DE HONORÁRIOS MÉDICOS**

No **TOTVS Gestão Hospitalar**, siga os passos abaixo para realizar o repasse de honorários médicos:

1. **Acesse a Rotina de Repasse**:

   * Navegue até **Faturamento > Repasses > Folha de Pagamento de Prestadores**.
2. **Selecione o Prestador e Convênio**:

   * Escolha o **Prestador** para o qual será realizado o repasse.
   * Selecione o **Convênio** para pesquisar os repasses apurados ou marque a opção **Todos os Convênios**.
   * Clique em **Pesquisar**.
3. **Selecione os Repasses**:

   * Selecione os repasses apurados que serão pagos naquele momento ou marque a opção **Selecionar Todos**.
   * Informe a **data de previsão de pagamento** e clique em **Liberar** para liberar os itens selecionados.
4. **Ajustes na Guia Créditos/Débitos/Descontos**:

   * Utilize a guia **Créditos/Débitos/Descontos** para realizar ajustes necessários antes do pagamento efetivo.
   * Clique em **Incluir**.
   * Selecione o tipo de acordo (**Crédito**, **Débito** ou **Desconto**).
   * Informe o **Valor**, a **Data** e o **Histórico**.
   * Clique em **Gravar**.
5. **Liberação para Pagamento**:

   * Informe a **data de previsão de pagamento** e clique em **Liberar**.
   * Na guia **Liberado para Pagamento**, selecione os itens que serão efetivamente pagos. Os valores ajustados na guia **Créditos/Débitos/Descontos** serão calculados automaticamente.
   * Informe a **data de liberação do repasse** e clique em **Gerar** para gerar um comando de pagamento.
6. **Consulta de Pagamentos**:

   * Na guia **Pagamentos**, são listados todos os pagamentos efetuados para o prestador selecionado.
   * Para cancelar um pagamento, clique em **Retornar para Correção**.
7. **Relatório de Liberados**:

   * Para gerar um relatório com os prestadores que possuem lançamentos liberados para pagamento, clique em **Liberados**.
   * Os itens serão exibidos na guia **Liberado para Pagamento**.

## **15. REPASSE POR INDICAÇÃO**

No **TOTVS Gestão Hospitalar**, siga os passos abaixo para configurar e gerenciar o repasse por indicação:

1. **Acesse a Configuração de Critério de Repasse**:

   * Navegue até **Cadastros > Outros Cadastros em Faturamento > Critério Geral de Repasse**.
   * Nessa tela, serão realizadas as parametrizações necessárias para o repasse por indicação.
2. **Observação Importante**:

   * Atualmente, o sistema permite o repasse por indicação **apenas antes do cliente realizar o controle de glosa**. Após o controle de glosa ser realizado, os valores não aparecerão mais na tabela.
   * Os valores relacionados ao repasse por indicação só poderão ser consultados por meio de **relatórios** ou **consultas SQL**.
