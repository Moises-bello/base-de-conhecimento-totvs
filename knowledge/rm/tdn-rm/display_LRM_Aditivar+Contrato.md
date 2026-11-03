---
content_hash: 9adc0fe20a0b9429849ac4e55071800775961fa12ef8b52444a3313d9877f688
fetched_at: '2026-06-29T00:09:49.446590+00:00'
page_id: '435105294'
product: rm
source: tdn-rm
title: Aditivar Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivar+Contrato
version: 2
---

**Aditivar Contrato**   
 Aditivo é uma opção do sistema para correção e alteração de contratos já efetivados devido a modificações solicitadas pelo cliente ou pela empresa.  
    
 Este processo deverá ser acessado através do Anexo do menu Vendas / Alugueis. Vale lembrar que só podemos criar Aditivos para vendas efetivadas e com o número do Contrato gerado.  
    
 Após a efetivação de qualquer Aditivo, além de atualizar as Parcelas no TOVS Incorporação e no TOTVS Gestão Financeira, o usuário poderá visualizar um histórico onde trará todas as alterações efetuadas. Este histórico está disponível como uma aba na edição do Aditivo.  
    
 O Aditivo terá etapas para a sua conclusão. Poderemos criar um Aditivo e o mesmo ficar em Preparação até que seja aprovado por um fluxo de aprovação e posteriormente ser concluído. O Aditivo será um anexo da Venda/Aluguel. O Fluxo de Aprovação é um recurso do produto TOTVS e é opcional a sua utilização.  
    
 As etapas do Aditivo são:  
    
 **Em Preparação:** Ao criar o Aditivo, o mesmo ficará com o status "Em Preparação", onde iremos cadastrar as Informações básicas como data do Aditivo, Descrição e selecionar o Tipo de Aditivo a ser executado. Poderemos selecionar mais de um tipo de Aditivo para ser executado simultaneamente e iremos cadastrar as informações de cada tipo de Aditivo.  
    
 **Efetivado:** Ao efetivar o Aditivo, o sistema irá perguntar se o mesmo será contabilizado e iremos informar o evento contábil. A efetivação do Aditivo consiste em realizar as alterações contratuais de cada tipo de Aditivo selecionado, efetuar a contabilização e incluir o histórico do Aditivo. Caso o Aditivo seja efetivado, não será possível desfazê-lo ou cancelá-lo.  
    
 **Cancelado:** Caso o Aditivo não esteja Efetivado, ele poderá ser cancelado.  
    
 Ao criar um novo Aditivo, será aberta a janela de Aditivos onde o usuário informa a Data do Aditivo, descrição e terá a sua disposição todos os tipos de aditivos, para que possam ser usados no processo.   
 Poderemos selecionar mais de um Tipo de Aditivo para execução. Logo abaixo, segue uma descrição de cada tipo.   
    
 **Observação:** Para gerar um aditivo é necessário que a venda possua um número de contrato, ou seja, que a venda já tenha o Plano de Financiamento gerado, esteja efetivada e gerado o contrato para a mesma. Também é necessário que as parcelas já estejam geradas no TOTVS Gestão Financeira.  
    
 Os Aditivos que tenham alterações de parcelas, sofrerão Reajuste do Plano de Financiamento em Memória até a data informada no Aditivo. Também será calculado os Juros de Mora e Multa de Atraso sobre este valor atualizado das Parcelas.  
 Este serviço de Reajuste do Plano de Financiamento em Memória será consumido também por um provider de dados, onde ficará disponível para o plano de financiamento que poderá ser reajustado pro-rata e exibido em relatórios.  
 **Observação:** este processo de reajuste nos Aditivos será executado somente se o parâmetro "Plano de financiamento reajustado em memória na exibição de aditivos" estiver marcado.  
    
    
 As alterações de contratos dividem-se nos seguintes tópicos:  
    
    
 **Alteração de Valor da Parcela**  
    
 Este tipo de aditivo permite que o usuário altere as parcelas do plano de financiamento de uma determinada venda.  
    
 Ao selecionar este tipo de Aditivo, será apresentado todas as Parcelas em aberto do plano de financiamento. O usuário poderá editar as parcelas onde será apresentado todos os componentes que compõe esta parcelas. Poderá ser informado um novo valor para cada componente e inserir novos componentes na parcela ou excluir componentes existentes.  
 **Observação:**

