---
content_hash: 9ff74aa49998123976813b23d8371f5de5dd189d76889525340049b90eebabe9
fetched_at: '2026-06-29T00:05:48.980373+00:00'
page_id: '1034798436'
product: rm
source: tdn-rm
title: Teste novidade versão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1034798436
version: 34
---

Ficha Financeira – TOTVS Incorporação

A **Ficha Financeira** apresenta, de forma detalhada, a composição financeira do contrato de venda,
permitindo acompanhar valores originais, reajustes, encargos, descontos, baixas e saldo devedor,
de acordo com as parametrizações realizadas no sistema.

---

### 📌 Desconto

Para que os **valores de desconto** aplicados pelo financeiro sejam exibidos na Ficha Financeira
e no Plano de Financiamento, é necessário cadastrar o componente do tipo:

* **910 – Desconto do Financeiro**

Somente após esse cadastro o valor de desconto será apresentado corretamente no relatório.

---

### 📅 Competência (Data Base)

Ao informar uma **Data Base** para geração da Ficha Financeira, o sistema apresenta os valores
correspondentes à **competência do mês e ano selecionados**.

Ou seja, o relatório sempre reflete o **estado das parcelas no último dia do mês informado**,
considerando os registros existentes na base de dados.

⚠️ Importante:

* A Ficha Financeira **não trabalha com valores pró-rata (por dia)**.
* O relatório **não busca informações históricas**, apenas os dados existentes na base.
* O reajuste só será considerado se a opção correspondente estiver marcada.

---

### 💡 Perda Financeira

Para que os valores de **perda financeira** sejam exibidos na Ficha Financeira,
é necessário habilitar o parâmetro:

**Parâmetros Gerais → Contrato de Venda → Plano de Financiamento → Exibir valores de perda financeira no relatório**

---

### 🆕 Novidade – Release 12.1.2506

A partir da versão **12.1.2506**, passou a ser possível definir
**quais componentes devem ser ignorados** na geração da Ficha Financeira.

Essa configuração é realizada por meio do parâmetro:

**Componentes a serem ignorados na Ficha Financeira**

---

### 📄 Ficha Financeira sem Data Base

Quando a Ficha Financeira é gerada **sem informar uma Data Base**,
o relatório apresenta diretamente o **valor do Plano de Financiamento do contrato**,
sem simulações de reajuste ou posição temporal.

---

### 📍 Caminho do Relatório

* **Processos → Relatórios → Ficha Financeira**
* **Relatórios → Novo Gerador de Ficha Financeira**

---

### ⚙️ Parâmetros do Relatório

* **Data Base Atual do Contrato**  
  Exibe a posição financeira considerando a data base selecionada.
  Este parâmetro fica bloqueado quando não é utilizada a opção de gerar por Data Base.
  
* **Exibir Resíduos**  
  Quando marcado, o relatório apresenta a soma de todos os resíduos do Plano de Financiamento.
  
* **Exibir Multa e Juros**  
  Acrescenta os valores de multa e juros na Ficha Financeira.
  Este parâmetro também depende da geração por Data Base.
  
* **Posição Atual com Reajuste**  
  Simula o reajuste com base nos dados atuais da base, sem buscar informações históricas
  e sem salvar o reajuste.

---

### 📊 Campos do Relatório

1. **Valor Original** – Valor do componente principal da parcela (sinal, mensal, financiamento, etc.).
2. **Juros** – Valor de juros calculado pelo sistema.
3. **Correção Monetária** – Valor da correção aplicada pelo processo de reajuste.
4. **Outros Valores** – Resíduo, seguro, IPTU, encargos e valores opcionais.
5. **Multa de Atraso** – Multa calculada pelo atraso no pagamento.
6. **Juros de Mora** – Juros calculados pelo atraso no pagamento.
7. **Desconto** – Valor de desconto aplicado no momento da baixa.
8. **Valor da Parcela** – Soma de todos os valores anteriores.
9. **Valor Baixado** – Total efetivamente pago.
10. **Saldo Devedor** – Diferença entre o valor da parcela e o valor pago.

---

### 📑 Grid Principal da Ficha Financeira

No início do relatório é exibido um **grid com os componentes geradores de parcelas**
do contrato de venda, como por exemplo:

* Sinal
* Parcelas Mensais
* Parcelas Intermediárias

O valor total apresentado corresponde à soma das parcelas do Plano de Financiamento.

---

### 📈 Ficha Financeira com Reajuste

Quando o contrato possui reajuste:

* Se a Data Base for **anterior ao reajuste**, os valores não serão reajustados.
* Se a Data Base for **posterior ao reajuste**, os valores reajustados serão considerados.

O mesmo comportamento se aplica em casos de **aditivos contratuais**,
onde o relatório passa a refletir os novos valores após a efetivação do aditivo.

---

### 💰 Baixa de Lançamentos

A Ficha Financeira também considera os valores de baixa realizados,
inclusive quando o pagamento ocorre **antes do vencimento**,
apresentando corretamente os valores integrados, descontos e saldo atualizado.

]]>
