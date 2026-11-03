---
article_id: 360022679592
category: RH - Folha de Pagamento
content_hash: 67137c1d64ed4e75b822ad0b387a5216f43c4e6277f7141c0df4b1ed1b0c5246
fetched_at: '2026-06-28T22:44:17.166306+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Salário família na admissão, sistema não está calculando
  de acordo com o salário que o empregado está recebendo
type: support-article
updated_at: '2025-06-11T19:20:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022679592-RH-Linha-Protheus-GPE-Sal%C3%A1rio-fam%C3%ADlia-na-admiss%C3%A3o-sistema-n%C3%A3o-est%C3%A1-calculando-de-acordo-com-o-sal%C3%A1rio-que-o-empregado-est%C3%A1-recebendo
---

**Dúvida**Sistema não está calculando o salário família de acordo com o que o empregado está recebendo no mês de admissão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Para admitidos no mês e demitidos no mês o sistema sempre irá considerar o salário base (Salário do cadastro, campo RA\_SALARIO), pois segundo a PORTARIA MPS Nº 348, DE 08 DE ABRIL DE 2003, artigo 8º§§ 1º e 2º o funcionário não terá direito ao recebimento do salário família pois a base de cálculo (§1º) é devida sobre a remuneração independentemente se ele trabalhou ou não todos os dias do mês, ou seja, nos meses de admissão e demissão a base para salário família não é o valor recebido em função dos dias/horas trabalhadas e sim sobre o valor que seria devido caso trabalhasse o mês todo.  
  
Apenas o valor da cota de salário família (Valor do pagamento do salário família) será proporcionalizado em função dos dias trabalhados.   
  
PORTARIA MPS Nº 348, DE 08 DE ABRIL DE 2003 , artigo 8º  
§ 1º O direito à cota do salário-família é definido em razão do salário-de-contribuição que seria devido ao empregado no mês, independentemente do número de dias efetivamente trabalhados.  
§ 2º A cota do salário-família é devida proporcionalmente aos dias trabalhados nos meses de admissão e demissão do empregado.

Exemplo:

Folha janeiro de 2019

Admissão: 15/01/2019

Salário, campo RA\_SALARIO:R$1.176,00

Id 0031 Salário na folha 17 dias = 666,40

Salário família = 32,80 (parâmetro envolvido MV\_SALFP)

Tabela salário família

Até R$1.364,43 cota R$32,80

Até R$907,77 cota R$46,54

Neste exemplo o sistema irá pagar a cota de R$32,80, porque o salário que está no cadastro de funcionários(**Atualizações > Funcionários > Gestão de Funcionários**), campo RA\_SALARIO está acima de 907.77, sistema não irá considerar o ID de cálculo 0031 para pagar o salário família.

Parâmetros envolvidos no calculo do salário família: **MV\_SALFP, MV\_SALFD e MV\_SALFDED**

Legislação:<http://www.planalto.gov.br/ccivil_03/decreto/d3048.htm>

Orientação tributária:  <http://tdn.totvs.com/pages/releaseview.action?pageId=142813581>

Sistema somente proporcionaliza a cota do salário família:<http://tdn.totvs.com/pages/releaseview.action?pageId=223913022>

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
