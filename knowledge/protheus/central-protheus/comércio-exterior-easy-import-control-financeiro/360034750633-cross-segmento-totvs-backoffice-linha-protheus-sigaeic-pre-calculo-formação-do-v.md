---
article_id: 360034750633
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 3c979e35beccf718c69d95fe75ed35579f0dcb0268f93cc9ea893803856c6b13
fetched_at: '2026-06-28T22:39:44.444494+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC- Pre calculo: formação
  do valor de frete'
type: support-article
updated_at: '2021-08-19T11:44:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034750633-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pre-calculo-forma%C3%A7%C3%A3o-do-valor-de-frete
---

**Dúvida**Como pode ser calculado o Frete na tabela pré-calculo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Formação do Valor de Frete:  
Sabemos que no cadastro da tabela de pré-Calculo existe um campo de porcentagem que será aplicado  sobre a despesa base, se for escolhida opção de porcentagem para essa despesa, e também o campo de moeda da despesa.  
No frete o cálculo é diferente. Não importa o que você informar nesses campos no cadastro, o sistema irá  ignorar.  
Primeiramente, é necessário entender as faixas de preço do frete. No cadastro da Via de Transporte existe essa funcionalidade que interfere diretamente no resultado final de frete no pré-Calculo.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045154973/mceclip5.png)

Digamos que tenhamos um processo com 3.546 kg de peso liquido, de acordo com a planilha abaixo o resultado seria US$ 14.184,00 (Peso \* Valor por Quilo). Esse controle será usado apenas quando não existir  
informação de Containers na capa do *Purchase Order* e no cadastro de *Containers* na Via de Transporte.   
  
Funciona assim:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044297394/mceclip0.png)

O calculo do frete se inicia com a configuração da moeda a ser tratada. A moeda do frete será a informada na Via de Transporte vinculada ao *Purchase Order* que está sendo base do relatório.

Depois de configurar a despesa frete do *Purchase Order*, o sistema irá verificar se os campos de *Container* no *Purchase Order* estão preenchidos. Se estiverem, o sistema fará os cálculos do frete em cima dessas informações de acordo com o cadastro de taxas dos containers, ou seja:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045153753/mceclip1.png)

Por outro lado, se o sistema não encontrar conteúdo nos campos de *Container* na capa do *Purchase Order* e no cadastro de taxas de containers, será verificado se existe valor cubado informado no processo. Caso esteja, o sistema se comportará da seguinte forma:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044297454/mceclip2.png)

Além desses, ainda existem regras mais específicas para o frete no Pré-Calculo.  
Digamos que temos o cenário em que não temos valores de *Containers* informados, e nem de valor cubado, o sistema verificará o peso líquido do processo e fará os cálculos de frete em cima dessa informação, de acordo com o cadastro de faixas de preço presente na Via de Transporte. Funciona da seguinte forma:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044297474/mceclip3.png)

Para finalizar os tratamentos de frete no Pré-Calculo, o sistema tem ainda a funcionalidade de calcular os valores baseado em uma paridade da moeda do processo com a moeda da Via de Transporte, caso sejam diferentes, pois o Pré-Calculo sempre será impresso de acordo com a moeda do processo. Vamos  
imaginar que temos um valor de frete de US$ 100,00 e a moeda da Via de Transporte é o Euro que tem uma cotação para aquele dia de 2,50, enquanto o Dólar tem 2,00. Por exemplo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044297554/mceclip4.png)

**Saiba mais**  
[Pré-cálculo - EICTP25A](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=554660153)
