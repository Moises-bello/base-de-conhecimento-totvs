---
content_hash: 2226f9299121b9238e1a9da3e7a4caf97a75e74b7c541b8972c4c94356a95dee
fetched_at: '2026-06-29T00:11:42.829694+00:00'
page_id: '799265691'
product: rm
source: tdn-rm
title: Fundo Promocional - Geração de Aluguel Complementar no Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799265691
version: 6
---

### Introdução

---

Existem momentos em que haverá a necessidade do fundo promocional percentual ser cobrado juntamente ao aluguel complementar. No intuito de flexibilizar esse tipo de cobrança, passamos a utilizar a opção "Considerar somente no faturamento" para realizar esse cálculo. Esta opção poderá ser selecionada ao associar um contrato de locação ao template de fundo promocional, que deverá ser definido como percentual. Resumindo, teremos as premissas abaixo:

* Template de Fundo Promocional do tipo "Percentual";
* Contrato de locação associado ao Template e parametrizado com a opção "Considerar somente no faturamento".

Estando atendidas estas premissas o sistema passará a considerar o fundo promocional na geração dos lançamentos de aluguel complementar. Abaixo, seguem alguns exemplos de cálculos para facilitar o entendimento da funcionalidade

### Exemplos de cálculos

---

Os cálculos abaixo são ilustrativos. Representam um contrato de locação que possui fundo promocional e o mesmo sendo gerado através do aluguel complementar.

CONSIDERA FPP COM CTO PERCENTUAL E ALUGUEL FIXO

Neste contrato temos

* Aluguel fixo de R$ 2500,00;
* CTO Percentual de 10%;
* Opção de considerar Fundo Promocional no contrato de locação marcada;
* Encargos no valor de R$ 2000,00.
* Faturamento na competência de 150.000,00

Ao gerar o aluguel complementar, teremos a geração do fundo promocional. O sistema irá calcular da seguinte forma:

Valor do faturamento: [150.000,00]  
Percentual sobre faturamento: [10,00%]  
Aluguel Complementar : (Valor do faturamento \* percentual) [150.000,00 \* 10,00% = 15.000,00]

Cálculo do fundo promocional no faturamento

Percentual do fundo promocional: [12,00%]  
Considerar condomínio: [Sim]  
Condomínio: [2000,00]  
Considerar fundo promocional: [Sim]  
Fundo Promocional: [300,00] + [1224,00]  
Considerar Locação: [Sim]  
Locação : [2500,00]  
Fórmula Custos totais ...........: ((Calc.Faturamento - (Locação + Condominio + FundoP. )) \* %FundoP.)  
Valores na Fórmula Custos totais : ((15000,0 - (2500 + 2000 + 300 )) \* 12%)  
Valor cálculo Custos totais .....: [**1224,00**]

Considerar condomínio: [Sim]  
Condomínio: [2000,00]

Considerar fundo promocional: [Sim]  
Fundo Promocional: [300,00]

Cálculo do valor do aluguel complementar (faturamento - valor do aluguel + valor do condomínio + valor do fundo promocional):  
15.000,00 - 6.024,00 = **8.976,00**

CONSIDERA FPP COM CTO MENSAL E ALUGUEL VARIAVEL

Neste contrato temos

* Aluguel variável;
* CTO Percentual de 10%;
* CTO Mensal de R$ 2500,00;
* Opção de considerar Fundo Promocional no contrato de locação marcada;
* Encargos no valor de R$ 2000,00.
* Faturamento na competência de 150.000,00

Ao gerar o aluguel complementar, teremos a geração do fundo promocional. O sistema irá calcular da seguinte forma:

Valor do faturamento: [150.000,00]  
Percentual sobre faturamento: [10,00%]  
Aluguel Complementar: (Valor do faturamento \* percentual) [150.000,00 \* 10,00% = 15.000,00]

Cálculo do fundo promocional no faturamento

Percentual do fundo promocional: [12,00%]  
Considerar condomínio: [Sim]  
Condomínio: [2000,00]  
Considerar fundo promocional: [Sim]  
Fundo Promocional : [53,57] + [1493,57]  
Considerar Locação: [Sim]  
Locação : [500]  
Fórmula Custos totais : ((Calc.Faturamento - (Locação + Condominio + FundoP. )) \* %FundoP.)  
Valores na Fórmula Custos totais : ((15000,0 - (500 + 2000 + 53,57 )) \* 12%)  
Valor cálculo Custos totais .....: [**1493,57**]

