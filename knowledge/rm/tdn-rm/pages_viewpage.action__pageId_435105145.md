---
content_hash: ac0d12acebd1f8f29853bcf471251b3dd63c52e21ad4fd856a551468e1e18a54
fetched_at: '2026-06-29T00:09:48.409993+00:00'
page_id: '435105145'
product: rm
source: tdn-rm
title: Parâmetro Componente Resíduo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105145
version: 1
---

**Parâmetro Componente Resíduo**

---

Cálculo do resíduo com Moeda Projetada:  
Marque este campo para efetuar o cálculo do resíduo utilizando Moeda Projetada.  
   
Observação:   
Pelo desuso da funcionalidade, aparecerá no plano de financiamento, ao incluir o componente de resíduo e marcar a opção de cálculo com moeda projetada a seguinte mensagem: "Resíduo Projetado será excluído do sistema na versão 12.1.25".  
A partir da versão 12.1.25 esta parte da funcionalidade de resíduo será descontinuada. Caso haja alguma sugestão, contate a equipe de suporte/desenvolvimento do TIN.   
   
   
Resíduo da parcela reajustado mensalmente pelos Juros de Contrato:  
Ao marcar esta opção, o resíduo calculado será reajustado pelos Juros de Contrato.  
   
Observação: Para calcular o reajuste de Juros de contrato do resíduo, tem-se como base o mês do reajuste e o mês da parcela. Acha-se a diferença entre estes meses e multiplica esta diferença pela taxa de Juros e aplica-se este novo valor dos juros no valor do resíduo.  
   
Exemplo: Taxa Juros = 1% Parcela: Fevereiro Reajuste: Maio Resíduo de Fevereiro = R$ 20,00 Diferença entre meses: Maio – Fevereiro = 3 meses Cálculo: 3 meses \* 1% = 3% Reajuste de Resíduo = 3% sobre R$ 20,00 = R$ 20,60  
   
Resíduo da parcela reajustado mensalmente pela Correção Monetária:  
Ao marcar esta opção, o resíduo calculado será reajustado pela Correção Monetária.  
   
Observação: Para calcular o reajuste de Correção Monetária do resíduo, tem-se como base o mês anterior ao mês do reajuste e o mês anterior ao mês de quitação da parcela. Acha-se a variação monetária entre este período e este índice é multiplicado pelo valor do resíduo.  
   
Exemplo: Parcela: Fevereiro Reajuste: Maio Resíduo de Fevereiro = R$ 20,00 Cálculo = Cotação de Abril / Cotação de Janeiro = índice. Reajuste de Resíduo = índice \* R$ 20,00  
   
Reajustar mensalmente as parcelas fora do período de Resíduo:  
Marque este campo para reajustar mensalmente as parcelas fora do período de Resíduo. O período de resíduo é compreendido entre 12 meses. Com o parâmetro marcado todas as parcelas fora deste período serão reajustadas.  
   
NÃO utilizar a mesma regra do grupo para o reajuste da parcela de Resíduo:  
   
Marque este campo quando não quiser utilizar a mesma regra dos componentes já existentes no grupo para efetuar o reajuste de Juros e Correção Monetária do resíduo. Ao marcar este parâmetro, os parâmetros "Reajusta a parcela de Resíduo com a Correção Monetária" e "Reajusta a parcela de Resíduo com o Juros de Contrato" ficarão habilitados.   
Reajusta a parcela de Resíduo com a Correção Monetária:  
Marque este campo para efetuar o reajuste de Correção Monetária do Resíduo diferentemente da regra principal de reajuste da venda. Será habilitado uma sub aba de Correção Monetária, onde poderá ser parametrizado as novas regras de reajuste.  
   
Observação: Este parâmetro somente será habilitado se já estiver sido marcado o parâmetro "NÃO utilizar a mesma regra do grupo para o reajuste da parcela de Resíduo".  
   
Reajusta a parcela de Resíduo com o Juros de Contrato:  
Marque este campo para efetuar o reajuste de Juros do Resíduo diferentemente da regra principal de reajuste da venda. Será habilitado uma sub aba de Juros, onde poderá ser parametrizado as novas regras de reajuste.  
   
Observação: Este parâmetro somente será habilitado se já estiver sido marcado o parâmetro "NÃO utilizar a mesma regra do grupo para o reajuste da parcela de Resíduo".  
Distribuir parcela de Resíduo:  
Com este parâmetro marcado, ao invés de ser criada uma parcela a parte de resíduo, será feito um rateio do valor desta parcela de resíduo entre as parcelas contidas no próximo período de 12 meses.   
   
Atenção: Para que isto ocorra, é necessário criar um componente que tenha o seu tipo de componente igual a "Distribuir Parcela Resíduo". Este componente será utilizado internamente pelo sistema durante o processo de reajuste no momento de distribuir o resíduo, não sendo permitido a utilização do mesmo em qualquer modalidade ou condições de vendas. Este componente pode ter um valor opcional no TOTVS Gestão Financeira ou não, se existir, o valor distribuído do resíduo será gravado no campo opcional informado.  
   
NÃO utilizar juros de contrato no cálculo do Resíduo:  
Marque este campo quando não quiser utilizar o valor dos Juros de Contrato para efetuar o cálculo do resíduo.  
Observação: Como regra do cálculo do resíduo anual, a data base do componente de Correção Monetária e Juros de Contrato devem ser sempre um mês após a data da venda.
