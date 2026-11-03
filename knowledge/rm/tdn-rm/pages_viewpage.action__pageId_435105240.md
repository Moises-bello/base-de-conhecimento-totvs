---
content_hash: a89838b6c5bbb19943f66c14902b88d1324edcf361ec7a92253102223c5fb635
fetched_at: '2026-06-29T00:09:49.130306+00:00'
page_id: '435105240'
product: rm
source: tdn-rm
title: Totvs Incorporação - Parâmetros - Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105240
version: 30
---

**Índice**

---

#### **Geral 1/2**

* **Utilizar Módulo de Aluguel:** CheckBox responsável por exibir ao usuário o menu Aluguel.

#### **Geral 2/2**

* **Habilita uso do App nos contratos:** Indica que o módulo de aluguel estará disponível para utilização no App Meu Imóvel.

Importante!Caso o usuário efetive contratos de locação que ultrapassem o numero de licenças disponíveis, o sistema irá informá-lo na abertura do módulo TOTVS incorporação que o número de licenças deve ser atualizado, num prazo de até três meses para que os usuários do Meu Imóvel e do Portal do Cliente não percam o acesso. 

#### **Imóvel**

* **Código da Administradora:** Responsável por atribuir uma Administradora padrão de um imóvel.
* **Código do Calendário:** Calendário padrão utilizado.
* **Cap Rate:** Este campo será utilizado para calcular o valor mensal de aluguel baseado no valor de venda do imóvel. Ao criar um imóvel a partir de uma subunidade, se o parâmetro Cap Rate a.m estiver preenchido, o cálculo do aluguel deve ser feito aplicando-se o % Cap Rate ao valor da subunidade definida na tabela de preços principal. O valor de aluguel será o default e poderá ser alterado no momento da inclusão.
* **Exemplo:** Caso o valor da subunidade seja R$ 200.000,00, e o valor de Cap Rate seja de 1 que representa 1%, o valor da subunidade gerada será de 1% de R$ 200.000,00, ou seja, R$ 2.000,00.

#### **Contrato de Locação**

* **Fórmula do Valor Final:** Fórmula utilizada para fazer o cálculo do valor final do contrato.
* **Utiliza Rateio Manual no Contrato de Locação:** Parâmetro que define o comportamento do Rateio por Centros de Custos  no Contrato de Locação.
* **Valor de Integração para descontos:** Parâmetro que define um valor de integração para armazenar os descontos gerados pelo aluguel. O lançamento no módulo de Gestão Financeira, terá o valor do desconto gravado como um valor de integração.
  + **Observação:** A ação para o valor de integração para desconto de alugueis deve ser **NADA**. O Módulo de Aluguéis já calcula o valor do lançamento abatendo o desconto, e caso a ação definida seja **"Descontar"**, o valor será descontado indevidamente em duplicidade, pois o TOTVS Gestão Financeira irá desconta-lo também. Esta parametrização é para o cálculo padrão do sistema. **O valor de integração de desconto é apenas informativo**.
* **Valor de Integração para resíduo:** Parâmetro que define um valor de integração para o resíduo que é calculado. O lançamento no módulo de Gestão Financeira, terá o valor do resíduo gravado como um valor de integração.
* **Valor de Integração para Aluguel em Dobro:** Parâmetro que define um valor de integração para o Aluguel em Dobro que é calculado. O lançamento no módulo de Gestão Financeira, terá o valor do Aluguel em Dobro gravado como um valor de integração.
  + **Observação:** A ação para o valor de integração para o Aluguel em Dobro do Contrato de Locação deve ser **ACRESCENTA.** O sistema não permite que seja inserido no parâmetro valores de integração com Ação **NADA** ou **DESCONTO**.
* **Permite o Contrato de Locação ter prazo indeterminado:** Este parâmetro permite que o campo "Final vigência" deixe de ser obrigatório no Contrato de Locação. Ao salvar um contrato sem informar a data final, o mesmo terá comportamento de prazo indeterminado.
  + **Observação:**
    - Quando marcada essa opção, o sistema impede que seja marcado a opção "Período do contrato" no parâmetro "Período de contabilização ". Pois para essa opção é necessário a Data de Final do Processo.
    - O sistema não permite desmarcar este parâmetro quando já houver Contratos de Locação configurados sem a data final de vigência, de forma a evitar inconsistências na base.
