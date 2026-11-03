---
article_id: 360052812153
category: Folha Mensal
content_hash: 13310b808f27bce9f22a199b24d58411c983e29a7380b397c7564074f9fcfeb4
fetched_at: '2026-06-28T22:46:59.499122+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Salário família considera salário nominal no mês da admissão/demissão
  do funcionário '
type: support-article
updated_at: '2023-03-30T19:12:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052812153-RH-RM-FOP-Sal%C3%A1rio-fam%C3%ADlia-considera-sal%C3%A1rio-nominal-no-m%C3%AAs-da-admiss%C3%A3o-demiss%C3%A3o-do-funcion%C3%A1rio
---

**Dúvida**

Mesmo desativando o parâmetro **Usa salário nominal**, o sistema está considerando o salário nominal no mês da admissão ou demissão do funcionário.  
  
 **Ambiente**

RM –  Folha de pagamento – Todas as versões  
  
**Solução**

Para admitidos no mês e demitidos no mês, o sistema sempre irá considerar o **salário** **base** (**salário** do cadastro do funcionário), pois segundo PORTARIA MPS Nº 348, DE 08 DE ABRIL DE 2003, artigo 8º§§ 1º e 2º, o funcionário não terá direito ao recebimento do **salário****família** pois a base de calculo (§1º) é devida sobre a remuneração independentemente se ele trabalhou ou não todos os dias do mês, ou seja, nos meses de **admissão** e **demissão** a base para **salário****família** não é o valor recebido em função dos dias/horas trabalhadas e sim sobre o valor que seria devido caso trabalhasse o mês todo.   
Caso **queria** pagar o salário família nestes casos, poderá lançar o valor para os funcionários através do **código de cálculo 65**.  
Apenas o valor da **cota** de **salário****família** (valor do pagamento do **salário****família**) será proporcionalizado em função dos dias trabalhados.
