---
content_hash: 563604b489b9af6195c7508cfb3c9160da802bfb26bffee54f6258adb57c4b71
fetched_at: '2026-06-29T00:09:49.463417+00:00'
page_id: '435105296'
product: rm
source: tdn-rm
title: Contratos - Contratos de Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+-+Contratos+de+Venda
version: 25
---

* **Identificação:**Nesta pasta, serão informados os dados que identificarão a Venda/Aluguel cadastrada. Campos a serem preenchidos:

* + trueInfo-CircletrueredTipo Contrato: Nesta opção o usuário irá selecionar se contrato será uma Venda ou um Aluguel.redINLINEA partir da versão 12.1.31 não será possível incluir contratos do tipo Aluguel na visão de contratos de venda. Esse cadastro será feito exclusivamente pelo novo módulo de Aluguel.
  + **Situação:** Este campo é controlado pelo sistema e informa a situação que a venda está naquele momento. As situações podem ser:

* + Em Preparação: 1ª situação da venda;
  + Efetivada: como o próprio nome diz, quando a venda já foi efetivada;
  + Quitada: situação alterada automaticamente quando a última parcela do plano de financiamento é quitada;
  + Cancelada: quando a venda foi distratada por um dos seguintes motivos: Cancelada / Distrato Bilateral / Distrato Unilateral / Outros / Inadimplência / Desistência.Bloqueada: esta é a única situação que o sistema não controla, ou seja, o usuário coloca uma venda como bloqueada e automaticamente a sub-unidade também fica bloqueada.

* + **Núm Venda:** Informe o Número da venda cadastrada.

O número da venda será sequencial ou não, dependendo da parametrização do sistema. Caso o parâmetro "Venda Sequencial" Menu Opções | Parâmetros | RMSGI | Contrato | Venda/Aluguel, esteja marcado, ao criar a venda, o sistema incluirá um número de venda, caso o parâmetro esteja desmarcado, o usuário deverá informar um número de venda;

* + **Núm. do Contrato:** Após a efetivação da venda e a geração do contrato neste campo aparece o número referente ao contrato.

Este campo não pode ser editado. Ele somente irá mostrar o número do contrato depois que ele for gerado.

* + **Cód. Cliente:** Informe o código do cliente que está no cadastro de Clientes. Neste campo, não será apresentado uma lista dos códigos dos clientes.

Este campo é preenchido automaticamente após preencher o campo Nome Cliente.

* + **Empreendimento:** Selecione o empreendimento da venda/aluguel.
  + **Cód Vendedor Pessoa Jurídica:** Informe o Código ou Nome do vendedor Jurídico da venda. Na lista de opções serão apresentados todos os vendedores cadastrados através do Menu Cadastro | Vendedores | Pessoa Jurídica;
  + **Cód Vendedor Pessoa Física:** Informe o Código ou Nome do vendedor Físico da venda. Na lista de opções serão apresentados todos os vendedores cadastrados através do Menu Cadastro | Vendedores | Pessoa Física;
  + **Cód Modalidade:** Selecione a Modalidade que será utilizada na venda. Na lista de opções serão apresentadas todas as modalidades cadastradas através do Menu Cadastro | Condições da Venda | Modalidade Venda;

Ao incluir ou editar um contrato de locação o usuário possa optar por preencher ou não o campo "Modelo de Contrato";  
A edição apenas é permitida para contratos com Situação igual a "Elaboração";  
Se o parâmetro "Não associar modalidades a Empreendimento", através do Menu Opções | Parâmetros | RM SGI | Contratos | Empreendimentos, estiver desmarcado, só ira ser apresentado na lista de opções as modalidades que foram associadas ao Empreendimento através do Menu Cadastro | Empreendimento, na aba Associação de Modalidade.

* + **Cód Conta Caixa:** Informe qual Conta Caixa será utilizada na venda que fará integração com o RM Fluxus.

* **Datas:**