* **Usar a opção "Utiliza Cálculo Pro Rata" como default no campo "Modelo de cálculo" do Contrato:** Este parâmetro é um default para o campo **Modelo de Cálculo** localizado na aba Identificação do **Contrato de Locação**. Caso ele esteja marcado, ao criar um novo contrato de locação o campo **Modelo de Cálculo** estará com a opção **Utiliza Cálculo Pro Rata** selecionada. Caso o parâmetro esteja desmarcado, a opção selecionada será **Não Utiliza Cálculo Pro Rata.**
  + **Observação:**
    - Para os períodos de parcelas **Inicial** e **Final** o sistema utilizará **Mês Civil** e para os períodos das outras parcelas será usado o **Mês Comercial**.
      * **Qual a diferença entre Mês Civil e Mês Comercial?**
        + **Mês Civil:** Expressão existente no mercado financeiro e administrativo que considera todos os dias do mês, da forma real mesmo. Por exemplo, em fevereiro teremos 28 ou 29 dias. Sendo assim, o **Ano Civil** é considerado com 365 dias.
        + **Mês Comercial:** Considera que todos os meses tenham 30 dias, com isso, o **Ano Comercial** é considerado com 360 dias.
* **Não permitir que a deflação altere o valor da Parcela para menos que o valor original:** Se marcado, ao reajustar a correção monetárias e a mesma houver uma deflação, o sistema não permitirá que o valor da parcela fique menor que o valor original.
  + **Observação:** Caso haja "**Aditivo de alteração de imóveis do contrato**", que altere o valor dos imóveis e do contrato, este passa a ser o valor considerado como o valor mínimo para reajuste, caso o parâmetro acima esteja marcado.
* **Considerar para o cálculo Pro Rata o dia após a data do aditivo:** Uma vez marcado esse parâmetro, ao efetivar aditivos de **Exclusão de Imóvel** ou **Alteração dos imóveis do Contrato de Locação**, se for promovida alteração do valor do contrato, ela só será considerada na **data posterior a data dos aditivos**. Por default esse campo vem desmarcado.
* **DIMOB**
  + **Gerar o log do cálculo da ficha de locação - Tipo R02**: Esse parâmetro possibilita, no final da geração da DIMOB, verificar os valores brutos e os valores de comissão gerados para a DIMOB em determinada competência, facilitando a conferência dos valores.

#### **Evento Financeiro**

* **Permite múltiplos eventos financeiros do tipo luva para o mesmo contrato de locação:** Ao marcar esse parâmetro será possível associar a um contrato de locação, mais de um Evento Financeiro do Tipo Luva.
* **Data de Emissão dos Lançamentos Financeiros de Locação:** Esse parâmetro permite definir qual será a forma de geração da Data de Emissão dos lançamentos do Contrato de Locação. Possui as seguintes opções:
  + **Data de Vencimento:** A data de emissão do lançamento será a data de vencimento do respectivo;
  + **Data da Geração:** A data de emissão dos lançamentos será a data em que eles foram gerados pelo sistema.
  + **Mês anterior vencimento:** A data de emissão do lançamentos será a data do vencimento do respectivo subtraído um mês. Dessa forma a data de emissão será um mês anterior ao vencimento do lançamento;
  + **Início Vigência Contrato:** A data de emissão dos lançamentos será a data de Inicio de Vigência do Contrato. Dessa forma todos os lançamentos terão a mesma data;
  + **Primeiro dia Mês do Vencimento:** A data de emissão dos lançamentos será o primeiro dia do mês do vencimento do respectivo lançamento.
  + **Fim Período Competência:** A data de emissão dos lançamentos será a data do último dia do período de competência no qual o lançamento está associado;
    - **Observação:** Esse parâmetro somente é aplicado a eventos financeiros do tipo Locação. Dessa forma evento avulsos terão suas datas geradas conforme a Data de Vencimento, que é o comportamento padrão do sistema.
  + **1º dia da Competência** - Primeiro dia do mês da competência da parcela do contrato. Por exemplo: Parcela de 01/2024. A data de emissão será 01/01/2024.
