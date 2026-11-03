---
content_hash: 24a7ef47527b9152b23368283bc33ac3f8191a8c9ee8ed60f0ad8319d7b87eed
fetched_at: '2026-06-29T00:10:55.981398+00:00'
page_id: '590049451'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Unidade de Diagnóstico > Resultados Laboratoriais
  > Preenchimento dos Resultados Laboratoriais > Calculo Expressão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590049451
version: 4
---

#### **CONTEÚDO**

1. Cadastrar Expressão para Resultado Laboratorial
2. Resultados Laboratoriais
3. Preenchimento dos Resultados Laboratoriais

Visão GeralCadastrar Expressão para Resultado

## **01. CADASTRAR EXPRESSÃO PARA RESULTADO LABORATORIAL**

Cadastros > Unidade de Diagnóstico > Métodos e Parâmetros de Exame

Faça o filtro desejado (nesse caso usamos o exame "Hemograma"), de um duplo click no exame selecionado e vá até a aba "Parâmetros"

Selecione o parâmetro desejado (nesse caso utilizamos o parâmetro "teste" com código "5") e preencha a "Expressão para cálculo do parâmetro"

Observe que o Parâmetro possui a seguinte expressão "P1 \*P2"  
P + o numero logo a frente representa o parâmetro de código 1, no caso parâmetro "Proteínas Totais" ou seja a letra P é uma referencia a palavra "Parâmetro" e o número é uma referencia ao código do parâmetro.

Exemplo:  
**Expressão - (P2+P5+P6 \*30)  
Expressão por extenso (Parâmetro 2 + Parâmetro 5 + Parâmetro 6 x 30)**

Resultados Laboratoriais

## **02. TELA RESULTADOS LABORATORIAIS**

Unidade de Diagnóstico > Resultados Laboratoriais > Selecione o exame desejado e dê um duplo click.

Preenchimento dos Resultados Laboratoriais

## **03. TELA PREENCHIMENTO DOS RESULTADOS LABORATORIAIS**

1. Tela com os parâmetros a serem preenchidos dentro de um exame.

2. Na parte inferior selecione a ação para "Digitar Exame" e clique em salvar.

3. Ao digitar no parâmetro que é utilizado em alguma expressão em outro parâmetro o resultado do mesmo (que possui expressão cadastrada) é automaticamente calculado.
