---
content_hash: 14eead40657dbba5358dca0cc6d45d9b5083053ce7ebfa66f750481c7e34f20f
fetched_at: '2026-06-29T00:09:49.755435+00:00'
page_id: '435105359'
product: rm
source: tdn-rm
title: Tipos de Componentes - Resíduo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105359
version: 2
---

**Resíduo - Componente Modalidade**   
 Veja abaixo, como utilizar os componentes de Resíduo:  
    
 **1- No TOTVS Incorporação, em Cadastros / Componentes é possível configurar os componentes de Resíduo.**  
    
   
    
 **2- É necessário ter um componente de Resíduo para a realização do reajuste do mesmo.**  
    
   
    
 **3- É necessário também um componente para a parcela de Resíduo.**   
    
   
    
 Repare que este componente acima tem o **Tipo Componente** igual a **2 - Principal**, que é um componente de parcela. Quando a parcela for gerada no plano de financiamento da venda, a mesma será criada em novo grupo, e o código do componente será 0908.  
    
 Já o campo **Tipo Parcela** tem que ser o mesmo para os 2 componentes. Em nosso exemplo o código do Tipo Parcela é **10 - Resíduo**.  
    
 A seguir temos os campos da tela de Resíduo na edição de uma venda, informe os seguintes campos:  
    
 **Data Base:** Informe a data base deste componente. Será através da data base deste componente que o sistema levará em consideração para verificar a data de próximo reajuste.  
    
 **Observação:**  
 Se este componente Monetário já existir na Modalidade escolhida para esta venda, este campo será preenchido automaticamente com a data da venda.  
    
 **Dia do Vencimento:**  
 Informe o dia do vencimento do componente de Resíduo caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.  
    
 **Data Próximo Reajuste:** Informe a data que será realizado o próximo reajuste deste componente.   
    
 **Observação:**  
 Se este componente Monetário já existir na Modalidade escolhida para esta venda, este campo será preenchido automaticamente de acordo com a data base e a periodicidade.  
    
 **Periodicidade (Mensal):** É informado automaticamente a periodicidade do componente de Resíduo.   
    
 **Parâmetros:**  
    
 **Cálculo do resíduo com Moeda Projetada:**  
 Marque este campo para efetuar o cálculo do resíduo utilizando Moeda Projetada.  
    
 **Distribuir parcela de Resíduo:**  
 Com este parâmetro marcado, ao invés de ser criada uma parcela a parte de resíduo, será feito um rateio do valor desta parcela de resíduo entre as parcelas contidas no próximo período de 12 meses.   
    
 **Atenção:**  
 Para que isto ocorra, é necessário criar um componente que tenha o seu tipo de componente igual a "Distribuir Parcela Resíduo". Este componente será utilizado internamente pelo sistema durante o processo de reajuste no momento de distribuir o resíduo, não sendo permitido a utilização do mesmo em qualquer modalidade ou condições de vendas. Este componente pode ter um valor opcional no RM Fluxus ou não, se existir, o valor distribuído do resíduo será gravado no campo opcional informado.  
    
 **Reajustar mensalmente as parcelas fora do período de Resíduo:**  
 Marque este campo para reajustar mensalmente as parcelas fora do período de Resíduo. O período de resíduo é compreendido entre 12 meses. Com o parâmetro marcado todas as parcelas fora deste período serão reajustadas.  
    
 Resíduo da parcela reajustado mensalmente pelos Juros de Contrato:  
 Ao marcar esta opção, o resíduo calculado será reajustado pelos Juros de Contrato.  
    
 **Observação:**  
 Para calcular o reajuste de Juros de contrato do resíduo, tem-se como base o mês do reajuste e o mês da parcela. Acha-se a diferença entre estes meses e multiplica esta diferença pela taxa de Juros e aplica-se este novo valor dos juros no valor do resíduo.  
    
 Exemplo  
 Taxa Juros = 1%  
 Parcela: Fevereiro  
 Reajuste: Maio  
 Resíduo de Fevereiro = R$ 20,00  
 Diferença entre meses: Maio – Fevereiro = 3 meses  
 Cálculo: 3 meses \* 1% = 3%  
 Reajuste de Resíduo = 3% sobre R$ 20,00 = R$ 20,60  
    
 **Cálculo do Resíduo da "Parcela Em Aberto"**  
    
 **NÃO utilizar o juros de contrato no cálculo do resíduo**  
 Marque este campo quando não quiser utilizar o valor dos Juros de Contrato para efetuar o cálculo do resíduo.  
    
 **NÃO utilizar a correção monetária no cálculo do resíduo**  
 Marque este campo quando não quiser utilizar o valor da Correção Monetária para efetuar o cálculo do resíduo.  
    
 **Reajuste sobre o "Resíduo da Parcela Quitada"**  
    
 **Resíduo da parcela reajustado mensalmente pelo juros**  
 Ao marcar esta opção, o resíduo calculado será reajustado pelos Juros de Contrato.  
    
 **Observação:**  
 Para calcular o reajuste de Juros de contrato do resíduo, tem-se como base o mês do reajuste e o mês da parcela. Acha-se a diferença entre estes meses e multiplica esta diferença pela taxa de Juros e aplica-se este novo valor dos juros no valor do resíduo.  
    
 **Exemplo:**  
 Taxa Juros = 1%  
 Parcela: Fevereiro  
 Reajuste: Maio  
 Resíduo de Fevereiro = R$ 20,00  
 Diferença entre meses: Maio – Fevereiro = 3 meses  
 Cálculo: 3 meses \* 1% = 3%  
 Reajuste de Resíduo = 3% sobre R$ 20,00 = R$ 20,60  
    
 **Resíduo da parcela reajustado mensalmente pela CM**  
 Ao marcar esta opção, o resíduo calculado será reajustado pela Correção Monetária.  
    
 **Observação:**  
 Para calcular o reajuste de Correção Monetária do resíduo, tem-se como base o mês anterior ao mês do reajuste e o mês anterior ao mês de quitação da parcela. Acha-se a variação monetária entre este período e este índice é multiplicado pelo valor do resíduo.  
    
 **Exemplo:**  
 Parcela: Fevereiro  
 Reajuste: Maio  
 Resíduo de Fevereiro = R$ 20,00  
 Cálculo = Cotação de Abril / Cotação de Janeiro = índice.  
 Reajuste de Resíduo = índice \* R$ 20,00  
    
    
  **O Resíduo pode ser utilizado das seguintes formas:**   
    
 **1 - Moeda Projetada –** O Resíduo parametrizado para moeda projetada deve estar configurado da seguinte forma:

