---
content_hash: 183b355a190c54fe67b6f5b9e973ee74d5afbda1a4e3904fb5c587051dce7f7c
fetched_at: '2026-06-29T00:10:07.270466+00:00'
page_id: '452719389'
product: rm
source: tdn-rm
title: Salário Família folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719389
version: 3
---

Etapa que define algumas opções de cálculo do salário família  
   
**Parâmetros**  
Proporcional admissão/demissão  
Com este parâmetro marcado, o sistema irá calcular o salário família proporcionalizando em casa de admissão e demissão. O sistema considerará o número de dias de trabalho efetivos no mês de admissão/demissão. Caso contrário, irá considerar valor integral para pagamento.  
   
Considera dias do mês p/ proporcionalização  
Marcando este parâmetro, o sistema irá proporcionalizar o salário família, dividindo pelo número de dias do mês (28, 29, 30 ou 31) e multiplicando pelo número de dias trabalhados no mês. Caso contrário, o sistema irá dividir por 30 e multiplicar pelo número de dias trabalhados no mês.

**Observação**

Este parâmetro somente ficará habilitado se o campo 'Proporcional admissão/demissão' estiver marcado.  
Dependente menor de 1 anos s/cartão vacina  
Com este parâmetro marcado, será considerado para pagamento de salário família, o dependente menor de 1 ano e com o parâmetro 'Entregou Cartão Vacina' desmarcado na aba identificação do cadastro de dependentes.   
   
Paga p/ afastados previdência  
Marcando este parâmetro, o sistema irá calcular o salário família para afastados pelo previdência, durante todo o período de afastamento.

**Observação**  
Em conformidade com o decreto 3048/99, art. 82, e a instrução normativa 20/2000, art. 185, observa-se que é de responsabilidade da Empresa o pagamento do Salário família durante o período em que a empregada estiver percebendo salário maternidade. Não estando no conceito de afastamento pela previdência.   
Paga p/ funcionários temporários  
Com este parâmetro marcado, será pago o salário família para os funcionários temporários.   
   
Usa salário nominal  
Com este parâmetro marcado, será considerado, para cálculo da faixa do salário família a ser pago, o salário base mais os eventos que incidem salário família.   
Se o parâmetro não for marcado, o sistema assumirá o valor recebido do evento com Código de Cálculo 1 e/ou Código de Cálculo 2 mais os eventos incidentes em salário família.

Ou seja,

* Se o parâmetro "Usa salário nominal" estiver marcado os CCs 1,2 e 145 não podem ter incidência em salário família.
* Se o parâmetro "Usa salário nominal" estiver desmarcado os CCs 1,2 e 145 devem ter incidência em salário família.

**Observação**  
Para admitidos e demitidos no mês, o sistema sempre considerará para cálculo da base do salário família, o salário do cadastro mais todos os eventos lançados que possuírem incidência em salário família, independente da incidência dos CCs 1,2 e 145.

Desconsidera múltiplos vínculos  
   
   
   
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<< Retornar para **Folha de Pagamento**