* + **Data Venda:** Informe a data em que a venda foi criada.

Se o parâmetro "Usar data do sistema para a data da venda", através do Menu Opções | Parâmetros | RM SGI, estiver marcado, ao criar uma venda, este campo será preenchido automaticamente com a data do sistema.

* + **Data do Cancelamento:** Caso a venda esteja com a situação cancelada, o sistema irá mostrar neste campo a data do cancelamento;
  + **Data Base:** É a data base que o sistema irá tomar como padrão para efetuar as correções do plano de financiamento.
  + **Data da Inclusão:** Campo preenchido automaticamente pelo sistema com a data atual do sistema no dia em que foi realizada a inclusão da venda;
  + **Data de Entrega das Chaves:** Informe a data que o cliente receberá as chaves do seu imóvel.
  + **Data da Assinatura:** Informe a data de Assinatura desta venda.
  + **Data Previsão Entrega:** Informe a data de previsão de entrega da subunidade desta venda.
  + **Referência de Entrega do para o componente existem quatro opções, são elas:**
  + **Data da Entrega do Empreendimento:** Se marcado, determina que a data de entrega do empreendimento será a referência para as correções.
  + **Data do Habite-se:** Se marcado, determina que a data do habite-se será a referência para as correções.
  + **Data da Entrega da Chave:** Se marcado, determina que a data da entrega das chaves será a referência para as correções.
  + **Data da Assinatura:** Se marcado, determina que a data da Assinatura será a referência para as correções.

* **Valores de Contrato:**

* + **Valores Negociados Inicialmente:**

* + - **Valor da Venda:** Valor do contrato definido no campo Valor do Item no cadastro do item da Venda/Aluguel.
    - **Valor do Desconto:** Valor do desconto definido no campo Valor Desconto no cadastro do item da Venda/Aluguel, para o caso de ter algum desconto na subunidade.
    - **Valor Total Financiado:** Este campo mostra a soma dos valores de financiamento do contrato. Estes valores são buscados do Plano de Financiamento.

* + **Valores Atualizados:**

* + - **Valor Atualizado:** É Valor da Venda atualizado por meio de reajustes e aditivos, Este valor considera o seguinte aspecto em relação às *Parcelas Quitadas*:
      * O sistema sempre considera o Valor Total pago pelo cliente, portanto, se a parcela foi paga em atraso, os valores de Juros e Multa, calculados pelo módulo Financeiro, serão considerados na composição deste *Valor Atualizado*.

* + - **Valor do Desconto:** Soma dos valores de desconto atualizados.
    - **Total baixado da venda/aluguel:** Soma de todos os valores baixados no contrato.

* + **Saldo Devedor Atual:** Soma de todos os valores em aberto restantes do contrato.
  + **Baixado (%):** Representação gráfica que mostra a soma de todos os valores baixados no contrato.

* **Item do Contrato:**Nesta aba deverá ser cadastrado o Item de Contrato utilizado na Venda/Aluguel. Campos a serem preenchidos:

* + **Empreendimento:** Traz o código e o nome do empreendimento que foi cadastrado na Venda.
  + **Observação:** Este campo não poderá ser editado, pois o empreendimento já foi cadastrado na pasta Identificação.
  + **Unidade:** Informe a Unidade a ser cadastrada.
  + **Sub-Unidade:** Informe a Sub-Unidade a ser cadastrada.
  + **Valor Sub-Unidade:** Informe o valor da Sub-Unidade.
  + **Observação:** Este campo será preenchido automaticamente de acordo com o valor cadastrado para esta sub-unidade. Este campo poderá ser modificado.
  + **Desconto Sub-Unidade:** Informe o valor do desconto da Sub-Unidade, se houver.

* **Plano de Financiamento**: Para gerar o Plano de Financiamento, é necessário entrar no Processo . Após a geração do Plano de Financiamento, será apresentado os dados nas seguintes abas:

