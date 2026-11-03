---
content_hash: ecd414abc55bac4abd3fea5b723f6911212ce996de42cadbed991f23f96ad426
fetched_at: '2026-06-29T00:09:28.611269+00:00'
page_id: '423938724'
product: rm
source: tdn-rm
title: Alteração de Medidor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938724
version: 3
---

Neste anexo é possível incluir ou excluir os lançamentos de Indicador de Uso que correspondem a alguma Alteração de Medidor.   
A Alteração de Medidor normalmente ocorre quando existe algum problema com o medidor, como uma quebra, ou quando é necessário zerá-lo.  
A visão apresenta os dados que identificam as Alterações de Medidor, com as respectivas datas e valores dos Medidores (antigo e novo):

* **Data da Alteração**: Indica a data em que a alteração foi realmente realizada no Objeto de Manutenção.
* **Data de Lançamento**: Indica sempre a data e a hora em que a medição foi inserida no sistema.
* **Medidor Antigo**: Indica o valor do medidor antes de ocorrer a alteração.
* **Medidor Novo**: Indica o novo valor para o medidor.

***Observação***: A exclusão de um lançamento de Alteração de Medidor somente será possível caso não exista lançamento posterior à data em que a alteração foi lançada.   
A medição relacionada com alteração de medidor não poderá ser excluída na tela de Indicador de Uso.  
Após realizar uma Alteração de Medidor, o sistema irá considerar os dados informados nessa alteração para calcular o Valor Acumulado nos Lançamentos de Histórico de Indicadores de Uso, exemplo, vamos supor um exemplo de lançamento de Alteração de Medidor, onde o novo lançamento irá começar a partir do zero.

1. Antes da alteração, vamos supor que o Hodômetro do Veículo XYZ quebrou-se com 14000 KM de medição realizada, e com isso surgiu a necessidade de realizar a Alteração de Medidor.
2. Com isso, acessamos a tela de Alteração de Medidor, e incluímos uma alteração informando a Quilometragem do Medidor Antigo (14000) e informamos a Quilometragem do Medidor Novo (0).
3. Após a inserção da Alteração de Medidor, o histórico deste Indicador de Uso irá gerar duas linhas:

* + A linha referente a medição do indicador de uso antigo;
  + A linha referente a medição do indicador de uso novo, sendo neste caso, com a medição 0 (zerada) e o Acumulado de 14000.

A partir dessa alteração de medidor, o Valor Acumulado no lançamento de Histórico de Indicadores de Uso irá seguir a parametrização definida na aba Identificação dos Parâmetros do RM Officina no campo Lançamento(s) de Indicador de Uso.

4. Se a parametrização do Lançamento de Indicador de Uso estiver definida como Atualização, ao incluir Históricos de Indicadores de Uso, o sistema irá somar com o Valor Acumulado no momento da Alteração de Medidor.

Neste exemplo, ao inserirmos um indicador de uso no valor de 500 KM logo após o lançamento de Alteração de Medidor, este será somado com o Valor Acumulado do medidor antigo, totalizando 14500 (para o valor acumulado) e 500 (para o medidor novo).   
Como o parâmetro está definido para Atualizar, o próximo lançamento deverá ser maior ou igual que o do lançamento anterior, que neste caso foi de 500 KM. Então, se é preciso lançar uma medição de 10 KM, devo informar um lançamento de 510 KM.  
Assim o lançamento ficará 14510 (para o valor acumulado) e 510 (para o medidor novo).

5. Se a parametrização do Lançamento de Indicador de Uso estiver definida como Incremento, ao incluir Históricos de Indicadores de Uso, o sistema sempre irá somar com o Valor Acumulado do lançamento anterior.

Neste exemplo, ao inserirmos um indicador de uso no valor de 500 KM logo após o lançamento de Alteração de Medidor, este será somado com o Valor Acumulado do medidor antigo, totalizando 14500 (para o valor acumulado) e 14500 (para o medidor novo), pois está sendo incrementado.   
Como o parâmetro está definido para Incrementar, o próximo lançamento não precisa ser maior ou igual que o do lançamento anterior, que neste caso foi de 500 KM.  
Então, se é preciso lançar uma medição de 10 KM, deve-se informar um lançamento de 10 KM.   
Assim, automaticamente o sistema irá somar com o valor acumulado do lançamento anterior. Totalizando 14510 (para o valor acumulado) e 14510 (para o medidor novo).
