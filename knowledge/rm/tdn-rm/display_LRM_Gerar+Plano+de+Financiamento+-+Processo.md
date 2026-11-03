---
content_hash: 8b2efedafe1f3b6bed23a4ae09c0a76f9d6e8b0a57215f2e46b6ebe3bbe90c1c
fetched_at: '2026-06-29T00:09:48.653956+00:00'
page_id: '435105211'
product: rm
source: tdn-rm
title: Gerar Plano de Financiamento - Processo
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Plano+de+Financiamento+-+Processo
version: 3
---

**Gerar Plano de Financiamento**   
A partir da versão 11.20 para acessar ao as Condições de Venda o usuário deverá acessar a opção de Processos | Gerar Plano de Financiamento, sendo que este processo está disponível na tela de Venda/Aluguel localizada em Vendas / Cobrança e na edição de Vendas e Aluguéis. Ao chamar este processo, será aberta a janela Gerar o Plano de Financiamento que possui as abas Condições de Venda, Plano de Financiamento e Componentes da Regra.  
   
Condições de Venda  
   
Será apresentado todos os componentes e suas devidas parametrizações, que foram previamente cadastrados na Modalidade escolhida para esta venda. Estes componentes foram definidos no cadastro de Componentes da Modalidade de Venda através do menu Cadastro | Condições da Venda | Modalidade de Venda.   
   
Para incluir, excluir ou alterar um componente das Condições da Venda, utilize os seguintes ícones:  
   
**Inclui Componente de Regra** – Inclui um novo Componente à modalidade de venda.  
   
**Edita Componente de Regra** – Altera dados de um componente já existente na modalidade de venda.   
   
**Excluir Componente de Regra** – Exclui um Componente já existente na modalidade de venda.  
   
**Copiar Regras da Modalidade da Venda**  
   
A opção Copiar Regras da Modalidade da Venda permite que o usuário no momento em que está gerando uma Condição de Vendas, voltar para a Modalidade de Venda inicial, já pré-cadastrada no Menu Cadastros em Condições de Venda.  
O processo de Copiar Regras da Modalidade da Venda só poderá ser executado através do processo de Geração do Plano de Financiamento.  
   
Em versões anteriores o nome desta funcionalidade era Restaurar Modalidade.  
   
**Copiar Grupo**  
   
O Processo de Copiar de Grupo está habilitado na aba de Condições de Vendas. Ele permite o usuário a copiar os Componentes de um Grupo já existente para um novo grupo com numeração seqüencial.   
   
É possível visualizar esse processo na Aba de Condições de Vendas de uma nova venda, no Aditivo de Renegociação de Contrato e no Distrato Bilateral.  
   
**Inclusão, edição e exclusão de componentes**  
   
Para o cadastro de um Componente nas Condições da venda, preencha corretamente os campos em branco apresentado na pasta de Identificação.  
   
Campos a serem preenchidos:  
   
**Núm. Venda/Aluguel:** Número da venda ou aluguel que é preenchido automaticamente.  
   
**Grupo:** Informe o número do grupo que este componente fará parte. Os componentes de reajustes somente terão efeito sobre os componentes de mesmo grupo.  
   
**Observação:**  
Uma modalidade de venda pode conter vários grupos de financiamento, ou seja, um mesmo componente poderá ser usado em grupos distintos, com regras diferentes.  
   
**Componente:** Informe o componente a ser cadastrado.  
   
**Tipo de Parcela:** Este campo será preenchido automaticamente, caso o componente selecionado no campo acima seja um componente gerador de parcela.  
   
Ao preencher estes campo mencionados acima, dependendo do Tipo de Componente do Componente escolhido, será apresentando outras abas para o devido preenchimento.  
   
**Entrada****:** Será apresentado se o Tipo de Componente for Entrada.  
   
**Principal****:** Será apresentado se o Tipo de Componente for Principal.  
   
**Juros****:** Será apresentado se o Tipo de Componente for Juros Fixo.  
   
**Monetária****:** Será apresentado se o Tipo de Componente for Correção Monetária.  
   
**Resíduo****:** Será apresentado se o Tipo de Componente for Resíduo  
   
