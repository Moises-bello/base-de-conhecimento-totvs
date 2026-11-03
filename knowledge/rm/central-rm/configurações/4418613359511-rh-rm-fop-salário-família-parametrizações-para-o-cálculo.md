---
article_id: 4418613359511
category: Configurações
content_hash: c424cc51b15d23096627345cd4a6cea9b1bec5592c9e1765b81b8ae7e4c5d9b3
fetched_at: '2026-06-28T22:46:49.539502+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Salário Família: parametrizações para o cálculo'
type: support-article
updated_at: '2024-09-16T18:35:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418613359511-RH-RM-FOP-Sal%C3%A1rio-Fam%C3%ADlia-parametriza%C3%A7%C3%B5es-para-o-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26409178170263) Tempo aproximado para leitura: **00:01:50 min****Dúvida**Quais as opções de parametrização para o cálculo do salário família?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**As opções de parametrização para o cálculo do Salário Família estão disponibilizadas no seguinte caminho: **Configurações | Parametrizador | Folha Normal | Salário Família.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26409178179351)

* **Proporcional admissão/demissão:** Com este parâmetro marcado, o sistema irá calcular o salário família proporcionalizando em casa de admissão e demissão. O sistema considerará o número de dias de trabalho efetivos no mês de admissão/demissão. Caso contrário, irá considerar valor integral para pagamento.
* **Considera dias do mês p/ proporcionalização:** Marcando este parâmetro, o sistema irá proporcionalizar o salário família, dividindo pelo número de dias do mês, por exemplo, 28, 29, 30 ou 31, e multiplicando pelo número de dias trabalhados no mês. Caso contrário, o sistema irá dividir por 30 e multiplicar pelo número de dias trabalhados no mês. Este parâmetro somente ficará habilitado se o campo **Proporcional admissão/demissão** estiver marcado.
* **Dependente menor de 1 anos s/cartão vacina:** Com este parâmetro marcado, será considerado para pagamento de salário família, o dependente menor de 1 ano e com o parâmetro **Entregou Cartão Vacina** desmarcado na aba **identificação do cadastro de dependentes**.
* **Paga p/ afastados previdência:** Marcando este parâmetro, o sistema irá calcular o salário família para afastados pelo previdência, durante todo o período de afastamento. Em conformidade com o **Decreto 3048/99, art. 82,** e a **Instrução Normativa 20/2000, art. 185**, observa-se que é de responsabilidade da Empresa o pagamento do Salário família durante o período em que a empregada estiver percebendo salário maternidade. Não estando no conceito de afastamento pela previdência.
* **Paga p/ funcionários temporários:** Com este parâmetro marcado, será pago o salário família para os funcionários temporários.
* **Usa salário nominal:** Com este parâmetro marcado, será considerado, para cálculo da faixa do salário família a ser pago, o salário base mais os eventos que incidem salário família. Se o parâmetro não for marcado, o sistema assumirá o valor recebido do evento com Código de Cálculo 1 e/ou Código de Cálculo 2 mais os eventos incidentes em salário família. Ou seja, se o parâmetro **Usa salário nominal** estiver marcado os códigos de cálculos 1,2 e 145 não podem ter incidência em salário família ou se o parâmetro **Usa salário nominal** estiver desmarcado os códigos de cálculos 1,2 e 145 devem ter incidência em salário família. Para admitidos e demitidos no mês, o sistema sempre considerará para cálculo da base do salário família, o salário do cadastro mais todos os eventos lançados que possuírem incidência em salário família, independente da incidência dos códigos de cálculos 1,2 e 145.
* **Desconsidera múltiplos vínculos:** Com este parâmetro marcado será desconsiderado os funcionários múltiplos vínculos.

**Saiba mais**  
[Dependentes](https://tdn.totvs.com/display/public/LRM/Dependentes)
