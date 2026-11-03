---
content_hash: 8569abdea78a21d5ae5449f2bea542dff17c12c756bf4f30799ad80e69eed7af
fetched_at: '2026-06-29T00:09:48.680854+00:00'
page_id: '435105217'
product: rm
source: tdn-rm
title: Alteração da data de Entrega
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105217
version: 11
---

**Alteração da data de Entrega**

---

Alteração da Entrega do EmpreendimentoData de Entrega

Na tela de Empreendimento existem dois botões que possuem a mesma funcionalidade, de alteração de data de entrega. Essa funcionalidade pode ser utilizada para alterar a Data de Entrega do Empreendimento ou a Data de Habite-se.

Ao acessar o processo temos os seguintes campos disponíveis:

**Data a ser alterada:** Informe qual a data será alterada, entrega do empreendimento ou habite-se.

**Deslocar a Data Base do Componente de Juros da Regra**: esta funcionalidade será utilizada para alterar a *Data Base* dos Componentes de Juros contratuais (juros com origem no TCGI) que é utilizada pelo sistema para calcular esses valores e que podem ser afetados na execução do processo de *Alteração da Data de Entrega*.

Ao marcar essa opção, o sistema irá validar as seguintes condições para ser aplicado:

* Se os *Componentes* de Juros contratuais estão configurados com o *Tipo de Correção Após Entrega* (XCOMPONENTE.TIPOENTREGACORRECAO) para *Após a Data de Entrega* ou *Ambos*; e
* Se os *Componentes* de Juros da*Regra de Financiamento* estão utilizando a *Data Base de Referência para Cálculo do Reajuste* como: *Data de Vencimento da Parcela*, *Data de Vencimento da 1a Parcela*, ou *Data Base do Componente*;

Caso ambas as condições acima não sejam atendidas, o sistema não aplicará essas alterações.

**Nova data de Entrega:**

* ### Alteração da Data de Entrega do Empreendimento – Novos Parâmetros

  Durante o processo de **alteração da data de entrega / habite-se do empreendimento**, é possível configurar o comportamento do sistema em relação às datas de vencimento dos contratos já gerados. Para isso, foram adicionados três novos parâmetros que controlam como a **prorrogação de vencimentos e datas-base de juros** será tratada:

  ---

  #### ✅ **1. Prorrogar o vencimento com a diferença entre a data base dos juros e a nova data de entrega / habite-se**

  + **Descrição:**  
    Ao marcar esta opção, o sistema irá **calcular a diferença de dias** entre a **data base dos juros** (informada na regra de financiamento) e a nova data de entrega/habite-se informada no processo.
  + **O que acontece:**  
    Essa diferença será **adicionada aos vencimentos do contrato**, empurrando as parcelas para frente, respeitando esse intervalo.
  + **Quando usar:**  
    Utilize esta opção quando você deseja manter o mesmo intervalo entre a **data base de juros** e os vencimentos, considerando que o empreendimento será entregue mais tarde.
  + **Exemplo prático:**  
    Se a data base dos juros era 01/01/2025 e a nova data de entrega é 01/03/2025 (diferença de 60 dias), todos os vencimentos serão ajustados **acrescentando 60 dias**.

  ---

  #### ✅ **2. Prorrogar o vencimento com a diferença entre a data do primeiro vencimento e a data de entrega/habite-se anterior**

  + **Descrição:**  
    Esta opção faz com que o sistema utilize a **diferença entre o primeiro vencimento do contrato** e a **data de entrega anterior**, para aplicar o mesmo intervalo com base na nova data de entrega.
  + **O que acontece:**  
    O primeiro vencimento será **recalculado** com base na nova data de entrega/habite-se, mantendo a distância que havia originalmente.
  + **Quando usar:**  
    Ideal quando a política da empresa é definir os vencimentos sempre a partir de uma **data fixa após a entrega**, independente da data base de juros.
  + **Exemplo prático:**  
    Se o primeiro vencimento era 01/05/2025 e a data de entrega anterior era 01/03/2025 (diferença de 60 dias), e a nova entrega é 01/06/2025, o novo primeiro vencimento será **01/08/2025** (mantendo 60 dias após a nova entrega).

  ---

  #### ✅ **3. Forçar a data do primeiro vencimento, a data base da regra e a data de entrega / habite-se com a data definida no processo**

  + **Descrição:**  
    Esta opção **força todos os marcos principais de data** do contrato (primeiro vencimento, data base dos juros e data de entrega) para a **mesma data definida** no processo de alteração.
  + **O que acontece:**  
    Não há cálculo de diferença ou prorrogação. O sistema **define diretamente a data informada** como sendo a nova referência para todos esses campos.
  + **Quando usar:**  
    Recomendado em casos onde a empresa deseja **padronizar todas as datas** a partir de uma nova entrega, zerando qualquer relação com datas anteriores.
  + **Exemplo prático:**  
    Se no processo você informar 01/12/2025 como a nova data de entrega, então:

    - Data de entrega = 01/12/2025
    - Data base dos juros = 01/12/2025
    - Primeiro vencimento = 01/12/2025

  ---

  ### 🔒 Observações Importantes

  + Os parâmetros **não são cumulativos**. O sistema considera **somente o parâmetro marcado** durante o processo.
  + A escolha de cada opção pode impactar **parcelas já geradas**, **cálculos de juros** e **relatórios financeiros**, por isso, recomendamos validar com a área financeira antes da aplicação.
  + Uma vez aplicadas, as alterações podem ser **irreversíveis**, especialmente em contratos já integrados com módulos financeiros ou contábeis.

**Motivo de Alteração de Data:** deve-se informar neste campo, que tem o seu preenchimento obrigatório, um descritivo do motivo da alteração da data de entrega, para fiz de histórico.

Prorrogação de Vencimento

Nesta aba deve-se marcar os tipos de parcelas quer terão o **vencimento prorrogado** após a nova data de entrega, caso seja necessário a prorrogação de vencimento de algum tipo de parcela (mensal, bimestral, trimestral, anual, balão, etc). Essa opção não é obrigatória.

Será possível escolher um ou mais dos tipos de parcelas cadastrados, e as vendas em que possuem este tipo de parcela selecionado, terão o seu vencimento prorrogado (virada do cálculo de Antes para Após a data de entrega).

**Regras para Alteração do Plano de Financiamento de Vendas com Alteração na Data de Entrega do Imóvel**

**Parâmetro: Considerar o Primeiro Vencimento a Data de Entrega/Chaves, utilizar?**

* Marcado: Quando não for juros PRICE e você deseja que os vencimentos da parcela acompanhe a **diferença de datas entra a data de entregue anterior e a data base do primeiro vencimento que fica na regra**, dessa forma , o sistema irá empurrar as datas seguindo o padrão de diferença anterior. Podendo ser positivo ou negativo a diferença.
* Desmarcado :  Quando o Juros de contrato com correção, tanto com o tipo de correção ambos (antes e após) a data de entrega, quanto com o tipo de correção apenas após essa data; e o tipo de data base deste componente for diferente da data da venda ou da data base da venda. Atendidas as condições, o sistema calculará a **diferença em meses entre a data base dos juros e a nova data de entrega do empreendimento**, para ajustar o vencimento das parcelas de cada uma das vendas afetadas. Se essas condições não forem atendidas para alguma das vendas, o sistema utilizará apenas a nova data de entrega. Caso a data de vencimento de alguma venda seja posterior à nova data de entrega, o sistema não realizará alterações nesta venda. A data de vencimento base do componente gerador de parcela e a data base dos juros do contrato das condições de financiamento só serão alteradas se a primeira parcela do plano ainda estiver em aberto.