* + **Condições de Venda:**Serão apresentados os componentes da regra do Plano de Financiamento.
  + **Consultar Log:** Nesta opção, iremos verificar o histórico das alterações realizadas em cada componente da regra.
  + **Consultar Reajustes Mensais:** Nesta opção, será apresentado todo o histórico do Contrato por data de alteração, quais foram os valores de Juros e Correção Monetária calculados, descontos concedidos e valores baixados.
  + **Plano de Financiamento:**Será apresentado o Plano de Financiamento, de acordo com os componente da Condições de Venda. Após a geração do Plano, poderemos realizar as seguintes Alterações:

* **Edição de Parcelas:**A opção Edição de Parcelas permite que você altere dados de uma Parcela já existente. Essa edição só é permitida em Vendas 'Em Preparação', que tenha o Plano de Financiamento Gerado e que ainda não tenha realizado a integração com o Financeiro. Este Processo permite funcionalidades como:

* + Inclusão, alteração e exclusão de Componentes na Parcela, atualizando o valor desta parcela consequentemente.
  + Alteração do Valor do Componente e Alteração da Data de Vencimento da Parcela.
  + Permite alterar o Centro de Custo, o Departamento e as Tabelas Opcionais da Parcela.
  + Inserir um comentário em cada componente para descrever a alteração a ser realizada.

O componente gerador da parcela não poderá ser excluído ao editar a parcela;  
Não é possível inserir componentes de reajuste na parcela;  
Parcela com juros pré-fixados, ao alterar a data de vencimento manualmente, não terá seu recálculo de juros efetuado.

* **Alterar Tipo Receita:**Esta opção permite alterar ou incluir um novo Tipo de Receita para a parcela selecionada. Ao selecionar o Tipo Receita = 'Nota Promissória', o Sistema mostra a ultima Nota Promissória utilizada no Plano de Financiamento e é habilitado na visão o Campo 'Nota Promissória', onde é informado o número da Nota Promissória da parcela com a opção de alterar este número. Para saber maiores informações sobre **Nota Promissória**.

Ao selecionar o Tipo Receita = 'Bens Diversos', o Sistema habilita o campo 'Bem', onde é permitido associar a parcela os Bens que foram cadastrados no sistema e associados a Subunidade da Venda.

* **Visualizar Lançamentos Filhos:**Esta opção permite visualizar as parcelas selecionadas e seus respectivos lançamentos filhos, ou seja, parcelas que foram criadas por ter sido realizado uma baixa parcial no Financeiro. Este processo só será habilitado quando selecionado uma parcela baixada parcialmente.
* **Consultar Log:** Nesta opção, iremos verificar o histórico das alterações realizadas em cada Parcela, com uma descrição dos cálculos realizados e os valores de cada componente da parcela.
* **Consultar Reajustes Mensais:** Nesta opção, será apresentado todo o histórico do Contrato por data de alteração, quais foram os valores de Juros e Correção Monetária calculados, descontos concedidos e valores baixados.
* **Componentes da Parcela:**Será apresentado as parcelas do Plano de Financiamento com os seus componentes de cada parcela, onde poderemos visualizar os seus valores e valores já baixados. Nesta aba teremos as mesmas opções de alterações da aba Plano de Financiamento.
* **Contabilidade:** A aba **Contabilidade** está localizada na edição de Venda/Aluguel, sendo que a mesma possui as seguintes sub-abas:
* **Venda/Aluguel:** Nesta aba, o usuário deve informar o evento contábil usado para contabilizar a inclusão de Vendas/Aluguéis.
* **Entrega de chave:** Nesta aba, o usuário informa o evento contábil para contabilizar a entrega de chaves e informa também o Valor entrega chave. A contabilização de entrega de chave só é possível após a efetivação da Venda/Aluguel.
* **Eventos no reajuste:** Esta aba possibilita a inserção de dois eventos, através dos campos Evento reajuste (Inflação) e Evento reajuste (Deflação).