* **Data de emissão dos lançamentos financeiros de Locação Complementar**: Define qual será a data de emissão dos lançamentos financeiros de locação complementar. São as seguintes opções:
  + **Data do vencimento** - data de vencimento do lançamento. A mesma é informada no cadastro de medição;
  + **Mês anterior ao vencimento** - um mês anterior à data de vencimento do lançamento. Por exemplo: data de vencimento igual a 15/02/2023. A  data de emissão será 15/01/2023;
  + **1º dia do vencimento** - primeiro dia do mês da data de vencimento do lançamento. Por exemplo: data de vencimento igual a 15/02/2023. A  data de emissão será 01/02/2023;
  + **Data da geração** - data do sistema no momento da execução do processo que irá gerar os lançamentos;
  + **Data da medição** - data informada no cadastro de medição;
  + **1º dia da competência** - primeiro dia do mês da competência informada na medição do faturamento. Por exemplo: competência igual a 01/2023. A data de emissão será 01/01/2023.
  + **Último dia da competência** - último dia do mês da competência informada na medição do faturamento. Por exemplo: competência igual a 01/2023. A data de emissão será 31/01/2023.
* **Data de emissão para todos os tipos de eventos financeiros avulsos.(Exceto Locação e Locação Complementar)**: Define qual será a data de emissão dos lançamentos financeiros avulsos. São as seguintes opções:
  + **Data do vencimento:** A data de emissão do lançamento será a data de vencimento do respectivo;
  + **Data da geração**: A data de emissão dos lançamentos será a data em que eles foram gerados pelo sistema;
  + **Mês anterior ao vencimento:**  A data de emissão do lançamentos será a data do vencimento do respectivo subtraído um mês. Dessa forma a data de emissão será um mês anterior ao vencimento do lançamento;
  + **Início Vigência Contrato:** A data de emissão dos lançamentos será a data de Inicio de Vigência do Contrato. Dessa forma todos os lançamentos terão a mesma data;
  + **1º dia do** **Vencimento:** A data de emissão dos lançamentos será o primeiro dia do mês do vencimento do respectivo lançamento.

* **Data de emissão para o fundo promocional**: Define qual será a data de emissão dos lançamentos financeiros oriundos do processo de fundo promocional. São as seguintes opções:
  + **Data do vencimento:** A data de emissão do lançamento será a data de vencimento do respectivo;
  + **Data da geração**: A data de emissão dos lançamentos será a data em que eles foram gerados pelo sistema;
  + **Mês anterior ao vencimento:** A data de emissão do lançamentos será a data do vencimento do respectivo subtraído um mês. Dessa forma a data de emissão será um mês anterior ao vencimento do lançamento;
  + **Início Vigência Contrato:** A data de emissão dos lançamentos será a data de Inicio de Vigência do Contrato. Dessa forma todos os lançamentos terão a mesma data;
  + **1º dia do****Vencimento:** A data de emissão dos lançamentos será o primeiro dia do mês do vencimento do respectivo lançamento.
  + **1º dia da Competência** - Primeiro dia do mês da competência da parcela do fundo promocional. Por exemplo: Parcela de 01/2024. A data de emissão será 01/01/2024.

#### **Contabilidade**

Foram criados os seguintes parâmetros para possibilitar flexibilização e automatização dos processos:

* **Habilitar integração contábil:** Define se o módulo de aluguel irá exibir e processar as opções referentes à integração contábil.
* **Contabilização Automática:**
  + Quando habilitada, a contabilização automática realizará os seguintes tratamentos e ajustes de parâmetros:
    - Será bloqueado, na tela de edição do contrato de locação, o campo "Período de contabilização do contrato".
    - Define o parâmetro "Período de contabilização do contrato", marcando a opção "Todo período do contrato".
    - Bloqueia o parâmetro "Permite editar período no contrato", deixando-o também desmarcado.
  + Quando desabilitada, a contabilização:
    - Não irá disparar a contabilização automaticamente, junto aos processos e nem mesmo exibir telas para executar a contabilização ao término de tais processamentos.
    - Permanecerá desbloqueado, na tela de edição do contrato, na criação ou edição de um contrato de locação, o campo **"Período de contabilização do contrato"**.
    - Desbloqueia o parâmetro **"Permite editar período no contrato"**, deixando-o também marcado.
    - O usuário poderá realizar a contabilização manualmente ou por agendamento.
    - Não irá interferir na exclusão da contabilização, onde os lançamentos **serão excluídos automaticamente ao reabrir o contrato (desfazer a efetivação do contrato de locação)**. Porque se o contrato estiver "Em preparação" não existe nada para ser contabilizado e não existe garantia que o contrato será efetivado novamente.
* **Exibe tela de contabilização:** Define se irá exibir ou não a tela da contabilidade, com prévia da contabilização e possibilidade de alterar o evento contábil e cancelar o processo de contabilização (se houver permissão).
  + A tela de contabilização será exibida para processamentos em lote, para cada período mensal a ser contabilizado do contrato de locação. (Exemplo: marcar vários contratos de locação)
  + A tela de contabilização deverá tratar as permissões do usuário, no que diz respeito à data de contabilização, alteração de evento, editar a contabilização.
