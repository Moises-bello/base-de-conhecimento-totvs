---
content_hash: 3f5301132eb0aae687b5f42cd7e5fb808ccd5229ab8d6b0b24a3a5962439c0c1
fetched_at: '2026-06-29T00:10:03.227757+00:00'
page_id: '452719062'
product: rm
source: tdn-rm
title: RECESSO REMUNERADO PARA ESTAGIÁRIO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719062
version: 1
---

**RECESSO REMUNERADO PARA ESTAGIÁRIO**

---

É assegurado ao estagiário, sempre que o estágio tenha duração igual ou superior a 1 (um) ano, período de recesso de 30 (trinta) dias, a ser gozado preferencialmente durante suas férias escolares.  
   
O recesso de que trata este artigo deverá ser remunerado quando o estagiário receber bolsa ou outra forma de contraprestação.  
   
Os dias de recesso serão concedidos de maneira proporcional, nos casos de o estágio ter duração inferior a 1 (um) ano.  
Considerando que o estágio pode ser celebrado pelo prazo mínimo de seis meses, correspondente a um semestre letivo, neste caso, o recesso, que corresponde a quinze dias, deverá ser concedido, por exemplo, após cinco meses e quinze dias de atividades, podendo o estagiário usufruir do recesso de quinze dias, até o término do compromisso de estágio.  
   
No caso de celebração de termo de compromisso de estágio anual, por simetria, o recesso se dará nos últimos trinta dias, quando o estagiário já deverá haver cumprido a sua parte daquilo a que se responsabilizou.  
   
**Observação:** Conforme citado no Artigo 13 da Lei especifica, Estagiários não tem direito a Férias, mas sim a um Recesso Remunerado.  
No parametrizador, em Férias / controle , marque o parâmetro "Considera tratamento para Recesso de Estagiário" para considerar o tratamento do Recesso de Estagiário.  
O cadastro do período de recesso do estagiário será realizado na mesma interface utilizada para o cadastro de férias. Observando que, no caso do recesso, diversos recursos serão desabilitados por não estarem associados ao recesso, conforme abaixo:

* Não poderá optar por 1a parcela 13º salário se for tipo T – Estagiário.
* Não poderá optar por recebimento de abono pecuniário.
* Não poderá optar por empréstimo de férias.
* Não haverá tratamento para pagamento de licença remunerada (férias coletivas).
* Não haverá consulta ao recibo de férias uma vez que os códigos de cálculo utilizados no cálculo de Férias não serão utilizados no cálculo do Recesso. O pagamento dos dias de recesso será realizado junto ao pagamento da bolsa.

O lançamento do recesso para a folha será realizado através do botão <Lançar>.  
Ao executar este processo será lançado para a folha o evento "RECESSO BOLSA ESTAGIO", e a situação do funcionário será alterada para G – "Recesso Remunerado Estágio". Quando for lançado o evento com código de cálculo 332 - RECESSO DE ESTÁGIO, este não poderá ser recalculado.  
   
O evento "RECESSO BOLSA ESTAGIO" será calculado e lançado no envelope de pagamento de acordo com o número total de dias de recesso, independente do fato dos dias serem compreendidos no mês atual ou no próximo mês.  
   
O valor base para o cálculo do RECESSO será o valor da Bolsa Estágio (cadastrado no campo Salário, do cadastro de funcionários) somado ao valor dos eventos que incidem salário. Este evento que incide em salário deverá ser lançado previamente no movimento da competência atual do estagiário.  
   
O término do período de recesso será realizado através do botão <Finalizar>. Ao executar este processo a situação do estagiário retornará para Ativo.  
   
Para as empresas que utilizam o código de cálculo 2 – DIAS TRABALHADOS no evento de "Bolsa Estágio", o sistema calculará o valor deste evento proporcional ao número de dias trabalhados no mês, considerando o número de dias de recesso no mês.  
   
**Exemplo:**  
Estagiário com valor da Bolsa de R$ 1.200,00   
Recesso do dia 16/06 a 05/07 (20 dias de recesso)  
   
Envelope de pagamento do mês de junho  
===============================  
Bolsa Estágio 15 dias 600,00  
Recesso          20 dias 800,00  
   
Envelope de pagamento do mês de julho  
===============================  
Bolsa Estágio 25 dias 1.000,00  
   
Será lançado recesso remunerado como verbas rescisórias quando o estagiário com contrato rescindido tem:

* Direito ao recesso proporcional para demitidos com menos 1 ano.
* Direito ao recesso indenizado no caso mais de um ano.

Verificando as seguintes condições:

* O parâmetro "Recebem verbas rescisórias" Estagiário deve estar desmarcado no parametrizador.
* Os eventos com códigos de Cálculo 333 - RECESSO DE ESTÁGIO VENCIDO e 334 - RECESSO DE ESTÁGIO PROPORCIONAL devem ser criados no cadastro de eventos. E será sempre lançado o recesso vencido e o recesso proporcional, independente do tipo de rescisão.

O controle de períodos aquisitivos para o recesso terá funcionamento semelhante ao já existente para férias de funcionários normais, onde a cada período de 12 meses o estagiário terá direito a 30 dias de recesso. O recesso poderá ser parcelado em mais de um período.  
No cadastro de períodos aquisitivos serão visualizados apenas o período aquisitivo atual e os anteriores, o novo período aquisitivo somente será criado após o estagiário finalizar os 30 dias de recesso do período atual, a criação deste novo período aquisitivo acontecerá no momento em que for processada a rotina "Finalizar Recesso".  
Para efeito de Histórico de Provisão cada mês estagiado dará direito a 2,5 dias de recesso.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Para informação mais detalhada sobre a lei consulte: [{+}](http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm)<http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm+>