Novidade

Agora é possível alterar os campos referentes a eventos contábeis de Aditivos e Distrato quando uma venda estiver na situação de Distratada para facilitar a contabilização após a efetivação do distrato da venda.

A partir da versão 11.40, para visualizar os dados contabilizados, o usuário deverá abrir Anexos | Contabilidade e as opções Consultar Operação Contábil da Venda/Aluguel ou Consultar Operação Contábil da Entrega das Chaves na tela de edição de Vendas/Aluguéis.  
A partir da versão 11.40, os processos de Efetivação de Vendas/Aluguéis, Aditivo, Distrato e Reajuste existe a possibilidade de Recontabilização e Estorno Contábil dos lançamentos já integrados. A seguir veja os passos para realizar o estorno em cada um desses processos:

* **Efetivação de Vendas/Aluguéis**: Deve-se voltar a situação da Venda/Aluguel, efetivar o mesmo novamente e no momento da efetivação informar os novos dados contábeis. Após a efetivação será criado um lote de estorno contendo os lançamentos da venda ou aluguel em questão.
* **Aditivo**: Deve-se acessar o processo de Aditivos em Anexo | Aditivos, em seguida editar o aditivo que deseja recontabilizar, abrindo o processo Recontabilizar. Com isso é preciso informar os novos dados contábeis. Após a recontabilização será criado um lote de estorno contendo os lançamentos do aditivo contabilizado na primeira vez.
* **Distrato**: Deve-se acessar o processo de Distrato em Anexo | Distrato Contratual, em seguida editar o distrato que deseja recontabilizar, abrindo o processo Recontabilizar. Com isso é preciso informar os novos dados contábeis. Após a recontabilização será criado um lote de estorno contendo os lançamentos do distrato contabilizado na primeira vez.
* **Reajuste**: Para Recontabilizar o processo de Reajuste, deve-se usar o processo de Atualização da Data do Reajuste da Venda, realizar as alterações necessárias na Venda/Aluguel ou alterações de Cotações/alterações de Juros. Em seguida reajustar novamente, com isso será criado o lote de estorno da venda em questão.

Para saber maiores informações sobre Eventos Contábeis no TOTVS Incorporação .  
Para saber maiores informações sobre a contabilização no Novo Modelo de BackOffice clique aqui.  
Para a contabilização do módulo de aluguel, caso o "Evento Contábil" seja configurado para buscar o "Default Contábil" do cadastro do "Modelo do Contrato", e este não esteja definido no contrato a ser contabilizado, será exibida a mensagem "Não houve contabilização para o período 01/01/2016".

* **Motivo da Compra:**
  + **Investimento:** Quando o cliente adquire um imóvel com finalidade de investimento, o objetivo principal é obter retorno financeiro futuro.
  + **Uso Próprio:**Quando a compra é destinada para uso próprio, o imóvel será utilizado para moradia do cliente ou de sua família.
* **Campos Complementares:**A aba Dados Adicionais teve seus campos convertidos para esta aba de Campos Complementares. Com isso o cadastro de Tabelas Opcionais do TOTVS Incorporação foi excluído. Foram excluídos também os Parâmetros por Coligada referentes aos campos de Data Opcional e Tabela Opcional da Venda / Aluguel. Todos os campos que estão marcados para utilização na parametrização e que estavam na aba Dados Adicionais do cadastro de Venda / Aluguel serão movidos para a aba de Campos Complementares. Para cadastrar novos Campos Complementares para Vendas / Aluguel basta acessar Cadastros | Campos Complementares | Venda. O único campo fixo nessa aba é o campo Observação que estava presente na antiga aba de Dados Adicionais.

false

Informações Complementares

---

false

Como Fazer

---

* [Copiar Contrato](http://tdn.totvs.com/display/LRM/Copiar+Contrato)
false

Veja Também

---
