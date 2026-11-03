---
content_hash: e1309cd5cd2d9c33d4b61c8b88dde7416f0c0d25fa8bb3b64699cdcb3510b8b6
fetched_at: '2026-06-29T00:09:47.973734+00:00'
page_id: '435105113'
product: rm
source: tdn-rm
title: Parâmetros - Contrato - Plano de Financiamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105113
version: 13
---

### **Etapa 1 - Parâmetros do Plano de Financiamento**

* **Nota Promissória c/ nº Sequencial:** Se marcado, o número da nota promissória será gerado sequencialmente independente da quantidade de grupos de financiamento na venda. **Observação:** No plano de financiamento temos também o campo "Número da Parcela" que é gerado sequencialmente por grupo de financiamento.
  + **Numerar por ordem de vencimento e grupo:** Este parâmetro será habilitado somente se Nota Promissória c/ nº Sequencial for marcado, se marcado, o número da nota promissória será ordenado pelo vencimento das parcelas e separados por cada grupo de componentes da venda.

Para saber maiores informações sobre **Nota Promissória** .

* **Gerar Plano sem Fração Ideal:** Fração Ideal é um campo da subunidade usado para cálculo da parcela de IPTU e Parcela de Instalação. Caso o parâmetro esteja desmarcado, o sistema irá consistir se nas condições da venda existe o componente de IPTU. Caso exista e se a fração ideal não estiver cadastrada, o sistema irá barrar a geração do plano.

### **Etapa 2 - Plano de financiamento por coligada**

* **Prorrogar vencimento para primeiro dia útil após feriado, sábado e domingo:** Se marcado, ao efetuar a geração de parcelas, se a data de vencimento cair em um feriado, sábado ou domingo, será prorrogada para o primeiro dia útil após.

### **Etapa 3 - Parâmetros de Integração**

* **Fontes do Centro de Custo:** Defina de onde o TCGI irá buscar o Centro de Custo para preencher o plano de financiamento. As opções são:

  + **Default:** O sistema irá verificar o que está preenchido e seguirá a ordem Tipo da Parcela / Subunidade / Unidade / Empreendimento / Parâmetro da Coligada para buscar os dados;
  + **Tipo da Parcela:** Definido no cadastro do Tipo de Parcela;
  + **Sub-Unidade:** Definido no cadastro de subunidade;
  + **Unidade:** Definido no cadastro da unidade;
  + **Empreendimento:**  Definido no cadastro do empreendimento;
  + **Parâmetros Coligada:**  Definido no cadastro da Coligada.

### **Etapa 4 - Plano de Financiamento**

**Contrato**

* **Bloquear a geração dos processos da Venda sem Contrato:** Caso esse parâmetro seja marcado será obrigatória a geração do contrato da venda para realizar processos como Aditivo e Distrato. Este parâmetro quando marcado também irá definir que somente as vendas com contrato gerado estarão visíveis no Portal do Cliente (PDC). Caso contrário, o PDC irá exibir a venda independente do contrato gerado ou não.
* **Visualizar os campos calculados dos valores de contrato na visão da venda:** A partir das versões revitalizadas as colunas "Valor Atualizado", "Saldo Devedor Atual" e "% Baixado" não são exibidas por padrão na visão de Contratos de Venda. Assim para manter a compatibilidade com versões anteriores, foi criado este parâmetro que permite habilitar estas colunas na visão de Contratos em base pós revitalização. Observação: Caso esse parâmetro seja marcado todas as parcelas do contrato serão calculadas através do processo de valor líquido o que pode onerar de forma relevante a exibição de vendas e respectivas parcelas dento do sistema.
* **Consistir Saldo Devedor com o valor APTO:** Esse parâmetro permite a consistência entre o valor do Saldo Devedor, gerado nas Condições de Venda e o valor do Imóvel. O mesmo é aplicado por Coligada, permitindo que em determinados cenários a regra seja diferenciada.
* **Tipo de Deságio no Cálculo de Valor Líquido no Financeiro (Reajuste em Memória)**
  + **Tipo de Deságio do modelo de cálculo pré-fixado(PRICE e SAC):** Com esse parâmetro é possível selecionar a forma de calcular o deságio (desconto) no momento da baixa, calculando o valor líquido para a data em que foi antecipada a parcela. O deságio é calculado para modelos pré-fixados (PRICE, SAC, etc). Para marcar esse parâmetro é necessário que o reajuste Online esteja habilitado. É possível escolher:
    - **Nenhum:** Não será calculado o deságio.
    - **Valor Presente Meses:** será calculado o valor presente da parcela de acordo com cada mês que for antecipado.
      * **Observação**: Para mais informações sobre o funcionamento do cálculo de deságio, acesse o link a seguir: .
    - **Valor Presente Dias:** será calculado o valor presente da parcela de acordo com o mês e a data de vencimento para o qual ele for antecipado realizando assim o cálculo pró rata dia, para esta antecipação.
