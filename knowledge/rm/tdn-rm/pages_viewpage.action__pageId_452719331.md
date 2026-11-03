---
content_hash: a5ac832d321eae84ec66e0bcf50dad4f57ffe843430ad120ec5ad87e091c9b79
fetched_at: '2026-06-29T00:10:06.703812+00:00'
page_id: '452719331'
product: rm
source: tdn-rm
title: Controle 1/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719331
version: 3
---

Nesta etapa são definidos alguns controles para as férias  
   
**Parâmetros e Campos**  
Lança salário família e contribuição sindical (março)  
Com este parâmetro marcado, o sistema irá lançar o evento com o Código de Cálculo 149 - Salário Família nas Férias e o evento de Código de Cálculo 12 - Contribuição Sindical, somente no mês de Março, sejam lançados automaticamente no recibo de férias para os funcionários durante o mês todo.

**Observações**

* + Estes funcionários precisam estar saindo de férias durante todo o mês para que o evento seja lançado em somente um recibo (férias)
  + Para o correto pagamento do salário família nas férias, o usuário deverá fazer as seguintes parametrizações quando o parâmetro 'Usa salário nominal' não está marcado em Configurações | Parâmetros |Parametrizador | Folha Normal | Salário Família:
    - Todos os eventos que irão incidir na base de salário família, inclusive os eventos com os códigos de cálculos de férias (CC 38 e CC 40), deverão está incidindo em salário família.
    - O evento de CC 149, deverá possuir prioridade maior que os eventos que incidem salário família.

**Exemplo**  
CC 38 prioridade 0 (zero)  
CC 40 prioridade 1 (um)  
CC 149 prioridade deverá ser maior que 1 (um)

* Para o correto pagamento do salário família nas férias, o usuário deverá fazer as seguintes parametrizações quando o parâmetro 'Usa salário nominal' está marcado em Configurações | Parâmetros |Parametrizador | Folha Normal | Salário Família
  + Os eventos não poderão incidir na base de salário família.
  + O evento de CC 149 poderá possuir qualquer prioridade.

**Atenção**  
Quando é acessando o parâmetrizador na etapa controle, o sistema emite uma mensagem informando ao usuário que é necessário cadastrar o evento de código de cálculo 149 para o perfeito funcionamento do lançamento do salário família nas férias.

Acerto de período aquisitivo obrigatório  
Com este parâmetro marcado, torna obrigatório o acerto de período aquisitivo antes de gerar o histórico de Provisões.  
   
Lança adiantamento de abono separado dos valores de férias  
Com este parâmetro marcado será lançado no envelope de pagamento do funcionário os valores pagos de abono pecuniário de férias separado dos valores de férias no mês no evento de desconto de adiantamento de férias, sendo o adiantamento de férias no mês lançado no evento de CC 45 e o adiantamento de abono pecuniário lançado no evento de CC 378.

**Exemplo**  
Funcionário com 20 dias de férias e 10 de abono pecuniário, foram lançadas as seguintes no recibo de férias:

|  |  |  |
| --- | --- | --- |
| CC | Prov./Desc./Base | Referencia |
| CC 38 | 4.984,07 | 20 |
| CC 39 | 2.492,04 | 10 |
| CC 40 | 1.676,46 | 20 |
| CC 56 | 838.23 | 10 |
| CC 0 | 45,21 | 0 |
| CC 47 | 22,65 | 0 |
| CC 82 | 384,86 | 11 |
| CC 30 | 1.781,05 | 27,5 |

No envelope de pagamento foi lançada as verbas acima e os eventos de adiantamento ficou com os seguintes valores:  
CC 378: R$ 3.352,92 - Que a soma dos eventos de CC 47, 56 e 39  
CC 43: R$ 4.539,92 - Que a soma dos eventos dos demais eventos menos os eventos de desconto de INSS e IRFF.  
   
**Observação**  
O adiantamento de férias continua sendo lançado no evento de CC 45, porém será desconsiderado os valores pagos de abono pecuniário,  1/3 de abono pecuniário, média de abono pecuniário.  
Os eventos de desconto de INSS e IRRF serão abatidos somente no evento de CC 45, mesmo que no abono pecuniário tenha incidência em IRRF de Férias e INSS. Isto é feito desta forma, pois não tem como separar as bases de cálculo e caso seja separadas o valor da base será menor, podendo até mesmo não ter o desconto, no caso do IRRF de férias, ficando com valores de desconto dos encargos inconsistentes.   
Caso o parâmetro esteja desmarcado, o lançamento do adiantamento de férias continua sendo feito o valor integral do liquido no evento de CC 45.  
   
