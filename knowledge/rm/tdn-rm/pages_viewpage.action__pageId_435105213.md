---
content_hash: 228ee9084fac1941f6767a2c4cc08a9d8541f7c6d135169badee052bb61c7783
fetched_at: '2026-06-29T00:09:48.658631+00:00'
page_id: '435105213'
product: rm
source: tdn-rm
title: Parâmetros - Contrato - Aditivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105213
version: 10
---

### **Etapa 1 - Parâmetros do aditivo**

* **Resíduo - Comportamento do resíduo em aditivos de troca de comprador:**Dentro do aditivo de troca de comprador, quando houver resíduo não gerado, é possível escolher o que será feito com este valor (se existir), após a efetivação do aditivo. As ações possíveis são as seguintes:
  + Impedir cancelamento
  + Incorporar resíduo ao novo comprador
  + Gerar parcela de resíduo
* **Renegociador - Distribuir via renegociador os valores dos componentes das parcelas nos componentes correspondentes: (O não preenchimento dos componentes, exceto o principal que é obrigatório, implica que não serão distribuídos os valores).**  É possível distribuir os valores das parcelas renegociadas em vários componentes, sendo que cada item que compõe a parcela será redistribuído no seu componente correspondente.
  + **Observação:** O Componente de CM não será distribuído, pois este será recalculado na parcela de destino através do reajuste online. O componente de Juros será apenas distribuído para os modelos pré-fixados, os demais serão recalculados na parcela de destino.
    - Por exemplo: Se uma parcela do Tipo Mensal, estiver em atraso e reajustada. Ao renegociar esta parcela é possível redistribuir os componentes de Juros (se for modelo de cálculo pré-fixado), Mora e multa, além do valor original. Cada um em componentes respectivos, como Juros antes aditivo, Multa antes aditivo, etc. Caso não for preenchido um dos componentes de Juros,  Mora e multa, então o valor será redistribuído apenas no valor principal - antes aditivo.
  + Os componentes disponíveis para distribuição são:
    - **Componente Principal - Antes aditivo (Obrigatório).**
    - **Componente Juros - Antes aditivo (Obrigatório para modelos de cálculo pré-fixados).**
    - **Componente Juros de Mora** - Antes aditivo.
    - **Componente Multa de Atraso** - Antes aditivo.
