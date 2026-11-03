---
content_hash: 4c8d5ea70779d052e50faf64ca700043f76c1a2257ef31cfd0ebaa48fff17b1b
fetched_at: '2026-06-29T00:11:44.294971+00:00'
page_id: '811724167'
product: rm
source: tdn-rm
title: Condomínio - Fechamento do Condomínio - Cálculos Pró-Rata
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=811724167
version: 8
---

### Introdução

---

O termo "pro-rata" significa proporcional. Ao usar o cálculo pro-rata em cobranças de condomínio, você está ajustando as despesas de acordo com a proporção de tempo que um proprietário ocupou a unidade durante um determinado período.

A fórmula básica do cálculo pro-rata é:

Valor Pro-rata = (Número de Dias Ocupados​/Total de Dias no Mes) × Valor Total Mensal

Isso garante que os proprietários paguem apenas pela parte do mês em que ocuparam a unidade. Se alguém ocupou o condomínio por metade do mês, por exemplo, eles pagariam metade do valor mensal. O cálculo é flexível e pode ser aplicado a diferentes períodos, dependendo da necessidade.  
***A partir da atualização mais recente, o sistema passa também a considerar períodos específicos de fechamento configurados para apuração da cobrança, e não apenas o mês completo.***

#### Mês Civil e Comercial

O "mês civil" refere-se ao mês comum que utilizamos no calendário, com 28, 30 ou 31 dias, enquanto o "mês comercial" geralmente é considerado composto por 30 dias. Quando aplicamos o cálculo pro-rata em cobranças de condomínio, podemos ter um cenário diferente dependendo da parametrização do sistema.

Vamos ver dois exemplos:

### Exemplo 1: Mês Civil de 31 dias

Suponha que o valor mensal do condomínio seja R$ 1.000.

* Se um morador ocupou a unidade por 15 dias em um mês civil de 31 dias:

Valor Pro-rata = (1531)×1.000 = R$483,87 Valor Pro-rata = (3115​)×1.000 = R$483,87

* Se um morador ocupou a unidade por 20 dias no mesmo mês:

Valor Pro-rata = (2031)×1.000 = R$645,16 Valor Pro-rata = (3120​)×1.000 = R$645,16

### Exemplo 2: Mês Comercial de 30 dias

Agora, considere o mesmo valor mensal de R$ 1.000.

* Para um morador que ocupou a unidade por 15 dias em um mês comercial de 30 dias:

Valor Pro-rata = (1530)×1.000 = R$500 Valor Pro-rata = (3015​)×1.000 = R$500

* Se a ocupação foi de 20 dias no mesmo mês comercial:

Valor Pro-rata = (2030)×1.000 = R$666,67 Valor Pro-rata = (3020​)×1.000 =R$666,67

Esses exemplos ilustram como o cálculo pro-rata ajusta as cobranças do condomínio com base na proporção de dias ocupados em relação ao total de dias no mês civil ou comercial.

### Exemplo 3: Mês Comercial de 30 dias, calculando vacância

No cálculo de vacância, o sistema contabiliza os dias vagos dentro de um período específico, subtraindo esses dias dos dias totais do mês. Neste caso, será considerado o mês comercial de 30 dias (até 30/08/2024).

Neste exemplo temos dois contratos dentro desse período:

1. **Contrato de 01/08/2024 a 15/08/2024**: Os dias ocupados vão de 01/08/2024 a 15/08/2024, totalizando **15 dias ocupados**.
2. **Contrato de 20/08/2024 a 31/08/2024**: Neste contrato, os dias ocupados são de 20/08/2024 a 31/08/2024, resultando em **12 dias ocupados**.

Somando os dias ocupados de ambos os contratos:

* 15 dias ocupados (do primeiro contrato)
* 12 dias ocupados (do segundo contrato)

Totalizando **27 dias ocupados**.

Agora, para calcular a vacância:

* O total de dias considerados é 30 (mês comercial).
* Subtraindo os 27 dias ocupados: 30 - 27 = **3 dias de vacância**.

Portanto, a vacância será de **3 dias** no mês de agosto, considerando o uso do mês comercial até o dia 30.  
  
Procedimentos para Utilização

---

Para a utilização do cálculo pro rata é necessário que o item de cobrança esteja marcado com a opção "Utiliza Pró-Rata:

E o contrato de locação, também deverá estar marcado com a opção "Utiliza Pró-Rata":

Estando os pré requisitos acima selecionados o sistema irá passar a considerar o cálculo Pró-Rata nos fechamentos de condomínio.

Abaixo, seguem alguns exemplos onde o sistema irá considerar Pró-Rata.

### Contrato Iniciando no meio do período

---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Inicio Vigência | Fim Vigência | Inicio Locação | Fim 1º Locação | Valor Contrato | Mês CIVIL |
| 17/09/2023 | - | 17/09/2023 | 30/09/2023 | R$ 2.000,00 | Sim |

