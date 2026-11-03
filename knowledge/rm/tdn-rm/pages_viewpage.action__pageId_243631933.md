---
content_hash: 91a1550441e65b445148b9420edde526b0a72b24e16a80b605210d359e418bd5
fetched_at: '2026-06-29T00:08:11.969952+00:00'
page_id: '243631933'
product: rm
source: tdn-rm
title: RPT00040.1.1 - Cuidados ao se Utilizar Formatação Condicional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243631933
version: 28
---

# Índice:

---

.\*ndice:

# Valores alfanuméricos (A-Z) :

---

      1 - **Valores alfanuméricos (A-Z)** têm que vir acompanhados de **"'"** (apóstrofo ou aspas simples).

**Exemplo:** [Chapa do Funcionário] == ‘00001’

**2image2016-7-6 18:47:13.png, image2016-7-6 18:47:20.png, image2016-7-6 18:47:29.png, image2016-7-6 18:47:35.png dateGaleria Formatação Condicional Valor Alfanumérico (Correto)**

**2image2016-7-6 18:46:7.png, image2016-7-6 18:47:5.png, image2016-7-6 18:47:29.png, image2016-7-6 18:47:35.pngdateGaleria Formatação Condicional Valor Alfanumérico (Errado)**

OBS

Observe que ao não se utilizar um valor alfanumérico entre apóstrofos, a formatação não é devidamente aplicada.

# Valores numéricos (0-9):

---

     2 - **Valores numéricos** **(0-9)** não podem ser acompanhados de outro caractere que não seja os convencionais utilizados em formatação numérica americana:

1. **a.** **“.” (ponto)** como separador decimal, em vez da **“,” (virgula)**.
2. **b.** **Separadores de milhar (não colocar)**
3. **c.** **Símbolos monetários (não colocar)**

**Exemplo:** [Salário] >= 0 And [Salário] <= 1050.99

**2image2016-7-6 18:46:7.png, image2016-7-6 18:47:5.png, image2016-7-6 18:47:13.png, image2016-7-6 18:47:20.pngdateGaleria Formatação Condicional Valor Numérico**

OBS

Em versões mais antigas do sistema era necessário que:

* O numeral viesse entre **“[]”**
* O símbolo de igual viesse duplicado **“==”**,porém nas versões mais atuais é **facultativo.**

# Valores em geral:

---

     3 - **Valores em geral -** Não devem vir acompanhados do nome da tabela, ao se formar a expressão de formatação condicional.

**Exemplo:** [Chapa do Funcionário] = '00001' **(Certo)**  
  [Funcionários.Chapa do Funcionário] = '00001' **(Errado)**

Tomando os devidos cuidados ao escrever a expressão de formatação, a mesma irá funcionar como o esperado.

# Itens de Relatório com valores decimais

---

     4 -  **Itens de Relatório com valores decimais** **-** Para utilizar um item de relatório com valor decimal (exemplo: Totalizador) no editor de condições de formatação é necessário fazer a conversão utilizando a expressão **ToDecimal**.

**Exemplo :** ToDecimal([ReportItems].[Totalizador3].[Text]) < ToDecimal('0,00') **(Certo)**  
                  ToDecimal([ReportItems].[Totalizador3]) < 0.00 **(Errado)**

false

Para correto funcionamento da conversão do item de relatório, esse item tem que estar em formatação **numérica #**.

# Condições:

---

false

Para correto funcionamento da formatação condicional que utilize campos de consultas SQL, **é necessário a utilização de alias únicos** nos campos utilizados nas condições de regras. Ou seja, atribuir alias que não existam em outras tabelas/Consultas SQL presentes no relatório.

# Importante

---

Uma das coisas que podem fazer com que a Formatação Condicional não funcione corretamente é a falta da tabela principal no relatório. Maiores detalhes sobre como definir uma tabela principal para o relatório podem ser obtidos [aqui](https://tdn.totvs.com/x/frIAL).

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Formatação Condicional

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