Considerar condomínio : [Sim]  
Condomínio : [2000]

Considerar fundo promocional : [Sim]  
Fundo Promocional : [53,57]  
Cálculo do valor do aluguel complementar (faturamento - valor CTO fixo (Valor Mensal)):  
15.000,00 - 4.047,14 = **10.952,86**

NÃO CONSIDERA FPP COM CTO PERCENTUAL E ALUGUEL FIXO

Neste contrato temos

* Aluguel fixo de R$ 2500,00;
* CTO Percentual de 10%;
* Opção de considerar Fundo Promocional no contrato de locação desmarcada;
* Encargos no valor de R$ 2000,00.
* Faturamento na competência de 150.000,00

Ao gerar o aluguel complementar, teremos a geração do fundo promocional. O sistema irá calcular da seguinte forma:

Valor do faturamento: [150.000,00]  
Percentual sobre faturamento: [10,00%]  
Aluguel Complementar: (Valor do faturamento \* percentual) [150.000,00 \* 10,00% = 15.000,00]

Cálculo do fundo promocional no faturamento

Percentual do fundo promocional: [8,00%]  
Considerar condomínio: [Sim]  
Condomínio: [2000,00]  
Considerar fundo promocional: [Não]  
Fundo Promocional: [0] + [840,00]  
Considerar Locação: [Sim]  
Locação: [2500,00]  
Fórmula Custos totais ...........: ((Calc.Faturamento - (Locação + Condominio + FundoP. )) \* %FundoP.)  
Valores na Fórmula Custos totais : ((15000,0 - (2500 + 2000 + 0 )) \* 8%)  
Valor cálculo Custos totais: [**840,00**]

Considerar condomínio: [Sim]  
Condomínio: [2000,00]

Cálculo do valor do aluguel complementar (faturamento - valor do aluguel + valor do condomínio):  
15.000,00 - 4.500,00 = **10.500,00**

NÃO CONSIDERA FPP COM CTO MENSAL E ALUGUEL ZERO

Neste contrato temos

* Aluguel variável;
* CTO Percentual de 5%;
* Opção de considerar Fundo Promocional no contrato de locação desmarcada;
* Encargos no valor de R$ 2000,00.
* Faturamento na competência de 150.000,00

Ao gerar o aluguel complementar, teremos a geração do fundo promocional. O sistema irá calcular da seguinte forma:

Valor do faturamento: [150.000,00]  
Percentual sobre faturamento: [5,00%]  
Aluguel Complementar: (Valor do faturamento \* percentual) [150.000,00 \* 5,00% = 7.500,00]

Cálculo do fundo promocional no faturamento

Percentual do fundo promocional: [10,00%]  
Considerar condomínio: [Sim]  
Condomínio: [2000,00]  
Considerar fundo promocional: [Não]  
Fundo Promocional: [0] + [250,00]  
Considerar Locação: [Sim]  
Locação: [2678,57]  
Fórmula Custos totais ...........: ((Calc.Faturamento - (Locação + Condominio + FundoP. )) \* %FundoP.)  
Valores na Fórmula Custos totais : ((7500,00 - (3000 + 2000 + 0 )) \* 10%)  
Valor cálculo Custos totais: [**250,00**]

Considerar condomínio: [Sim]  
Condomínio: [2000,00]

Cálculo do valor do aluguel complementar (faturamento - valor CTO fixo (Valor Mensal)):  
7.500,00 - 5000,00 = **2.500,00**

### **Cancelamento do Fundo Promocional gerado no aluguel complementar**

---

Para cancelarmos os lançamentos de fundo promocional gerados durante o aluguel complementar, basta utilizar o processo de cancelar aluguel complementar. Este processo além de cancelar os lançamentos de aluguel complementar, irá também cancelar todos os lançamentos de fundo promocional associados à competência.

Importante

* Caso o contrato de locação esteja associado também a algum template de fundo promocional que não é gerador no aluguel complementar, a forma de cancelamento para estes lançamentos de fundo promocional não irá mudar. Neste cenário, para cancelar o lançamento de fundo, basta cancelar os lançamentos financeiros ou utlizar o processo de cancelar os lançamentos de fundo promocional, caso seja gerado de forma isolada.
* Quando no contrato a opção "considera fundo promocional" estiver marcada, vale lembrar que os cálculos do aluguel complementar serão baseados nas parcelas de fundo promocional geradas na mesma competência da medição.