* Valores de multa de atraso e juros mora serão exibidos, más estes valores são meramente informativos e não fazem parte do valor da parcela.
* Componentes geradores de parcelas e componentes de reajustes não poderão ser inseridos nas parcelas.
* Não poderá ser excluído o componente que gerou a parcela. Ex: Mensal  
   **Ignorar Reajuste em parcela que houve alteração de valor após efetivação:** Ao marcar este parâmetro, as parcelas alteradas não serão mais reajustadas pelo sistema.  
   **Valor Parcelas Alteradas Atual:** Soma dos valores atuais das parcelas selecionadas que sofrerão alterações.  
   **Valor Parcelas Alteradas Novo:** Soma dos valores das parcelas selecionadas com as alterações.  
      
      
   **Alteração de Vencimento**  
      
   Este tipo de aditivo permite que o usuário altere a data de vencimento das parcelas do plano de financiamento de uma determinada venda.  
      
   Ao selecionar este tipo de Aditivo, será apresentado todas as Parcelas em aberto do plano de financiamento. O Sistema permite que o usuário selecione uma nova data para a Parcela desejada, selecionando um novo valor no Campo 'Novo Vencimento'.  
   **Observação:** Valores de multa de atraso e juros mora serão exibidos para que o usuário saiba de valores que poderá estar abrindo mão de cobrar. Uma vez efetivado este aditivo, este valores serão desconsiderados e não serão mais cobrados. O usuário esta aceitando alterar a data da parcela sem a necessidade de estar alterando ou atualizando nenhum valor da parcela.  
   **Ignorar Reajuste em parcela que houve alteração de vencimento após efetivação:** Ao marcar este parâmetro, as parcelas alteradas não serão mais reajustadas pelo sistema.  
   **Valor Total Multas de Atraso das Parcelas Alteradas:** Soma dos valores de Multa de Atraso das parcelas alteradas.   
   **Valor Total Juros de Mora das Parcelas Alteradas:** Soma dos valores de Juros de Mora das parcelas alteradas.  
      
      
   **Antecipação de Parcela**  
      
   Este tipo de aditivo permite que o usuário antecipe o pagamento das parcelas do plano de financiamento de uma determinada venda, inserindo um desconto de antecipação e alterando a data de vencimento.  
      
   Ao selecionar este tipo de Aditivo, será apresentado todas as Parcelas em aberto do plano de financiamento. O Sistema permite que o usuário selecione uma nova data para a Parcela desejada, selecionando um novo valor no Campo 'Novo Vencimento', com isto, inserindo um desconto de acordo com o Tipo de Antecipação selecionado e a Taxa de Juros informada.  
      
   Campos a serem preenchidos:  
   **Tipo de Antecipação:** Este campo possibilita a escolha do tipo de Antecipação a ser realizado, são eles:
  + Valor Presente:\* Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Antecipação de acordo com a fórmula de Valor Presente. A taxa de Juros será convertida para diária e verificado o número de dias de Antecipação.
  + Valor Presente Parcial:\* Este modelo funciona conforme o tipo "Valor Presente", más é para antecipações parciais.
  + Valor Presente Meses:\* Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Antecipação de acordo com a fórmula de Valor Presente.  
                     Calculo Valor Presente:  VP = VF / (1 + TJAD) ~ N  
     VP - Valor presente da parcela  
     VF - Valor futuro da parcela  
     TJAD - Taxa de juros ao dia  
     N - Número de dias que a parcela será antecipada"  
     Para sabermos o valor de desconto basta subtrair VD = VF - VP"
  + Valor Presente Meses Parcial:\* Este modelo funciona conforme o tipo "Valor Presente Meses", más é para antecipações parciais.
  + Percentual Fixo:\* Neste modelo, é necessário informar um percentual da Taxa de Juros Fixo. Esta taxa será descontada independente da quantidade de meses de antecipação.
  + Valor Fixo:\* Neste modelo, ao editar as parcelas e informar a nova data de vencimento, podemos informar um valor fixo de desconto na parcela. Não será realizado nenhum cálculo.
  + Número de Meses Percentual:\* Neste modelo, é necessário informar um percentual da Taxa de Juros. Esta taxa será descontada de acordo com a quantidade de meses de antecipação.
  + Número de Meses Valor:\* Neste modelo, é necessário informar um Valor de Desconto. Este valor será descontado de acordo com a quantidade de meses de antecipação.
  + Deságio Mensal: {\*}Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Antecipação de acordo com a fórmula de Valor Presente. A taxa de Juros será convertida para diária e verificado o número de dias de Antecipação, utilizando o cálculo de ano comercial (360 dias) ao invés de ano corrido (365 dias).  
     **Ignorar Reajuste em parcela antecipada após efetivação:** Ao marcar este parâmetro, as parcelas alteradas não serão mais reajustadas pelo sistema.   
     **Taxa de Juros Presente a.m.:** Informe a taxa de juros que o Tipo de Antecipação utilizará para realizar o cálculo da antecipação da Parcela.  
     **Valor Atual Total das Parcelas Alteradas:** Soma dos valores das parcelas selecionadas sem as alterações.  
     **Valor Novo Total das Parcelas Alteradas:** Soma dos valores das parcelas selecionadas com as alterações.  
     **Valor Desconto Total das Parcelas Alteradas:** Soma dos valores de Desconto das parcelas Antecipadas.  
        
        
     **Outros**  
        
     Armazena um descritivo e gera um histórico da venda.  
        
     Campos a serem preenchidos:  
     **Texto:** Campo utilizado para inserção do texto.  
        
        
     **Prorrogação de Vencimento**  
        
     Utilizado para prorrogar o vencimento de uma determinada parcela, possibilitando também a inclusão de juros.  
        
     Ao selecionar este tipo de Aditivo, será apresentado todas as Parcelas em aberto do plano de financiamento. O Sistema permite que o usuário selecione uma nova data para a Parcela desejada, selecionando um novo valor no Campo 'Novo Vencimento', com isto, inserindo um valor de Juros na parcela.  
        
     Campos a serem preenchidos:  
     **Tipo de Prorrogação:** Este campo possibilita a escolha do tipo de Prorrogação a ser realizado, são eles:
  + Valor Futuro:\* Neste modelo, é necessário informar o percentual da Taxa de Juros para que o sistema calcule a Prorrogação de acordo com a fórmula de Valor Futuro. A taxa de Juros será convertida para diária e verificado o número de dias de Prorrogação.
  + Valor Futuro Parcial:\* Este modelo funciona conforme o tipo "Valor Futuro", más é para Prorrogações parciais.
  + Valor Futuro Meses:\* Neste modelo, é necessário informar o percentual da Taxa de Juros Futuro para que o sistema calcule a Prorrogação de acordo com a fórmula de Valor Futuro.  
                     Calculo Valor Futuro:  VF = VP (1 + TJAD) ~ N  
     VP - Valor presente da parcela  
     VF - Valor futuro da parcela  
     TJAD - Taxa de juros ao dia  
     N - Número de dias que a parcela será Prorrogado"  
     Para sabermos o valor de juros de acordo basta subtrair VJA = VF - VP"
  + Valor Futuro Meses Parcial:\* Este modelo funciona conforme o tipo "Valor Futuro Meses", más é para Prorrogações parciais.
  + Percentual Fixo:\* Neste modelo, é necessário informar um percentual da Taxa de Juros Futuro Fixo. Esta taxa será Inserida independente da quantidade de meses de Prorrogação.
  + Valor Fixo:\* Neste modelo, ao editar as parcelas e informar a nova data de vencimento, podemos informar um valor fixo a ser inserido na parcela. Não será realizado nenhum cálculo.
  + Número de Meses Percentual:\* Neste modelo, é necessário informar um percentual da Taxa de Juros Futuro. Esta taxa será inserida de acordo com a quantidade de meses de Prorrogação.
  + Número de Meses Valor:\* Neste modelo, é necessário informar um Valor a ser inserido. Este valor será inserido de acordo com a quantidade de meses de Prorrogação.
  + Incorporar Multa de Atraso e Juros de Mora:\* Ao efetivarmos um aditivo de prorrogação de vencimento com este novo tipo de prorrogação e a parcela estiverem atrasados, criaremos um componente de juros de acordo que guardará os valores de multa de atraso e juros de mora incorporando assim ao valor total da parcela.  
     **Taxa de Juros Futuro a.m.:** Informe a taxa de juros Futuro que o Tipo de Prorrogação utilizará para realizar o cálculo da Prorrogação da Parcela.  
     **Ignorar Reajuste em parcela prorrogada após efetivação:** Ao marcar este parâmetro, as parcelas alteradas não serão mais reajustadas pelo sistema.   
     **Valor Atual Total das Parcelas Alteradas:** Soma dos valores das parcelas selecionadas sem as alterações.  
     **Valor Novo Total das Parcelas Alteradas:** Soma dos valores das parcelas selecionadas com as alterações.  
     **Valor Juros Acordo Total das Parcelas Alteradas:** Soma dos valores de Juros de Acordo das parcelas Prorrogadas.  
        
        
     **Renegociação de Contrato**  
        
     Este tipo de aditivo permite que o usuário altere o plano de financiamento de uma determinada venda.  
        
     Ao selecionar este tipo de Aditivo, será apresentado todas as Parcelas em aberto do plano de financiamento na aba "Selecione as Parcelas a Renegociar". O Sistema permite que o usuário selecione as parcelas que serão canceladas no Aditivo.  
        
     Campos a serem preenchidos:  
     **Tipo de Renegociação:** Este campo possibilita a escolha do tipo de renegociação a ser realizado, são eles:
  + Padrão:\* Usado quando o usuário for realizar o aditivo para excluir parcelas do Plano de Financiamento e inserir novas parcelas.
  + Melhoria de Bens:\* Permite a criação de uma ou mais parcelas no plano de financiamento. Exemplo de aplicação: Será realizada uma limpeza no terreno, então neste caso será necessária a inclusão do valor a ser cobrado no plano de financiamento.
  + Cancelamento:\* Realiza o cancelamento de parcelas, sem a geração de uma nova parcela.  
     **Permitir Renegociar Valores Diferente:** Permite que o novo plano ou nova parcela, tenha um valor diferente, do valor das parcelas selecionadas para serem excluídas.  
     **Permitir Renegociar sem Valor de Multa e Juros:** Permite que o novo plano ou nova parcela seja renegociado sem o valor dos juros e multa.  
     **Proporcionalizar Valores nos Componentes:** Caso o usuário opte por Sim, os valores dos componentes da(s) nova(s) parcela(s) criada(s) serão proporcionalizados após o cancelamento das parcelas selecionadas no campo Parcelas.  
     Os valores de Juros e Correção Monetária, já existentes nas parcelas a serem canceladas são proporcionalizados de acordo com o número de novas parcelas nos componentes Juros de Contrato antes do Aditivo e Correção Monetária antes do Aditivo.  
     **Usar Fórmulas para calcular valores Informativos:** Clicando neste parâmetro será habilitado os campos:
