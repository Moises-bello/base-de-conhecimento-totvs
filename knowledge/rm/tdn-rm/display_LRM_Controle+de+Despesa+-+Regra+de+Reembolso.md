---
content_hash: 9f7813535ad0d6c2c73c85adad51a8e8ab64f27a65ccaa41b9638bed29465712
fetched_at: '2026-06-29T00:11:44.980395+00:00'
page_id: '818450966'
product: rm
source: tdn-rm
title: Controle de Despesa - Regra de Reembolso
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Regra+de+Reembolso
version: 6
---

## 🔹Cadastro de Regras de Reembolso

O cadastro de **Regras de Reembolso** permite criar definições de como serão gerados os lançamentos financeiros de reembolso no sistema.

---

🔹 **Campos do Cadastro**

O cadastro é composto pelos campos abaixo:

⚙️ **Código**  
Campo que armazena o código da regra de reembolso.

⚙️ **Descrição**  
Campo utilizado para informar a descrição da regra de reembolso cadastrada.

---

🔹 **Prioridade de Cobrança**

Neste campo, o usuário define qual será a prioridade de cobrança das despesas, podendo escolher entre **Locatário** e/ou **Locador**.  
Para isso, basta marcar o item desejado e definir a prioridade utilizando as setas para cima ou para baixo.

✅ **Comportamento do sistema:**

* Se **Locatário** e **Locador** estiverem desmarcados, as despesas não serão cobradas.
* Se **Locatário** e **Locador** estiverem marcados, o sistema irá buscar o responsável conforme a primeira prioridade definida. Caso não exista, será utilizada a segunda prioridade.

---

🔹 **Utiliza cálculo pro-rata dia**

Quando este parâmetro está marcado, indica que a despesa será calculada de forma **pro-rata dia**.  
Para o cálculo das parcelas **Inicial** e **Final**, será utilizado o conceito de **Mês Civil**.

---

## 🔹O que é Mês Civil?

📌 **Mês Civil** é uma expressão utilizada no mercado financeiro e administrativo que considera todos os dias reais do mês.  
Por exemplo, fevereiro pode possuir 28 ou 29 dias. Sendo assim, o **Ano Civil** é considerado com 365 dias.

---

📌 **Exemplo de Cálculo Pro-rata**

📌 **Despesa:**

* Primeiro vencimento: 01/01/2018
* Nº de parcelas de reembolso: 10
* Valor das parcelas de reembolso: R$ 310,00

📌 **Contrato de Locação:**

* Data de início da locação: 15/01/2018
* Data final da locação: 31/12/2018

📌 **Cálculo Pro-rata:**

Na primeira parcela de reembolso da despesa, o valor a ser calculado para o locatário será:

* Dias civis do mês de janeiro: 31
* Parcela / dias civis: 310 / 31 = R$ 10,00
* Dias em que o locatário é responsável pelo pagamento da despesa: 17

📌 **Cálculo final:**  
(Parcela / dias civis) × Dias em que o locatário é responsável pelo pagamento da despesa  
(310 / 31) × 17 = **R$ 170,00**

Nesse caso, o **Locatário** irá pagar o valor de **R$ 170,00** na primeira parcela e o valor integral de **R$ 310,00** nas demais parcelas.

---

## 🔹 Cancelar lançamento no encerramento/rescisão do contrato

Quando este parâmetro está marcado, indica que os **Lançamentos Financeiros de Reembolso da Despesa** serão cancelados quando o **Contrato de Locação** associado ao imóvel da despesa for **encerrado ou rescindido**.

✅ **Comportamento do sistema:**

* Serão cancelados apenas os lançamentos que possuam **data de vencimento posterior** à data de Encerramento/Rescisão.
* Os lançamentos só serão cancelados caso o status no financeiro esteja como **"Em Aberto"**.

⚠️ **Observações importantes:**

* Caso exista algum lançamento de reembolso **baixado** com vencimento posterior à data de Encerramento/Rescisão do contrato de locação, o sistema irá criar um **lançamento financeiro a pagar** com o valor baixado desses lançamentos.
* O sistema **não permite** marcar este parâmetro juntamente com o parâmetro **"Cobrar o reembolso agregado ao aluguel"**, pois, dessa forma, para excluir os lançamentos de despesas, seria necessário excluir também os lançamentos do contrato de locação.

---

## 🔹 Cobrar o reembolso agregado ao aluguel

Quando este parâmetro está marcado, indica que os valores financeiros de reembolso serão gerados como **valores de integração** dos lançamentos do **Contrato de Locação** associado ao imóvel da despesa.

Dessa forma, os valores de reembolso serão gerados **juntamente com a geração dos lançamentos do contrato de locação**.

false

⚠️ **Observações**

* O sistema **não permite** marcar este parâmetro juntamente com o parâmetro **"Cancelar lançamento no encerramento/rescisão do contrato"**, pois, dessa forma, para excluir os lançamentos de despesas, seria necessário excluir também os lançamentos do contrato de locação.
* Ao marcar este parâmetro, é **obrigatório** informar qual será o **valor de integração a som**

---

## 🔹Valor de Integração

⚙️ **Valor de Integração**  
Neste campo, o usuário informa o valor de integração que será utilizado na geração dos valores de reembolso da despesa junto às parcelas do contrato de locação.

false

⚠️ **Observações**

* Este campo só será habilitado quando a opção **"Cobrar o reembolso agregado ao aluguel"** estiver marcada.

**Figura 1 - Tela de Regra de Reembolso Origem Aluguel**
