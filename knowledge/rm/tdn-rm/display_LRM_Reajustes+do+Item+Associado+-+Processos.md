---
content_hash: ebca7857a866a57094df0697dd685291ba5474bd875bba6d4a0e6d8e00005eb6
fetched_at: '2026-06-29T00:09:16.803042+00:00'
page_id: '421385564'
product: rm
source: tdn-rm
title: Reajustes do Item Associado - Processos
type: documentation
url: https://tdn.totvs.com/display/LRM/Reajustes+do+Item+Associado+-+Processos
version: 16
---

Em alguns contratos, é necessário que o reajuste aconteça a nível de item contratado, como por exemplo em clientes que trabalham para o DNIT e que necessitam que esse reajuste aconteça por vários índices, sendo que cada um é aplicado para um determinado grupo de tarefas, assim como:

Ex. Índice para reajuste de serviços de Terraplenagem, índice para reajuste de serviços de Pavimentação, etc.

Por esse motivo, foi desenvolvido no módulo de contratos do TOTVS Construção, Obras e Projetos, a possibilidade de realizar reajustes para os itens associados aos contratos.  
Na tela de edição de contratos, na aba de "Reajuste" foi criado um novo tipo de reajuste, disponível para os tipos de contrato de Prestação de Serviços, Insumos, Fornecimento de Material e Extra-Histograma.

As opções de tipo de reajuste são:

**Sem Reajuste:** Para contratos que não utilizam reajuste.