* No cadastro de componentes verifique se o componente de resíduo escolhido para compor a modalidade de venda, além de ser do tipo resíduo, não tem o campo tipo parcela preenchido. Isto porque o resíduo de moeda projetada compõe a parcela.
* Verifique na modalidade de venda se o parâmetro deste componente de resíduo está marcado: Cálculo do resíduo com moeda projetada.
* O componente Principal tem que ser do tipo MODELO PADRÃO para que ocorra o resíduo.  
      
   A utilização da moeda projetada funciona da seguinte forma:  
   É informado (projetado) um valor (valor não real, ou seja, não imposto pelo governo) para a cotação de uma moeda em um determinado mês que será utilizado na venda.  
   É efetuada a correção Monetária e baixado a parcela deste mês.  
   No mês seguinte, o governo já informou a cotação do mês anterior, então é necessário atualizar esta cotação.  
   Ao efetuar o reajuste de correção do mês atual, o sistema verifica que no mês anterior houve uma atualização, e esta atualização será jogado no componente de Resíduo do mês atual.  
   Para tanto, é necessário estar parametrizado que, a correção monetária será mensal, o parâmetro Cálculo do resíduo com moeda projetada está marcado e os parâmetros de reajustar pela correção e juros também estejam marcados.  
      
   **2 - Resíduo Anual –** O Resíduo parametrizado para gerar uma parcela de resíduo anualmente deve estar configurado da seguinte forma:
* No cadastro de componentes verifique se o componente de resíduo escolhido para compor a modalidade de venda, além de ser do tipo resíduo, tem o campo tipo parcela preenchido. Isto porque este tipo de resíduo gera parcela.
* Verifique na modalidade de venda se o paramento deste componente de resíduo não está marcado: Cálculo do resíduo com moeda projetada.
* Na tela de venda, guia condições da venda, atente para a periodicidade dos componentes de correção monetária(antes e após): deve ser sempre anual.
* O componente Principal tem que ser do tipo MODELO PADRÃO para que ocorra o resíduo.  
      
   Ao utilizar o resíduo no modelo padrão e se os componentes de Correção Monetária e Juros de Contrato forem anuais, as suas datas bases irão ser sempre 1 mês após a data da venda. O sistema sempre irá utilizar a data base do componente de resíduo para efetuar os cálculos.  
      
   **Exemplo:**  
   Data da venda:  01/01/03  
   Data Base Sinal: 01/01/03  
   Data Base Mensal: 01/02/03  
   Data Base CM:  01/02/03  
   Data Base Juros: 01/02/03  
   Data Base Resíduo: 01/01/03  
      
   **Observação:**  
   Sendo resíduo anual, distribuído ou não, ao quitar a ultima parcela do plano de financiamento, se ainda existir resíduo a ser cobrado, será criado uma nova parcela de resíduo para o pagamento da mesma, com a sua data de vencimento setada para o último dia do mês no qual foi pago a última parcela do plano.  
      
   **Atenção:**  
   Para gerar a parcela de resíduo a qualquer instante é necessário entrar na Manutenção de Parcelas, no menu Vendas, selecionar as parcelas que terão o seu valor de resíduo gerado e clicar no ícone "Gerar parcela de Resíduo".  
    

  |  |  |
  | --- | --- |
  |  | Como Fazer |

  ---

  Resíduo Moeda Projetada  
   Resíduo Anual  
   Outras formas de gerar a Parcela de Resíduo
