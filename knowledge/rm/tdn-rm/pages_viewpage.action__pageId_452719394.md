---
content_hash: c2d4c65055390d8d9fd7d6e8dbc324a83bf803739af55f68ef930117f955de91
fetched_at: '2026-06-29T00:10:07.294146+00:00'
page_id: '452719394'
product: rm
source: tdn-rm
title: Alteração de Dias Úteis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719394
version: 5
---

Os dias úteis para cálculo do vale transporte são cadastrados no cadastro de funcionários e devem ser alterados mensalmente de acordo com a quantidade de dias úteis do mês.  
   
É possível alterar coletivamente o número de dias úteis do mês e do próximo mês para que no momento do desconto do vale-transporte, esses dias alterados sejam correspondentes ao mês do processamento da folha.   
   
Normalmente esta alteração é realizada no início de cada mês, ou seja, logo após a liberação da competência. Os dados serão alterados na pasta Parâmetros do cadastro de Funcionários.  
   
Os dias são cadastrados e poderão ser alterados como "Expediente Integral" ou "Meio Expediente".  
   
**Observação:** A opção "Meio Expediente" é apenas para os casos em que há distribuição diferenciada de vales para dias de apenas meio expediente. Só é possível selecionar uma opção de cada vez.   
   
As opções para alteração serão:

* **Alterar os campos "Mês atual" e "Próximo mês"** – para que o valor que está informado no cadastro do funcionário no campo "Próximo mês" seja transferido para o campo "Mês atual" e o valor informado nesta alteração seja cadastrado no campo "Próximo mês".
* **Alterar somente o campo "Mês atual"** – para que o valor que está informado no cadastro do funcionário seja alterado apenas no campo "Mês atual" com o valor informado nesta alteração.
* **Alterar somente o campo "Próximo mês"** - para que o valor que está informado no cadastro do funcionário seja alterado apenas no campo "Próximo mês" com o valor informado nesta alteração.
* **Alterar somente "Após Reajuste"** - para que o valor que está informado no cadastro do funcionário seja alterado apenas no campo "Após Reajuste" com o valor informado nesta alteração.

O valor a ser preenchido na coluna "DE" (nº de dias atual) é referente ao campo que demonstra o número de "Dias Úteis no Próximo Mês" que está no cadastro do funcionário. Ou seja, o valor dos "Dias Úteis no Próximo Mês" será transferido para o campo "Dias úteis do mês" se for igual ao valor informado nesta coluna "DE".  
   
**Atenção:**

* Se o campo "Dias Úteis no Próximo Mês" tiver valores diferentes para determinados funcionários, poderá ser utilizada a seta (do teclado) para que seja criada uma nova linha de alteração. Assim, o sistema realizará várias alterações simultâneas.
* Se o valor do campo "De" for nulo a alteração afetará todos os funcionários da seleção.

O novo valor do campo "Dias Úteis no Próximo Mês" será preenchido com o valor da coluna "PARA" (novo valor a ser assumido). Ou poderá ser utilizada fórmula previamente cadastrada, informando o código de fórmula para alteração.  
   
Ao final do processo será informado um LOG de avisos para funcionários em que a alteração dos dias úteis de vale transporte não foi realizada.

Atenção

A partir da versão 12.1.29.144 estará disponível a atualização de alteração de dias uteis para multicoligadas, ou seja, será possível realizar a alteração para mais coligadas ao mesmo tempo, os parâmetros de utilização são os mesmo descritos acima.

e também a disponibilidade de realizar agendamentos.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Linhas de Transporte  
Tarifas de Transporte
