---
content_hash: 29d2487b9709bcef475fcbc8d97f0dee5f3306586401117f7e203a0d52fa5c5e
fetched_at: '2026-06-29T00:10:53.963955+00:00'
page_id: '590043088'
product: rm
source: tdn-rm
title: SEFIP - Afastamento temporário referente aos primeiros 15 (quinze) dias que
  antecedem ao auxílio-doença por motivo de doença ou de acidente (movimentações O3
  e P3) a partir da competência 11/2020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590043088
version: 22
---

false

**A partir das Versões:**

* 12.1.27.337
* 12.1.28.246
* 12.1.29.192
* 12.1.31.103
* Ou superiores

# Objetivo:

---

Apresentar os tratamentos que foram realizados na SEFIP conforme manual 8.4 para Afastamento temporário referente aos primeiros 15 (quinze) dias que antecedem ao auxílio-doença por motivo de doença ou de acidente (movimentações O3 e P3).

---

1true1SEFIPSEFIP2true1Ex. afastamento tipo TExemplo afastamento tipo T

Exemplo Conforme manual SEFIP

Feito o cadastro do afastamento para o funcionário

No envelope de pagamento foram lançadas as seguintes verbas, dias trabalhados, o evento de atestado medico com o código de calculo 445 referente ao período dos quinze dias.

Ao gerar a sefip será gerado o arquivo com o código de ocorrência e a movimentação do afastamento da funcionária conforme print abaixo, será levado o valor de base de cálculo da previdência social (valores dos eventos que incidem em INSS).

campo Movimentação – 05/11/2020 (dia imediatamente anterior ao efetivo afastamento) e o código O3;

campo Movimentação – 20/11/2020 (último dia dos primeiros 15 dias) e o código Z6;

campo Movimentação – 20/11/2020 (último dia dos primeiros 15 dias) e o código O1;

**Observação:**A movimentação para o afastamento correta é a Z6, ao tentar enviar a movimentação com o Z2 conforme manual apresenta erro na simulação do validador.

2Ex. afastamento tipo PExemplo afastamento tipo P

Funcionário entrou com um afastamento do tipo P - Af.Previdência de vinte dias a partir do dia 01/01/2021 ocorrendo afastamento pelo INSS.

Feito o cadastro do afastamento para o funcionário

No envelope de pagamento foram lançadas as seguintes verbas, dias trabalhados, o evento de atestado medico com o código de calculo 445 referente ao período dos quinze dias.

Ao gerar a sefip será gerado o arquivo com o código de ocorrência e a movimentação do afastamento da funcionária conforme print abaixo, será levado o valor de base de cálculo da previdência social (valores dos eventos que incidem em INSS).

campo Movimentação – 31/12/2020 (dia imediatamente anterior ao efetivo afastamento) e o código P3;

campo Movimentação – 20/01/2021 (último dia dos primeiros 15 dias) e o código Z5;

campo Movimentação – 20/11/2020 (último dia dos primeiros 15 dias) e o código P1;

campo Movimentação – 20/01/2020 (último dia do afastamento) e o código Z5;

3Ex. afastamento tipo OExemplo afastamento tipo O

Funcionário entrou com um afastamento do tipo O - Doença Ocupacional de cinco dias a partir do dia 01/01/2021, após dez dia entrou com outro afastamento de mais quinze do tipo O - Doença Ocupacional ocorrendo afastamento pelo INSS

Feito o cadastro do afastamento para o funcionário

No envelope de pagamento foram lançadas as seguintes verbas, dias trabalhados, o evento de atestado medico com o código de calculo 445 referente ao período dos quinze dias.

Ao gerar a sefip será gerado o arquivo com o código de ocorrência e a movimentação do afastamento da funcionária conforme print abaixo, será levado o valor de base de cálculo da previdência social (valores dos eventos que incidem em INSS).

campo Movimentação – 31/12/2020 (dia imediatamente anterior ao efetivo afastamento) e o código O3;

campo Movimentação – 05/01/2021 (último dia do primeiro afastamento) e o código Z6;

campo Movimentação – 14/01/2021 (dia imediatamente anterior ao efetivo afastamento) e o código O3;

campo Movimentação – 24/01/2020 (último dia do primeiro afastamento) e o código Z6;

campo Movimentação – 24/01/2021 (dia imediatamente anterior ao efetivo afastamento) e o código O1;

campo Movimentação – 29/01/2020 (último dia do afastamento) e o código Z2;

4Ex. afastamento tipo P e licença maternidadeExemplo afastamento tipo P e licença maternidade

Exemplo Conforme manual SEFIP

Feito o cadastro do afastamento para o funcionário

 

**Novembro**

No envelope de pagamento foram lançadas as seguintes verbas, dias trabalhados, o evento de atestado medico com o código de calculo 445 referente ao período dos quinze dias.

Ao gerar a sefip será gerado o arquivo com o código de ocorrência e a movimentação do afastamento da funcionária conforme print abaixo, será levado o valor de base de cálculo da previdência social (valores dos eventos que incidem em INSS).

campo Movimentação – 04/11/2020 (dia imediatamente anterior ao efetivo afastamento) e o código P3;

campo Movimentação – 19/11/2020 (último dia dos primeiros 15 dias) e o código Z5;

campo Movimentação – 19/11/2020 (último dia dos primeiros 15 dias) e o código P1;

**Dezembro**

No envelope de pagamento foram lançadas as seguintes verbas, dias trabalhados, o evento de  licença-maternidade, por motivo de aborto não criminoso.

Ao gerar a sefip será gerado o arquivo com o código de ocorrência e a movimentação do afastamento da funcionária conforme print abaixo, será levado o valor de base de cálculo da previdência social (valores dos eventos que incidem em INSS).

campo Movimentação – 19/11/2020 (último dia dos primeiros 15 dias) e o código P1;

campo Movimentação – 06/12/2020 (último dia do afastamento) e o código Z5;

campo Movimentação – 06/12/2020 (dia imediatamente anterior a licença maternidade) e o código Q3;

campo Movimentação – 20/12/2020  (último dia da licença maternidade) e o código Z1;

campo Movimentação – 20/12/2020  (dia imediatamente anterior ao efetivo afastamento) e o código P2;

campo Movimentação – 29/12/2020  (último dia do afastamento) e o código Z5;