* **Efetivar Aditivo via Renegociador Global:** Será possível definir se o(s) aditivo(s) criado(s) através do [Aditivo Global de Renegociador](https://tdn.totvs.com/display/LRM/Aditivo+-+Aditivo+Global+de+Renegociador) será(ão) efetivado(s) automaticamente ou então será(ão) criado(s) "Em Preparação".
* **Evento contábil de aditivo de troca de subunidade:** Caso necessário, informe o evento contábil default para realizar a contabilização dos aditivo de troca de subunidade;
* **Usa mês comercial aditivo vencimento com cálculo em meses:** Marque esta opção caso queira que o cálculo do aditivo de alteração de vencimento seja realizado pelo mês comercial e não pelo mês civil, quando este estiver parametrizado para realizar o cálculo em meses.

### **Etapa 2 - Parâmetros do aditivo por coligada**

* **Plano de financiamento reajustado em memória na exibição de aditivos:** Quando habilitado muda o comportamentos dos aditivos chamando o reajuste do plano de financiamento somente em memoria ajustando os valores de acordo com a data do aditivo. Os tipos de aditivos afetados por este parâmetro são o de "Alteração de valor da parcela", "Alteração de vencimento", "Antecipação de parcela", "Prorrogação de vencimento" e o de "Renegociação de contrato"; Isso porque para as negociações que são realizadas neles é exibido em telas as parcelas em aberto do plano de financiamento. Ao realizar a efetivação do Aditivo, o reajuste em memória será gravado na base nas parcelas que foram alteradas.
* **Permite que os aditivos possam reduzir o Saldo Devedor:** Se esta opção for marcada, ao realizar um Aditivo que tenha alterações de valores, o sistema irá permitir a redução do saldo devedor do contrato. Com o parâmetro desmarcado, não poderemos reduzir o saldo devedor nos Aditivos que tenham alterações de valores, somente poderemos aumentar.
  + **Observação**: O Aditivo de Antecipação de Parcelas fica indisponível caso esteja parametrizado para não permitir redução no saldo devedor, pois ele sempre gera um valor de desconto e consequentemente redução de valor do saldo devedor.
* **Permite que os aditivos possam determinar o congelamento da parcela:** Ao marcar esta opção, será habilitado os 4 parâmetros abaixo para seleção.
  + Na tela de cada tipo de aditivo relacionado a estes parâmetros de sistema existira também um checkbox com mesma finalidade, veja então como funciona esta hierarquia de parametrização:
  1. 1. Se o parâmetro de sistema estiver marcado, o checkbox da tela vem por default marcado e não permite desmarcar, ou seja, o administrador esta configurando o sistema para não permitir ao usuário do sistema decida se vai ignorar ou não a parcela nos reajustes.
     2. Se o parâmetro de sistema estiver desmarcado o checkbox vem por default desmarcado e permite marcar e desmarcar, ou seja, o administrador esta configurando o sistema permitindo que esta decisão seja tomada pelo usuário do sistema.

* + **Ignorar o reajuste em parcelas que tiveram o valor alterado por aditivo:** Quando habilitado muda o comportamento do aditivo do tipo "Alteração de valor da parcela", marca as parcelas que este tipo de aditivo modificou e após a efetivação todos os reajustes subsequentes desconsideram estas parcelas marcadas, ficando congeladas.  
          - No momento de criar o aditivo aparecerá uma coluna na grid de parcelas para marcar que é para ignorar o reajuste, para que se mantenha o valor alterado em componentes alterados pelo reajuste o usuário deverá marcar a caixa da coluna para a parcela desejada.
  + **Ignorar o reajuste em parcelas que tiveram o vencimento alterado por aditivo:** Quando habilitado muda o comportamento do aditivo do tipo "Alteração de vencimento", marca as parcelas que este tipo de aditivo modificou e após a efetivação todos os reajustes subsequentes desconsideram estas parcelas marcadas, ficando congeladas.
  + **Ignorar o reajuste em parcelas antecipadas por aditivo:** Quando habilitado muda o comportamento do aditivo do tipo "Antecipação de parcela", marca as parcelas que este tipo de aditivo modificou e após a efetivação todos os reajustes subsequentes desconsideram estas parcelas marcadas, ficando congeladas.
  + **Ignorar o reajuste em parcelas prorrogadas por aditivo:** Quando habilitado muda o comportamento do aditivo do tipo "Prorrogação de vencimento", marca as parcelas que este tipo de aditivo modificou e após a efetivação todos os reajustes subsequentes desconsideram estas parcelas marcadas, ficando congeladas.

### **Etapa 3 - Parâmetros globais do aditivo**

* **Permitir alterar o valor de Juros e Correção Monetária no aditivo de alteração de valor de parcela:** Se marcado, será possível alterar o valor de Juros e Correção Monetária.
* **Contabilizar sempre o aditivo de renegociação:** Mesmo que não haja diferença de valores na renegociação, o aditivo será contabilizado para que estes valores sejam redistribuídos nas contas contábeis. Os valores selecionados serão desfeitos na contabilização do evento deflacionário e refeitos com os valores renegociados no evento inflacionário. Como envolve dois eventos ao mesmo tempo na contabilização do aditivo, então não será exibida a tela de pré-visualização da contabilização. (Este parâmetro só está disponível para clientes com a base revitalizada).

### **Etapa 4 - Parâmetros do aditivo/acordo**

Ao marcar o parâmetro "Proporcionalizar no Renegociador", os componentes dos valores de integração das parcelas selecionadas serão proporcionalizados nas novas parcelas com os componentes abaixo. Se não preencher, o sistema buscará o primeiro componente que encontrar no cadastro.  Estão disponíveis para parametrização os seguintes componentes:

* **Componente CM Antes/Ambos (CM Antes Aditivo):** Informe o componente que irá receber o valor da CM Antes Entrega, no momento da execução do acordo ou do aditivo de renegociação do contrato;
* **Componente CM Após (CM Antes Aditivo):** Informe o componente que irá receber o valor da CM Após Entrega, no momento da execução do acordo ou do aditivo de renegociação do contrato;
* **Componente Juros (Juros Antes Aditivo):** Informe o componente que irá receber o valor da Juros Antes da Entrega, no momento da execução do acordo ou do aditivo de renegociação do contrato;

Os encargos financeiros serão distribuídos nos componentes correspondentes, se não preencher serão distribuídos no principal. Estão disponíveis para parametrização os seguintes componentes:

* **Componente Juros de Mora (Tipo Encargos):** Informe o componente que irá receber o valor dos Juros de Mora, no momento da execução do acordo ou do aditivo de renegociação do contrato;
* **Componente de Multa de Atraso (Tipo de Encargos):** Informe o componente que irá receber o valor da Multa de Atraso, no momento da execução do acordo ou do aditivo de renegociação do contrato;
* **Componente Desconto Financeiro (Tipo Desconto):** Informe o componente que irá receber o valor do Desconto Financeiro, no momento da execução do acordo ou do aditivo de renegociação do contrato;