* **Período de contabilização do contrato:** Irá definir o parâmetro default para a definição do período das contabilizações dos contratos:
  + **Todo período do contrato**: considera a data inicial de contabilização, definida no parâmetro "Data para início da contabilização" do contrato de locação.
  + **Informar período:** exibir a tela para selecionar qual o período será contabilizado. Mesmo que o usuário informe data inicial menor que a **"Data para início da contabilização"** o sistema sempre respeitará o parâmetro e não permitirá contabilizações em períodos inferiores, gerando os lançamentos contábeis apenas a partir da data parâmetro.
  + **Bloqueia edição do período no contrato:** Caso seja marcado, irá bloquear, na tela de edição do contrato, o campo usado para definir o tratamento da contabilização "Período de contabilização do contrato" e o contrato será criado com o valor default definido para este campo, nos parâmetros da coligada.

#### **Integração Portais**

Estes parâmetros estão disponíveis a partir da versão 12.1.28 e serão responsáveis pela definição do preenchimento do header (obrigatório) do arquivo .xml que será utilizado na [integração com o portal Zap Imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=538492830)

* Responsável pelo desenvolvimento do arquivo
* Contato responsável pelo desenvolvimento do arquivo
* Telefone do responsável pelo desenvolvimento do arquivo
* E-mail do responsável pelo desenvolvimento do arquivo

#### **Renegociação de Contrato**

Estes parâmetros do sistema estão disponíveis a partir da versão 12.1.29, possibilitam configurar como os recursos de Renegociação de Contrato de Aluguel serão utilizados no Portal do Cliente e no aplicativo Meu Imóvel. Veja abaixo maiores detalhes destes recursos:

* **Utiliza regra de vencimento do contrato de locação:**Este parâmetro determina se irá utilizar a regra de vencimento do contrato de locação. Quando o parâmetro é marcado o parâmetro "Número de dias corridos para o primeiro vencimento" será desabilitado.
  + **Número de dias corridos para o primeiro vencimento:**Neste campo é preciso informar a quantidade de dias corridos para o primeiro vencimento. Somente estará disponível caso não utilize  o parâmetro da regra de vencimento do contrato de locação.
* **Termo da Renegociação**: Neste campo deveremos preencher o relatório que possui os termos da renegociação, que será apresentado na visão de renegociação ao realizar uma proposta no Meu Imóvel e no PDC.
* **Classificação para documentação do termo de renegociação**: Neste campo é preciso informar uma classificação de documentação, para que a documentação do termo de renegociação seja associada e posteriormente exibida nos contratos de aluguel.
* **Número máximo de parcelas:**Neste parâmetro é informado o número máximo de parcelas para a renegociação.
* **Motivo do aditivo:** Neste parâmetro é informado o motivo do aditivo que será gerado pelo Aplicativo no momento da solicitação de uma renegociação.

#### **Controle de Faturamento**

**Habilita controle de faturamento:** Este parâmetro habilita o controle de faturamento. É importante frisar que, quando este parâmetro estiver marcado, toda a inclusão de faturamento diário estará sujeita a periodicidade, tolerância e dia base listados abaixo. Ou seja, somente será possível incluir faturamento para os dias liberados através do processo de liberação. Com o parâmetro desmarcado o sistema irá permitir a inclusão de faturamentos diários em qualquer período.

**Parâmetros para bloqueios de períodos**

* **Tolerância**: A tolerância em dias, até que ocorra o bloqueio de período num número de dias corridos. Ou seja, se tenho 2 dias de tolerância, continuarei com o período anterior em aberto até dois dias antes do bloqueio ser efetivado. No dia base, fecharei o período anterior e irei liberar o novo, baseado no dia base e na periodicidade.
* **Dia Base para Bloqueio:** O dia base, ou data base da semana que irá ocorrer o bloqueio dos períodos. Exemplo: Se defino meu dia base para toda segunda-feira e executo o processo de liberação de período, toda a liberação será a partir da segunda feira, de acordo com a periodicidade abaixo e a tolerância definida.
* **Periodicidade:** A periodicidade, baseada no dia base, que será efetivo o bloqueio.

[Voltar](http://tdn.totvs.com/pages/viewpage.action?pageId=435105436)
