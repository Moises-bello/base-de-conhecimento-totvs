---
content_hash: 52188a67ca7405aca595c905d5c30e9bb652daafb15e240af679b456c57764f8
fetched_at: '2026-06-29T00:08:49.633333+00:00'
page_id: '331852043'
product: rm
source: tdn-rm
title: Exemplos de Geração Valor de Desconto Antecipação.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331852043
version: 2
---

Segue alguns Exemplos de  Gerações de Lançamentos utilizando o **Valor de Desconto Antecipação.**

Valor de Desconto Antecipação **( Matriz Aplicada )**

**Item do Desconto por Antecipação com 20% de desconto se for utilizado até o dia 5 Fixo e do dia 6 até dia 8 será concedido um desconto de 10%.**

**Desconto Antecipação cadastrado na ( Matriz Aplicada ) em** :  Matriz Aplicada | Anexos | Desconto por antecipação por matriz aplicada.

Desconto Antecipação inserido no cadastro da Matriz Aplicada

# 1º Exemplo:

Parcela do Aluno no Valor de **R$ 1.000,00** Reais .

* Parcela contem Desconto de 10% na Parcela sobre o **Valor Original** .
* Possui o Desconto Antecipação ( 20% até dia **5** ou 10% até dia **8** ) sobre o **Valor Original** .
* Possui 2 Bolsas **SOMAR** – *Ordem 1*

\*\* Bolsa Somar 1 com 15% de desconto.

\*\* Bolsa Somar 2 com 15% de desconto.

\*\* Total de desconto da Bolsa SOMAR = 30% Aplicados sobre o **Valor original.**

* Possui uma Bolsa Cascata – *Ordem 2*

\*\* Bolsa Cascata com 50% de desconto = Aplicado sobre o **Valor original** – **Desconto da Parcela** – **Desconto Antecipação** – **Bolsa Somar** *Ordem 1*

Parcela com Desconto Cadastrado.

Bolsas Cadastras no contrato.

30% Somar – *Ordem 1*

50% Cascata – *Ordem 2*

**Valores ..**

R$ 1.000,00 Parcela ( **Valor Original** )

Primeiro Desconto 10% na Parcela sobre **Valor Original** = R$ 100,00

Desconto Antecipação de 20% sobre o **Valor Original** = R$ 200,00

Bolsa Somar ( *Ordem 1* ) 30 % sobre o **Valor Orignal** = R$ 300,00

Bolsa Cascata ( *Ordem 2* ) 50% sobre:

* **Valor Original:** R$ 1.000,00
* ( Menos ) Desconto da Parcela = R$ 100,00
* ( Menos ) Desconto Antecipação = R$ 200,00
* ( Menos ) Bolsa Somar ( *ordem 1* ) = R$ 300,00

Bolsa Cascata sendo aplicada sobre o Valor de R$ 400,00.

*50% de cascata sobre R$ 400,00 = R$ 200,0 Reais*

# 2º Exemplo:

**Valor de Perda de Desconto Antecipação.**

**Exemplo:**

Aluno com uma Parcela no valor de R$ 1.000,00 Reais e tem os Itens de Desconto cadastrado da seguinte forma:

Se pagar até o **dia 5 ele terá 20% de desconto antecipação** , ou seja , o desconto para o aluno passa a ser de **R$ 200,00** Reais, mas se a parcela for paga do **dia 6 até dia 8 o desconto cai para 10%** , e o aluno passa a ter       **R$ 100,00** Reais de desconto gerando a perda de **R$ 100,00** Reais.

**Exemplo** = **Dia 5** pegou o desconto **de 20%** sobre o valor Original .

No **dia 8** passou para Segundo ítem do desconto antecipação e o desconto passou a ser **de 10%**

Levando uma perda de **R$ 100,00** do desconto.

Nos ítens da Baixa do Lançamento esta Perda do Desconto Antecipação fica registrado conforme Print Abaixo:

Anexos | Baixas do Lançamento.

**Mostrando a Perda de Antecipação com seu Valor de R$ 100,00 Reais.**

Parametrização Valor de Integração ( **Perda de Desconto Antecipação** )

Ambiente | Parâmetros | Educacional | 15.05.03.01 - Educacional | Fin - Vlrs. Opcionais/Integração 1/3

Informar o Desconto por Antecipação : O Valor Integração criado para Perda de Antecipação , lembrando que no cadastro o mesmo tem que estar com **AÇÃO** = **NADA**

Cadastro dos Valores de Integração em :

Financeiro / Contábil | Financeiro | Valores de Integração Financeira

# 3º Exemplo:

**Bolsa Cascata**  Aplicada **após desconto Antecipação com Perda**.

**Observação:** Sobre aplicação da Bolsa Cascata : O desconto da Bolsa Cascata é Aplicado sobre o **Valor Original** – **Valor de Desconto Antecipação** ( Mas em caso de perda do desconto antecipação o valor do desconto da Bolsa Cascata será **SEMPRE** aplicado sobre o **MAIOR** desconto do Desconto Antecipação , sem considerar sua perda.

**Veja no exemplo Abaixo:**

Valor da Parcela = R$ 1.000,00.

Desconto Antecipação = **20% se for gerada até o dia 5.**

Desconto Antecipação = **10% se for gerada do dia 6 até 8** ( Perda de 10% ).

Bolsa Cascata =  **50% será aplicada após o Desconto Antecipação.**

**Dia 5** a Geração  com o desconto de **20 % de Antecipação.**

Parcela de R$ 1.000,00 Aplicado os ( 20% de Desconto Antecipação ) = **200 Reais de desconto.**

R$ 1.000,00 – R$ 200,00 = **R$ 800,00.**

50% de Bolsa Cascata sobre os R$ 800,00 = **R$ 400,00 .**

**Exemplo agora com Geração dia 08/01 com uma Perda de 10% do Desconto Antecipação:**

Note que o Desconto Antecipação passou **para 10%.** O desconto que antes era de R$ 200,00 passou para R$ 100,00 , **porém** o desconto da **Bolsa Cascata** , continua considerando o **MAIOR** desconto do **Desconto Antecipação** que era de **20%**.

**Dia 8** a Geração  com o desconto de **10 % de Antecipação**.

Parcela de R$ 1.000,00 Aplicado os ( 10% de Desconto Antecipação ) = **100 Reais de desconto.**

R$ 1.000,00 – R$ 100,00 = **R$ 900,00.**

50% de Bolsa Cascata sobre os R$ 800,00 = R$ 400,00 ( **Considerando o MAIOR Desconto Antecipação** ).

R$ 1.000,00 – R$ 100,00 ( Antecipaçao ) – R$ 400,00 ( Cascata ) = **R$ 500,00 .**