**Encargos Financiamento****:** Será apresentado se o Tipo de Componente for Encargos Financiamento  
   
**% de desconto sobre o juros de Contrato****:** Será apresentado se o Tipo de Componente for Desconto de Juros de Contrato  
   
**% de desconto sobre a Correção Monetária****:** Será apresentado se o Tipo de Componente for Desconto na Correção Monetária  
   
**Seguro****:** Será apresentado se o Tipo de Componente for Seguro  
   
**Desconto****:** Será apresentado se o Tipo de Componente for Descontos  
   
**Valor Tipo de Parcela****:** Será apresentado se o Tipo de Componente for Entrada, Principal, Resíduo, Seguro ou Alíquota  
   
**Financiamento CEF****:** Será apresentado se o Tipo de Componente for Financiamento CEF  
   
**Terreno CEF****:** Será apresentado se o Tipo de Componente for Terreno CEF  
   
**Subsídio CEF****:** Será apresentado se o Tipo de Componente for Subsídio CEF  
   
**Recurso Mutuário CEF****:** Será apresentado se o Tipo de Componente for Recurso Mutuário CEF  
   
**FGTS CEF****:** Será apresentado se o Tipo de Componente for FGTS CEF  
   
   
Parâmetros:  
   
**Situação ativa:** Marque este campo quando o Componente estiver ativo. Se o campo estiver desmarcado este Componente não poderá ser usado na Modalidade de Venda.  
   
**Observação:**  
Nos componentes de reajustes, com ação antes da entrega do empreendimento, este campo será desmarcado após a sua utilização, ou seja, enquanto a venda estiver antes da entrega do empreendimento, o componente estará ativo, após a entrega do empreendimento, o componente será desativado.  
   
A partir da versão 11.20 foi criado o quadro "Cliente para o qual serão geradas as parcelas deste componente" com os seguintes campos:  
   
**Cod cliente:** Cliente que será informado para ter o nome registrado nos lançamentos do Fluxus. Caso este campo esteja em branco, as parcelas do Fluxus serão registradas com o cliente informado na Identificação da Venda/Aluguel.  
   
**Endereço para envio de boleto:** Endereço que será informado para ter o endereço registrado nos lançamentos do Fluxus.   
   
**Observação:**  
Se o parâmetro "**Consistir Saldo Devedor c/ Valor Sub-Unidade**", através do Menu Opções | Parâmetros | RM SGI, estiver marcado, o sistema irá comparar o valor da Sub-unidade com o valor total do plano de financiamento, se não for igual, será negado a geração do plano de financiamento.  
   
Ao incluir componentes de Juros e/ ou Correção Monetária, devemos observar as seguintes consistências:

* Grupos com modelo de calculo pós-fixado devem ter todos os componentes de juros e CM com a mesma configuração de pro rata dia.
* Grupos com modelo de calculo prefixado, apenas os componentes de CM devem ter a mesma configuração de pro rata dia.
* Todos os componentes de juros do mesmo grupo devem possuir a mesma periodicidade.
* Todos os componentes de CM do mesmo grupo devem parametrizar a mesma periodicidade.
* Todos os componentes de juros e CM do mesmo grupo devem ter a mesma referencia de entrega.
* Todos os componentes de juros do mesmo grupo devem possuir a mesma configuração de juros acumulado.
* É permitido a inclusão de N componentes de Juros Antes, Juros Após, CM Antes e CM Após no mesmo grupo, (Exceto Juros Ambos e CM Ambos).
* É permitido a inclusão de N componentes de Juros Ambos e CM Ambos no mesmo grupo, (Exceto Juros Antes e Após, CM Antes e Após).

Importante:

 O cliente não pode ter no mesmo grupo o mesmo tipo de componente com regra de reajuste diferentes, por exemplo, um com pro-rata e outro sem pro-rata, seja no momento Antes e Após entrega.  
 Existem um caso onde permitimos utilizar uma outra forma de configuração de componentes. Quando o cliente quiser usar pro-rata somente para parcelas vencidas, e reajuste mensal para parcelas não vencidas, ele pode fazer essa configuração desde que:  
 - Esteja no reajuste revitalizado;  
 - Que ele use essa configuração somente no CM Antes ou no CM Após.