* Fórmula: Insira a fórmula que irá calcular o valor da Renegociação. Temos disponível somente as fórmulas Refinanciamento 01 e Refinanciamento 02.
* Taxa de Juros: Taxa de Juros que será utilizado para o cálculo das fórmulas.
* Ref. Grupo: Grupo de referência que será utilizado para o cálculo das fórmulas.  
   **Total Parcelas Selecionadas:** Soma dos valores das parcelas selecionadas. Esta informação será calculada automaticamente.  
   **Total Multa de Atraso:** Soma dos valores das multas de Atraso das parcelas selecionadas. Esta informação será calculada automaticamente.  
   **Total Juros de Mora:** Soma dos valores dos Juros de Mora das parcelas selecionadas. Esta informação será calculada automaticamente.  
   **Desconto de Multa de Atraso:** Informe o valor de desconto que será dado sobre o total do valor da Multa de Atraso.  
   **Desconto Juros de Mora:** Informe o valor de desconto que será dado sobre o total do valor de Juros de Mora.  
   **Total a Renegociar:** Soma dos valores das parcelas selecionadas. Esta informação será calculada automaticamente.  
   **Total Renegociado:** Soma dos valores a serem gerados através do recurso de Condições de Venda. Esta informação será calculada automaticamente.  
   **Diferença de Renegociado por a Renegociar:** É a diferença do valor a ser gerado com o valor selecionado a ser cancelado. Esta informação será calculada automaticamente.  
   **Aba Selecione as Parcelas a Renegociar:** Através desta aba, poderemos selecionar as parcelas do Plano de Pagamento que serão canceladas.  
   **Aba Condições de Venda:** Através desta aba, poderemos efetuar a inclusão dos novos grupos e dos componentes que irão compor, as novas condições no plano de financiamento.  
   **Aba Simular Novo Plano:** Através desta aba, poderemos efetuar a simulação no novo Plano de Financiamento de acordo com a nova regra determinada nas condições de venda e das parcelas excluídas.  
      
      
   **Troca de Comprador**  
   Altera o(s) cliente(s) da venda para o(s) novo(s) cliente(s) escolhido(s).  
      
   Ao selecionar este tipo de Aditivo, será apresentado todos os Clientes da Venda/Aluguel e temos a opção de excluí-los.  
   Foram unificados os aditivos de Troca de Comprador e Agente Complementar. Agora na versão 11.60 o conceito de Agente   
   Complementar vai ser descontinuado e poderemos ter mais de um Comprador em conjunto e inclusive assumindo grupos de parcelas.  
   **Aba Lista de Compradores**  
      
   **Novo Comprador:** Possibilita o usuário selecionar um novo Cli/For.  
   **Botão Incluir:** Inclui o comprador que estiver selecionado no campo Novo Comprador.  
   **Botão Excluir:** Exclui o comprador que estiver selecionado.  
      
   **Esta aba ainda possui as colunas:**   
      
   **Seleção:** Coluna usada para marcar e desmarcar os clientes.  
   **Cliente/Fornecedor:** Código do Cliente/Fornecedor.  
   **Nome:** Nome do Cliente.  
   **Percentual de Participação:** Percentual de cada Comprador onde a soma de todos os percentuais não poderá ultrapassar 100%.   
   **Comprador Principal:** Deve ser marcado apenas um Comprador Principal.  
      
   **Aba Séries de Pagamento**  
      
   Esta aba mostra as informações referentes aos Compradores envolvidos nos pagamentos.  
      
   **As colunas mostradas são:**   
      
   **Código do Grupo:** Código do Grupo no plano de financiamento.  
   **Coligada / Cliente:** Código da coligada e o código do cliente. **Nome:** Nome do Cliente.  
   **Todas em Aberto:** Marcando essa todos os lançamentos em aberto terão o nome do cliente alterado para o que estiver selecionado, impossibilitando alterações na coluna Data de entrada no plano.  
   **Data de entrada no plano:** Nesta coluna o usuário define a partir de qual data o novo cliente terá seu nome incluído nas parcelas.   
      
   A data informada nesta coluna irá afetar diretamente os lançamentos financeiros no RM Fluxus, pois a Data de entrada no plano é o parâmetro para alteração dos lançamentos financeiros "Em Aberto".   
   Por exemplo: Se a Data de entrada no plano é 01/01/2009, todos os lançamentos financeiros referentes de uma determinada venda, serão alterados a partir desta data para o novo comprador.  
      
  **Troca de Fiador**  
      
   Altera o Fiador atual da venda para o novo Fiador escolhido.  
      
   Ao selecionar este tipo de Aditivo, será apresentado todos Fiadores da Venda/Aluguel e temos a opção de excluí-los.  
      
   Campos a serem preenchidos:  
   **Buscar Novo Fiador:** Neste campo é possível informar o novo Fiador da Venda/Aluguel. Para inserí-lo, basta clicar no botão "Incluir". Ao selecionar um fiador que não esteja relacionado com a sub-unidade, o relacionamento é feito automaticamente, ao executar o Aditivo.  
      
      
   **Troca de Lote**  
      
   Altera a sub-unidade atual da venda para a nova sub-unidade escolhida.  
      
   Ao selecionar este tipo de Aditivo, será apresentado todos os dados da SubUnidade atual: Empreendimento, Unidade, SubUnidade, Valor e Desconto.  
      
   Campos a serem preenchidos:  
   **Empreendimento:** Será apresentado o Empreendimento da Venda. Este campo não poderá ser alterado, pois a troca de SubUnidade deverá ser realizada dentro de um mesmo Empreendimento.  
   **Unidade:** Informa a Unidade para a alteração da nova SubUnidade.  
   **Sub-Unidade:** Informe a nova SubUnidade da Venda/Aluguel. Será apresentado somente SubUnidades disponíveis para a Venda/Aluguel.  
   **Valor :** Será mostrado automaticamente o valor da nova SubUnidade selecionada.  
   **Desconto:** Informe o desconto cedido para a nova SubUnidade selecionada.  
   **Observação:** Após a efetivação do Aditivo Troca de Lote, as situações das SubUnidades serão atualizadas. A SubUnidade antiga irá para disponível para Venda e a nova SubUnidade irá para Vendida/Alugada.  
      
   **Troca Mútua de Imóveis**  
      
   Possibilita a troca entre lotes que já estão vinculados a vendas.  
      
   Ao selecionar este tipo de Aditivo, será apresentado todos os dados da SubUnidade atual: Empreendimento, Unidade, SubUnidade, Valor e Desconto.  
      
   Campos a serem preenchidos:  
   **Empreendimento:** Será apresentado o Empreendimento da Venda. Este campo não poderá ser alterado, pois a troca de SubUnidade deverá ser realizada dentro de um mesmo Empreendimento.  
   **Unidade:** Informa a Unidade para a alteração entre as SubUnidades.  
   **Sub-Unidade:** Informe a SubUnidade da outra Venda/Aluguel. Será apresentado somente SubUnidades Vendidas para a troca.  
   **Valor:** Será mostrado automaticamente o valor da nova SubUnidade selecionada.  
   **Desconto:** Informe o desconto cedido para a nova SubUnidade selecionada.  
      
    

  |  |  |
  | --- | --- |
  |  | Como Fazer |

  ---

  Efetivar

  Recontabilizar

  Cancelar