**Atenção**  
Para o correto funcionamento do parâmetro, é necessário que o evento com o CC 378 esteja cadastrado na base. Caso o evento não esteja cadastrado na base, é emitido uma mensagem de erro no processo de lançamento de férias e o mesmo não é concluído.

Considera tratamento para Recesso de Estagiário  
É assegurado ao estagiário, sempre que o estágio tenha duração igual ou superior a 1 (um) ano, período de recesso de 30 (trinta) dias, a ser gozado preferencialmente durante suas férias escolares.   
O recesso de que trata este artigo deverá ser remunerado quando o estagiário receber bolsa ou outra forma de contraprestação.  
Os dias de recesso serão concedidos de maneira proporcional, nos casos de o estágio ter duração inferior a 1 (um) ano.  
Considerando que o estágio pode ser celebrado pelo prazo mínimo de seis meses, correspondente a um semestre letivo, neste caso, o recesso, que corresponde a quinze dias, deverá ser concedido, por exemplo, após cinco meses e quinze dias de atividades, podendo o estagiário usufruir do recesso de quinze dias, até o término do compromisso de estágio.   
No caso de celebração de termo de compromisso de estágio anual, por simetria, o recesso se dará nos últimos trinta dias, quando o estagiário já deverá haver cumprido a sua parte daquilo a que se responsabilizou.  
   
Conforme citado no Artigo 13 da Lei especifica, Estagiários não tem direito a Férias, mas sim a um Recesso Remunerado. Para que o sistema considere o tratamento do Recesso de Estagiário é necessário que o parâmetro "Considera tratamento para Recesso de Estagiário" esteja marcado.  
Com este parâmetro marcado, o cadastro do período de recesso do estagiário será realizado na mesma interface utilizada para o cadastro de férias. Observando que, no caso do recesso, diversos recursos serão desabilitados por não estarem associados ao recesso, conforme abaixo:

* Não poderá optar por 1a parcela 13º salário se for tipo T – Estagiário.
* Não poderá optar por recebimento de abono pecuniário.
* Não poderá optar por empréstimo de férias.
* Não haverá tratamento para pagamento de licença remunerada (férias coletivas).
* Não haverá consulta ao recibo de férias uma vez que os códigos de cálculo utilizados no cálculo de Férias não serão utilizados no cálculo do Recesso. O pagamento dos dias de recesso será realizado junto ao pagamento da bolsa.

O lançamento do recesso para a folha será realizado através do botão 'Lançar'.   
Ao executar este processo será lançado para a folha o evento com código de cálculo 332 - RECESSO DE ESTÁGIO, e a situação do funcionário será alterada para G – "Recesso Remunerado Estágio".   
Quando for lançado o evento com CC 332, este não poderá ser recalculado. O evento será calculado e lançado no envelope de pagamento de acordo com o número total de dias de recesso, independente do fato dos dias serem compreendidos no mês atual ou no próximo mês.   
O valor base para o cálculo do RECESSO será o valor da Bolsa Estágio (cadastrado no campo Salário, do cadastro de funcionários) somado ao valor dos eventos que incidem salário. Este evento que incide em salário deverá ser lançado previamente no movimento da competência atual do estagiário.   
O término do período de recesso será realizado através do botão 'Finalizar'. Ao executar este processo a situação do estagiário retornará para Ativo.  
Para as empresas que utilizam o código de cálculo 2 – DIAS TRABALHADOS no evento de "Bolsa Estágio", o sistema calculará o valor deste evento proporcional ao número de dias trabalhados no mês, considerando o número de dias de recesso no mês.

**Exemplo**  
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
   
Lança Recesso de Estagiário proporcional aos dias de cada competência  
   
   
Média de saldo na provisão de férias considerando somente dias úteis  
   
   
Provisão de férias desconsidera avo em mês de 30 dias para admitido no dia 17  
   
   
Evento para pagamento do complemento salarial, quando período de férias atinge 3 meses  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Para informação mais detalhada sobre a lei do Recesso Estagiário, consulte: <http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm>  
   
<< Retornar para **Férias**