* **Permitir vencimento no primeiro mês da venda para modalidade para o tipo principal :** Agora é possível definir a data de vencimento no mesmo mês da venda para componentes do tipo “Mensal”, desde que o parâmetro *“PERMITIR VENCIMENTO NO PRIMEIRO MÊS DA VENDA PARA MODALIDADE PARA O TIPO MENSAL”* esteja habilitado.

**Distrato**

* **Ao efetivar recalcular fórmula do distrato e consistir com valor distribuído no plano de distrato:** Caso esse parâmetro seja marcado será validado se a fórmula inserida possui o mesmo valor do plano do distrato.
* **Realizar a contabilidade para o distrato apenas se o evento contábil informado, se desmarcado sempre contabiliza:** Com esse parâmetro marcado apenas se houver um evento contábil informado no processo de distrato haverá a contabilização.
* **Cancelar parcelas da venda ao efetivar distrato:** Com este parâmetro marcado, ao efetivar um distrato de um contrato de vendas no TIN, todos os lançamentos financeiros desta venda serão cancelados. Lembrando que o cancelamento de lançamentos é irreversível.

**Aditivo**

* **Realizar a contabilidade para o aditivo apenas se o evento contábil for informado, se desmarcado sempre contabiliza.** Com esse parâmetro marcado apenas se houver um evento contábil informado no processo de aditivo haverá a contabilização.

**Resíduo**

* **Permite gerar parcela de resíduo de parcelas não quitadas no processo de gerar resíduo:** Caso esse parâmetro seja marcado será possível gerar a parcela de resíduo mesmo que existam parcelas baixadas parcialmente;

**Relatório de Informe de Pagamentos (IP):**

* **Utilizar o comprador do lançamento:** Marque esta opção para que o relatório de informe de pagamentos busque o comprador/clifor responsável pelo pagamento, informado nas parcelas financeiras.
* **Componentes a serem ignorados no IP:** Informe o código dos componentes que serão ignorados na geração do relatório de Informe de Pagamentos. Esta parametrização pode ser utilizada para retirar, por exemplo, os componentes da Minha Casa, Minha Vida (500 - Financiamento CEF, 515, Terreno CEF, 530 - Subsidio, 545 - Recurso Mutuário CEF, 550 - FGTS, etc.) ou qualquer outro componente, deste relatório.

**Relatório de Ficha Financeira (FF):**

* **Exibir valores de Perda Financeira no relatório:** Marque esta opção para exibir os valores das baixas por Perda Financeira no relatório da Ficha Financeira.
* **Componentes a serem ignorados na FF:** Informe o código dos componentes que serão ignorados na geração do relatório de Ficha Financeira. Esta parametrização pode ser utilizada para retirar, por exemplo, os componentes da Minha Casa, Minha Vida (500 - Financiamento CEF, 515, Terreno CEF, 530 - Subsidio, 545 - Recurso Mutuário CEF, 550 - FGTS, etc.) ou qualquer outro componente, deste relatório.

### **Etapa 5 - Condição de financiamento**

**Nota promissória**

* **Tipo de ordenação de nota promissória:** Nesta parâmetro é possível definir a ordenação da apresentação dos campos na nota promissória. As opções são:
  + Número sequencial de agrupamento, vencimento, grupo e tipo de parcela;
  + Número sequencial de agrupamento, vencimento, tipo de parcela e grupo;
  + Grupo, tipo de parcela e vencimento;
  + Número sequencial de agrupamento, grupo e vencimento;

### **Etapa 6 - MCMV (Minha Casa Minha Vida)**

**Arquivo DCD (Demonstrativo de Cronograma Desembolso)**

* **Limite de Diferença importação DCD/MCMV (R$):** Esse parâmetro é responsável por definir um valor aceitável para a diferença da parcela no momento da importação do arquivo DCD.

**Avanço de Obra (Minha Casa Minha Vida)**

* **Incluir automaticamente diferença de avanço de obra 100% em avanços de obra MCMV:**

**Geração de Plano de Financiamento (Minha Casa Minha Vida)**

* **Calcular valor do terreno com base no valor do terreno do empreendimento e fração ideal para contratos com origem externa ao sistema:** Ao marcar esta opção o sistema utilizará as informações do valor do terreno do empreendimento e a fração ideal cadastradas, para calcular o valor do terreno para contratos cuja origem for externa ao TCGI;
* **Inserir o componente de terreno ao inserir o componente de financiamento MCVM quando o componente existir na modalidade e for via web service:** Marque esta opção para que o sistema insira automaticamente do componente de terreno nos plano de financiamento com modalidade MCMV, via webservice.