**Por Contrato:** Reajuste simples, sua aplicação e exemplo podem ser consultados na documentação de [Contratos](https://tdn.totvs.com.br/display/LRM/Contratos+-+TCOP), aba Reajuste.

**Por item Associado:**Ao selecionar o tipo de reajuste Por Item Associado, deverá informar no campo **Período Reajuste**, uma das opções Anual ou Mensal. Além disso, deverá selecionar "**Data Base de Reajuste**" e "**Aplicação do Reajuste**" que informará sobre qual valor o índice ou percentual de reajuste será aplicado: Valor Unitário Inicial ou Valor Atual.

Para os projetos que possuem o parâmetro  marcado, na aba de reajuste do contrato será apresentado somente as opções de reajuste "**Sem reajuste**" e "**Por item associado**".  Já a opção de Aplicação de Reajuste é apresentada somente a opção de "**Valor Unitário Inicial**":

Dessa forma, ao utilizar **Valor Unitário Inicial**, um item contratado por 100,00, ao aplicar um índice de 10%, esse item passa a ter o valor de 110,00. Caso venha aplicar novo reajuste, de por exemplo, 15%, o valor base para cálculo será o inicial contratado novamente, ou seja, 100,00, fazendo com que o novo valor seja de 115,00.

Já, caso utilize a opção de **Valor Atual** (Parâmetro "Utilizar Valor do Reajuste na Medição PI+R" desmarcado), o reajuste será aplicado em cima do valor atual, ou seja, no mesmo exemplo acima, o índice do segundo reajuste seria aplicado em cima do valor de 110,00 e não sobre 100,00 que foi o inicial contratado.

Caso selecione o tipo "**Por Item Associado**", os índices associados, caso existam, serão excluídos, pois o reajuste por item associado dependerá de índices que deverão ser informados manualmente no processo de "**Reajuste de Itens Associados ao Contrato**" o qual será explicado logo a seguir.

**Processo de Reajuste de Itens Associados ao Contrato**

Algumas regras e/ou restrições a serem consideradas:

* Reajuste dos itens contratados: Para aplicar em todo o contrato basta selecionar todos os itens do contrato;
* Reajuste anual ou mensal que acontece somente a partir da "**Data Base de Reajuste**" definida na tela de edição/criação do contrato, na aba reajuste;
* O reajuste deverá incidir no preço do item contratado ou valor atual, dependendo do parâmetro "**Aplicação do Reajuste**" na aba Reajuste da tela de criação/edição do contrato;
* Poderá ser utilizado o cadastro de índices para que o reajuste seja aplicado para um grupo de serviços que tenha esse índice associado, para utilizar, deverá informar no item pelo anexo de itens do contrato ou na associação de itens, na coluna Índice de Reajuste, qual o índice pertencente a esse item. Dessa forma, na tela de reajuste, poderá informar o percentual de reajuste para esse índice, fazendo com que seja aplicado para todos os itens desse índice;
* Possibilidade de selecionar mais de um item contratado para a aplicação de um mesmo índice ou percentual;
* Deverão ser exibidos os índices utilizados no reajuste anterior assim como o valor antes do reajuste atual;
* O item somente será reajustado se a data for maior ou igual a data base de reajuste do contrato selecionado e se não existirem reajustes realizados para o item no período corrente;
* Se existir algum item de aditivo disponível para reajuste, o mesmo ocorrerá sem restrições;
* Caso haja itens que estão sendo reajustados em períodos medidos em data superior à que o reajuste está sendo aplicado, os períodos medidos deverão sofrer recalculo, considerando o novo valor desse item;
* Caso haja itens que estão sendo reajustados em períodos liberados em data superior à que o reajuste está sendo aplicado, esse período liberado não sofrerá recalculo, mas vai ser criado um período complementar de reajuste, com o valor da diferença entra o período liberado e o percentual que foi aplicado de reajuste, esse período complementar de reajuste é criado já medido, mas com quantidade 0. Somente com o valor da diferença do reajuste para o período liberado principal. Dessa forma, esse período também deverá ser liberado. 

  + Exemplo:

               Período 1 com item 001.01.01 liberado com valor de 100,00;  
               Reajuste para o item 001.01.01 em 20% no período 1 (Já liberado)   
               O período 1 liberado continua como 100,00, mas é criado o período de reajuste 001R0001 no valor de 20, 00.  
               A partir do período 2 em diante, o valor assumido para o item é de 120,00.

* Caso haja um reajuste para o contrato, não será possível fazer um realinhamento pelo processo e nem pela associação de itens;
* Os períodos que tiverem períodos complementares criados deverão considerar os valores dos itens em relação ao período principal, sofrendo recalculo caso esteja medido;
* Se um contrato for paralisado, e novamente for colocado em andamento, caso os períodos não sejam reprogramados, os valores considerados na medição e liberação deverão obedecer ao período de reajuste, conforme exemplo: Contrato 0001/2015 de 01/01/2015 à 31/12/2016: Período 0001 - 01/01/2015 a 31/01/2015 Contrato paralisado em 01/02/2015 Contrato em andamento em 01/03/2016 Reajuste realizado em 01/01/2016 Valores de medição e liberação até o 12º deverão ser considerados antes do reajuste de 01/01/2016

No processo de medição deverá ser exibido um alerta para que o usuário saiba que o contrato necessita de um reajuste caso o mesmo não tenha sido realizado. Dependendo da Data Base definida.  
Os contratos do tipo **Contratos de Insumo, Contratos de Fornecimento de Material e Contratos Extra-Histograma** também permitem que os objetos associados possam ter os valores reajustados através do processo de Reajustar Itens Associados ao Contrato.

Para esse tipo de contrato algumas particularidades podem ser consideradas assim como:

**1 -** **Cadastro de Contratos**

O tipo de reajuste "Por Item Associado" pode ser selecionado para contratos de insumo, de fornecimento de material ou extra-histograma, também com a obrigatoriedade de se informar o **Período de Reajuste**, ou seja, qual a sua periodicidades que irá ser aplicado (Mensal ou Anual), a **Data Base de Reajuste**, que define partir de qual data será considerado para base dos reajustes a aplicados e a **Aplicação do Reajuste** (Se o reajuste será aplicado sempre em cima do Valor Inicial Contratado ou do Valor Atual). 

A Data Base de Reajuste, não poderá ser maior que a data final do contrato. Esta, considerando aditivos do contrato.

**2 - Processo de Reajustar Itens Associados ao Contrato**

A tela do processo, é possível visualizar os objetos (insumos) associados aos contratos, onde para cada objeto, poderá ser definido um percentual de reajuste     - Para os contratos que utilizam objetos associados, não existem agrupadores por índices assim como existe para contratos de Prestação de Serviços;     - Para contratos de fornecimento de material, o reajuste somente será possível se NÃO existirem consumos para o objeto selecionado, pois quem controla o consumo e liberação do período é o módulo de "Geração de Pedidos", portanto, para esse tipo de contrato, o período de reajuste não será criado.

**3 - No FLUIG:**

A funcionalidade de Consumir Objetos em HTML tem o mesmo comportamento que o processo da MDI, onde a inclusão e exclusão não são permitidos para períodos de reajuste, onde o valor contratado deve obedecer aos reajustes realizados e onde a mensagem de alerta deve ser exibida para períodos que tem objetos passíveis de reajustes.

**4 - Geração de Pedidos e Pedido Extra**

No módulo de Geração de Pedidos e Pedido Extra, o valor do item do pedido (Preço), quando associado à um determinado contrato que sofreu reajuste (Contrato de Fornecimento de Material por exemplo), considera a data em que foi realizado o reajuste, assim como citado em relação ao processo de consumir objetos do contrato. Ao criar uma nova solicitação de pedido, o período do contrato é criado com as datas inicial e final igual à data de solicitação. Se o reajuste tiver sido realizado após a data de solicitação, o preço exibido deverá ser diferente do Valor Unitário Contratado, que já foi alterado pelo reajuste, pois o mesmo ainda não havia entrado e vigor.

**5- Deduções e Retenções**

O período de reajuste (Ex.: 0001R001) é criado a partir de períodos principal e complementar que se encontram liberados. Assim como acontece com os rateios em contratos de serviços, as dedução e retenções também são incluídas nos novos períodos de reajuste e não somente para os contratos de serviços mas para todos os contratos que utilizam reajuste por item associado e que também permitem inclusão de deduções e retenções. Períodos de reajuste permitem a inclusão/alteração/exclusão de deduções e retenções a partir desta versão. Na inclusão das deduções e retenções que ocorre ao solicitar o reajuste de um determinado item, é feito o cálculo para encontrar a proporção de cada dedução ou retenção em relação ao resíduo. Uma mesma dedução ou retenção pode estar associada à um período principal e a um período complementar, sendo assim os valores no período de reajuste devem considerar essa possibilidade.

**6 - Cálculo do Contrato**

O cálculo do valor dos contratos de insumo, fornecimento de material e extra-histograma considera esse novo tipo de período de reajuste, porém desconsiderando a quantidade zero (0) consumida do mesmo, apenas o valor consumido. Esse valor do objeto no período de reajuste considera os consumos realizados acima de 100%, porém, no cálculo do projeto o mesmo valor não é considerado, assim como ocorre com os consumos até 100%. Para o período de reajuste é descontado o valor que ultrapassa os 100% do objeto contratado.

**7 – Reajuste de Deflação**

O Totvs Obras e projetos é permitido informar o reajuste de deflação para os contratos, quando possui uma queda sobre o valor contratado. Para que informe o valor de reajuste de deflação é necessário acessar o processo de **Reajustar itens Associados ao Contrato,** em seguida informar um valor negativo no campo de Percentual de reajuste.

**8 – Reajuste Provisório**  
O reajuste provisório está disponível somente com o parâmetro de **Utilizar Valor do Reajuste na Medição (PI + R)** habilitado.  
No reajuste Provisório, o fator é volátil. Podendo receber alterações, enquanto o mesmo não for efetivado. Para que seja realizado o reajuste provisório é necessário acessar o processo de "**Reajustar itens Associados ao Contrato**", em seguida marcar a opção de **Provisório**. A qualquer momento o reajuste provisório pode ser efetivado através do processo de "**Efetivar Reajustes Provisórios do Item**".  
Más, não é permitido dois reajustes provisórios para o mesmo contrato. Reajuste provisório é uma previsão do fator esperado para o reajuste desta forma não é permitido adicionar novos reajustes, enquanto o fator não for efetivado.

**Anexo de reajustes do Item de Contrato**  
Foi desenvolvido no anexo de Itens do Contrato um outro anexo de "Reajustes do Item" que poderá ser visualizado na tela de edição do Item. Nesse anexo será possível consultar todos os reajustes que foram realizados para o item.

**Rateio por Centro de Custo, Produto e Estado/Município quando houver períodos de Reajuste:**

No período de reajuste, deverá conter todos os rateios (produto, centro de custo e estado e município) realizados para os itens dos períodos de origem. O cálculo do rateio, levará em conta a proporção do valor para definir o novo percentual, pois os mesmos devem fechar em 100%:  
O cálculo do valor do contrato deverá considerar esse novo tipo de período, porém desconsiderando a quantidade zero (0) do mesmo, apenas o valor. O valor medido do período de reajuste considera as medições realizadas acima de 100% do item contratado, porém, no cálculo do projeto o mesmo valor não deverá ser considerado, assim como ocorre com as medições comuns, para o período de reajuste deverá ser descontado o valor que ultrapassa os 100% do item contratado.  
   
**Parâmetro de Medição Acima de 100%:**   
Todo reajuste/realinhamento utilizado quando a medição/liberação acima de 100% não reflete no TOTAL do CONTRATO. E quando há saldo, por exemplo 50% medido e depois 60%, os 10% "ultrapassado" não deverá ser refletido no contrato.

Veja Também

 

[Processo para Atualizar valor medido Preço Inicial e Valor medido Reajuste do Contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=421385089)
