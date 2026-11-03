---
content_hash: b9402dea950f040bffd152859d3744bd4c8a7cb1c1c86d7669570c2549b031e2
fetched_at: '2026-06-29T00:09:21.732942+00:00'
page_id: '422545889'
product: rm
source: tdn-rm
title: Crédito Outorgado (Outras Informações)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545889
version: 7
---

**Passo a Passo:**

Habilitar o campo Utiliza Crédito Outorgado e indicar o Percentual do Credito Outorgado a ser aplicado sobre o valor do débito total referente às operações fins de direito no menu Cadastro | Filiais | Pasta Dados Fiscais | Tipo Estabelecimento.   
Incluir os lançamentos de Entrada sem a indicação de tributação normal de ICMS, ou seja, inserir as Notas Fiscais de Entrada sem aproveitamento do crédito, pelo fato de ter optado pelo Crédito Outorgado  
Incluir os lançamentos de Saída de acordo com cada situação tributária das Notas Fiscais emitidas. A forma de escrituração das operações de saída não sofrerão mudanças na apuração do Imposto sob regime de Crédito Outorgado.  
Liberar os lotes do período de apuração em que se deseja apurar o Crédito Outorgado.  
Encerrar o Período de Apuração em que se deseja apurar o Crédito através do módulo Lançamentos | Períodos de Apuração. O cálculo será feito aplicando o percentual definido no Cadastro de Filiais sobre o somatório do valor de ICMS e valores referentes a ICMS Próprio em caso de naturezas com S.T. dos Lançamentos Fiscais associados às Naturezas de Operação dos Grupos 5.62 e 6.62 (Exerc. 2002) e 5.352; 6.352; 5.353; 6.353; 5.354, 6.354; 5.355, 6.355; 5.356, 6.356 (Exerc. 2003). O sistema lançará o valor calculado no campo Crédito Outorgado na Pasta Apuração do Período de Apuração.

**Relatório Resumo de Apuração do ICMS:**  
Nas Entradas, as colunas que deverão ser escrituradas serão as colunas de Vr.Contábil e Outras.   
Nas Saídas, o preenchimento permanecerá normal.  
Na coluna de Crédito do Imposto, que lança a apuração de todas as Entradas do período, somente deverá ser preenchida a coluna de Outros Créditos com o texto "Credito Outorgado Conforme o Artigo 11 do Anexo III, Decreto 45.490/2000 do Regulamento de ICMS/SP".  
A escrituração da Coluna de Débito do Imposto não sofrerá alterações.

Exemplo de como será calculado o Credito Outorgado e a Apuração do Saldo

Total do Débitos de todas as Operações do período: 1.620,00;  
Total do Débitos das Operações. Fins de Direito: 980,00 (900,00 de ICMS e 80,00 de ICMS Próprio para CFOP's com S.T.);  
Percentual a ser Aplicado sobre o total do Débito: 20%;  
O valor do Crédito Outorgado a ser abatido será: 196,00;  
Valor a ser escriturado na coluna Crédito do Imposto**:** 196,00;

Neste caso o valor a ser pago do imposto, tomando como base este nosso exemplo é:  
1.620,00 - 196,00 = 1.424,00 (este é o valor a ser pago depois da opção pelo crédito Outorgado)

ObservaçãoOs Layout's dos Livros Fiscais emitidos mensalmente sob outra forma de apuração não deverão ser alterados. Os Layout's dos livros devem estar em conformidade com o Convênio 106/96.
