---
content_hash: 18d0dd5d62b2517aae8215225fb6c3014d7f8cdcd0643bf024bfbf617d7f8548
fetched_at: '2026-06-29T00:06:30.264759+00:00'
page_id: '235317327'
product: rm
source: tdn-rm
title: ER_PCREQ-10736_Faturamento_de_Produtos_com_Quantidade_Real_Consumida
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10736_Faturamento_de_Produtos_com_Quantidade_Real_Consumida
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contrato |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto** | R\_C&P\_TOP011 | **IRM** |  |
| **Requisito** |  | **Subtarefa** |  |
| **Chamado** | Não se aplica. | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link para o Wikihelp** | | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | Contratos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx> | | Contrato de Insumo | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.ContratosInsumo.aspx> | | | |
| **Integração** | TOP x Protheus | | |

   

## Objetivo

Este documento tem o objetivo de demonstrar a funcionalidade de faturamento com consumo real no contrato de insumo.   
 

## **Regra de Negocio**

 Toda a regra de negócio implementada está disponível a partir da versão 12.1.11. Esta implementação torna-se necessária para clientes realizarem o faturamento do contrato de insumo, com a quantidade real consumida, mas torne-se importante o usuário se atentar as regras envolvidas em cada parametrização do contrato. Para melhor entendimento do processo, iremos detalhar cada parametrização e suas diferentes combinações quando habilitamos o parâmetro *“Considerar produtos associados no faturamento de contratos de insumos”*.

**Apenas o parâmetro de faturar contrato de insumo**

Quando o usuário apenas habilita a opção *‘Considerar produtos associados no faturamento de contrato de insumos’* (), o TOP entende que toda dedução e retenção deste contrato, será deduzida pela formula do contrato, que por padrão é a fórmula A. Quando o usuário escolhe essa parametrização, o TOP não enviará a quantidade real consumida no contrato, deixaremos a quantidade default igual 1 e valor total deduzido de retenção e dedução. Para melhor entendimento do problema e os motivos desta definição, mostraremos os detalhes no exemplo abaixo:

No cenário acima podemos verificar que a quantidade consumida do produto 01.01, foi de 15 e o valor total consumido foi de R$44,25. Como tivemos o valor de R$ 5,94 a ser deduzido nesta liberação, devido estarmos usando a *fórmula A* neste contrato, torna-se necessário deduzir o valor total dos descontos pelo consumo, alterando os valores totais proporcionalmente:

Produto 01.01 = 44,25, desconto de 4,314375, total = 39,94.  
Produto 01.02 = 16,65, desconto de 1,623375, total = 15,03.

Como o valor total ficou alterado não é possível neste cenário que o TOP envie a quantidade real consumida, pois o valor unitário do item ficará alterado podendo gerar dizima.

Produto 01.01 = 39,94, Quantidade consumida = 15, novo valor encontrado para o insumo = 2,6626666666.....  
Produto 01.02 = 16,65, Quantidade Consumida = 5. novo valor encontrado para o insumo = 3,006

Se neste cálculo for gerado dizima, o TOP e o Suprimentos/Faturamento irão possuir valores distintos de liberação provocando erros no processo.

**Selecionar o parâmetro de faturar contrato de insumo e enviar retenção e dedução no campo desconto**

Quando o usuário seleciona a opção *‘Considerar produtos associados no faturamento de contrato de insumos’*, recomendamos que o mesmo também marque a opção de *“Enviar retenção como desconto na liberação do período*” (). Nesta configuração o TOP conseguirá enviar a quantidade real consumida no faturamento do contrato, pois a dedução e a retenção serão descontadas apenas no movimento e não no TOP, pois neste cenário a fórmula a ser utilizado no contrato é a fórmula C. Neste cenário o TOP envia o valor Bruto e as deduções e retenções serão enviadas para o campo desconto do movimento, garantindo a integridade do Valor e quantidade consumidos no contrato, como demostrado no exemplo abaixo:

 

 

No cenário acima podemos verificar que a quantidade consumida do produto 01.01, foi de 15 e o valor total consumido foi de R$44,25. Estes valores foram enviados corretamente para o Movimento, mantendo a integridade do consumo dos insumos no contrato, e o próprio movimento se encarrega de deduzir os valores de retenção e dedução. Este cenário também é utilizado na integração com Protheus.

**Selecionar o parâmetro de faturar contrato de insumo e discriminar retenção e dedução no moviment**o

Quando o usuário seleciona a opção *‘Considerar produtos associados no faturamento de contrato de insumos’*, e também marca a opção de *“Discriminar valores de retenção e dedução”* (). Nesta configuração o TOP conseguirá enviar a quantidade real consumida no faturamento do contrato, pois a dedução e a retenção serão descontadas de forma diferente no movimento e não no TOP, a fórmula a ser utilizado no contrato para este cenário é a fórmula C. Neste cenário o TOP envia o valor Bruto, a dedução irá para o campo desconto do movimento e a retenção serão enviadas em cada item do movimento. Neste cenário é necessário que o usuário altere a formula de valor Bruto nos parâmetros do movimento, realizando o abatimento da retenção de cada item, como demostrado no .

Não realizamos o abatimento da retenção no TOP quando o parâmetro *“Considerar produtos associados no faturamento de contrato de insumo”* estiver marcado, pois o envio da quantidade afeta diretamente o valor do movimento e a integridade dos dados. Sendo assim quando habilitado somente o parâmetro de *‘Discriminar valores de retenção e dedução’* não é necessário alterar a formula do Suprimentos/Faturamento, pois a retenção no item é abatida antes do envio.

## 

## **Faturamento**

Com o usuário clicando no processo “Gerar integração para Suprimentos/Faturamento”, o TOP irá exibir um alerta para o usuário, de acordo com a parametrização escolhida:

* + **Apenas com o parâmetro faturar produto:** Quando o usuário decide que a o TOP deverá deduzir o valor de retenção e dedução, não será enviado no movimento a quantidade real do item consumido, sendo assim será exibido abaixo do Grid de Produtos o seguinte alerta "*A parametrização do projeto, impede que a quantidade real consumida possa ser enviada para o movimento. Para mais informações consulte WilkHelp Totvs*" () .
  + **Parâmetro de faturar contrato de insumo e enviar retenção e dedução no campo desconto:** Quando o usuário define que retenção e dedução devem ir no movimento como desconto, não será mostrado nenhum alerta no formulário de envio, pois este cenário é o comportamento ideal quando se utiliza quantidade real consumida e integração com Protheus(.
  + **Selecionar o parâmetro de faturar contrato de insumo e discriminar  retenção e dedução no movimento:** Quando o usuário define que a retenção vai para o item do movimento e a dedução vai para o campo desconto do movimento, será exibido um alerta "*A parametrização do projeto, exige que o usuário altere a fórmula do valor bruto do movimento no Suprimentos/Faturamento, para deduzir retenção*", mostrando para o usuário que é necessário alterar manualmente a parametrização do movimento, modificando a formula para que seja deduzida a retenção no próprio movimento, uma vez que, o TOP irá enviar o valor bruto consumido sem descontar a retenção ().

Independentemente da combinação da parametrização do projeto o usuário poderá alterar o produto da solicitação no momento do envio para faturamento, este comportamento é responsável apenas pelo parâmetro de *‘Considerar produtos associados no faturamento de contrato de insumos’,* mas podendo apenas selecionar produtos que estão associados ao insumo.

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

******Protótipo 03******

********Protótipo 04********

**********Protótipo 05**********

************Protótipo 06************

**************Protótipo 07**************

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