|  |  |  |  |
| --- | --- | --- | --- |
| Inicio Parcela | Fim Parcela | dias Cobrados | dias Mês |
| 17/09/2023 | 30/09/2023 | 14 | 30 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Competência | Tipo | Rateio | Valor | Valor calculado | Total | Vacância |
| Setembro - 2023 | Medição | Fixo | R$ 500,00 | R$ 233,33 | R$ 1.446,67 | R$ 1.653,33 |
| Cob. direta | Rateio m² Const; | R$ 600,00 | R$ 280,00 |
| Orçamento | CRD | R$ 2.000,00 | R$ 933,33 |

Os lançamentos de vacância serão gerados de acordo com os parâmetros do empreendimento.

Para saber mais sobre rateio de vacância, veja na sessão Veja Mais logo abaixo.

### Contrato com um distrato no meio do período

---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Inicio Vigência | Fim Vigência | Inicio Locação | Fim 1º Locação | Valor Contrato | Mês CIVIL |
| 05/09/2023 | 31/08/2024 | 05/09/2023 | 30/09/2023 | R$ 2.000,00 | Não |

|  |  |  |  |
| --- | --- | --- | --- |
| Inicio Parcela | Fim Parcela | dias Cobrados | dias Mês |
| 05/09/2023 | 30/09/2023 | 26 | 30 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Competência | Tipo | Rateio | Valor | Valor calculado | Total | Vacancia |
| Setembro - 2023 | Medição | Fixo | R$ 500,00 | R$ 433,33 | R$ 1.369,33 | R$ 210,67 |
| Cob. direta | Rateio m² Const; | R$ 600,00 | R$ 520,00 |
| Orçamento | CRD | R$ 480,00 | R$ 416,00 |

### Orçamento com Subunidades definidas como "Valor Fixo"

---

Quando o empreendimento possui subunidades com valores fixos cadastrados na associação de cobrança por orçamento, devemos levar em consideração seu histórico de alteração de valores e se o mesmo ocorre num mesmo mês.  
Neste cenário, o sistema irá considerar o pró-rata e realizar a proporção de valores.

É importante salientar que este comportamento também está atrelado às premissas da cobrança pró rata, ou seja, os itens de cobrança devem possuir a opção "pró rata" marcada, bem como o contrato de locação.

***NOVO CONCEITO – Período de Fechamento***

Além de considerar os dias do mês (civil ou comercial), o sistema agora permite configurar um intervalo de fechamento, como por exemplo: de 10 a 25 do mês.  
Neste caso, o cálculo pró-rata utiliza apenas os dias dentro desse intervalo para identificar:

* Dias utilizados pelo contrato
* Dias de vacância (dias sem contrato ativo)

Esse comportamento permite que a cobrança seja proporcional ao período realmente apurado no fechamento do condomínio, e não obrigatoriamente ao primeiro e último dia do mês.  
  
***Cálculo de Valor Diário***

Para garantir proporcionalidade correta, o sistema agora calcula o valor por dia da competência antes de aplicar o pró-rata:

Valor por Dia = Valor Mensal ÷ Total de dias do Mês (civil ou comercial)

Esse valor diário é usado tanto para calcular os dias utilizados quanto para calcular a vacância no período de fechamento***.***

### Exemplo com fechamento (Cálculo Pró-Rata com Período de Fechamento)

---

Este exemplo representa a lógica nova aplicada ao cálculo, incorporando **orçamento + pró-rata + vacância** dentro de um período definido no fechamento do condomínio.

### Dados

* Valor mensal do contrato: **R$ 5.000,00**
* Competência: **Março (31 dias)**
* Período do fechamento: **10/03 a 25/03 → 16 dias**
* Início do contrato: **15/03**

1. Identificar dias de cobrança

* Dias utilizados (contrato ativo): **15/03 a 25/03 → 11 dia**
* Dias vagos (vacância): **10/03 a 14/03 → 5 dias**

2. Valor diário  
      5.000 ÷ 31 = **R$ 161,29****3. Cálculo proporcional**

* **Contrato:** 161,29 × 11 = **R$ 1.774,19**
* **Vacância:** 161,29 × 5 = **R$ 806,45**Neste caso, o sistema distribui proporcionalmente o valor mensal entre dias utilizados e dias vagos dentro do intervalo definido pelo fechamento.

**Orçamento com Subunidades definidas como "Valor Fixo"**  
Quando o item de cobrança é do tipo Orçamento, o sistema:

* Verifica **subunidades com valor fixo cadastradas**;
* Considera **mudanças de valor dentro da mesma competência**;
* Aplicará **pró-rata automaticamente** para fazer a proporção correta.

### Atenção

Este comportamento depende das **mesmas premissas**:

✔ Item marcado como *pró-rata*  
✔ Contrato marcado como *pró-rata*

### Veja Também

---

---
